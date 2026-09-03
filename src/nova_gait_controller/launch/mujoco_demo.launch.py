import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription, TimerAction
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node
from launch_ros.parameter_descriptions import ParameterValue


def generate_launch_description():
    gait_share = get_package_share_directory('nova_gait_controller')
    nova_share = get_package_share_directory('nova_sm3_description')

    simulation = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(nova_share, 'launch', 'mujoco_sim.launch.py')),
        launch_arguments={
            'headless': LaunchConfiguration('headless'),
            'sim_speed_factor': LaunchConfiguration('sim_speed_factor'),
            'mujoco_model': LaunchConfiguration('mujoco_model'),
        }.items())
    controller = Node(
        package='nova_gait_controller', executable='gait_controller', output='screen',
        parameters=[os.path.join(gait_share, 'config', 'gaits.yaml'), {
            'step_fore_aft_shift': ParameterValue(
                LaunchConfiguration('step_fore_aft_shift'), value_type=float),
            'step_height': ParameterValue(
                LaunchConfiguration('step_height'), value_type=float),
        }])
    monitoring = os.path.join(gait_share, 'config', 'monitoring.yaml')
    metrics = Node(
        package='nova_gait_controller', executable='metrics_node', output='screen',
        parameters=[monitoring])
    comparator = Node(
        package='nova_gait_controller', executable='contact_comparator', output='screen',
        parameters=[monitoring])
    stability = Node(
        package='nova_gait_controller', executable='stability_monitor', output='screen',
        parameters=[monitoring])
    safety = Node(
        package='nova_gait_controller', executable='safety_supervisor', output='screen',
        parameters=[monitoring])

    return LaunchDescription([
        DeclareLaunchArgument('headless', default_value='false'),
        DeclareLaunchArgument('sim_speed_factor', default_value='1.0'),
        DeclareLaunchArgument('step_fore_aft_shift', default_value='0.0'),
        DeclareLaunchArgument('step_height', default_value='0.008'),
        DeclareLaunchArgument(
            'mujoco_model',
            default_value=os.path.join(
                nova_share, 'mujoco', 'nova_sm3.xml')),
        simulation,
        TimerAction(period=5.0, actions=[controller, metrics, comparator,
                                         stability, safety]),
    ])
