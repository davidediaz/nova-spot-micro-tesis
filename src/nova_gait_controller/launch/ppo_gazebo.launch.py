import os
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription, TimerAction
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    share=get_package_share_directory('nova_gait_controller')
    demo=IncludeLaunchDescription(PythonLaunchDescriptionSource(os.path.join(share,'launch','demo.launch.py')),
        launch_arguments={'trajectory_topic':'/nova/nominal_trajectory'}.items())
    policy=Node(package='nova_gait_controller',executable='ppo_residual_node',output='screen',parameters=[{
        'policy_path':LaunchConfiguration('policy_path'),'input_topic':'/nova/nominal_trajectory',
        'output_topic':'/joint_trajectory_controller/joint_trajectory','enabled':LaunchConfiguration('enabled')}])
    return LaunchDescription([DeclareLaunchArgument('policy_path'),DeclareLaunchArgument('enabled',default_value='true'),demo,TimerAction(period=6.0,actions=[policy])])
