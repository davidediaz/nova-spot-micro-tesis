from math import cos, pi, sin

import pytest

from types import SimpleNamespace

from nova_gait_controller.safety import (
    diagnostic_reasons, invalid_trajectory_reasons, quaternion_to_rpy,
    stale_sources, unsafe_reasons,
)


def test_quaternion_to_rpy_roll():
    roll, pitch, yaw = quaternion_to_rpy(sin(pi / 8), 0.0, 0.0, cos(pi / 8))
    assert roll == pytest.approx(pi / 4)
    assert pitch == pytest.approx(0.0)
    assert yaw == pytest.approx(0.0)


def test_unsafe_reasons_and_nominal_pose():
    assert unsafe_reasons(0.224, 0.0, 0.0, 0.16, 0.32, 0.35) == []
    assert unsafe_reasons(0.10, 0.40, 0.0, 0.16, 0.32, 0.35) == [
        'altura_baja', 'roll']


@pytest.mark.parametrize('value', [float('nan'), float('inf'), -float('inf')])
def test_unsafe_reasons_rejects_nonfinite_pose(value):
    assert unsafe_reasons(value, 0.0, 0.0, 0.16, 0.32, 0.35) == ['pose_no_finita']


def test_stale_sources_detects_missing_expired_and_nonfinite_data():
    stamps = {'pose': 9.8, 'contacts': None, 'stability': float('nan')}
    assert stale_sources(stamps, now=10.0, timeout=0.5) == ['contacts', 'stability']
    assert stale_sources({'pose': 9.0}, now=10.0, timeout=0.5) == ['pose']


def test_diagnostics_detect_contact_margin_and_nonfinite_margin():
    contact = {'comparison_available': True, 'match': False}
    stability = {'available': True, 'margin_m': -0.006}
    assert diagnostic_reasons(contact, stability, -0.005) == [
        'contactos_no_coinciden', 'margen_estabilidad']
    stability['margin_m'] = float('nan')
    assert diagnostic_reasons(None, stability, -0.005) == ['margen_no_finito']


def test_invalid_trajectory_rejects_nonfinite_and_limit_violation():
    names = [f'{leg}_{joint}_joint' for leg in
             ('front_left', 'front_right', 'rear_left', 'rear_right')
             for joint in ('coxa', 'femur', 'tibia')]
    point = SimpleNamespace(positions=[0.0, 0.4, -0.8] * 4)
    assert invalid_trajectory_reasons(names, [point]) == []
    point.positions[0] = float('nan')
    point.positions[1] = 2.0
    assert invalid_trajectory_reasons(names, [point]) == [
        'referencia_no_finita', 'limite_articular']
