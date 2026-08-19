"""Regression checks that keep code, URDF/Xacro and MuJoCo parameters aligned."""

from pathlib import Path
import xml.etree.ElementTree as ET

import pytest

from nova_gait_controller.mathematical_model import DEFAULT_PARAMETERS, MG996R


ROOT = Path(__file__).resolve().parents[2]
XACRO = ROOT / 'nova_sm3_description' / 'urdf' / 'nova_sm3.urdf.xacro'
MUJOCO = ROOT / 'nova_sm3_description' / 'mujoco' / 'nova_sm3.xml'
XACRO_NS = '{http://www.ros.org/wiki/xacro}'


def _xacro_properties():
    root = ET.parse(XACRO).getroot()
    return {item.attrib['name']: float(item.attrib['value'])
            for item in root.findall(f'{XACRO_NS}property')}


def test_geometry_and_masses_match_xacro():
    properties = _xacro_properties()
    expected = {
        'hip_spacing_x': DEFAULT_PARAMETERS.hip_spacing_x,
        'hip_spacing_y': DEFAULT_PARAMETERS.hip_spacing_y,
        'coxa_length': DEFAULT_PARAMETERS.coxa_length,
        'femur_length': DEFAULT_PARAMETERS.femur_length,
        'tibia_length': DEFAULT_PARAMETERS.tibia_length,
        'body_mass': DEFAULT_PARAMETERS.body_mass,
        'coxa_mass': DEFAULT_PARAMETERS.coxa_mass,
        'femur_mass': DEFAULT_PARAMETERS.femur_mass,
        'tibia_mass': DEFAULT_PARAMETERS.tibia_mass,
        'foot_mass': DEFAULT_PARAMETERS.foot_mass,
    }
    for name, value in expected.items():
        assert properties[name] == pytest.approx(value)


def test_mujoco_defaults_match_computable_model():
    root = ET.parse(MUJOCO).getroot()
    joint = root.find('./default/joint')
    geom = root.find('./default/geom')
    assert float(joint.attrib['damping']) == pytest.approx(DEFAULT_PARAMETERS.joint_damping)
    assert float(joint.attrib['frictionloss']) == pytest.approx(DEFAULT_PARAMETERS.coulomb_friction)
    assert float(joint.attrib['armature']) == pytest.approx(DEFAULT_PARAMETERS.rotor_armature)
    assert float(geom.attrib['friction'].split()[0]) == pytest.approx(
        DEFAULT_PARAMETERS.ground_friction)


def test_mujoco_total_mass_matches_nominal_total():
    root = ET.parse(MUJOCO).getroot()
    body_mass = float(root.find(".//body[@name='base_link']/inertial").attrib['mass'])
    total = body_mass
    for leg in ('front_left', 'front_right', 'rear_left', 'rear_right'):
        total += float(root.find(f".//body[@name='{leg}_coxa_link']/inertial").attrib['mass'])
        total += float(root.find(f".//body[@name='{leg}_femur_link']/inertial").attrib['mass'])
        # MuJoCo combines tibia and fixed foot into one composite inertia.
        total += float(root.find(f".//body[@name='{leg}_tibia_link']/inertial").attrib['mass'])
    assert total == pytest.approx(DEFAULT_PARAMETERS.total_mass)


def test_urdf_actuator_envelope_uses_mg996r_catalogue_limit():
    root = ET.parse(XACRO).getroot()
    limits = root.findall(".//limit")
    dynamics = root.findall(".//dynamics")
    assert len(limits) == 3 and len(dynamics) == 3
    for limit in limits:
        assert float(limit.attrib['effort']) == pytest.approx(MG996R.stall_torque)
        assert float(limit.attrib['velocity']) == pytest.approx(MG996R.no_load_speed)
    for item in dynamics:
        assert float(item.attrib['damping']) == pytest.approx(DEFAULT_PARAMETERS.joint_damping)
        assert float(item.attrib['friction']) == pytest.approx(DEFAULT_PARAMETERS.coulomb_friction)
