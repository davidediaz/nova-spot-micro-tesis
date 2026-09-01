import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription, TimerAction
from launch.substitutions import LaunchConfiguration
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node


def generate_launch_description():
    gait_share = get_package_share_directory('nova_gait_controller')
    nova_share = get_package_share_directory('nova_sm3_description')
    speed_factor = LaunchConfiguration('speed_factor')
    enable_stability_stop = LaunchConfiguration('enable_stability_stop')
    stability_topic = LaunchConfiguration('stability_topic')
    startup_grace_period = LaunchConfiguration('startup_grace_period')

    simulation = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(os.path.join(nova_share, 'launch', 'sim.launch.py')))
    controller = Node(
        package='nova_gait_controller', executable='gait_controller', output='screen',
        parameters=[os.path.join(gait_share, 'config', 'gaits.yaml'),
                    {'speed_factor': speed_factor}])
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
        parameters=[monitoring_parameters,
                    {'enable_stability_stop': enable_stability_stop,
                     'stability_topic': stability_topic,
                     'startup_grace_period': startup_grace_period}])
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
        DeclareLaunchArgument(
            'speed_factor', default_value='1.0',
            description='Factor multiplicativo de velocidad de las fases'),
        DeclareLaunchArgument(
            'enable_stability_stop', default_value='false',
            description='Habilita parada provocada por margen de estabilidad'),
        DeclareLaunchArgument(
            'stability_topic', default_value='/nova/stability',
            description='Tópico de estabilidad escuchado por el supervisor'),
        DeclareLaunchArgument(
            'startup_grace_period', default_value='8.0',
            description='Gracia de arranque del supervisor en segundos'),
        simulation,
        pose_bridge,
        TimerAction(period=5.0, actions=[
            controller, metrics, supervisor, contacts, contact_comparator,
            stability]),
    ])
