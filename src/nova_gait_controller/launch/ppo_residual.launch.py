from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node

def generate_launch_description():
    args=[DeclareLaunchArgument('policy_path'), DeclareLaunchArgument('enabled',default_value='true')]
    node=Node(package='nova_gait_controller',executable='ppo_residual_node',output='screen',parameters=[{
        'policy_path':LaunchConfiguration('policy_path'),'enabled':LaunchConfiguration('enabled'),
        'input_topic':'/nova/nominal_trajectory','output_topic':'/joint_trajectory_controller/joint_trajectory'}])
    return LaunchDescription(args+[node])
