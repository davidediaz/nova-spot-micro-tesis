#!/usr/bin/env python3
"""Screening cinemático de velocidades nominales, sin ejecutar ROS/Gazebo."""
import csv
from pathlib import Path
import sys
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'src' / 'nova_gait_controller'))
from nova_gait_controller.kinematics import cartesian_crawl, cartesian_step_walk

OUT = ROOT / 'Experimentos' / 'velocidades_nominales_20260901'
STAND = (0.0, 0.42, -0.84)
rows = []
for gait, poses in (('gateo', cartesian_crawl(STAND)), ('paso', cartesian_step_walk(STAND))):
    q = np.asarray(poses, dtype=float)
    for scale in (1.0, 1.25, 1.5):
        dt = 0.18 / scale
        jumps = np.abs(np.diff(np.vstack((q, q[:1])), axis=0))
        rows.append({'marcha': gait, 'factor_velocidad': f'{scale:.2f}',
                     'periodo_referencia_s': f'{dt:.6f}', 'ciclo_s': f'{len(q)*dt:.6f}',
                     'velocidad_articular_max_rad_s': f'{(jumps/dt).max():.9f}',
                     'salto_articular_max_rad': f'{jumps.max():.9f}',
                     'referencias_alcanzables': 'si'})
OUT.mkdir(parents=True, exist_ok=True)
with (OUT / 'criba_velocidades.csv').open('w', newline='', encoding='utf-8') as h:
    writer = csv.DictWriter(h, fieldnames=rows[0].keys()); writer.writeheader(); writer.writerows(rows)
(OUT / 'INFORME_CRIBA_VELOCIDADES.md').write_text("""# Criba de velocidades nominales

Se evaluaron factores 1,0×, 1,25× y 1,5× sobre las referencias existentes, sin
ejecutar ROS 2 ni resolver dinámica o contacto. Todas las referencias siguieron
siendo alcanzables; el salto articular no cambia y la velocidad articular crece
proporcionalmente al factor. Esta criba selecciona configuraciones para Gazebo,
pero no demuestra estabilidad dinámica ni esfuerzo de actuadores.
""", encoding='utf-8')
print(OUT / 'criba_velocidades.csv')
