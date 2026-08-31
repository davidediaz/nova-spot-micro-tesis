"""Pure helpers for measured-versus-expected foot contact diagnostics."""

from math import sqrt


LEG_NAMES = ('fl', 'fr', 'rl', 'rr')


def debounced_contact(stable, candidate, candidate_since, raw, now,
                      off_delay=0.12, on_delay=0.03):
    """Update a contact state only after the raw state persists.

    Gazebo can briefly stop publishing contact messages while a foot still
    skims the floor. Symmetric state tracking with a longer off delay prevents
    classifying a timeout-sized gap as a complete flight.
    """
    if raw == stable:
        return stable, raw, None
    if candidate != raw or candidate_since is None:
        return stable, raw, now
    delay = on_delay if raw else off_delay
    if now - candidate_since >= delay:
        return raw, raw, None
    return stable, candidate, candidate_since


def compare_contact_sets(expected, observed):
    """Return deterministic missing and unexpected contact lists."""
    expected_set = set(expected)
    observed_set = set(observed)
    return {
        'missing_contacts': [leg for leg in LEG_NAMES
                             if leg in expected_set and leg not in observed_set],
        'unexpected_contacts': [leg for leg in LEG_NAMES
                                if leg in observed_set and leg not in expected_set],
        'match': expected_set == observed_set,
    }


def wrench_force_magnitude(wrench):
    """Return the largest body-force magnitude from a Gazebo JointWrench."""
    def magnitude(force):
        return sqrt(force.x * force.x + force.y * force.y + force.z * force.z)

    return max(magnitude(wrench.body_1_wrench.force),
               magnitude(wrench.body_2_wrench.force))


def approximate_contact_force(contacts):
    """Sum one force magnitude per contact point as a useful simulation metric."""
    return sum(wrench_force_magnitude(wrench)
               for contact in contacts for wrench in contact.wrenches)
