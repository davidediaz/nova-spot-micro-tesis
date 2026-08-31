"""Publish measured foot contacts and compare them with the gait phase plan."""

import json
import time

import rclpy
from rclpy.executors import ExternalShutdownException
from rclpy.node import Node
from rclpy.qos import DurabilityPolicy, HistoryPolicy, QoSProfile, ReliabilityPolicy
from ros_gz_interfaces.msg import Contacts
from std_msgs.msg import String

from .contacts import LEG_NAMES, approximate_contact_force, debounced_contact


CONTACT_INPUTS = {
    'fl': '/nova/contacts/front_left',
    'fr': '/nova/contacts/front_right',
    'rl': '/nova/contacts/rear_left',
    'rr': '/nova/contacts/rear_right',
}


class ContactMonitor(Node):
    def __init__(self):
        super().__init__('nova_contact_monitor')
        self.declare_parameter('contacts_topic', '/nova/foot_contacts')
        self.declare_parameter('contact_timeout', 0.10)
        self.declare_parameter('contact_off_debounce', 0.12)
        self.declare_parameter('contact_on_debounce', 0.03)

        self.samples = {
            leg: {'contact': False, 'approximate_force_n': 0.0,
                  'received_at': None, 'sensor_stamp_sec': None}
            for leg in LEG_NAMES
        }
        self.last_publish_at = 0.0
        self.last_contact_processed = {leg: 0.0 for leg in LEG_NAMES}
        self.filters = {
            leg: {'initialized': False, 'stable': False, 'candidate': None,
                  'candidate_since': None} for leg in LEG_NAMES}
        self.contacts_publisher = self.create_publisher(
            String, self.get_parameter('contacts_topic').value, 10)
        contact_qos = QoSProfile(
            history=HistoryPolicy.KEEP_LAST, depth=1,
            reliability=ReliabilityPolicy.BEST_EFFORT,
            durability=DurabilityPolicy.VOLATILE)
        for leg, topic in CONTACT_INPUTS.items():
            self.create_subscription(
                Contacts, topic,
                lambda message, selected_leg=leg: self.contact_callback(
                    selected_leg, message),
                contact_qos)
        self.get_logger().info(
            'Agregador de contactos listo; salida limitada a 100 Hz.')

    def contact_callback(self, leg, message):
        now = time.monotonic()
        if now - self.last_contact_processed[leg] < 0.005:
            return
        self.last_contact_processed[leg] = now
        self.samples[leg] = {
            'contact': bool(message.contacts),
            'approximate_force_n': approximate_contact_force(message.contacts),
            'received_at': time.monotonic(),
            'sensor_stamp_sec': (message.header.stamp.sec
                                 + message.header.stamp.nanosec * 1e-9),
        }
        if now - self.last_publish_at >= 0.01:
            self.last_publish_at = now
            self.publish()

    def publish(self):
        now = time.monotonic()
        timeout = float(self.get_parameter('contact_timeout').value)
        feet = {}
        observed = []
        all_valid = True
        for leg in LEG_NAMES:
            sample = self.samples[leg]
            received_at = sample['received_at']
            age = None if received_at is None else max(0.0, now - received_at)
            # Gazebo contact sensors publish while a collision exists and can
            # become silent after liftoff. Once initialized, silence beyond
            # the timeout therefore means no contact, not a dead sensor.
            valid = age is not None
            raw_contact = bool(valid and age <= timeout and sample['contact'])
            state = self.filters[leg]
            if valid and not state['initialized']:
                state.update(initialized=True, stable=raw_contact,
                             candidate=None, candidate_since=None)
            elif valid:
                stable, candidate, since = debounced_contact(
                    state['stable'], state['candidate'],
                    state['candidate_since'], raw_contact, now,
                    float(self.get_parameter('contact_off_debounce').value),
                    float(self.get_parameter('contact_on_debounce').value))
                state.update(stable=stable, candidate=candidate,
                             candidate_since=since)
            contact = bool(valid and state['stable'])
            all_valid = all_valid and valid
            if contact:
                observed.append(leg)
            feet[leg] = {
                'contact': contact,
                'raw_contact': raw_contact,
                'transition_pending': state['candidate_since'] is not None,
                'valid': valid,
                'age_s': age,
                'approximate_force_n': (sample['approximate_force_n']
                                        if contact else 0.0),
            }

        sensor_stamps = [sample['sensor_stamp_sec'] for sample in self.samples.values()
                         if sample['sensor_stamp_sec'] is not None]
        stamp = max(sensor_stamps) if sensor_stamps else None
        measured = {
            'stamp_sec': stamp,
            'all_sensors_valid': all_valid,
            'observed_contacts': observed,
            'feet': feet,
        }
        self.contacts_publisher.publish(String(
            data=json.dumps(measured, separators=(',', ':'))))


def main(args=None):
    rclpy.init(args=args)
    node = ContactMonitor()
    try:
        rclpy.spin(node)
    except (KeyboardInterrupt, ExternalShutdownException):
        pass
    except RuntimeError:
        # The Gazebo bridge can destroy its contact type support while this
        # subscriber is shutting down. Do not hide errors during normal run.
        if rclpy.ok():
            raise
    finally:
        node.destroy_node()
        if rclpy.ok():
            rclpy.shutdown()
