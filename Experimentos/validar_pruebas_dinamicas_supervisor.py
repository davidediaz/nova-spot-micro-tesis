#!/usr/bin/env python3
"""Validate reports produced by the isolated ROS 2 safety scenarios."""
import argparse
import json
from pathlib import Path


EXPECTED_REASONS = {
    'margin': 'margen_estabilidad',
    'contact': 'perdida_contacto',
    'timeout': 'datos_vencidos:pose,contacts,stability',
    'low_height': 'altura_baja',
    'high_height': 'altura_alta',
    'roll': 'roll',
    'pitch': 'pitch',
    'joint_limit': 'limite_articular',
    'discontinuity': 'discontinuidad_articular',
}


def validate(directory):
    failures = []
    for scenario, expected_reason in EXPECTED_REASONS.items():
        path = directory / f'{scenario}.json'
        if not path.exists():
            failures.append(f'{scenario}: falta {path}')
            continue
        report = json.loads(path.read_text(encoding='utf-8'))
        statuses = [json.loads(event['status']) for event in report['events']
                    if 'status' in event]
        commands = [event['command'] for event in report['events']
                    if 'command' in event]
        reasons = [status.get('reason') for status in statuses]
        if not report.get('triggered'):
            failures.append(f'{scenario}: no se recibió triggered=true')
        if expected_reason not in reasons:
            failures.append(f'{scenario}: razones {reasons}, esperada {expected_reason}')
        if 'stand' not in commands:
            failures.append(f'{scenario}: no se recibió la orden stand')
    if failures:
        raise SystemExit('\n'.join(failures))
    print(f'{len(EXPECTED_REASONS)} escenarios dinámicos aprobados')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('directory', type=Path)
    args = parser.parse_args()
    validate(args.directory)


if __name__ == '__main__':
    main()
