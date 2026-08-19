from math import cos, pi, sin

import pytest

from nova_gait_controller.safety import quaternion_to_rpy, unsafe_reasons


def test_quaternion_to_rpy_roll():
    roll, pitch, yaw = quaternion_to_rpy(sin(pi / 8), 0.0, 0.0, cos(pi / 8))
    assert roll == pytest.approx(pi / 4)
    assert pitch == pytest.approx(0.0)
    assert yaw == pytest.approx(0.0)


def test_unsafe_reasons_and_nominal_pose():
    assert unsafe_reasons(0.224, 0.0, 0.0, 0.16, 0.32, 0.35) == []
    assert unsafe_reasons(0.10, 0.40, 0.0, 0.16, 0.32, 0.35) == [
        'altura_baja', 'roll']
