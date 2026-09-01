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
