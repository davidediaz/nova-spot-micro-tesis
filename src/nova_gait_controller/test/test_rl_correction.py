import numpy as np
import pytest

from nova_gait_controller.rl_correction import (
    ResidualLimits, apply_residual, bounded_residual_action, residual_reward,
    residual_termination,
)


def test_residual_action_enforces_amplitude_and_slew():
    limits = ResidualLimits(max_action_rad=0.08, max_action_step_rad=0.02)
    first = bounded_residual_action(np.ones(12), np.zeros(12), limits)
    assert first == pytest.approx(np.full(12, 0.02))
    action = first
    for _ in range(10):
        action = bounded_residual_action(np.ones(12), action, limits)
    assert action == pytest.approx(np.full(12, 0.08))


def test_residual_action_rejects_nonfinite_or_wrong_dimension():
    with pytest.raises(ValueError):
        bounded_residual_action([0.0], np.zeros(12))
    bad = np.zeros(12); bad[3] = np.nan
    with pytest.raises(ValueError):
        bounded_residual_action(bad, np.zeros(12))


def test_corrected_reference_preserves_joint_limits():
    corrected = apply_residual([0.59, 1.19, -2.19] * 4, [0.08, 0.08, -0.08] * 4)
    assert corrected == pytest.approx([0.60, 1.20, -2.20] * 4)


def test_reward_prefers_nominal_stable_small_action():
    nominal = residual_reward(0, 0, 0, np.zeros(12), np.zeros(12))
    disturbed = residual_reward(0.1, -0.1, 0.02, np.ones(12) * 0.03,
                                np.ones(12) * 0.05)
    assert nominal > disturbed
    assert residual_reward(0, 0, 0, np.zeros(12), np.zeros(12), True) < -90


@pytest.mark.parametrize('state,reason', [
    ((0.10, 0.0, 0.0, False), 'altura'),
    ((0.22, 0.40, 0.0, False), 'inclinacion'),
    ((0.22, 0.0, 0.0, True), 'supervisor'),
    ((float('nan'), 0.0, 0.0, False), 'estado_no_finito'),
])
def test_residual_termination_contract(state, reason):
    assert residual_termination(*state) == (True, reason)


def test_residual_nominal_state_continues():
    assert residual_termination(0.224, 0.0, 0.0, False) == (False, '')
