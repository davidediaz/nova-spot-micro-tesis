#!/usr/bin/env python3
"""Genera evidencia reproducible de workspace, singularidad y velocidad."""
import csv
from pathlib import Path
import sys
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'src' / 'nova_gait_controller'))
from nova_gait_controller.gait_controller import STAND
from nova_gait_controller.kinematics import cartesian_crawl, cartesian_step_walk, forward_leg
from nova_gait_controller.mathematical_model import leg_jacobian

OUT = ROOT / 'Documento_TESIS' / 'Figures' / 'Resultados'
JOINTS = ('coxa', 'femur', 'tibia')
VELOCITY_LIMIT = 6.981317
SIGMA_THRESHOLD = 0.005
CONDITION_THRESHOLD = 100.0


def workspace_and_singularities():
    points, sigma, condition = [], [], []
    for qc in np.linspace(-0.60, 0.60, 31):
        for qf in np.linspace(-1.20, 1.20, 41):
            for qt in np.linspace(-2.20, 0.10, 41):
                q = (qc, qf, qt)
                s = np.linalg.svd(np.asarray(leg_jacobian(*q, 1)), compute_uv=False)
                points.append(forward_leg(*q, side=1)); sigma.append(s[-1])
                condition.append(s[0] / max(s[-1], 1e-12))
    points, sigma, condition = map(np.asarray, (points, sigma, condition))
    p0 = forward_leg(*STAND, side=1)
    s0 = np.linalg.svd(np.asarray(leg_jacobian(*STAND, 1)), compute_uv=False)
    kappa0 = s0[0] / s0[-1]
    near = sigma < SIGMA_THRESHOLD

    fig = plt.figure(figsize=(13, 4.4), constrained_layout=True)
    ax = fig.add_subplot(131, projection='3d')
    ax.scatter(points[:, 0], points[:, 1], points[:, 2], c=sigma, s=1.2,
               cmap='viridis', alpha=.22, rasterized=True)
    ax.scatter(*p0, c='#d62728', s=42, label='Postura nominal')
    ax.set(xlabel='x (m)', ylabel='y (m)', zlabel='z (m)',
           title='Workspace por límites articulares'); ax.legend(fontsize=8)
    ax2 = fig.add_subplot(132)
    ax2.scatter(points[~near, 0], points[~near, 2], s=1, c='#8bb8df',
                alpha=.12, rasterized=True, label='Regular')
    ax2.scatter(points[near, 0], points[near, 2], s=2, c='#c62828',
                alpha=.35, rasterized=True, label=r'$\sigma_{min}<0,005$ m/rad')
    ax2.scatter(p0[0], p0[2], c='#111111', marker='*', s=70, label='Postura nominal')
    ax2.set(xlabel='x (m)', ylabel='z (m)', title='Proximidad singular localizada')
    ax2.grid(alpha=.2); ax2.legend(fontsize=8)
    ax3 = fig.add_subplot(133)
    ax3.hist(np.log10(np.maximum(condition, 1.0)), bins=50, color='#4472c4', alpha=.85)
    ax3.axvline(np.log10(CONDITION_THRESHOLD), color='#c62828', ls='--', label=r'Umbral $\kappa=100$')
    ax3.axvline(np.log10(kappa0), color='#111111', ls=':', label=f'Nominal: κ={kappa0:.3f}')
    ax3.set(xlabel=r'$\log_{10}(\kappa)$', ylabel='Configuraciones',
            title='Condicionamiento del Jacobiano'); ax3.legend(fontsize=8)
    fig.savefig(OUT / 'workspace_singularidades.png', dpi=220); plt.close(fig)
    np.savetxt(OUT / 'workspace_muestra.csv', np.c_[points, sigma, condition, near.astype(int)],
               delimiter=',', header=('x_m,y_m,z_m,sigma_min_m_rad,condition_number,'
                                       'near_singular_sigma_lt_0p005'), comments='')
    return dict(samples=len(points), sigma_min=sigma.min(), sigma_max=sigma.max(),
                near_count=int(near.sum()), ill_count=int((condition > CONDITION_THRESHOLD).sum()),
                nominal_sigma=s0[-1], nominal_condition=kappa0)


def joint_velocities():
    scenarios = (('gateo', cartesian_crawl(STAND, samples=24), 4.32),
                 ('paso', cartesian_step_walk(STAND, samples=32), 5.76))
    rows, summary = [], {}
    fig, axes = plt.subplots(2, 1, figsize=(9.2, 6.8), constrained_layout=True)
    for ax, (name, poses, period) in zip(axes, scenarios):
        q = np.asarray(poses).reshape(len(poses), 4, 3); dt = period / len(q)
        velocity = (np.roll(q, -1, axis=0) - q) / dt
        time_s = np.arange(len(q)) * dt
        for joint, color in zip(range(3), ('#1f77b4', '#ff7f0e', '#2ca02c')):
            ax.step(time_s, np.max(np.abs(velocity[:, :, joint]), axis=1),
                    where='post', color=color, label=JOINTS[joint].capitalize())
        maximum = np.max(np.abs(velocity), axis=(1, 2))
        ax.plot(time_s, maximum, color='#111111', lw=1.8, label='Máxima entre 12')
        ax.axhline(VELOCITY_LIMIT, color='#b22222', ls='--', label='Límite URDF provisional')
        ax.set(title=f'{name.capitalize()} — ciclo {period:.2f} s', ylabel='|velocidad| (rad/s)',
               xlim=(0, period), ylim=(0, VELOCITY_LIMIT * 1.08)); ax.grid(alpha=.25)
        ax.legend(ncol=3, fontsize=8); summary[name] = float(maximum.max())
        for sample in range(len(q)):
            for leg in range(4):
                for joint in range(3):
                    rows.append(dict(marcha=name, muestra=sample, tiempo_s=f'{time_s[sample]:.6f}',
                                     pata=leg, articulacion=JOINTS[joint],
                                     velocidad_rad_s=f'{velocity[sample, leg, joint]:.9f}'))
    axes[-1].set_xlabel('Tiempo dentro del ciclo (s)')
    fig.suptitle('Velocidades de las referencias articulares nominales')
    fig.savefig(OUT / 'velocidades_articulares.png', dpi=220); plt.close(fig)
    with (OUT / 'velocidades_articulares.csv').open('w', newline='', encoding='utf-8') as handle:
        writer = csv.DictWriter(handle, fieldnames=rows[0], lineterminator='\n')
        writer.writeheader(); writer.writerows(rows)
    return summary


def write_report(w, v):
    total = w['samples']
    text = f"""# Workspace, singularidades y velocidades articulares

Se exploraron {total} configuraciones uniformes dentro de los límites del URDF
para una pata izquierda. No representa espacio libre de colisiones ni una región
físicamente calibrada.

- Sigma mínima: {w['sigma_min']:.9f} a {w['sigma_max']:.9f} m/rad.
- Proximidad singular (sigma mínima < 0,005 m/rad): {w['near_count']} ({100*w['near_count']/total:.3f} %).
- Mal condicionadas (kappa > 100): {w['ill_count']} ({100*w['ill_count']/total:.3f} %).
- Postura nominal: sigma mínima {w['nominal_sigma']:.9f} m/rad y kappa {w['nominal_condition']:.6f}.
- Velocidad máxima de gateo: {v['gateo']:.9f} rad/s (ciclo 4,32 s).
- Velocidad máxima de paso: {v['paso']:.9f} rad/s (ciclo 5,76 s).

Las velocidades son diferencias hacia adelante entre referencias discretas,
incluido el cierre cíclico. El límite de 6,981317 rad/s procede del URDF y no
sustituye la caracterización del MG996R bajo carga.
"""
    (OUT / 'INFORME_GRAFICAS_CINEMATICA.md').write_text(text, encoding='utf-8')


if __name__ == '__main__':
    OUT.mkdir(parents=True, exist_ok=True)
    write_report(workspace_and_singularities(), joint_velocities())
    print(f'Figuras y datos generados en {OUT}')
