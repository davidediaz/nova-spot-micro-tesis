# Workspace, singularidades y velocidades articulares

Se exploraron 52111 configuraciones uniformes dentro de los límites del URDF
para una pata izquierda. No representa espacio libre de colisiones ni una región
físicamente calibrada.

- Sigma mínima: 0.000269816 a 0.064923868 m/rad.
- Proximidad singular (sigma mínima < 0,005 m/rad): 6045 (11.600 %).
- Mal condicionadas (kappa > 100): 3069 (5.889 %).
- Postura nominal: sigma mínima 0.038037375 m/rad y kappa 6.647045.
- Velocidad máxima de gateo: 0.944519549 rad/s (ciclo 4,32 s).
- Velocidad máxima de paso: 0.372327354 rad/s (ciclo 5,76 s).

Las velocidades son diferencias hacia adelante entre referencias discretas,
incluido el cierre cíclico. El límite de 6,981317 rad/s procede del URDF y no
sustituye la caracterización del MG996R bajo carga.
