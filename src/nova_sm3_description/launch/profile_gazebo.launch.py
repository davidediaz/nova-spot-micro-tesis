"""Launch a generated, audited Gazebo profile."""
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription, OpaqueFunction, TimerAction
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution
from launch_ros.actions import Node
from launch_ros.parameter_descriptions import ParameterValue
from launch_ros.substitutions import FindPackageShare


def setup(context):
    model_file = LaunchConfiguration('model_file').perform(context)
    world_file = LaunchConfiguration('world_file').perform(context)
    description = {'robot_description': ParameterValue(
        open(model_file, encoding='utf-8').read(), value_type=str)}
    gz = IncludeLaunchDescription(PythonLaunchDescriptionSource(PathJoinSubstitution(
        [FindPackageShare('ros_gz_sim'), 'launch', 'gz_sim.launch.py'])),
        launch_arguments={'gz_args': f'-r -s {world_file}'}.items())
    publisher = Node(package='robot_state_publisher', executable='robot_state_publisher',
                     parameters=[description, {'use_sim_time': True}])
    spawn = Node(package='ros_gz_sim', executable='create',
                 arguments=['-topic', 'robot_description', '-name', 'nova_sm3', '-z', '0.245'])
    controllers = PathJoinSubstitution([FindPackageShare('nova_sm3_description'), 'config', 'controllers.yaml'])
    spawners = [Node(package='controller_manager', executable='spawner',
                     arguments=[name, '--param-file', controllers])
                for name in ('joint_state_broadcaster', 'joint_trajectory_controller')]
    return [gz, publisher, spawn, TimerAction(period=5.0, actions=spawners)]


def generate_launch_description():
    return LaunchDescription([
        DeclareLaunchArgument('model_file'), DeclareLaunchArgument('world_file'),
        OpaqueFunction(function=setup)])
