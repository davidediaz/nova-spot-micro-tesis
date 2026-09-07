# Análisis de contactos medidos durante gateo

- Bolsa: `Experimentos/campanas_mujoco/gateo_nominal_5x20_20260903/rosbag2/gateo_r4`.
- Ventana gateo--stand: 95.024202 s.
- Ciclos completos según `/nova/gait_phase`: 22.
- Índices de ciclo completos: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21].
- Estados comprimidos analizados: 558.
- Coincidencia simultánea filtrada de las cuatro patas: 68.701 %.

## Resultado por pata

| Pata | Coincidencia | Retardo despegue medio | Retardo aterrizaje medio |
|---|---:|---:|---:|
| fl | 85.999 % | 0.069468 s | 0.030829 s |
| fr | 86.018 % | 0.068855 s | 0.031558 s |
| rl | 87.541 % | sin pares | sin pares |
| rr | 87.465 % | sin pares | sin pares |

## Comparación crudo frente a filtrado

- Coincidencia simultánea cruda: 71.169 %.
- Coincidencia simultánea filtrada: 68.701 %.

| Pata | Coincidencia cruda | Coincidencia filtrada |
|---|---:|---:|
| fl | 86.476 % | 85.999 % |
| fr | 86.441 % | 86.018 % |
| rl | 87.565 % | 87.541 % |
| rr | 87.524 % | 87.465 % |

| Pata | Transición | Retardo crudo medio | Retardo filtrado medio |
|---|---|---:|---:|
| fl | liftoff | 0.036467 s | 0.069468 s |
| fl | landing | 0.021659 s | 0.030829 s |
| fr | liftoff | 0.036175 s | 0.068855 s |
| fr | landing | 0.021855 s | 0.031558 s |
| rl | liftoff | 0.040534 s | sin pares |
| rl | landing | -0.495907 s | sin pares |
| rr | liftoff | 0.040188 s | sin pares |
| rr | landing | -0.493088 s | sin pares |

Persistencia cruda exigida para declarar vuelo filtrado: 0.120 s.

| Pata | Episodios acotados | Duración media | Duración máxima | Episodios que superan el umbral |
|---|---:|---:|---:|---:|
| fl | 45 | 0.514235 s | 0.537487 s | 44 |
| fr | 47 | 0.492661 s | 0.548287 s | 44 |
| rl | 7 | 0.003381 s | 0.007522 s | 0 |
| rr | 8 | 0.006998 s | 0.022006 s | 0 |

Un retardo positivo indica que la transición medida ocurrió después de la prevista; uno negativo indica que ocurrió antes. Los pares se buscan dentro de ±1,8 s. Los porcentajes están ponderados por tiempo, no por número de mensajes.

El análisis es descriptivo y no activa decisiones del supervisor.
