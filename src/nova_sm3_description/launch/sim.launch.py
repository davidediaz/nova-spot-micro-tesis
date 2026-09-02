from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, TimerAction
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import Command, PathJoinSubstitution
from launch_ros.actions import Node
from launch_ros.parameter_descriptions import ParameterValue
from launch_ros.substitutions import FindPackageShare


def generate_launch_description():
    share = FindPackageShare('nova_sm3_description')
    model = PathJoinSubstitution([share, 'urdf', 'nova_sm3.urdf.xacro'])
    description = {'robot_description': ParameterValue(Command([
        'xacro ', model,
        ' use_fake_hardware:=false use_mujoco:=false use_gazebo:=true',
    ]), value_type=str)}
    gz = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(PathJoinSubstitution(
            [FindPackageShare('ros_gz_sim'), 'launch', 'gz_sim.launch.py'])),
        launch_arguments={'gz_args': [
            '-r -s ', PathJoinSubstitution([share, 'worlds', 'nova_empty.sdf'])
        ]}.items())
    state_publisher = Node(
        package='robot_state_publisher', executable='robot_state_publisher',
        output='both', parameters=[description, {'use_sim_time': True}])
    spawn = Node(
        package='ros_gz_sim', executable='create', output='screen',
        arguments=['-topic', 'robot_description', '-name', 'nova_sm3',
                   '-x', '0', '-y', '0', '-z', '0.245'])
    controllers = PathJoinSubstitution([share, 'config', 'controllers.yaml'])
    spawners = [Node(
        package='controller_manager', executable='spawner', output='both',
        arguments=[name, '--param-file', controllers])
        for name in ('joint_state_broadcaster', 'joint_trajectory_controller')]
    return LaunchDescription([
        gz, state_publisher, spawn,
        TimerAction(period=5.0, actions=spawners),
    ])
