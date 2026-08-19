"""Independent provisional pose supervisor for simulation."""

from math import degrees, radians

import rclpy
from rclpy.executors import ExternalShutdownException
from rclpy.node import Node
from std_msgs.msg import Bool, String
from tf2_msgs.msg import TFMessage

from .safety import quaternion_to_rpy, unsafe_reasons


class SafetySupervisor(Node):
    def __init__(self):
        super().__init__('nova_safety_supervisor')
        self.declare_parameter('pose_topic', '/world/empty/dynamic_pose/info')
        self.declare_parameter('model_frame', 'nova_sm3')
        self.declare_parameter('command_topic', '/nova/gait_command')
        self.declare_parameter('min_height', 0.16)
        self.declare_parameter('max_height', 0.32)
        self.declare_parameter('max_tilt_deg', 20.0)
        self.declare_parameter('consecutive_unsafe_samples', 3)
        self.declare_parameter('startup_grace_period', 8.0)
        self.command = self.create_publisher(
            String, self.get_parameter('command_topic').value, 10)
        self.triggered = self.create_publisher(Bool, '/nova/safety/triggered', 10)
        self.subscription = self.create_subscription(
            TFMessage, self.get_parameter('pose_topic').value,
            self.pose_callback, 10)
        self.started_at = self.get_clock().now()
        self.unsafe_count = 0
        self.latched = False
        self.get_logger().info(
            'Supervisor listo (simulación): altura %.3f--%.3f m, inclinación %.1f grados.' % (
                self.get_parameter('min_height').value,
                self.get_parameter('max_height').value,
                self.get_parameter('max_tilt_deg').value))

    def pose_callback(self, message):
        if self.latched or not message.transforms:
            return
        elapsed = (self.get_clock().now() - self.started_at).nanoseconds * 1e-9
        if elapsed < float(self.get_parameter('startup_grace_period').value):
            return
        model_frame = self.get_parameter('model_frame').value
        model_transform = next((item for item in message.transforms
                                if item.child_frame_id == model_frame), None)
        if model_transform is None:
            return
        pose = model_transform.transform
        roll, pitch, _ = quaternion_to_rpy(
            pose.rotation.x, pose.rotation.y, pose.rotation.z, pose.rotation.w)
        reasons = unsafe_reasons(
            pose.translation.z, roll, pitch,
            float(self.get_parameter('min_height').value),
            float(self.get_parameter('max_height').value),
            radians(float(self.get_parameter('max_tilt_deg').value)))
        self.unsafe_count = self.unsafe_count + 1 if reasons else 0
        required = int(self.get_parameter('consecutive_unsafe_samples').value)
        if self.unsafe_count < required:
            return
        self.latched = True
        self.command.publish(String(data='stand'))
        self.triggered.publish(Bool(data=True))
        self.get_logger().error(
            'PARADA PREVENTIVA -> stand: %s; z=%.3f m, roll=%.1f°, pitch=%.1f°' % (
                ','.join(reasons), pose.translation.z, degrees(roll), degrees(pitch)))


def main(args=None):
    rclpy.init(args=args)
    node = SafetySupervisor()
    try:
        rclpy.spin(node)
    except (KeyboardInterrupt, ExternalShutdownException):
        pass
    finally:
        node.destroy_node()
        if rclpy.ok():
            rclpy.shutdown()
