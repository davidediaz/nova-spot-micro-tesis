#!/usr/bin/env python3
"""Resume campañas Gazebo/MuJoCo bajo un contrato ROS 2 común."""

import argparse
import csv
import json
from pathlib import Path

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from rclpy.serialization import deserialize_message
from rosbag2_py import ConverterOptions, SequentialReader, StorageOptions
from rosidl_runtime_py.utilities import get_message


def csv_rows(path, limit):
    with path.open(encoding='utf-8') as handle:
        return list(csv.DictReader(handle))[:limit]


def bag_diagnostics(path, limit):
    reader = SequentialReader()
    reader.open(StorageOptions(uri=str(path), storage_id='sqlite3'),
                ConverterOptions('cdr', 'cdr'))
    types = {item.name: item.type for item in reader.get_all_topics_and_types()}
    contacts, stability, phase_stamps = [], [], []
    while reader.has_next():
        topic, raw, _ = reader.read_next()
        if topic not in ('/nova/contact_diagnostics', '/nova/stability', '/nova/gait_phase'):
            continue
        msg = deserialize_message(raw, get_message(types[topic]))
        data = json.loads(msg.data)
        cycle = data.get('cycle_index')
        if topic == '/nova/gait_phase':
            if data.get('mode') == 'step' and cycle is not None and int(cycle) < limit:
                phase_stamps.append(_)
            continue
        if topic == '/nova/contact_diagnostics':
            if (data.get('mode') == 'step' and data.get('comparison_available')
                    and cycle is not None and int(cycle) < limit):
                contacts.append(bool(data.get('match')))
        elif data.get('available') and data.get('margin_m') is not None:
            stability.append((_, float(data['margin_m'])))
    if phase_stamps:
        margins = [value for stamp, value in stability
                   if phase_stamps[0] <= stamp <= phase_stamps[-1]]
    else:
        margins = []
    return {
        'contact_match_percent': 100.0 * np.mean(contacts) if contacts else float('nan'),
        'stability_margin_mean_m': float(np.mean(margins)) if margins else float('nan'),
        'stability_margin_min_m': float(np.min(margins)) if margins else float('nan'),
        'stability_available_samples': len(margins),
    }


def summarize(name, bag, movement_csv, tracking_csv, limit):
    movement = csv_rows(movement_csv, limit)
    tracking = csv_rows(tracking_csv, limit)
    steady_movement = movement[1:] if len(movement) > 1 else movement
    steady_tracking = tracking[1:] if len(tracking) > 1 else tracking
    mean = lambda rows, key: float(np.mean([float(row[key]) for row in rows]))
    result = {
        'simulador': name,
        'ciclos_comparados': min(len(movement), len(tracking)),
        'avance_m_ciclo': mean(steady_movement, 'avance_m'),
        'roll_max_deg': mean(steady_movement, 'roll_max_abs_deg'),
        'pitch_max_deg': mean(steady_movement, 'pitch_max_abs_deg'),
        'altura_media_m': mean(steady_movement, 'altura_media_m'),
        'seguimiento_rms_rad': mean(steady_tracking, 'error_rms_rad'),
        'seguimiento_max_rad': max(float(row['error_max_abs_rad']) for row in tracking),
        'salto_max_rad': max(float(row['salto_articular_max_rad']) for row in movement),
    }
    result.update(bag_diagnostics(bag, limit))
    return result


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--gazebo-bag', type=Path, required=True)
    parser.add_argument('--mujoco-bag', type=Path, required=True)
    parser.add_argument('--gazebo-analysis', type=Path, required=True)
    parser.add_argument('--mujoco-analysis', type=Path, required=True)
    parser.add_argument('--gazebo-tracking', type=Path, required=True)
    parser.add_argument('--mujoco-tracking', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--cycles', type=int, default=11)
    args = parser.parse_args()
    args.output.mkdir(parents=True, exist_ok=True)
    rows = [
        summarize('Gazebo', args.gazebo_bag,
                  args.gazebo_analysis / 'metricas_por_ciclo.csv',
                  args.gazebo_tracking / 'metricas_mujoco_por_ciclo.csv', args.cycles),
        summarize('MuJoCo', args.mujoco_bag,
                  args.mujoco_analysis / 'metricas_por_ciclo.csv',
                  args.mujoco_tracking / 'metricas_mujoco_por_ciclo.csv', args.cycles),
    ]
    with (args.output / 'comparacion_simuladores.csv').open('w', newline='', encoding='utf-8') as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader(); writer.writerows(rows)

    fields = [('avance_m_ciclo', 'Avance/ciclo (m)'), ('roll_max_deg', 'Roll máx. (°)'),
              ('pitch_max_deg', 'Pitch máx. (°)'), ('seguimiento_rms_rad', 'Error RMS (rad)'),
              ('contact_match_percent', 'Coincidencia contactos (%)'),
              ('stability_margin_mean_m', 'Margen medio (m)')]
    fig, axes = plt.subplots(2, 3, figsize=(12, 7), constrained_layout=True)
    for axis, (field, label) in zip(axes.flat, fields):
        axis.bar([row['simulador'] for row in rows], [row[field] for row in rows],
                 color=['#1f77b4', '#ff7f0e'])
        axis.set_ylabel(label); axis.grid(True, axis='y', alpha=.3)
    fig.suptitle(f'Campañas equivalentes: {args.cycles} ciclos (ciclo 1 transitorio)')
    fig.savefig(args.output / 'comparacion_gazebo_mujoco.png', dpi=180)
    plt.close(fig)

    lines = ['# Comparación Gazebo–MuJoCo', '',
             f'Configuración común: marcha paso, 32 muestras, 0,18 s/muestra; {args.cycles} ciclos. '
             'Las medias dinámicas excluyen el ciclo 1 como transitorio.', '',
             '| Simulador | Avance/ciclo (m) | Roll máx. (°) | Pitch máx. (°) | Altura (m) | Error RMS (rad) | Coincidencia contactos | Margen medio (m) | Margen mínimo (m) |',
             '|---|---:|---:|---:|---:|---:|---:|---:|---:|']
    for row in rows:
        lines.append(f"| {row['simulador']} | {row['avance_m_ciclo']:.6f} | {row['roll_max_deg']:.6f} | {row['pitch_max_deg']:.6f} | {row['altura_media_m']:.6f} | {row['seguimiento_rms_rad']:.6f} | {row['contact_match_percent']:.3f} % | {row['stability_margin_mean_m']:.6f} | {row['stability_margin_min_m']:.6f} |")
    lines += ['', 'Los resultados verifican equivalencia de interfaces y procedimiento, no identidad física. '
              'Las diferencias cuantitativas reflejan motores de contacto y parámetros provisionales distintos; '
              'el sistema se mantiene denominado **modelo digital configurable**.', '']
    (args.output / 'INFORME_EQUIVALENCIA.md').write_text('\n'.join(lines), encoding='utf-8')
    print(json.dumps(rows, indent=2, ensure_ascii=False))


if __name__ == '__main__':
    main()
