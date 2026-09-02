#!/usr/bin/env python3
"""Generate paired Gazebo/URDF and MuJoCo assets from one profile file."""
import argparse
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import xml.etree.ElementTree as ET

import yaml

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'src' / 'nova_gait_controller'))
from nova_gait_controller.mathematical_model import MG996R, saturated_actuator_torque

PROFILE_FILE = ROOT / 'src/nova_sm3_description/config/digital_twin_profiles.yaml'
XACRO = ROOT / 'src/nova_sm3_description/urdf/nova_sm3.urdf.xacro'
MJCF = ROOT / 'src/nova_sm3_description/mujoco/nova_sm3.xml'
WORLD = ROOT / 'src/nova_sm3_description/worlds/nova_empty.sdf'


def sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_profile(name):
    document = yaml.safe_load(PROFILE_FILE.read_text(encoding='utf-8'))
    if name not in document['profiles']:
        raise ValueError(f'Perfil desconocido: {name}')
    profile = document['profiles'][name]
    for key in ('mass_scale', 'inertia_scale', 'joint_damping', 'joint_friction',
                'ground_friction', 'voltage_v', 'current_limit_per_servo_a'):
        if float(profile[key]) <= 0:
            raise ValueError(f'{key} debe ser positivo')
    for key in ('backlash_rad', 'command_delay_ms', 'sensor_delay_ms'):
        if float(profile[key]) < 0:
            raise ValueError(f'{key} no puede ser negativo')
    return profile


def effective_limits(profile):
    torque, _, _ = saturated_actuator_torque(
        100.0, 0.0, float(profile['voltage_v']),
        float(profile['current_limit_per_servo_a']))
    voltage = float(profile['voltage_v'])
    fraction = ((voltage-MG996R.min_voltage) /
                (MG996R.nominal_voltage-MG996R.min_voltage))
    velocity = MG996R.no_load_speed_4v8 + fraction * (
        MG996R.no_load_speed-MG996R.no_load_speed_4v8)
    return torque, velocity


def generate_urdf(profile, output, effort, velocity):
    args = [
        'xacro', str(XACRO), 'include_ros2_control:=true', 'use_fake_hardware:=false',
        'use_gazebo:=true',
        f"mass_scale:={profile['mass_scale']}",
        f"inertia_scale:={profile['inertia_scale']}",
        f"joint_damping:={profile['joint_damping']}",
        f"joint_friction:={profile['joint_friction']}",
        f'actuator_effort:={effort}', f'actuator_velocity:={velocity}',
    ]
    output.write_bytes(subprocess.check_output(args))


def generate_mjcf(profile, output, effort):
    tree = ET.parse(MJCF); root = tree.getroot()
    mass_scale = float(profile['mass_scale']); inertia_scale = float(profile['inertia_scale'])
    joint = root.find('./default/joint')
    joint.set('damping', str(profile['joint_damping']))
    joint.set('frictionloss', str(profile['joint_friction']))
    geom = root.find('./default/geom'); friction = geom.get('friction').split()
    friction[0] = str(profile['ground_friction']); geom.set('friction', ' '.join(friction))
    for inertial in root.findall('.//inertial'):
        inertial.set('mass', f"{float(inertial.get('mass')) * mass_scale:.12g}")
        values = [float(x) * mass_scale * inertia_scale
                  for x in inertial.get('diaginertia').split()]
        inertial.set('diaginertia', ' '.join(f'{x:.12g}' for x in values))
    for actuator in root.findall('./actuator/position'):
        actuator.set('forcelimited', 'true'); actuator.set('forcerange', f'{-effort:.12g} {effort:.12g}')
    custom = ET.Element('custom')
    for name in ('backlash_rad', 'command_delay_ms', 'sensor_delay_ms',
                 'voltage_v', 'current_limit_per_servo_a'):
        ET.SubElement(custom, 'numeric', name=name, data=str(profile[name]))
    root.insert(2, custom); ET.indent(tree, space='  ')
    tree.write(output, encoding='utf-8', xml_declaration=True)


def generate_world(profile, output):
    tree = ET.parse(WORLD); collision = tree.find(".//model[@name='ground_plane']//collision")
    surface = ET.SubElement(collision, 'surface'); friction = ET.SubElement(surface, 'friction')
    ode = ET.SubElement(friction, 'ode')
    ET.SubElement(ode, 'mu').text = str(profile['ground_friction'])
    ET.SubElement(ode, 'mu2').text = str(profile['ground_friction'])
    ET.indent(tree, space='  '); tree.write(output, encoding='utf-8', xml_declaration=True)


def main():
    parser = argparse.ArgumentParser(); parser.add_argument('profile')
    parser.add_argument('--output-root', type=Path,
                        default=ROOT / 'Experimentos/modelos_gemelo_generados')
    args = parser.parse_args(); profile = load_profile(args.profile)
    out = args.output_root / args.profile; out.mkdir(parents=True, exist_ok=True)
    effort, velocity = effective_limits(profile)
    urdf, mjcf, world = out/'nova_gazebo.urdf', out/'nova_mujoco.xml', out/'nova_world.sdf'
    generate_urdf(profile, urdf, effort, velocity); generate_mjcf(profile, mjcf, effort)
    generate_world(profile, world)
    manifest = {'profile': args.profile, 'status': 'provisional_not_identified',
                'parameters': profile, 'effective_stall_torque_nm': effort,
                'effective_no_load_speed_rad_s': velocity,
                'common_ros_layer': {'backlash_rad': profile['backlash_rad'],
                    'command_delay_ms': profile['command_delay_ms'],
                    'sensor_delay_ms': profile['sensor_delay_ms']},
                'files': {p.name: sha256(p) for p in (urdf, mjcf, world)}}
    (out/'manifest.json').write_text(json.dumps(manifest, indent=2)+'\n', encoding='utf-8')
    print(out/'manifest.json')


if __name__ == '__main__':
    main()
