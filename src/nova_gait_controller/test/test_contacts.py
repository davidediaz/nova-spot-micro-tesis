from types import SimpleNamespace

import pytest

from nova_gait_controller.contacts import (
    approximate_contact_force, compare_contact_sets, debounced_contact,
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


def test_contact_debounce_rejects_timeout_sized_false_gap():
    stable, candidate, since = debounced_contact(True, None, None, False, 1.0)
    assert stable and candidate is False and since == 1.0
    stable, candidate, since = debounced_contact(
        stable, candidate, since, True, 1.10)
    assert stable and since is None


def test_contact_debounce_accepts_sustained_flight_and_recontact():
    stable, candidate, since = debounced_contact(True, None, None, False, 2.0)
    stable, candidate, since = debounced_contact(
        stable, candidate, since, False, 2.13)
    assert not stable and since is None
    stable, candidate, since = debounced_contact(
        stable, candidate, since, True, 2.20)
    stable, candidate, since = debounced_contact(
        stable, candidate, since, True, 2.24)
    assert stable and since is None
