#!/usr/bin/env python3
"""Reject paired simulator assets whose physical profile is inconsistent."""
import argparse
import json
from pathlib import Path
import xml.etree.ElementTree as ET


def values(text):
    return [float(x) for x in text.split()]


def main():
    parser = argparse.ArgumentParser(); parser.add_argument('directory', type=Path)
    args = parser.parse_args(); root = args.directory
    manifest = json.loads((root/'manifest.json').read_text(encoding='utf-8'))
    profile = manifest['parameters']
    urdf = ET.parse(root/'nova_gazebo.urdf').getroot()
    mjcf = ET.parse(root/'nova_mujoco.xml').getroot()
    urdf_mass = sum(float(x.attrib['value']) for x in urdf.findall('.//inertial/mass'))
    mjcf_mass = sum(float(x.attrib['mass']) for x in mjcf.findall('.//inertial'))
    # MuJoCo combines each tibia and fixed foot in its composite inertial.
    expected = 2.72 * float(profile['mass_scale'])
    checks = {
        'urdf_total_mass': abs(urdf_mass-expected) < 1e-9,
        'mjcf_total_mass': abs(mjcf_mass-expected) < 1e-9,
        'joint_damping': all(abs(float(x.attrib['damping'])-float(profile['joint_damping'])) < 1e-12
                             for x in urdf.findall('.//joint/dynamics')),
        'joint_friction': all(abs(float(x.attrib['friction'])-float(profile['joint_friction'])) < 1e-12
                              for x in urdf.findall('.//joint/dynamics')),
        'mujoco_ground_friction': abs(values(mjcf.find('./default/geom').attrib['friction'])[0]
                                      - float(profile['ground_friction'])) < 1e-12,
        'same_effort_limit': all(abs(float(x.attrib['effort'])-
                                     manifest['effective_stall_torque_nm']) < 1e-9
                                 for x in urdf.findall('.//joint/limit')),
    }
    result = {'profile': manifest['profile'], 'expected_total_mass_kg': expected,
              'urdf_total_mass_kg': urdf_mass, 'mujoco_total_mass_kg': mjcf_mass,
              'checks': checks, 'compatible': all(checks.values())}
    (root/'AUDITORIA_COMPATIBILIDAD.json').write_text(
        json.dumps(result, indent=2)+'\n', encoding='utf-8')
    if not result['compatible']:
        raise SystemExit(f'Perfil incompatible: {checks}')
    print(root/'AUDITORIA_COMPATIBILIDAD.json')


if __name__ == '__main__':
    main()
