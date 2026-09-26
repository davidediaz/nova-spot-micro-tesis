#!/usr/bin/env python3
"""Train residual PPO through the live ROS 2 Gazebo simulation.

The script starts the isolated Gazebo PPO launch, publishes one residual
action per gait phase and builds the same 27-element observation used by the
MuJoCo trainer. It is intentionally single-environment and conservative:
episodes reset the world when the Gazebo service is available, and no hardware
node or Raspberry connection is involved.
"""

from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
import threading
import time
from pathlib import Path

import gymnasium as gym
import numpy as np
import rclpy
from gymnasium import spaces
from rclpy.executors import MultiThreadedExecutor
from ros_gz_interfaces.msg import Contacts
from ros_gz_interfaces.srv import ControlWorld
from sensor_msgs.msg import Imu, JointState
from std_msgs.msg import Bool, Float32MultiArray, String
from stable_baselines3 import PPO
from stable_baselines3.common.callbacks import BaseCallback, CheckpointCallback, CallbackList
from tf2_msgs.msg import TFMessage

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src" / "nova_gait_controller"))
from nova_gait_controller.kinematics import (  # noqa: E402
    BODY_HEIGHT,
    BODY_LENGTH,
    BODY_WIDTH,
    COXA_LENGTH,
    FEMUR_LENGTH,
    HIP_SPACING_X,
    HIP_SPACING_Y,
    TIBIA_LENGTH,
)


JOINTS = (
    "front_left_coxa_joint", "front_left_femur_joint", "front_left_tibia_joint",
    "front_right_coxa_joint", "front_right_femur_joint", "front_right_tibia_joint",
    "rear_left_coxa_joint", "rear_left_femur_joint", "rear_left_tibia_joint",
    "rear_right_coxa_joint", "rear_right_femur_joint", "rear_right_tibia_joint",
)
CONTACT_NAMES = ("front_left", "front_right", "rear_left", "rear_right")


def quaternion_roll_pitch(q):
    sin_roll = 2.0 * (q.w * q.x + q.y * q.z)
    cos_roll = 1.0 - 2.0 * (q.x * q.x + q.y * q.y)
    sin_pitch = 2.0 * (q.w * q.y - q.z * q.x)
    return float(np.arctan2(sin_roll, cos_roll)), float(
        np.arcsin(np.clip(sin_pitch, -1.0, 1.0)))


class GazeboResidualEnv(gym.Env):
    """Gym adapter around the running ROS 2 Gazebo simulation."""

    metadata = {"render_modes": []}

    def __init__(self, gait="crawl", episode_cycles=5, startup_wait=12.0,
                 output_dir=None, reset_world=True):
        super().__init__()
        if gait not in ("crawl", "step"):
            raise ValueError("gait debe ser crawl o step")
        self.gait = gait
        self.samples = 24 if gait == "crawl" else 32
        self.episode_cycles = int(episode_cycles)
        self.max_steps = self.samples * self.episode_cycles
        self.reset_world_enabled = bool(reset_world)
        self.output_dir = Path(output_dir or ROOT / "Experimentos" /
                                "entrenamiento_ppo_gazebo_20260924")
        self.output_dir.mkdir(parents=True, exist_ok=True)
        self.action_space = spaces.Box(-1.0, 1.0, shape=(12,), dtype=np.float32)
        self.observation_space = spaces.Box(
            low=-np.inf, high=np.inf, shape=(27,), dtype=np.float32)
        self.lock = threading.Condition()
        self.q = np.zeros(12, dtype=float)
        self.roll = 0.0
        self.pitch = 0.0
        self.height = 0.235
        self.accel = np.zeros(3, dtype=float)
        self.gyro = np.zeros(3, dtype=float)
        self.contacts = np.ones(4, dtype=float)
        self.x = 0.0
        self.phase_index = 0
        self.phase_counter = 0
        self.safety = False
        self.safety_reason = ""
        self.last_obs = np.zeros(27, dtype=np.float32)
        self.node = rclpy.create_node("ppo_gazebo_training_env")
        self.command_pub = self.node.create_publisher(String, "/nova/gait_command", 10)
        self.action_pub = self.node.create_publisher(Float32MultiArray, "/nova/rl_action", 10)
        self.reset_client = self.node.create_client(ControlWorld, "/world/empty/control")
        self.node.create_subscription(JointState, "/joint_states", self._joint_cb, 10)
        self.node.create_subscription(Imu, "/nova/imu", self._imu_cb, 10)
        self.node.create_subscription(TFMessage, "/world/empty/dynamic_pose/info", self._pose_cb, 10)
        self.node.create_subscription(String, "/nova/gait_phase", self._phase_cb, 10)
        self.node.create_subscription(Bool, "/nova/safety/triggered", self._safety_cb, 10)
        for index, name in enumerate(CONTACT_NAMES):
            self.node.create_subscription(
                Contacts, f"/nova/contacts/{name}",
                lambda msg, i=index: self._contact_cb(msg, i), 10)
        self.executor = MultiThreadedExecutor(num_threads=2)
        self.executor.add_node(self.node)
        self.executor_thread = threading.Thread(
            target=self.executor.spin, name="gazebo-training-ros", daemon=True)
        self.executor_thread.start()
        self.log_handle = (self.output_dir / "gazebo_launch.log").open(
            "w", encoding="utf-8")
        self.launch_process = subprocess.Popen(
            ["ros2", "launch", "nova_gait_controller", "ppo_gazebo.launch.py",
             "enabled:=false", "action_topic:=/nova/rl_action"],
            cwd=ROOT, env=os.environ.copy(), stdout=self.log_handle,
            stderr=subprocess.STDOUT)
        self._wait_for(lambda: self.phase_counter > 0, startup_wait)

    def _joint_cb(self, msg):
        values = dict(zip(msg.name, msg.position))
        with self.lock:
            self.q = np.asarray([values.get(name, 0.0) for name in JOINTS])
            self.lock.notify_all()

    def _imu_cb(self, msg):
        with self.lock:
            self.accel = np.array([
                msg.linear_acceleration.x, msg.linear_acceleration.y,
                msg.linear_acceleration.z])
            self.gyro = np.array([
                msg.angular_velocity.x, msg.angular_velocity.y,
                msg.angular_velocity.z])
            self.roll, self.pitch = quaternion_roll_pitch(msg.orientation)
            self.lock.notify_all()

    def _pose_cb(self, msg):
        for transform in msg.transforms:
            if transform.child_frame_id in ("base_link", "nova_sm3") or not transform.child_frame_id:
                with self.lock:
                    self.x = float(transform.transform.translation.x)
                    self.height = float(transform.transform.translation.z)
                    self.lock.notify_all()
                return

    def _phase_cb(self, msg):
        try:
            phase = json.loads(msg.data)
            sample = int(phase.get("sample_index", 0))
        except (TypeError, ValueError, json.JSONDecodeError):
            return
        with self.lock:
            self.phase_index = sample % self.samples
            self.phase_counter += 1
            self.lock.notify_all()

    def _contact_cb(self, msg, index):
        with self.lock:
            self.contacts[index] = 1.0 if msg.contacts else 0.0

    def _safety_cb(self, msg):
        with self.lock:
            self.safety = bool(msg.data)
            if self.safety:
                self.safety_reason = "supervisor"
            self.lock.notify_all()

    def _wait_for(self, predicate, timeout):
        deadline = time.monotonic() + float(timeout)
        with self.lock:
            while not predicate():
                remaining = deadline - time.monotonic()
                if remaining <= 0.0:
                    return False
                self.lock.wait(min(0.1, remaining))
        return True

    def _publish_command(self, command):
        msg = String()
        msg.data = command
        for _ in range(3):
            self.command_pub.publish(msg)
            time.sleep(0.05)

    def _reset_world(self):
        if not self.reset_world_enabled or not self.reset_client.wait_for_service(timeout_sec=2.0):
            return False
        request = ControlWorld.Request()
        request.world_control.reset.all = True
        future = self.reset_client.call_async(request)
        deadline = time.monotonic() + 5.0
        while not future.done() and time.monotonic() < deadline:
            time.sleep(0.02)
        return bool(future.done() and future.result() and future.result().success)

    def _observation(self):
        with self.lock:
            phase = self.phase_index / float(self.samples)
            obs = np.r_[self.roll, self.pitch, self.height - 0.235,
                         self.accel, self.gyro, self.contacts, self.q,
                         np.sin(2.0 * np.pi * phase),
                         np.cos(2.0 * np.pi * phase)]
        self.last_obs = np.asarray(obs, dtype=np.float32)
        return self.last_obs.copy()

    def reset(self, *, seed=None, options=None):
        super().reset(seed=seed)
        self._publish_action(np.zeros(12))
        self._publish_command("stand")
        self._reset_world()
        with self.lock:
            self.safety = False
            self.safety_reason = ""
            self.phase_counter = 0
        self._publish_command(self.gait)
        if not self._wait_for(lambda: self.phase_counter > 0, 3.0):
            raise RuntimeError("Gazebo no publicó /nova/gait_phase al reiniciar")
        return self._observation(), {
            "geometry": {
                "hip_spacing_x_m": HIP_SPACING_X,
                "hip_spacing_y_m": HIP_SPACING_Y,
                "body_height_m": BODY_HEIGHT,
                "coxa_m": COXA_LENGTH,
                "femur_m": FEMUR_LENGTH,
                "tibia_m": TIBIA_LENGTH,
            }
        }

    def _publish_action(self, action_rad):
        msg = Float32MultiArray()
        msg.data = np.asarray(action_rad, dtype=np.float32).tolist()
        self.action_pub.publish(msg)

    def step(self, action):
        action = np.asarray(action, dtype=float)
        if action.shape != (12,):
            raise ValueError("la acción debe tener 12 componentes")
        before_x = self.x
        before_phase = self.phase_counter
        self._publish_action(np.clip(action, -1.0, 1.0) * 0.08)
        if not self._wait_for(lambda: self.phase_counter > before_phase, 1.0):
            return self.last_obs.copy(), -10.0, True, False, {"timeout": True}
        obs = self._observation()
        dx = self.x - before_x
        reward = float(
            1.0 + 18.0 * dx - 8.0 * self.roll**2 - 8.0 * self.pitch**2
            - 25.0 * (self.height - 0.235)**2
            - 0.04 * float(np.dot(action, action))
            + 0.003 * float(np.sum(self.contacts)))
        terminated = bool(
            self.safety or not np.isfinite(obs).all()
            or self.height < 0.12 or self.height > 0.40
            or abs(self.roll) > 0.60 or abs(self.pitch) > 0.60)
        truncated = self.phase_counter >= self.max_steps
        return obs, reward, terminated, truncated, {
            "x": self.x, "dx": dx, "roll": self.roll,
            "pitch": self.pitch, "height": self.height,
            "safety_reason": self.safety_reason,
        }

    def close(self):
        if getattr(self, "launch_process", None) is not None:
            if rclpy.ok():
                self._publish_action(np.zeros(12))
                self._publish_command("stand")
            self.launch_process.terminate()
            try:
                self.launch_process.wait(timeout=5.0)
            except subprocess.TimeoutExpired:
                self.launch_process.kill()
                self.launch_process.wait()
            self.launch_process = None
        if getattr(self, "executor", None) is not None:
            self.executor.shutdown()
            self.executor_thread.join(timeout=10.0)
            self.node.destroy_node()
            if rclpy.ok():
                rclpy.shutdown()
            self.executor = None
        if getattr(self, "log_handle", None) is not None:
            self.log_handle.close()
            self.log_handle = None


class MetricsCallback(BaseCallback):
    def __init__(self, output, verbose=0):
        super().__init__(verbose)
        self.output = Path(output)
        self.handle = None

    def _on_training_start(self):
        self.output.parent.mkdir(parents=True, exist_ok=True)
        self.handle = self.output.open("w", encoding="utf-8")

    def _on_step(self):
        if self.handle is not None and self.num_timesteps % 100 == 0:
            self.handle.write(json.dumps({
                "timesteps": self.num_timesteps,
                "mean_reward": float(np.mean([
                    info["r"] for info in self.model.ep_info_buffer
                    if "r" in info])) if self.model.ep_info_buffer else None,
            }) + "\n")
            self.handle.flush()
        return True

    def _on_training_end(self):
        if self.handle is not None:
            self.handle.close()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--gait", choices=("crawl", "step"), default="crawl")
    parser.add_argument("--timesteps", type=int, default=2000)
    parser.add_argument("--seed", type=int, default=11)
    parser.add_argument("--episode-cycles", type=int, default=5)
    parser.add_argument("--no-world-reset", action="store_true")
    parser.add_argument("--resume", type=Path, default=None,
                        help="política SB3 desde la que se continúa el ajuste")
    parser.add_argument("--checkpoint-freq", type=int, default=0,
                        help="guardar checkpoint cada N pasos; 0 desactiva")
    parser.add_argument("--verbose", type=int, choices=(0, 1, 2), default=1)
    parser.add_argument("--output", type=Path, default=ROOT /
                        "Experimentos/entrenamiento_ppo_gazebo_20260924")
    args = parser.parse_args()
    rclpy.init(args=None)
    env = GazeboResidualEnv(
        gait=args.gait, episode_cycles=args.episode_cycles,
        output_dir=args.output / f"{args.gait}_semilla_{args.seed}",
        reset_world=not args.no_world_reset)
    output = args.output / f"{args.gait}_semilla_{args.seed}"
    try:
        if args.resume is not None:
            algorithm = PPO.load(args.resume, env=env, seed=args.seed,
                                 device="cpu", print_system_info=False)
        else:
            algorithm = PPO(
                "MlpPolicy", env, seed=args.seed, verbose=args.verbose,
                n_steps=128, batch_size=64, learning_rate=3e-4, gamma=0.99,
                gae_lambda=0.95, clip_range=0.2,
            )
        callbacks = [MetricsCallback(output / "training_trace.jsonl")]
        if args.checkpoint_freq > 0:
            checkpoint_dir = output / "checkpoints"
            checkpoint_dir.mkdir(parents=True, exist_ok=True)
            callbacks.append(CheckpointCallback(
                save_freq=args.checkpoint_freq,
                save_path=str(checkpoint_dir),
                name_prefix=f"{args.gait}_semilla_{args.seed}"))
        algorithm.learn(
            total_timesteps=args.timesteps,
            callback=CallbackList(callbacks),
        )
        algorithm.save(output / "policy")
        metadata = {
            "simulator": "gazebo",
            "gait": args.gait,
            "seed": args.seed,
            "timesteps": args.timesteps,
            "resume_policy": str(args.resume) if args.resume else None,
            "checkpoint_freq": args.checkpoint_freq,
            "dimensions_m": {
                "hip_spacing_x": HIP_SPACING_X, "hip_spacing_y": HIP_SPACING_Y,
                "body_length": BODY_LENGTH, "body_width": BODY_WIDTH,
                "body_height": BODY_HEIGHT, "coxa": COXA_LENGTH,
                "femur": FEMUR_LENGTH, "tibia": TIBIA_LENGTH,
            },
            "observation_dim": 27,
            "action_dim": 12,
            "residual_limit_rad": 0.08,
            "max_action_step_rad": 0.02,
            "external_action_applied_to_nominal": True,
            "hardware_transfer": False,
        }
        (output / "metadata.json").write_text(
            json.dumps(metadata, indent=2), encoding="utf-8")
    finally:
        env.close()


if __name__ == "__main__":
    main()
