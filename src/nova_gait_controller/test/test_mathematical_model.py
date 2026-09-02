import math

import pytest
import numpy as np

from nova_gait_controller.kinematics import forward_leg
from nova_gait_controller.mathematical_model import (
    DEFAULT_PARAMETERS, MG996R, actuator_current, actuator_torque_limit,
    apply_backlash, compliant_contact_force, coriolis_torque, foot_force_to_joint_torque,
    inverse_dynamics, leg_jacobian, leg_link_com_positions, leg_mass_matrix,
    mat_vec, robot_center_of_mass, static_stability_margin,
    saturated_actuator_torque)


def test_actuator_saturates_by_current_and_speed():
    torque, current, saturated = saturated_actuator_torque(2.0, 0.0, current_limit=0.8)
    assert 0.0 < torque < 1.0787315
    assert current <= 0.8
    assert saturated
    assert saturated_actuator_torque(0.1, 0.0)[0] == pytest.approx(0.1)


def test_backlash_dead_zone_and_direction():
    assert apply_backlash(0.01, 0.0, 0.02) == 0.0
    assert apply_backlash(0.10, 0.0, 0.02) == pytest.approx(0.08)
    assert apply_backlash(-0.10, 0.0, 0.02) == pytest.approx(-0.08)


def test_total_mass_matches_urdf_reference():
    assert math.isclose(DEFAULT_PARAMETERS.total_mass, 2.72, abs_tol=1e-12)


@pytest.mark.parametrize('side', (-1, 1))
def test_analytic_jacobian_matches_central_difference(side):
    q = (0.13, 0.38, -0.79)
    velocity = (0.21, -0.17, 0.09)
    predicted = mat_vec(leg_jacobian(*q, side), velocity)
    dt = 1e-6
    plus = forward_leg(*(q[i] + dt * velocity[i] for i in range(3)), side)
    minus = forward_leg(*(q[i] - dt * velocity[i] for i in range(3)), side)
    measured = tuple((a - b) / (2.0 * dt) for a, b in zip(plus, minus))
    assert predicted == pytest.approx(measured, abs=1e-9)


def test_jacobian_transpose_preserves_virtual_power():
    q = (0.10, 0.42, -0.84)
    q_dot = (0.2, -0.1, 0.05)
    force = (3.0, -1.0, 8.0)
    velocity = mat_vec(leg_jacobian(*q, 1), q_dot)
    torque = foot_force_to_joint_torque(q, force, 1)
    assert sum(f * v for f, v in zip(force, velocity)) == pytest.approx(
        sum(t * speed for t, speed in zip(torque, q_dot)), abs=1e-12)


def test_static_stability_margin_inside_boundary_and_outside():
    contacts = [(-0.1, -0.08), (0.1, -0.08), (0.1, 0.08), (-0.1, 0.08)]
    assert static_stability_margin((0.0, 0.0), contacts) == pytest.approx(0.08)
    assert static_stability_margin((0.1, 0.0), contacts) == pytest.approx(0.0)
    assert static_stability_margin((0.12, 0.0), contacts) == pytest.approx(-0.02)


def test_stability_requires_a_polygon():
    with pytest.raises(ValueError):
        static_stability_margin((0.0, 0.0), [(0.0, 0.0), (1.0, 0.0)])


@pytest.mark.parametrize('side', (-1, 1))
def test_link_chain_ends_at_forward_kinematics(side):
    q = (0.10, 0.42, -0.84)
    assert leg_link_com_positions(q, side)[-1] == pytest.approx(forward_leg(*q, side))


@pytest.mark.parametrize('side', (-1, 1))
def test_mass_matrix_is_symmetric_positive_definite(side):
    matrix = leg_mass_matrix((0.10, 0.42, -0.84), side)
    assert matrix == pytest.approx(matrix.T, abs=1e-12)
    assert np.linalg.eigvalsh(matrix).min() > 0.0


def test_coriolis_is_zero_at_zero_velocity():
    assert coriolis_torque((0.1, 0.4, -0.8), (0.0, 0.0, 0.0), 1) == pytest.approx((0, 0, 0))


def test_inverse_dynamics_returns_finite_joint_torques():
    torque = inverse_dynamics((0.1, 0.42, -0.84), (0.1, 0.0, -0.1),
                              (0.0, 0.2, 0.0), 1, (0.0, 0.0, 5.0))
    assert np.isfinite(torque).all()


def test_mg996r_catalogue_envelope_and_current():
    assert actuator_torque_limit(0.0) == pytest.approx(MG996R.stall_torque)
    assert actuator_torque_limit(MG996R.no_load_speed) == pytest.approx(0.0)
    assert actuator_torque_limit(0.0, 4.8) == pytest.approx(9.4 * 0.0980665)
    assert MG996R.no_load_speed_4v8 == pytest.approx((math.pi / 3.0) / 0.19)
    assert actuator_current(0.0) == pytest.approx(MG996R.no_load_current)
    assert actuator_current(MG996R.stall_torque) == pytest.approx(MG996R.stall_current)


def test_robot_com_is_symmetric_in_neutral_stance():
    stance = {leg: (0.0, 0.0, 0.0) for leg in ('fl', 'fr', 'rl', 'rr')}
    com = robot_center_of_mass(stance)
    assert com[0] == pytest.approx(0.0, abs=1e-12)
    assert com[1] == pytest.approx(0.0, abs=1e-12)
    assert com[2] < 0.0


def test_compliant_contact_is_unilateral_and_opposes_slip():
    assert compliant_contact_force((0, 0, 0.01), (1, 0, -1)) == (0, 0, 0)
    force = compliant_contact_force((0, 0, -0.001), (0.2, -0.1, -0.02))
    assert force[0] < 0.0 and force[1] > 0.0 and force[2] > 0.0
