#!/usr/bin/env python3
"""Compara métricas disponibles y audita sensores equivalentes."""
import csv
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'Experimentos' / 'comparacion_gazebo_mujoco_20260902'
GZ = ROOT / 'Experimentos' / 'resultados_paso_r2_20260901' / 'metricas_por_ciclo.csv'
MJ = ROOT / 'Experimentos' / 'analisis' / 'paso_mujoco_20260814' / 'metricas_mujoco_por_ciclo.csv'

def read(path):
    with path.open(encoding='utf-8') as f: return list(csv.DictReader(f))

def main():
    OUT.mkdir(parents=True, exist_ok=True)
    gz, mj = read(GZ), read(MJ)
    n = min(len(gz), len(mj)); gz, mj = gz[:n], mj[:n]
    rows = []
    for a, b in zip(gz, mj):
        rows.append({'ciclo': a['ciclo'], 'gazebo_duracion_s': a['duracion_observada_s'],
                     'mujoco_duracion_s': b['duracion_s'],
                     'gazebo_velocidad_articular_max_rad_s': a['velocidad_articular_max_rad_s'],
                     'mujoco_error_rms_rad': b['error_rms_rad'],
                     'mujoco_error_max_abs_rad': b['error_max_abs_rad']})
    with (OUT / 'comparacion_por_ciclo.csv').open('w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
    gd = np.array([float(r['gazebo_duracion_s']) for r in rows]); md = np.array([float(r['mujoco_duracion_s']) for r in rows])
    fig, ax = plt.subplots(2, 1, figsize=(9, 6), sharex=True, constrained_layout=True)
    ax[0].plot(gd, label='Gazebo: duración observada'); ax[0].plot(md, label='MuJoCo: duración de ciclo')
    ax[0].set_ylabel('Duración (s)'); ax[0].grid(alpha=.3); ax[0].legend()
    ax[1].plot(np.array([float(r['gazebo_velocidad_articular_max_rad_s']) for r in rows]), label='Gazebo: velocidad máxima')
    ax[1].plot(np.array([float(r['mujoco_error_rms_rad']) for r in rows]), label='MuJoCo: error RMS')
    ax[1].set_xlabel('Ciclo compartido'); ax[1].set_ylabel('Magnitud (rad/s o rad)'); ax[1].grid(alpha=.3); ax[1].legend()
    fig.suptitle('Comparación de ejecución paso: Gazebo–MuJoCo')
    fig.savefig(OUT / 'comparacion_gazebo_mujoco.png', dpi=220); plt.close(fig)
    report = ['# Comparación Gazebo–MuJoCo', '', f'- Ciclos comparados: {n}.',
              f'- Duración media Gazebo: {gd.mean():.6f} s.', f'- Duración media MuJoCo: {md.mean():.6f} s.',
              f'- Diferencia relativa de duración: {(md.mean()-gd.mean())/gd.mean()*100:.4f} %.',
              '', '## Sensores equivalentes', '',
              'MuJoCo incorpora en `mujoco/nova_sm3.xml` un acelerómetro y cuatro sensores táctiles, equivalentes conceptualmente a la IMU `/nova/imu` y a los cuatro tópicos `/nova/contacts/*` de Gazebo.',
              'La bolsa MuJoCo histórica usada en esta comparación fue grabada antes de exponer esos sensores en ROS 2; por eso contiene `/joint_states` y `/tf`, pero no tópicos de IMU/contacto. La comparación cuantitativa de contactos e IMU queda marcada como siguiente adquisición, no se infiere a partir de datos ausentes.',
              '', 'La figura compara únicamente variables con registro común y no afirma equivalencia física entre motores.']
    (OUT / 'INFORME_COMPARACION.md').write_text('\n'.join(report), encoding='utf-8')
    print(f'Comparación generada: {n} ciclos')

if __name__ == '__main__': main()
