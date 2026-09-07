# Análisis de contactos medidos durante marcha paso

- Bolsa: `Experimentos/campanas_mujoco/barrido_friccion_paso_r2_20260903/friction_12/rosbag2/paso_r1`.
- Ventana paso--stand: 29.440953 s.
- Ciclos completos según `/nova/gait_phase`: 5.
- Índices de ciclo completos: [0, 1, 2, 3, 4].
- Estados comprimidos analizados: 125.
- Coincidencia simultánea filtrada de las cuatro patas: 23.371 %.

## Resultado por pata

| Pata | Coincidencia | Retardo despegue medio | Retardo aterrizaje medio |
|---|---:|---:|---:|
| fl | 79.492 % | 0.440573 s | -0.330196 s |
| fr | 81.033 % | 0.436685 s | -0.332185 s |
| rl | 75.522 % | sin pares | sin pares |
| rr | 75.508 % | sin pares | sin pares |

## Comparación crudo frente a filtrado

- Coincidencia simultánea cruda: 24.263 %.
- Coincidencia simultánea filtrada: 23.371 %.

| Pata | Coincidencia cruda | Coincidencia filtrada |
|---|---:|---:|
| fl | 79.450 % | 79.492 % |
| fr | 80.969 % | 81.033 % |
| rl | 75.522 % | 75.522 % |
| rr | 75.508 % | 75.508 % |

| Pata | Transición | Retardo crudo medio | Retardo filtrado medio |
|---|---|---:|---:|
| fl | liftoff | 0.406535 s | 0.440573 s |
| fl | landing | -0.340409 s | -0.330196 s |
| fr | liftoff | 0.404998 s | 0.436685 s |
| fr | landing | -0.341514 s | -0.332185 s |
| rl | liftoff | sin pares | sin pares |
| rl | landing | sin pares | sin pares |
| rr | liftoff | sin pares | sin pares |
| rr | landing | sin pares | sin pares |

Persistencia cruda exigida para declarar vuelo filtrado: 0.120 s.

| Pata | Episodios acotados | Duración media | Duración máxima | Episodios que superan el umbral |
|---|---:|---:|---:|---:|
| fl | 18 | 0.297760 s | 0.697545 s | 10 |
| fr | 13 | 0.410186 s | 0.696478 s | 10 |
| rl | 0 | sin episodios | sin episodios | 0 |
| rr | 0 | sin episodios | sin episodios | 0 |

Un retardo positivo indica que la transición medida ocurrió después de la prevista; uno negativo indica que ocurrió antes. Los pares se buscan dentro de ±1,8 s. Los porcentajes están ponderados por tiempo, no por número de mensajes.

El análisis es descriptivo y no activa decisiones del supervisor.
