"""Publish a nominal online support polygon and static stability margin."""

import json

import rclpy
from rclpy.executors import ExternalShutdownException
from rclpy.node import Node
from sensor_msgs.msg import JointState
from std_msgs.msg import String
from tf2_msgs.msg import TFMessage

from .stability import nominal_foot_points, support_result


class StabilityMonitor(Node):
    def __init__(self):
        super().__init__('nova_stability_monitor')
        self.declare_parameter('pose_topic', '/world/empty/dynamic_pose/info')
        self.declare_parameter('model_frame', 'nova_sm3')
        self.declare_parameter('contacts_topic', '/nova/foot_contacts')
        self.declare_parameter('joint_states_topic', '/joint_states')
        self.declare_parameter('output_topic', '/nova/stability')
        self.pose = None
        self.joints = None
        self.contacts = None
        self.publisher = self.create_publisher(
            String, self.get_parameter('output_topic').value, 10)
        self.create_subscription(TFMessage, self.get_parameter('pose_topic').value,
                                 self.pose_callback, 10)
        self.create_subscription(JointState,
                                 self.get_parameter('joint_states_topic').value,
                                 self.joints_callback, 10)
        self.create_subscription(String, self.get_parameter('contacts_topic').value,
                                 self.contacts_callback, 10)

    def pose_callback(self, message):
        model = self.get_parameter('model_frame').value
        item = next((tf for tf in message.transforms
                     if tf.child_frame_id == model), None)
        if item is not None:
            self.pose = item.transform
            self.publish()

    def joints_callback(self, message):
        self.joints = message

    def contacts_callback(self, message):
        try:
            self.contacts = json.loads(message.data)
        except (TypeError, ValueError):
            self.contacts = None

    def publish(self):
        if self.pose is None or self.joints is None or self.contacts is None:
            return
        translation = self.pose.translation
        rotation = self.pose.rotation
        try:
            points = nominal_foot_points(
                self.joints.name, self.joints.position,
                (translation.x, translation.y, translation.z),
                (rotation.x, rotation.y, rotation.z, rotation.w))
        except KeyError:
            return
        contacts = self.contacts.get('observed_contacts', [])
        result = support_result((translation.x, translation.y), points, contacts)
        data = {
            'stamp_sec': self.contacts.get('stamp_sec'),
            'model': 'nominal_not_identified',
            'contacts': contacts,
            'com_projection_xy': [translation.x, translation.y],
            'foot_points_xy': {leg: [point[0], point[1]]
                               for leg, point in points.items()},
            **result,
        }
        self.publisher.publish(String(data=json.dumps(data, separators=(',', ':'))))


def main(args=None):
    rclpy.init(args=args)
    node = StabilityMonitor()
    try:
        rclpy.spin(node)
    except (KeyboardInterrupt, ExternalShutdownException):
        pass
    finally:
        node.destroy_node()
        if rclpy.ok():
            rclpy.shutdown()
