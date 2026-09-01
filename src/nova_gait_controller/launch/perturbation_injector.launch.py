from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node


def generate_launch_description():
    names = {
        'delay_ms': '0.0', 'pose_noise_std_m': '0.0',
        'imu_accel_noise_std': '0.0', 'imu_gyro_noise_std': '0.0',
        'contact_dropout_probability': '0.0', 'noise_seed': '20260901',
        'push_force_x': '0.0', 'push_force_y': '0.0', 'push_force_z': '0.0',
        'push_start_s': '-1.0', 'push_duration_s': '0.10',
        'push_entity_name': 'nova_sm3',
    }
    args = [DeclareLaunchArgument(k, default_value=v) for k, v in names.items()]
    node = Node(
        package='nova_gait_controller', executable='perturbation_injector',
        output='screen', parameters=[{k: LaunchConfiguration(k) for k in names}],
    )
    return LaunchDescription(args + [node])
