import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, TimerAction
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node


def generate_launch_description():
    gait_share = get_package_share_directory('nova_gait_controller')
    nova_share = get_package_share_directory('nova_sm3_description')

    simulation = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(os.path.join(nova_share, 'launch', 'sim.launch.py')))
    controller = Node(
        package='nova_gait_controller', executable='gait_controller', output='screen',
        parameters=[os.path.join(gait_share, 'config', 'gaits.yaml')])
    monitoring_parameters = os.path.join(gait_share, 'config', 'monitoring.yaml')
    pose_bridge = Node(
        package='ros_gz_bridge', executable='parameter_bridge', output='screen',
        arguments=[
            '/world/empty/dynamic_pose/info@tf2_msgs/msg/TFMessage[gz.msgs.Pose_V',
            '/nova/contacts/front_left@ros_gz_interfaces/msg/Contacts[gz.msgs.Contacts',
            '/nova/contacts/front_right@ros_gz_interfaces/msg/Contacts[gz.msgs.Contacts',
            '/nova/contacts/rear_left@ros_gz_interfaces/msg/Contacts[gz.msgs.Contacts',
            '/nova/contacts/rear_right@ros_gz_interfaces/msg/Contacts[gz.msgs.Contacts',
            '/nova/imu@sensor_msgs/msg/Imu[gz.msgs.IMU',
        ])
    metrics = Node(
        package='nova_gait_controller', executable='metrics_node', output='screen',
        parameters=[monitoring_parameters])
    supervisor = Node(
        package='nova_gait_controller', executable='safety_supervisor', output='screen',
        parameters=[monitoring_parameters])
    contacts = Node(
        package='nova_gait_controller', executable='contact_monitor', output='screen',
        parameters=[monitoring_parameters])
    contact_comparator = Node(
        package='nova_gait_controller', executable='contact_comparator', output='screen',
        parameters=[monitoring_parameters])
    stability = Node(
        package='nova_gait_controller', executable='stability_monitor',
        output='screen', parameters=[monitoring_parameters])

    return LaunchDescription([
        simulation,
        pose_bridge,
        TimerAction(period=5.0, actions=[
            controller, metrics, supervisor, contacts, contact_comparator,
            stability]),
    ])
