import pytest

from nova_gait_controller.stability import (
    nominal_foot_points, rotate_vector_by_quaternion, support_result,
)


def test_quaternion_rotation_identity():
    assert rotate_vector_by_quaternion((1, 2, 3), (0, 0, 0, 1)) == (1, 2, 3)


def test_nominal_points_and_support_margin():
    names = []
    values = []
    for prefix in ('front_left', 'front_right', 'rear_left', 'rear_right'):
        names.extend([f'{prefix}_coxa_joint', f'{prefix}_femur_joint',
                      f'{prefix}_tibia_joint'])
        values.extend([0.10, 0.42, -0.84])
    points = nominal_foot_points(names, values, (0, 0, 0.224), (0, 0, 0, 1))
    assert set(points) == {'fl', 'fr', 'rl', 'rr'}
    result = support_result((0, 0), points, list(points))
    assert result['available']
    assert result['margin_m'] > 0


def test_support_margin_unavailable_with_two_contacts():
    points = {'fl': (0.1, 0.1, 0), 'rr': (-0.1, -0.1, 0)}
    result = support_result((0, 0), points, ['fl', 'rr'])
    assert not result['available']
    assert result['margin_m'] is None
