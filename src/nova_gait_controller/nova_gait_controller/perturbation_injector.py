"""Deterministic sensor perturbation injector for Gazebo campaigns.

The node deliberately publishes to separate topics.  This makes each campaign
reproducible and prevents an experiment from silently changing the nominal
controller.  Noise is Gaussian with a fixed seed; delay is implemented with a
small FIFO and a wall-clock timer so that simulation time can be paused.
"""

from collections import deque
import copy
import random
import time

import rclpy
from rclpy.node import Node
from ros_gz_interfaces.msg import Contacts
from ros_gz_interfaces.msg import EntityWrench
from sensor_msgs.msg import Imu
from tf2_msgs.msg import TFMessage


class PerturbationInjector(Node):
    def __init__(self):
        super().__init__('perturbation_injector')
        self.declare_parameter('input_pose_topic', '/tf')
        self.declare_parameter('output_pose_topic', '/nova/perturbed/tf')
        self.declare_parameter('input_imu_topic', '/nova/imu')
        self.declare_parameter('output_imu_topic', '/nova/perturbed/imu')
        self.declare_parameter('input_contact_topic', '/nova/foot_contacts')
        self.declare_parameter('output_contact_topic', '/nova/perturbed/foot_contacts')
        self.declare_parameter('delay_ms', 0.0)
        self.declare_parameter('pose_noise_std_m', 0.0)
        self.declare_parameter('imu_accel_noise_std', 0.0)
        self.declare_parameter('imu_gyro_noise_std', 0.0)
        self.declare_parameter('contact_dropout_probability', 0.0)
        self.declare_parameter('noise_seed', 20260901)
        self.declare_parameter('enabled', True)
        self.declare_parameter('push_topic', '/nova/perturbations/wrench')
        self.declare_parameter('push_entity_name', 'nova_sm3')
        self.declare_parameter('push_force_x', 0.0)
        self.declare_parameter('push_force_y', 0.0)
        self.declare_parameter('push_force_z', 0.0)
        self.declare_parameter('push_start_s', -1.0)
        self.declare_parameter('push_duration_s', 0.10)

        self._enabled = bool(self.get_parameter('enabled').value)
        self._delay = max(0.0, float(self.get_parameter('delay_ms').value) / 1000.0)
        self._pose_std = max(0.0, float(self.get_parameter('pose_noise_std_m').value))
        self._accel_std = max(0.0, float(self.get_parameter('imu_accel_noise_std').value))
        self._gyro_std = max(0.0, float(self.get_parameter('imu_gyro_noise_std').value))
        self._dropout = min(1.0, max(0.0, float(self.get_parameter('contact_dropout_probability').value)))
        self._rng = random.Random(int(self.get_parameter('noise_seed').value))
        self._queue = deque()
        self._push_start = float(self.get_parameter('push_start_s').value)
        self._push_duration = max(0.0, float(self.get_parameter('push_duration_s').value))
        self._push_t0 = time.monotonic()

        self._pose_pub = self.create_publisher(TFMessage, self.get_parameter('output_pose_topic').value, 10)
        self._imu_pub = self.create_publisher(Imu, self.get_parameter('output_imu_topic').value, 10)
        self._contact_pub = self.create_publisher(Contacts, self.get_parameter('output_contact_topic').value, 10)
        self._wrench_pub = self.create_publisher(EntityWrench, self.get_parameter('push_topic').value, 10)
        self.create_subscription(TFMessage, self.get_parameter('input_pose_topic').value, self._pose_cb, 20)
        self.create_subscription(Imu, self.get_parameter('input_imu_topic').value, self._imu_cb, 20)
        self.create_subscription(Contacts, self.get_parameter('input_contact_topic').value, self._contact_cb, 20)
        self.create_timer(0.002, self._flush)
        self.create_timer(0.005, self._push_cb)
        self.get_logger().info(
            'Perturbaciones: enabled=%s delay=%.1f ms pose=%.4f m accel=%.4f gyro=%.4f dropout=%.3f seed=%d'
            % (self._enabled, self._delay * 1000, self._pose_std, self._accel_std,
               self._gyro_std, self._dropout, int(self.get_parameter('noise_seed').value)))

    def _enqueue(self, publisher, message):
        if self._enabled and self._delay > 0:
            self._queue.append((time.monotonic() + self._delay, publisher, message))
        else:
            publisher.publish(message)

    def _flush(self):
        now = time.monotonic()
        while self._queue and self._queue[0][0] <= now:
            _, publisher, message = self._queue.popleft()
            publisher.publish(message)

    def _push_cb(self):
        """Publish a timed horizontal wrench for a Gazebo bridge.

        A negative ``push_start_s`` disables the push.  The topic can be
        bridged to Gazebo's world wrench topic when running the corresponding
        ros_gz_bridge configuration.
        """
        if not self._enabled or self._push_start < 0:
            return
        elapsed = time.monotonic() - self._push_t0
        if self._push_start <= elapsed < self._push_start + self._push_duration:
            msg = EntityWrench()
            msg.entity.name = str(self.get_parameter('push_entity_name').value)
            msg.entity.type = 2  # MODEL
            msg.wrench.force.x = float(self.get_parameter('push_force_x').value)
            msg.wrench.force.y = float(self.get_parameter('push_force_y').value)
            msg.wrench.force.z = float(self.get_parameter('push_force_z').value)
            self._wrench_pub.publish(msg)

    def _gauss(self, std):
        return self._rng.gauss(0.0, std) if self._enabled and std > 0 else 0.0

    def _pose_cb(self, msg):
        out = copy.deepcopy(msg)
        for transform in out.transforms:
            p = transform.transform.translation
            p.x += self._gauss(self._pose_std)
            p.y += self._gauss(self._pose_std)
            p.z += self._gauss(self._pose_std)
        self._enqueue(self._pose_pub, out)

    def _imu_cb(self, msg):
        out = copy.deepcopy(msg)
        a, g = out.linear_acceleration, out.angular_velocity
        a.x += self._gauss(self._accel_std); a.y += self._gauss(self._accel_std); a.z += self._gauss(self._accel_std)
        g.x += self._gauss(self._gyro_std); g.y += self._gauss(self._gyro_std); g.z += self._gauss(self._gyro_std)
        self._enqueue(self._imu_pub, out)

    def _contact_cb(self, msg):
        # Contacts has no boolean per-foot field; a dropout models a lost
        # contact packet and is therefore directly observable by the monitor.
        if self._enabled and self._rng.random() < self._dropout:
            return
        self._enqueue(self._contact_pub, copy.deepcopy(msg))


def main(args=None):
    rclpy.init(args=args)
    node = PerturbationInjector()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
