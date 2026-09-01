#!/usr/bin/env python3
"""Criba determinista de sensibilidad del modelo nominal, sin simulador."""

import argparse
import csv
from dataclasses import replace
from pathlib import Path
import sys

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT / 'src' / 'nova_gait_controller'
sys.path.insert(0, str(PACKAGE))

from nova_gait_controller.kinematics import cartesian_crawl, cartesian_step_walk
from nova_gait_controller.mathematical_model import (
    DEFAULT_PARAMETERS, actuator_current, inverse_dynamics,
)


def trajectory_metrics(poses, duration, parameters):
    q = np.asarray(poses, dtype=float).reshape(len(poses), 4, 3)
    q_cycle = np.concatenate((q[-1:], q, q[:1]), axis=0)
    velocity = (q_cycle[2:] - q_cycle[:-2]) / (2.0 * duration)
    acceleration = (q_cycle[2:] - 2.0 * q_cycle[1:-1] + q_cycle[:-2]) / duration**2
    torques = []
    for sample in range(len(q)):
        for leg, side in enumerate((1, -1, 1, -1)):
            torques.extend(inverse_dynamics(
                q[sample, leg], velocity[sample, leg], acceleration[sample, leg],
                side, parameters=parameters))
    torques = np.abs(np.asarray(torques))
    return float(torques.max()), float(np.percentile(torques, 95)), \
        float(max(actuator_current(value) for value in torques))


def scenarios():
    p = DEFAULT_PARAMETERS
    yield 'nominal', p
    for label, scale in (('masa_menos_10', 0.9), ('masa_mas_10', 1.1)):
        yield label, replace(p, body_mass=p.body_mass * scale,
                             coxa_mass=p.coxa_mass * scale,
                             femur_mass=p.femur_mass * scale,
                             tibia_mass=p.tibia_mass * scale,
                             foot_mass=p.foot_mass * scale)
    yield 'amortiguamiento_menos_50', replace(p, joint_damping=p.joint_damping * 0.5)
    yield 'amortiguamiento_mas_50', replace(p, joint_damping=p.joint_damping * 1.5)
    yield 'friccion_articular_menos_50', replace(p, coulomb_friction=p.coulomb_friction * 0.5)
    yield 'friccion_articular_mas_50', replace(p, coulomb_friction=p.coulomb_friction * 1.5)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', type=Path, default=ROOT / 'Experimentos' / 'sensibilidad_nominal_20260901')
    args = parser.parse_args()
    args.output.mkdir(parents=True, exist_ok=True)
    stand = (0.0, 0.42, -0.84)
    gaits = {
        'gateo': (cartesian_crawl(stand), 0.18),
        'paso': (cartesian_step_walk(stand), 0.18),
    }
    rows = []
    for gait, (poses, duration) in gaits.items():
        nominal = None
        for scenario, parameters in scenarios():
            maximum, p95, current = trajectory_metrics(poses, duration, parameters)
            if scenario == 'nominal':
                nominal = maximum
            rows.append({
                'marcha': gait, 'escenario': scenario,
                'par_max_nm': f'{maximum:.9f}', 'par_p95_nm': f'{p95:.9f}',
                'corriente_max_servo_estimada_a': f'{current:.9f}',
                'cambio_par_max_pct': f'{100.0 * (maximum / nominal - 1.0):.6f}',
            })
    csv_path = args.output / 'sensibilidad_dinamica.csv'
    with csv_path.open('w', newline='', encoding='utf-8') as handle:
        writer = csv.DictWriter(handle, fieldnames=rows[0].keys())
        writer.writeheader(); writer.writerows(rows)
    largest = max(rows, key=lambda row: abs(float(row['cambio_par_max_pct'])))
    report = f"""# Criba de sensibilidad dinámica nominal

Fecha: 1 de septiembre de 2026. Análisis determinista sin Gazebo ni MuJoCo.

Se evaluaron {len(rows)} combinaciones de marcha y escenario. La mayor variación
del par máximo frente al caso nominal fue {largest['cambio_par_max_pct']} % en
`{largest['marcha']}/{largest['escenario']}`. Los pares proceden de dinámica
inversa sobre referencias discretas; la corriente usa la envolvente de catálogo
del MG996R y no constituye una predicción eléctrica validada.

Este análisis prioriza masas y resistencias articulares. Geometría, fricción de
suelo, contacto y retardos deben estudiarse en simuladores porque esta criba no
integra movimiento del cuerpo ni solución temporal del contacto.
"""
    (args.output / 'INFORME_SENSIBILIDAD.md').write_text(report, encoding='utf-8')
    print(csv_path)


if __name__ == '__main__':
    main()
