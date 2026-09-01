"""Publish isolated diagnostics to exercise the safety supervisor."""
import argparse
import json
import time

import rclpy
from rclpy.node import Node
from std_msgs.msg import Bool, String


class SafetyTestNode(Node):
    def __init__(self, scenario, output):
        super().__init__('nova_safety_test_node')
        self.scenario = scenario
        self.output = output
        self.triggered = False
        self.events = []
        self.pub_stability = self.create_publisher(String, '/nova/stability_test', 10)
        self.pub_contact = self.create_publisher(String, '/nova/contact_diagnostics_test', 10)
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
            self.pub_contact.publish(String(data=json.dumps({'comparison_available': True, 'match': False})))
        if elapsed >= 4.0:
            self.write_report()
            rclpy.shutdown()

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
    parser.add_argument('--scenario', choices=('margin', 'contact', 'timeout'), required=True)
    parser.add_argument('--output', required=True)
    parsed, ros_args = parser.parse_known_args(args)
    rclpy.init(args=ros_args)
    node = SafetyTestNode(parsed.scenario, parsed.output)
    rclpy.spin(node)
    node.destroy_node()


if __name__ == '__main__':
    main()
