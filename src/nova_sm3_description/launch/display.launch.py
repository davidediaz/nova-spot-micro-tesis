from launch import LaunchDescription
from launch.substitutions import Command, PathJoinSubstitution
from launch_ros.actions import Node
from launch_ros.parameter_descriptions import ParameterValue
from launch_ros.substitutions import FindPackageShare


def generate_launch_description():
    model = PathJoinSubstitution(
        [FindPackageShare('nova_sm3_description'), 'urdf', 'nova_sm3.urdf.xacro'])
    description = {'robot_description': ParameterValue(
        Command(['xacro ', model, ' include_ros2_control:=false']), value_type=str)}
    rviz_config = PathJoinSubstitution(
        [FindPackageShare('nova_sm3_description'), 'rviz', 'nova_sm3.rviz'])
    return LaunchDescription([
        Node(package='robot_state_publisher', executable='robot_state_publisher',
             parameters=[description]),
        Node(package='joint_state_publisher_gui', executable='joint_state_publisher_gui'),
        Node(package='rviz2', executable='rviz2', arguments=['-d', rviz_config]),
    ])
