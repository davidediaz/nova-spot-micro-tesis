#!/usr/bin/env python3
"""Regenera figuras propias del documento final desde los CSV aceptados."""

import csv
from pathlib import Path

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np


HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
OUTPUT = HERE / 'Figures' / 'Resultados'


def read_csv(path):
    with path.open(encoding='utf-8') as handle:
        return list(csv.DictReader(handle))


def plot_contact_episodes():
    path = (ROOT / 'Experimentos' / 'analisis'
            / 'contactos_debounce_nominal_valido_20260901_0828'
            / 'episodios_sin_contacto_crudo.csv')
    rows = read_csv(path)
    legs = ('fl', 'fr', 'rl', 'rr')
    durations = {
        leg: [float(row['duration_s']) for row in rows
              if row['leg'] == leg and row['duration_s']]
        for leg in legs
    }
    means = [np.mean(durations[leg]) for leg in legs]
    maxima = [np.max(durations[leg]) for leg in legs]
    x = np.arange(len(legs))
    width = 0.35
    figure, axis = plt.subplots(figsize=(9, 5.2), constrained_layout=True)
    axis.bar(x - width / 2, means, width, label='Duración media')
    axis.bar(x + width / 2, maxima, width, label='Duración máxima')
    axis.axhline(0.12, color='#b22222', linestyle='--', linewidth=1.6,
                 label='Debounce de pérdida: 0,12 s')
    axis.set_xticks(x, [leg.upper() for leg in legs])
    axis.set_ylabel('Duración del episodio crudo sin contacto (s)')
    axis.set_title('Persistencia de las pérdidas crudas de contacto')
    axis.grid(True, axis='y', alpha=0.3)
    axis.legend()
    figure.savefig(OUTPUT / 'contacto_persistencia_cruda.png', dpi=180)
    plt.close(figure)


def plot_mujoco_tracking():
    path = (ROOT / 'Experimentos' / 'analisis' / 'paso_mujoco_20260814'
            / 'metricas_mujoco_por_ciclo.csv')
    rows = read_csv(path)
    cycles = [int(row['ciclo']) for row in rows]
    rms = [float(row['error_rms_rad']) for row in rows]
    maximum = [float(row['error_max_abs_rad']) for row in rows]
    duration_error_ms = [
        1000.0 * (float(row['duracion_s']) - 5.76) for row in rows]
    figure, axes = plt.subplots(2, 1, figsize=(9, 7), sharex=True,
                               constrained_layout=True)
    axes[0].plot(cycles, rms, marker='o', label='Error RMS')
    axes[0].plot(cycles, maximum, marker='s', label='Error máximo absoluto')
    axes[0].set_ylabel('Error articular (rad)')
    axes[0].grid(True, alpha=0.3)
    axes[0].legend()
    axes[1].plot(cycles, duration_error_ms, marker='o', color='#2e8b57')
    axes[1].axhline(0.0, color='0.35', linestyle='--',
                    label='Duración nominal: 5,76 s')
    axes[1].set_ylabel('Error de duración (ms)')
    axes[1].set_xlabel('Ciclo')
    axes[1].set_xticks(cycles)
    axes[1].grid(True, alpha=0.3)
    axes[1].legend()
    figure.suptitle('Marcha paso en MuJoCo: seguimiento y cadencia')
    figure.savefig(OUTPUT / 'paso_mujoco_seguimiento.png', dpi=180)
    plt.close(figure)


def main():
    OUTPUT.mkdir(parents=True, exist_ok=True)
    plot_contact_episodes()
    plot_mujoco_tracking()
    print(f'Figuras generadas en {OUTPUT}')


if __name__ == '__main__':
    main()
