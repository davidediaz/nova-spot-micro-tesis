#!/usr/bin/env python3
"""Genera las figuras de workspace, manipulabilidad y velocidad articular."""
from pathlib import Path
import sys
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'src' / 'nova_gait_controller'))
from nova_gait_controller.kinematics import (forward_leg, cartesian_crawl,
                                              cartesian_step_walk)
from nova_gait_controller.mathematical_model import leg_jacobian
from nova_gait_controller.gait_controller import STAND

OUT = ROOT / 'Documento_TESIS' / 'Figures' / 'Resultados'

def workspace_and_singularities():
    q0 = np.array(STAND)
    points, dexterity, cond = [], [], []
    for qc in np.linspace(-0.60, 0.60, 31):
        for qf in np.linspace(-1.20, 1.20, 41):
            for qt in np.linspace(-2.20, 0.10, 41):
                q = (qc, qf, qt)
                p = forward_leg(*q, side=1)
                s = np.linalg.svd(np.asarray(leg_jacobian(*q, 1)), compute_uv=False)
                points.append(p); dexterity.append(s[-1]); cond.append(s[0] / max(s[-1], 1e-12))
    points, dexterity, cond = map(np.asarray, (points, dexterity, cond))
    fig = plt.figure(figsize=(10, 4.5), constrained_layout=True)
    ax = fig.add_subplot(121, projection='3d')
    sc = ax.scatter(points[:, 0], points[:, 1], points[:, 2], c=dexterity,
                    s=2, cmap='viridis', alpha=.25)
    ax.scatter(*forward_leg(*q0, 1), c='r', s=45, label='Postura nominal')
    ax.set(xlabel='x (m)', ylabel='y (m)', zlabel='z (m)', title='Workspace alcanzable')
    ax.legend(loc='upper left'); fig.colorbar(sc, ax=ax, shrink=.7, label='σmín (m/rad)')
    ax2 = fig.add_subplot(122)
    ax2.hist(np.log10(cond), bins=45, color='#4472c4', alpha=.85)
    ax2.axvline(np.log10(6.647), color='#b22222', ls='--', label='Nominal: κ=6,647')
    ax2.set(xlabel='log10(número de condición κ)', ylabel='Configuraciones',
            title='Distribución de cercanía a singularidad')
    ax2.legend(); fig.savefig(OUT / 'workspace_singularidades.png', dpi=220); plt.close(fig)
    np.savetxt(OUT / 'workspace_muestra.csv', np.c_[points, dexterity, cond], delimiter=',',
               header='x_m,y_m,z_m,sigma_min_m_rad,condition_number', comments='')

def joint_velocities():
    scenarios = [('Gateo', cartesian_crawl(STAND, samples=24), 5.76),
                 ('Paso', cartesian_step_walk(STAND, samples=32), 5.76)]
    fig, axes = plt.subplots(2, 1, figsize=(9, 6.5), sharex=False, constrained_layout=True)
    for ax, (name, poses, period) in zip(axes, scenarios):
        q = np.asarray(poses); dt = period / len(q)
        vel = np.vstack((q[1:] - q[:-1], q[0] - q[-1])) / dt
        ax.plot(np.arange(len(q)) * dt, np.max(np.abs(vel), axis=1), label='Máxima entre 12 articulaciones')
        ax.plot(np.arange(len(q)) * dt, np.mean(np.abs(vel), axis=1), label='Media absoluta')
        ax.axhline(6.981317, color='#b22222', ls='--', label='Límite URDF: 6,981 rad/s')
        ax.set_title(name); ax.set_ylabel('Velocidad (rad/s)'); ax.grid(alpha=.3); ax.legend()
    axes[-1].set_xlabel('Tiempo dentro del ciclo (s)')
    fig.suptitle('Velocidades articulares de las referencias nominales')
    fig.savefig(OUT / 'velocidades_articulares.png', dpi=220); plt.close(fig)
    np.savetxt(OUT / 'velocidades_articulares.csv', np.c_[np.arange(len(scenarios[0][1])) * scenarios[0][2] / len(scenarios[0][1]),
        np.max(np.abs((np.vstack((np.asarray(scenarios[0][1])[1:] - np.asarray(scenarios[0][1])[:-1], np.asarray(scenarios[0][1])[0] - np.asarray(scenarios[0][1])[-1])) / (scenarios[0][2]/len(scenarios[0][1])))), axis=1)], delimiter=',', header='tiempo_s,velocidad_max_gateo_rad_s', comments='')

if __name__ == '__main__':
    OUT.mkdir(parents=True, exist_ok=True)
    workspace_and_singularities(); joint_velocities()
    print(f'Figuras generadas en {OUT}')
