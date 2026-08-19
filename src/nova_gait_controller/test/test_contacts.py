from types import SimpleNamespace

import pytest

from nova_gait_controller.contacts import (
    approximate_contact_force, compare_contact_sets,
)


def test_contact_comparison_reports_missing_and_unexpected_feet():
    result = compare_contact_sets(['fl', 'fr', 'rl'], ['fl', 'fr', 'rr'])
    assert result == {
        'missing_contacts': ['rl'],
        'unexpected_contacts': ['rr'],
        'match': False,
    }


def test_contact_comparison_matches_independent_of_order():
    result = compare_contact_sets(['fl', 'rr', 'fr'], ['rr', 'fr', 'fl'])
    assert result['match']
    assert result['missing_contacts'] == []
    assert result['unexpected_contacts'] == []


def test_contact_force_uses_one_body_and_sums_contact_points():
    force = lambda x, y, z: SimpleNamespace(x=x, y=y, z=z)
    wrench = lambda first, second: SimpleNamespace(
        body_1_wrench=SimpleNamespace(force=first),
        body_2_wrench=SimpleNamespace(force=second))
    contacts = [SimpleNamespace(wrenches=[
        wrench(force(3, 4, 0), force(-3, -4, 0)),
        wrench(force(0, 0, 2), force(0, 0, -2)),
    ])]
    assert approximate_contact_force(contacts) == pytest.approx(7.0)
