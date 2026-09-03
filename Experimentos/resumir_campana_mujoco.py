#!/usr/bin/env python3
"""Valida repeticiones MuJoCo y resume sus métricas sin mezclar ciclos."""
import argparse
import csv
import json
import re
from pathlib import Path
import numpy as np


def value(report, pattern):
    match = re.search(pattern, report)
    if not match:
        raise ValueError(f'No coincide: {pattern}')
    return float(match.group(1).replace(',', '.'))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('root', type=Path)
    parser.add_argument('--expected', type=int, required=True)
    parser.add_argument('--minimum-cycles', type=int, required=True)
    args = parser.parse_args()
    if args.minimum_cycles < 2:
        raise SystemExit('Se requieren al menos dos ciclos: el primero es transitorio')
    rows = []
    for directory in sorted((args.root / 'analisis').glob('*')):
        movement = list(csv.DictReader((directory / 'metricas_por_ciclo.csv').open()))
        name = directory.name
        tracking_report = (args.root / 'articulaciones' / name / 'INFORME_MUJOCO.md').read_text()
        contact_report = (args.root / 'contactos' / name / 'INFORME_CONTACTOS.md').read_text()
        if len(movement) < args.minimum_cycles:
            raise SystemExit(f'{name}: solo {len(movement)} ciclos completos')
        steady = movement[1:args.minimum_cycles]
        rows.append({
            'ensayo': name,
            'ciclos': len(movement),
            'avance_m_ciclo': np.mean([float(row['avance_m']) for row in steady]),
            'roll_max_deg': np.mean([float(row['roll_max_abs_deg']) for row in steady]),
            'pitch_max_deg': np.mean([float(row['pitch_max_abs_deg']) for row in steady]),
            'error_rms_rad': value(tracking_report, r'Error RMS articular medio: ([0-9.]+)'),
            'contact_match_percent': value(contact_report, r'Coincidencia simultánea filtrada de las cuatro patas: ([0-9.]+)'),
        })
    if len(rows) != args.expected:
        raise SystemExit(f'Se esperaban {args.expected} ensayos y hay {len(rows)}')
    output = args.root / 'resumen_ensayos.csv'
    with output.open('w', newline='', encoding='utf-8') as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader(); writer.writerows(rows)
    summary = {key: float(np.mean([float(row[key]) for row in rows]))
               for key in rows[0] if key not in ('ensayo', 'ciclos')}
    (args.root / 'resumen_campana.json').write_text(
        json.dumps({'ensayos': len(rows), 'promedios': summary}, indent=2), encoding='utf-8')
    print(json.dumps({'ensayos': len(rows), 'promedios': summary}, indent=2))


if __name__ == '__main__':
    main()
