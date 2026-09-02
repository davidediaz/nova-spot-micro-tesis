import os

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, OpaqueFunction, Shutdown
from launch.substitutions import Command, FindExecutable, LaunchConfiguration, PathJoinSubstitution
from launch_ros.actions import Node
from launch_ros.parameter_descriptions import ParameterFile, ParameterValue
from launch_ros.substitutions import FindPackageShare


def launch_setup(context):
    share = FindPackageShare('nova_sm3_description')
    model = PathJoinSubstitution([share, 'urdf', 'nova_sm3.urdf.xacro'])
    headless = LaunchConfiguration('headless')
    mujoco_model = LaunchConfiguration('mujoco_model')
    description_text = Command([
        FindExecutable(name='xacro'), ' ', model,
        ' use_fake_hardware:=false use_mujoco:=true headless:=', headless,
        ' mujoco_model:=', mujoco_model,
    ]).perform(context)
    description = {'robot_description': ParameterValue(description_text, value_type=str)}
    controllers = PathJoinSubstitution([share, 'config', 'controllers.yaml'])
    observations = PathJoinSubstitution([share, 'config', 'mujoco_observations.yaml'])

    state_publisher = Node(
        package='robot_state_publisher', executable='robot_state_publisher',
        output='both', parameters=[description, {'use_sim_time': True}])
    control = Node(
        package='mujoco_ros2_control', executable='ros2_control_node',
        output='both', emulate_tty=True,
        parameters=[{'use_sim_time': True}, ParameterFile(controllers),
                    ParameterFile(observations)],
        remappings=([('~/robot_description', '/robot_description')]
                    if os.environ.get('ROS_DISTRO') == 'humble' else []),
        on_exit=Shutdown())
    spawners = [Node(
        package='controller_manager', executable='spawner', output='both',
        arguments=[name, '--param-file', controllers])
        for name in ('joint_state_broadcaster', 'joint_trajectory_controller')]
    return [state_publisher, control, *spawners]


def generate_launch_description():
    return LaunchDescription([
        DeclareLaunchArgument('headless', default_value='false'),
        DeclareLaunchArgument('mujoco_model', default_value=PathJoinSubstitution([
            FindPackageShare('nova_sm3_description'), 'mujoco', 'nova_sm3.xml'])),
        OpaqueFunction(function=launch_setup),
    ])
