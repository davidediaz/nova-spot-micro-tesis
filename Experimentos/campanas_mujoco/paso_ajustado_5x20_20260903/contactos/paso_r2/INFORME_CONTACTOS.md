# Análisis de contactos medidos durante marcha paso

- Bolsa: `Experimentos/campanas_mujoco/paso_ajustado_5x20_20260903/rosbag2/paso_r2`.
- Ventana paso--stand: 122.679147 s.
- Ciclos completos según `/nova/gait_phase`: 21.
- Índices de ciclo completos: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20].
- Estados comprimidos analizados: 465.
- Coincidencia simultánea filtrada de las cuatro patas: 36.665 %.

## Resultado por pata

| Pata | Coincidencia | Retardo despegue medio | Retardo aterrizaje medio |
|---|---:|---:|---:|
| fl | 75.189 % | 0.251282 s | -0.142254 s |
| fr | 75.509 % | 0.250089 s | -0.142928 s |
| rl | 75.334 % | sin pares | sin pares |
| rr | 75.131 % | sin pares | sin pares |

## Comparación crudo frente a filtrado

- Coincidencia simultánea cruda: 37.447 %.
- Coincidencia simultánea filtrada: 36.665 %.

| Pata | Coincidencia cruda | Coincidencia filtrada |
|---|---:|---:|
| fl | 75.141 % | 75.189 % |
| fr | 75.479 % | 75.509 % |
| rl | 75.384 % | 75.334 % |
| rr | 75.165 % | 75.131 % |

| Pata | Transición | Retardo crudo medio | Retardo filtrado medio |
|---|---|---:|---:|
| fl | liftoff | 0.218634 s | 0.251282 s |
| fl | landing | -0.152729 s | -0.142254 s |
| fr | liftoff | 0.218811 s | 0.250089 s |
| fr | landing | -0.152008 s | -0.142928 s |
| rl | liftoff | 1.205493 s | sin pares |
| rl | landing | -0.160122 s | sin pares |
| rr | liftoff | 1.013911 s | sin pares |
| rr | landing | -0.284748 s | sin pares |

Persistencia cruda exigida para declarar vuelo filtrado: 0.120 s.

| Pata | Episodios acotados | Duración media | Duración máxima | Episodios que superan el umbral |
|---|---:|---:|---:|---:|
| fl | 43 | 1.064354 s | 1.074163 s | 43 |
| fr | 42 | 1.064962 s | 1.078112 s | 42 |
| rl | 14 | 0.004405 s | 0.016080 s | 0 |
| rr | 13 | 0.003231 s | 0.005828 s | 0 |

Un retardo positivo indica que la transición medida ocurrió después de la prevista; uno negativo indica que ocurrió antes. Los pares se buscan dentro de ±1,8 s. Los porcentajes están ponderados por tiempo, no por número de mensajes.

El análisis es descriptivo y no activa decisiones del supervisor.
