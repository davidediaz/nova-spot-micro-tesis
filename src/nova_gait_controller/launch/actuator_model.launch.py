from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node


def generate_launch_description():
    defaults = {
        'input_topic': '/nova/ideal_trajectory',
        'output_topic': '/joint_trajectory_controller/joint_trajectory',
        'backlash_rad': '0.0', 'command_delay_ms': '0.0',
        'max_speed_rad_s': '6.981317',
    }
    arguments = [DeclareLaunchArgument(name, default_value=value)
                 for name, value in defaults.items()]
    node = Node(package='nova_gait_controller', executable='actuator_model_node',
                output='screen', parameters=[{
                    name: LaunchConfiguration(name) for name in defaults}])
    return LaunchDescription(arguments + [node])
