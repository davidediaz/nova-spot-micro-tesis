"""Pure helpers for measured-versus-expected foot contact diagnostics."""

from math import sqrt


LEG_NAMES = ('fl', 'fr', 'rl', 'rr')


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
