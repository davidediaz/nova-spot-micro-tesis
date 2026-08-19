"""Synchronized body-pose and joint-state metrics for experiments."""

import json
from math import degrees

import rclpy
from diagnostic_msgs.msg import DiagnosticArray, DiagnosticStatus, KeyValue
from rclpy.executors import ExternalShutdownException
from rclpy.node import Node
from sensor_msgs.msg import JointState
from std_msgs.msg import String
from tf2_msgs.msg import TFMessage

from .safety import quaternion_to_rpy


class MetricsNode(Node):
    def __init__(self):
        super().__init__('nova_metrics')
        self.declare_parameter('pose_topic', '/world/empty/dynamic_pose/info')
        self.declare_parameter('model_frame', 'nova_sm3')
        self.declare_parameter('joint_states_topic', '/joint_states')
        self.declare_parameter('sync_tolerance', 0.10)
        self.declare_parameter('sync_queue_size', 30)
        self.diagnostics = self.create_publisher(
            DiagnosticArray, '/nova/metrics/diagnostics', 10)
        self.json_publisher = self.create_publisher(String, '/nova/metrics/json', 10)

        self.latest_joints = None
        self.latest_joints_received = None
        self.create_subscription(
            JointState, self.get_parameter('joint_states_topic').value,
            self.joints_callback, 30)
        self.create_subscription(
            TFMessage, self.get_parameter('pose_topic').value,
            self.pose_callback, 30)
        self.get_logger().info('Métricas listas: odometría y articulaciones sincronizadas.')

    def joints_callback(self, message):
        self.latest_joints = message
        self.latest_joints_received = self.get_clock().now()

    @staticmethod
    def stamp_seconds(stamp):
        return stamp.sec + stamp.nanosec * 1e-9

    def pose_callback(self, message):
        if not message.transforms or self.latest_joints is None:
            return
        model_frame = self.get_parameter('model_frame').value
        transform = next((item for item in message.transforms
                          if item.child_frame_id == model_frame), None)
        if transform is None:
            return
        joints = self.latest_joints
        pose_received = self.get_clock().now()
        joint_stamp = self.stamp_seconds(joints.header.stamp)
        # Gazebo Pose_V has no per-transform timestamp in this bridge version,
        # so synchronization uses ROS reception time while the sample retains
        # the simulation timestamp supplied by JointState.
        sync_error = abs(
            (pose_received - self.latest_joints_received).nanoseconds * 1e-9)
        if sync_error > float(self.get_parameter('sync_tolerance').value):
            return
        pose = transform.transform
        roll, pitch, yaw = quaternion_to_rpy(
            pose.rotation.x, pose.rotation.y, pose.rotation.z, pose.rotation.w)
        data = {
            'stamp_sec': joint_stamp,
            'sync_error_s': sync_error,
            'x_m': pose.translation.x,
            'y_m': pose.translation.y,
            'height_m': pose.translation.z,
            'roll_deg': degrees(roll),
            'pitch_deg': degrees(pitch),
            'yaw_deg': degrees(yaw),
            'joint_names': list(joints.name),
            'joint_positions_rad': list(joints.position),
            'joint_velocities_rad_s': list(joints.velocity),
        }
        self.json_publisher.publish(String(data=json.dumps(data, separators=(',', ':'))))

        status = DiagnosticStatus(
            level=DiagnosticStatus.OK, name='nova_sm3/body_and_joints',
            message='muestra sincronizada', hardware_id='nova_sm3_sim')
        status.values = [KeyValue(key=key, value=f'{value:.9g}') for key, value in (
            ('x_m', data['x_m']), ('y_m', data['y_m']),
            ('height_m', data['height_m']), ('roll_deg', data['roll_deg']),
            ('pitch_deg', data['pitch_deg']), ('yaw_deg', data['yaw_deg']),
            ('joint_count', len(joints.name)))]
        self.diagnostics.publish(DiagnosticArray(header=transform.header, status=[status]))


def main(args=None):
    rclpy.init(args=args)
    node = MetricsNode()
    try:
        rclpy.spin(node)
    except (KeyboardInterrupt, ExternalShutdownException):
        pass
    finally:
        node.destroy_node()
        if rclpy.ok():
            rclpy.shutdown()
