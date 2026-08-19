import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription, TimerAction
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node


def generate_launch_description():
    gait_share = get_package_share_directory('nova_gait_controller')
    nova_share = get_package_share_directory('nova_sm3_description')

    simulation = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(nova_share, 'launch', 'mujoco_sim.launch.py')),
        launch_arguments={'headless': LaunchConfiguration('headless')}.items())
    controller = Node(
        package='nova_gait_controller', executable='gait_controller', output='screen',
        parameters=[os.path.join(gait_share, 'config', 'gaits.yaml')])

    return LaunchDescription([
        DeclareLaunchArgument('headless', default_value='false'),
        simulation,
        TimerAction(period=5.0, actions=[controller]),
    ])
