"""Compare the low-rate consolidated contacts with the gait phase plan."""

import json

import rclpy
from rclpy.callback_groups import MutuallyExclusiveCallbackGroup
from rclpy.executors import ExternalShutdownException, MultiThreadedExecutor
from rclpy.node import Node
from std_msgs.msg import String

from .contacts import compare_contact_sets


class ContactComparator(Node):
    def __init__(self):
        super().__init__('nova_contact_comparator')
        self.declare_parameter('gait_phase_topic', '/nova/gait_phase')
        self.declare_parameter('contacts_topic', '/nova/foot_contacts')
        self.declare_parameter('diagnostics_topic', '/nova/contact_diagnostics')
        self.phase = None
        self.measured = None
        self.phase_callbacks = MutuallyExclusiveCallbackGroup()
        self.contact_callbacks = MutuallyExclusiveCallbackGroup()
        self.publisher = self.create_publisher(
            String, self.get_parameter('diagnostics_topic').value, 10)
        self.create_subscription(
            String, self.get_parameter('gait_phase_topic').value,
            self.phase_callback, 20, callback_group=self.phase_callbacks)
        self.create_subscription(
            String, self.get_parameter('contacts_topic').value,
            self.contacts_callback, 1, callback_group=self.contact_callbacks)
        self.get_logger().info(
            'Comparador fase-contacto listo; sin actuación automática.')

    def phase_callback(self, message):
        try:
            self.phase = json.loads(message.data)
            self.publish_diagnostic()
        except (TypeError, ValueError):
            self.get_logger().warning('Fase de marcha con JSON inválido.')

    def contacts_callback(self, message):
        try:
            self.measured = json.loads(message.data)
        except (TypeError, ValueError):
            self.get_logger().warning('Contactos medidos con JSON inválido.')
            return
        self.publish_diagnostic()

    def publish_diagnostic(self):
        if self.measured is None:
            return
        measured = self.measured
        plan_available = bool(
            self.phase and self.phase.get('contact_plan_available', False))
        expected = self.phase.get('expected_contacts', []) if plan_available else []
        observed = measured.get('observed_contacts', [])
        sensors_valid = bool(measured.get('all_sensors_valid', False))
        diagnostic = {
            'stamp_sec': measured.get('stamp_sec'),
            'comparison_available': plan_available and sensors_valid,
            'contact_plan_available': plan_available,
            'all_sensors_valid': sensors_valid,
            'mode': self.phase.get('mode') if self.phase else None,
            'cycle_index': self.phase.get('cycle_index') if self.phase else None,
            'sample_index': self.phase.get('sample_index') if self.phase else None,
            'expected_contacts': expected,
            'observed_contacts': observed,
            **compare_contact_sets(expected, observed),
        }
        if not diagnostic['comparison_available']:
            diagnostic['match'] = None
        self.publisher.publish(String(
            data=json.dumps(diagnostic, separators=(',', ':'))))


def main(args=None):
    rclpy.init(args=args)
    node = ContactComparator()
    executor = MultiThreadedExecutor(num_threads=2)
    executor.add_node(node)
    try:
        executor.spin()
    except (KeyboardInterrupt, ExternalShutdownException):
        pass
    finally:
        executor.shutdown()
        node.destroy_node()
        if rclpy.ok():
            rclpy.shutdown()
