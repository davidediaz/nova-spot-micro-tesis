#!/usr/bin/env python3
"""Evaluate one Gazebo PPO policy against the matching nominal gait."""

from __future__ import annotations

import argparse
import csv
import sys
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "Experimentos"))
from entrenar_ppo_gazebo import GazeboResidualEnv  # noqa: E402


def evaluate(env, model, condition, episodes):
    values = []
    for episode in range(episodes):
        obs, _ = env.reset(seed=100 + episode)
        initial_x = env.x
        total_reward = 0.0
        max_tilt = 0.0
        steps = 0
        terminated = False
        truncated = False
        while not (terminated or truncated):
            if model is None:
                action = np.zeros(12, dtype=np.float32)
            else:
                action, _ = model.predict(obs, deterministic=True)
            obs, reward, terminated, truncated, info = env.step(action)
            total_reward += float(reward)
            max_tilt = max(max_tilt, abs(float(info["roll"])),
                           abs(float(info["pitch"])))
            steps += 1
        values.append({
            "return": total_reward,
            "advance_m": float(env.x - initial_x),
            "max_tilt_rad": max_tilt,
            "steps": steps,
            "terminated": int(terminated),
        })
    row = {
        "simulator": "gazebo", "gait": env.gait, "condition": condition,
        "episodes": episodes,
    }
    for key in ("return", "advance_m", "max_tilt_rad", "steps", "terminated"):
        row[key] = float(np.mean([item[key] for item in values]))
    return row


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--gait", choices=("crawl", "step"), required=True)
    parser.add_argument("--seed", type=int, required=True)
    parser.add_argument("--policy", type=Path, required=True)
    parser.add_argument("--episodes", type=int, default=1)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    from stable_baselines3 import PPO
    import rclpy

    args.output.parent.mkdir(parents=True, exist_ok=True)
    rclpy.init(args=None)
    env = GazeboResidualEnv(
        gait=args.gait, episode_cycles=5,
        output_dir=args.output.parent / f"{args.gait}_semilla_{args.seed}")
    try:
        model = PPO.load(args.policy)
        rows = [evaluate(env, None, "nominal", args.episodes),
                evaluate(env, model, "ppo", args.episodes)]
    finally:
        env.close()
    with args.output.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)
    print(f"Evaluación Gazebo escrita en {args.output}")


if __name__ == "__main__":
    main()
