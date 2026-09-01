import pytest
from rclpy.time import Time

from nova_gait_controller.gait_controller import (
    advance_phase_deadline, expected_contact_state, gait_mode_allowed,
    scaled_phase_duration,
)


def test_phase_deadline_does_not_accumulate_callback_delay():
    deadline = Time(nanoseconds=1_000_000_000)
    observed_callback_delay = 20_000_000

    for phase in range(1, 25):
        callback_time = Time(nanoseconds=deadline.nanoseconds + observed_callback_delay)
        deadline = advance_phase_deadline(deadline, 0.18)
        expected = 1_000_000_000 + phase * 180_000_000
        assert deadline.nanoseconds == pytest.approx(expected, abs=1)
        assert callback_time.nanoseconds != deadline.nanoseconds

    assert deadline.nanoseconds - 1_000_000_000 == pytest.approx(
        4_320_000_000, abs=1)


def test_speed_factor_scales_phase_duration_without_changing_geometry():
    assert scaled_phase_duration(0.18, 1.25) == pytest.approx(0.144)
    assert scaled_phase_duration(0.18, 1.5) == pytest.approx(0.12)


def test_speed_factor_must_be_positive_and_finite():
    for value in (0.0, -1.0, float('inf')):
        with pytest.raises(ValueError):
            scaled_phase_duration(0.18, value)


def test_crawl_contact_plan_exposes_preload_and_swing_subphases():
    expected_order = ['fl', 'rr', 'fr', 'rl']
    observed = []
    for phase in range(24):
        state = expected_contact_state('crawl', phase, 24, cycle_index=3)
        assert state['contact_plan_available']
        assert state['cycle_index'] == 3
        local = phase % 6
        if local in (0, 1, 5):
            assert len(state['expected_contacts']) == 4
            assert state['swing_leg'] is None
        else:
            assert len(state['expected_contacts']) == 3
            assert state['swing_leg'] not in state['expected_contacts']
        if local == 0:
            observed.append(state['planned_leg'])
    assert observed == expected_order
    assert [expected_contact_state('crawl', phase, 24, 0)['gait_subphase']
            for phase in range(6)] == [
                'transfer_start', 'preload', 'liftoff', 'flight',
                'landing', 'touchdown']


def test_step_contact_sequence_remains_one_swing_leg_per_quarter():
    observed = []
    previous = None
    for phase in range(32):
        state = expected_contact_state('step', phase, 32, cycle_index=3)
        assert len(state['expected_contacts']) == 3
        assert state['gait_subphase'] == 'swing'
        if state['swing_leg'] != previous:
            observed.append(state['swing_leg'])
            previous = state['swing_leg']
    assert observed == ['fl', 'rr', 'fr', 'rl']


def test_contact_plan_is_explicitly_unavailable_for_gallop():
    state = expected_contact_state('gallop', 0, 5, 0)
    assert not state['contact_plan_available']
    assert state['swing_leg'] is None
    assert state['expected_contacts'] == []


def test_gallop_requires_explicit_experimental_opt_in():
    assert not gait_mode_allowed('gallop')
    assert gait_mode_allowed('gallop', enable_experimental_gallop=True)
    assert gait_mode_allowed('crawl')
    assert gait_mode_allowed('step')
