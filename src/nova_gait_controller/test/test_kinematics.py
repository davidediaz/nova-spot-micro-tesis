import math

import pytest

from nova_gait_controller.kinematics import (
    cartesian_crawl, cartesian_step_walk, crawl_sample_profile,
    crawl_swing_height, forward_leg, inverse_leg,
)


def test_forward_inverse_round_trip():
    for side in (-1, 1):
        expected = (0.10, 0.42, -0.84)
        foot = forward_leg(*expected, side)
        actual = inverse_leg(*foot, side)
        for wanted, obtained in zip(expected, actual):
            assert math.isclose(wanted, obtained, abs_tol=1e-9)


def test_cartesian_crawl_is_reachable_and_smooth():
    poses = cartesian_crawl((0.10, 0.42, -0.84))
    assert len(poses) == 24
    assert all(len(item) == 12 for item in poses)
    cyclic = poses + poses[:1]
    largest_jump = max(
        abs(cyclic[index][joint] - cyclic[index - 1][joint])
        for index in range(1, len(cyclic)) for joint in range(12))
    assert largest_jump < 0.20


def test_cartesian_crawl_has_liftoff_touchdown_and_expected_sequence():
    stand = (0.10, 0.42, -0.84)
    poses = cartesian_crawl(stand)
    neutral_z = forward_leg(*stand, side=1)[2]
    order = (0, 9, 3, 6)  # FL, RR, FR, RL offsets in the flattened pose.

    for quarter, joint_offset in enumerate(order):
        heights = []
        for sample in range(quarter * 6, (quarter + 1) * 6):
            side = 1 if joint_offset in (0, 6) else -1
            z = forward_leg(*poses[sample][joint_offset:joint_offset + 3], side)[2]
            heights.append(z - neutral_z)
        assert abs(heights[0]) < 1e-9
        assert abs(heights[-1]) < 1e-9
        assert 0.010 < max(heights) <= 0.014 + 1e-9


def test_cartesian_crawl_weight_transfer_is_bounded_and_periodic():
    stand = (0.10, 0.42, -0.84)
    poses = cartesian_crawl(
        stand, lateral_shift=0.004, fore_aft_shift=0.004)
    # At every quarter boundary the common transfer is exactly zero.
    for sample in (0, 6, 12, 18):
        expected_x, expected_y, _ = forward_leg(*stand, side=1)
        actual_x, actual_y, _ = forward_leg(*poses[sample][0:3], side=1)
        phase = ((sample / 24.0) + 0.75) % 1.0
        gait_x = expected_x + 0.018 * (-0.5 if phase >= 0.75 else 0.5 - phase / 0.75)
        assert math.isclose(actual_x, gait_x, abs_tol=1e-9)
        assert math.isclose(actual_y, expected_y, abs_tol=1e-9)


def test_crawl_profile_preloads_before_liftoff_and_ends_in_contact():
    profiles = [crawl_sample_profile(index, 6) for index in range(6)]
    assert [item[2] for item in profiles] == [
        'transfer_start', 'preload', 'liftoff', 'flight', 'landing',
        'touchdown']
    assert profiles[0][3] and profiles[1][3] and profiles[-1][3]
    assert all(not item[3] for item in profiles[2:-1])
    assert profiles[1][0] > profiles[0][0]
    assert max(item[0] for item in profiles) == 1.0


def test_crawl_landing_height_can_be_tuned_by_axle_without_changing_liftoff():
    profiles = [crawl_sample_profile(index, 6) for index in range(6)]
    front = [crawl_swing_height(item[1], item[2], 0.2) for item in profiles]
    rear = [crawl_swing_height(item[1], item[2], 0.8) for item in profiles]

    assert front[:4] == rear[:4]
    assert front[4] == 0.2
    assert rear[4] == 0.8
    assert front[5] == rear[5] == pytest.approx(0.0, abs=1e-12)


def test_crawl_landing_ratio_shapes_the_complete_descent():
    progress_values = (0.50, 0.625, 0.75, 0.875, 1.0)
    early = [crawl_swing_height(value, 'flight', 0.2)
             for value in progress_values]
    nominal = [crawl_swing_height(value, 'flight', 2 ** -0.5)
               for value in progress_values]
    late = [crawl_swing_height(value, 'flight', 0.8)
            for value in progress_values]

    assert early[0] == nominal[0] == late[0] == pytest.approx(1.0)
    assert early[-1] == nominal[-1] == late[-1] == pytest.approx(0.0)
    assert all(early[index] < nominal[index] < late[index]
               for index in range(1, len(progress_values) - 1))
    assert early[2] == pytest.approx(0.2)
    assert late[2] == pytest.approx(0.8)
    assert all(sequence[index] >= sequence[index + 1]
               for sequence in (early, nominal, late)
               for index in range(len(sequence) - 1))


def test_crawl_descent_tuning_does_not_change_ascent():
    progress_values = (0.0, 0.125, 0.25, 0.375, 0.5)
    early = [crawl_swing_height(value, 'liftoff', 0.2)
             for value in progress_values]
    late = [crawl_swing_height(value, 'liftoff', 0.8)
            for value in progress_values]
    assert early == pytest.approx(late)


def test_cartesian_step_walk_is_reachable_smooth_and_periodic():
    poses = cartesian_step_walk((0.10, 0.42, -0.84))
    assert len(poses) == 32
    assert all(len(item) == 12 for item in poses)
    cyclic = poses + poses[:1]
    largest_jump = max(
        abs(cyclic[index][joint] - cyclic[index - 1][joint])
        for index in range(1, len(cyclic)) for joint in range(12))
    assert largest_jump < 0.08


def test_step_walk_weight_shift_is_bounded():
    poses = cartesian_step_walk((0.10, 0.42, -0.84), weight_shift=0.004)
    neutral_y = forward_leg(0.10, 0.42, -0.84, side=1)[1]
    observed = []
    for item in poses:
        observed.append(forward_leg(*item[0:3], side=1)[1] - neutral_y)
    assert max(abs(value) for value in observed) <= 0.004 + 1e-9
