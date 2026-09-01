import importlib.util
from pathlib import Path


SCRIPT = (Path(__file__).parents[3] / 'Experimentos'
          / 'analizar_contactos_rosbag.py')
SPEC = importlib.util.spec_from_file_location('contact_analysis', SCRIPT)
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


def test_diagnostic_state_distinguishes_raw_and_filtered_contacts():
    state = MODULE.diagnostic_state({
        'expected_contacts': ['fl', 'fr', 'rl'],
        'raw_observed_contacts': ['fl', 'rr'],
        'filtered_observed_contacts': ['fl', 'fr', 'rr'],
        'observed_contacts': ['fl', 'fr', 'rr'],
    })
    assert state == (
        (True, True, True, False),
        (True, True, False, True),
        (True, False, False, True),
    )


def test_diagnostic_state_accepts_historical_bag_contract():
    state = MODULE.diagnostic_state({
        'expected_contacts': ['fl', 'fr', 'rl'],
        'observed_contacts': ['fl', 'fr', 'rr'],
    })
    assert state == (
        (True, True, True, False),
        (True, True, False, True),
        None,
    )


def test_contact_loss_episodes_measure_only_bounded_false_intervals():
    states = [
        (0, ((True,), (True, True, True, True))),
        (100_000_000, ((True,), (True, True, False, True))),
        (175_000_000, ((True,), (True, True, True, True))),
        (300_000_000, ((True,), (True, True, True, False))),
    ]
    episodes = MODULE.contact_loss_episodes(states, 400_000_000)
    assert episodes['rl'] == [(100_000_000, 175_000_000)]
    assert episodes['rr'] == [(300_000_000, None)]
