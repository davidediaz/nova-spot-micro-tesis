"""Publish isolated diagnostics to exercise the safety supervisor."""
import argparse
import json
from math import cos, radians, sin
import time

import rclpy
from geometry_msgs.msg import TransformStamped
from rclpy.node import Node
from std_msgs.msg import Bool, String
from tf2_msgs.msg import TFMessage
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint


JOINT_NAMES = [
    f'{leg}_{joint}_joint'
    for leg in ('front_left', 'front_right', 'rear_left', 'rear_right')
    for joint in ('coxa', 'femur', 'tibia')
]


class SafetyTestNode(Node):
    def __init__(self, scenario, output):
        super().__init__('nova_safety_test_node')
        self.scenario = scenario
        self.output = output
        self.triggered = False
        self.completed = False
        self.events = []
        self.pub_stability = self.create_publisher(String, '/nova/stability_test', 10)
        self.pub_contact = self.create_publisher(String, '/nova/contact_diagnostics_test', 10)
        self.pub_pose = self.create_publisher(TFMessage, '/nova/pose_test', 10)
        self.pub_trajectory = self.create_publisher(
            JointTrajectory, '/nova/joint_trajectory_test', 10)
        self.create_subscription(Bool, '/nova/safety/triggered', self.on_trigger, 10)
        self.create_subscription(String, '/nova/safety/status', self.on_status, 10)
        self.create_subscription(String, '/nova/gait_command', self.on_command, 10)
        self.started = time.monotonic()
        self.timer = self.create_timer(0.1, self.tick)

    def tick(self):
        elapsed = time.monotonic() - self.started
        if self.scenario == 'margin' and elapsed < 3.0:
            self.pub_stability.publish(String(data=json.dumps({'available': True, 'margin_m': -0.20})))
        elif self.scenario == 'contact' and elapsed < 3.0:
            self.pub_contact.publish(String(data=json.dumps({
                'comparison_available': True,
                'match': False,
                'expected_contacts': ['fl', 'fr', 'rl'],
                'observed_contacts': ['fl', 'fr'],
            })))
        elif self.scenario in ('low_height', 'high_height', 'roll', 'pitch') and elapsed < 3.0:
            self.pub_pose.publish(self.unsafe_pose())
        elif self.scenario in ('joint_limit', 'discontinuity') and elapsed < 3.0:
            self.pub_trajectory.publish(self.invalid_trajectory())
        if elapsed >= 4.0:
            self.write_report()
            self.completed = True
            self.timer.cancel()

    def unsafe_pose(self):
        transform = TransformStamped()
        transform.child_frame_id = 'nova_sm3'
        if self.scenario == 'low_height':
            transform.transform.translation.z = 0.10
        elif self.scenario == 'high_height':
            transform.transform.translation.z = 0.36
        else:
            transform.transform.translation.z = 0.224
        angle = radians(30.0)
        if self.scenario == 'roll':
            transform.transform.rotation.x = sin(angle / 2.0)
        elif self.scenario == 'pitch':
            transform.transform.rotation.y = sin(angle / 2.0)
        transform.transform.rotation.w = cos(angle / 2.0) if self.scenario in ('roll', 'pitch') else 1.0
        return TFMessage(transforms=[transform])

    def invalid_trajectory(self):
        message = JointTrajectory(joint_names=JOINT_NAMES)
        first = JointTrajectoryPoint(positions=[0.0] * 12)
        first.time_from_start.sec = 1
        if self.scenario == 'joint_limit':
            first.positions[0] = 0.70
            message.points = [first]
        else:
            second = JointTrajectoryPoint(positions=[0.0] * 12)
            second.positions[0] = 0.40
            second.time_from_start.sec = 2
            message.points = [first, second]
        return message

    def on_trigger(self, message):
        self.triggered = bool(message.data)
        self.events.append({'triggered': self.triggered, 't': time.monotonic() - self.started})

    def on_status(self, message):
        self.events.append({'status': message.data, 't': time.monotonic() - self.started})

    def on_command(self, message):
        self.events.append({'command': message.data, 't': time.monotonic() - self.started})

    def write_report(self):
        payload = {'scenario': self.scenario, 'triggered': self.triggered,
                   'events': self.events, 'duration_s': time.monotonic() - self.started}
        with open(self.output, 'w', encoding='utf-8') as stream:
            json.dump(payload, stream, ensure_ascii=False, indent=2)


def main(args=None):
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--scenario',
        choices=(
            'margin', 'contact', 'timeout', 'low_height', 'high_height',
            'roll', 'pitch', 'joint_limit', 'discontinuity'),
        required=True)
    parser.add_argument('--output', required=True)
    parsed, ros_args = parser.parse_known_args(args)
    rclpy.init(args=ros_args)
    node = SafetyTestNode(parsed.scenario, parsed.output)
    while rclpy.ok() and not node.completed:
        rclpy.spin_once(node, timeout_sec=0.2)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
