from glob import glob
import os
from setuptools import find_packages, setup

package_name = 'nova_gait_controller'

setup(
    name=package_name,
    version='0.1.0',
    packages=find_packages(),
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob('launch/*.launch.py')),
        (os.path.join('share', package_name, 'config'), glob('config/*.yaml')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='pavilion',
    maintainer_email='pavilion@example.com',
    description='Discrete gait controller for NovaSM3',
    license='BSD-3-Clause',
    entry_points={
        'console_scripts': [
            'gait_controller = nova_gait_controller.gait_controller:main',
            'metrics_node = nova_gait_controller.metrics_node:main',
            'safety_supervisor = nova_gait_controller.safety_supervisor:main',
            'contact_monitor = nova_gait_controller.contact_monitor:main',
            'contact_comparator = nova_gait_controller.contact_comparator:main',
            'stability_monitor = nova_gait_controller.stability_monitor:main',
            'safety_test_node = nova_gait_controller.safety_test_node:main',
            'perturbation_injector = nova_gait_controller.perturbation_injector:main',
            'actuator_model_node = nova_gait_controller.actuator_model_node:main',
            'ppo_residual_node = nova_gait_controller.ppo_residual_node:main',
        ],
    },
)
