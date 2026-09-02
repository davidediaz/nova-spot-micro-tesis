"""Independent, latched and conservative supervisor for simulation."""

import json
import time
from math import degrees, radians

import rclpy
from rclpy.executors import ExternalShutdownException
from rclpy.node import Node
from std_msgs.msg import Bool, String
from tf2_msgs.msg import TFMessage
from trajectory_msgs.msg import JointTrajectory

from .safety import (
    diagnostic_reasons, invalid_trajectory_reasons, quaternion_to_rpy,
    reference_jump_reasons, stale_sources, unsafe_reasons,
)


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
        self.declare_parameter('trajectory_topic',
                               '/joint_trajectory_controller/joint_trajectory')
        self.declare_parameter('contact_diagnostics_topic',
                               '/nova/contact_diagnostics')
        self.declare_parameter('stability_topic', '/nova/stability')
        self.declare_parameter('status_topic', '/nova/safety/status')
        self.declare_parameter('data_timeout', 0.50)
        self.declare_parameter('min_stability_margin', -0.005)
        self.declare_parameter('enable_reference_stop', True)
        self.declare_parameter('enable_data_timeout_stop', False)
        self.declare_parameter('enable_contact_stop', False)
        self.declare_parameter('enable_stability_stop', False)
        self.command = self.create_publisher(
            String, self.get_parameter('command_topic').value, 10)
        self.triggered = self.create_publisher(Bool, '/nova/safety/triggered', 10)
        self.status = self.create_publisher(
            String, self.get_parameter('status_topic').value, 10)
        self.subscription = self.create_subscription(
            TFMessage, self.get_parameter('pose_topic').value,
            self.pose_callback, 10)
        self.create_subscription(
            JointTrajectory, self.get_parameter('trajectory_topic').value,
            self.trajectory_callback, 10)
        self.create_subscription(
            String, self.get_parameter('contact_diagnostics_topic').value,
            self.contact_callback, 10)
        self.create_subscription(
            String, self.get_parameter('stability_topic').value,
            self.stability_callback, 10)
        self.started_at = self.get_clock().now()
        self.started_monotonic = time.monotonic()
        self.last_received = {'pose': None, 'contacts': None, 'stability': None}
        self.latest_contact = None
        self.latest_stability = None
        self.unsafe_count = 0
        self.last_reference_positions = None
        self.latched = False
        self.create_timer(0.10, self.watchdog_callback)
        self.get_logger().info(
            'Supervisor listo (simulación): altura %.3f--%.3f m, inclinación %.1f grados.' % (
                self.get_parameter('min_height').value,
                self.get_parameter('max_height').value,
                self.get_parameter('max_tilt_deg').value))

    def pose_callback(self, message):
        self.last_received['pose'] = time.monotonic()
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
        self.trigger(','.join(reasons), {
            'height_m': pose.translation.z, 'roll_deg': degrees(roll),
            'pitch_deg': degrees(pitch)})

    def trajectory_callback(self, message):
        if self.latched or not self.get_parameter('enable_reference_stop').value:
            return
        reasons = invalid_trajectory_reasons(message.joint_names, message.points)
        if message.points:
            reasons.extend(reference_jump_reasons(
                self.last_reference_positions, message.points[0].positions))
        if reasons:
            self.trigger(','.join(reasons))
            return
        self.last_reference_positions = tuple(message.points[-1].positions)

    def contact_callback(self, message):
        self.last_received['contacts'] = time.monotonic()
        try:
            self.latest_contact = json.loads(message.data)
        except (TypeError, ValueError):
            self.latest_contact = None
            if self.get_parameter('enable_contact_stop').value:
                self.trigger('contacto_json_invalido')

    def stability_callback(self, message):
        self.last_received['stability'] = time.monotonic()
        try:
            self.latest_stability = json.loads(message.data)
        except (TypeError, ValueError):
            self.latest_stability = None

    def watchdog_callback(self):
        if self.latched:
            return
        now = time.monotonic()
        if now - self.started_monotonic < float(
                self.get_parameter('startup_grace_period').value):
            return
        timeout = float(self.get_parameter('data_timeout').value)
        missing = stale_sources(self.last_received, now, timeout)
        if missing and self.get_parameter('enable_data_timeout_stop').value:
            self.trigger('datos_vencidos:' + ','.join(missing))
            return
        diagnostic = diagnostic_reasons(
            self.latest_contact if self.get_parameter('enable_contact_stop').value else None,
            self.latest_stability if self.get_parameter('enable_stability_stop').value else None,
            float(self.get_parameter('min_stability_margin').value))
        if diagnostic:
            self.trigger(','.join(diagnostic), {
                'margin_m': (self.latest_stability or {}).get('margin_m')})

    def trigger(self, reason, values=None):
        if self.latched:
            return
        self.latched = True
        data = {'latched': True, 'reason': reason, 'values': values or {},
                'simulation_only': True}
        self.command.publish(String(data='stand'))
        self.triggered.publish(Bool(data=True))
        self.status.publish(String(data=json.dumps(data, separators=(',', ':'))))
        self.get_logger().error('PARADA PREVENTIVA -> stand: %s' % reason)


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
