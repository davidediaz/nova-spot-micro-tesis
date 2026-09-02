"""Common command-side backlash, delay and slew model for both simulators."""
from collections import deque
import copy
import time

import rclpy
from rclpy.node import Node
from trajectory_msgs.msg import JointTrajectory

from .mathematical_model import apply_backlash


class ActuatorModelNode(Node):
    def __init__(self):
        super().__init__('nova_actuator_model')
        self.declare_parameter('input_topic', '/nova/ideal_trajectory')
        self.declare_parameter('output_topic', '/joint_trajectory_controller/joint_trajectory')
        self.declare_parameter('backlash_rad', 0.0)
        self.declare_parameter('command_delay_ms', 0.0)
        self.declare_parameter('max_speed_rad_s', 6.981317)
        self._backlash = float(self.get_parameter('backlash_rad').value)
        self._delay = float(self.get_parameter('command_delay_ms').value) / 1000.0
        self._speed = float(self.get_parameter('max_speed_rad_s').value)
        if self._backlash < 0 or self._delay < 0 or self._speed <= 0:
            raise ValueError('Parámetros físicos del actuador fuera de rango')
        self._previous = {}; self._queue = deque()
        self._last_time = time.monotonic()
        self._publisher = self.create_publisher(
            JointTrajectory, self.get_parameter('output_topic').value, 10)
        self.create_subscription(JointTrajectory,
                                 self.get_parameter('input_topic').value,
                                 self._callback, 10)
        self.create_timer(0.002, self._flush)

    def _callback(self, message):
        if not message.points:
            return
        now = time.monotonic(); dt = max(1e-6, now - self._last_time); self._last_time = now
        output = copy.deepcopy(message)
        for point in output.points:
            values = []
            for name, target in zip(output.joint_names, point.positions):
                previous = self._previous.get(name, float(target))
                value = apply_backlash(target, previous, self._backlash)
                delta = max(-self._speed * dt, min(self._speed * dt, value - previous))
                value = previous + delta; self._previous[name] = value; values.append(value)
            point.positions = values
        self._queue.append((now + self._delay, output))

    def _flush(self):
        now = time.monotonic()
        while self._queue and self._queue[0][0] <= now:
            self._publisher.publish(self._queue.popleft()[1])


def main(args=None):
    rclpy.init(args=args); node = ActuatorModelNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node(); rclpy.shutdown()
