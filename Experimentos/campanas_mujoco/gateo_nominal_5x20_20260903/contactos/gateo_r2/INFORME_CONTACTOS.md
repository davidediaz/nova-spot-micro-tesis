# Análisis de contactos medidos durante gateo

- Bolsa: `Experimentos/campanas_mujoco/gateo_nominal_5x20_20260903/rosbag2/gateo_r2`.
- Ventana gateo--stand: 92.482363 s.
- Ciclos completos según `/nova/gait_phase`: 21.
- Índices de ciclo completos: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20].
- Estados comprimidos analizados: 554.
- Coincidencia simultánea filtrada de las cuatro patas: 68.931 %.

## Resultado por pata

| Pata | Coincidencia | Retardo despegue medio | Retardo aterrizaje medio |
|---|---:|---:|---:|
| fl | 85.961 % | 0.069713 s | 0.030386 s |
| fr | 86.302 % | 0.069771 s | 0.032453 s |
| rl | 87.744 % | sin pares | sin pares |
| rr | 87.427 % | sin pares | sin pares |

## Comparación crudo frente a filtrado

- Coincidencia simultánea cruda: 71.293 %.
- Coincidencia simultánea filtrada: 68.931 %.

| Pata | Coincidencia cruda | Coincidencia filtrada |
|---|---:|---:|
| fl | 86.383 % | 85.961 % |
| fr | 86.670 % | 86.302 % |
| rl | 87.789 % | 87.744 % |
| rr | 87.472 % | 87.427 % |

| Pata | Transición | Retardo crudo medio | Retardo filtrado medio |
|---|---|---:|---:|
| fl | liftoff | 0.036373 s | 0.069713 s |
| fl | landing | 0.022680 s | 0.030386 s |
| fr | liftoff | 0.037537 s | 0.069771 s |
| fr | landing | 0.022509 s | 0.032453 s |
| rl | liftoff | 0.040798 s | sin pares |
| rl | landing | -0.493911 s | sin pares |
| rr | liftoff | 0.038536 s | sin pares |
| rr | landing | -0.493268 s | sin pares |

Persistencia cruda exigida para declarar vuelo filtrado: 0.120 s.

| Pata | Episodios acotados | Duración media | Duración máxima | Episodios que superan el umbral |
|---|---:|---:|---:|---:|
| fl | 45 | 0.501627 s | 0.535657 s | 43 |
| fr | 46 | 0.480069 s | 0.535329 s | 42 |
| rl | 9 | 0.004646 s | 0.008802 s | 0 |
| rr | 11 | 0.003778 s | 0.007045 s | 0 |

Un retardo positivo indica que la transición medida ocurrió después de la prevista; uno negativo indica que ocurrió antes. Los pares se buscan dentro de ±1,8 s. Los porcentajes están ponderados por tiempo, no por número de mensajes.

El análisis es descriptivo y no activa decisiones del supervisor.
