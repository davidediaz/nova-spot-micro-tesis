# Análisis de contactos medidos durante marcha paso

- Bolsa: `Experimentos/campanas_mujoco/paso_5x20_r2_20260902/rosbag2/paso_r1`.
- Ventana paso--stand: 121.178754 s.
- Ciclos completos según `/nova/gait_phase`: 21.
- Índices de ciclo completos: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20].
- Estados comprimidos analizados: 96.
- Coincidencia simultánea filtrada de las cuatro patas: 0.000 %.

## Resultado por pata

| Pata | Coincidencia | Retardo despegue medio | Retardo aterrizaje medio |
|---|---:|---:|---:|
| fl | 74.940 % | sin pares | sin pares |
| fr | 75.038 % | sin pares | sin pares |
| rl | 74.977 % | sin pares | sin pares |
| rr | 75.045 % | sin pares | sin pares |

## Comparación crudo frente a filtrado

- Coincidencia simultánea cruda: 0.013 %.
- Coincidencia simultánea filtrada: 0.000 %.

| Pata | Coincidencia cruda | Coincidencia filtrada |
|---|---:|---:|
| fl | 74.953 % | 74.940 % |
| fr | 75.038 % | 75.038 % |
| rl | 74.977 % | 74.977 % |
| rr | 75.045 % | 75.045 % |

| Pata | Transición | Retardo crudo medio | Retardo filtrado medio |
|---|---|---:|---:|
| fl | liftoff | 0.227177 s | sin pares |
| fl | landing | 0.241579 s | sin pares |
| fr | liftoff | sin pares | sin pares |
| fr | landing | sin pares | sin pares |
| rl | liftoff | sin pares | sin pares |
| rl | landing | sin pares | sin pares |
| rr | liftoff | sin pares | sin pares |
| rr | landing | sin pares | sin pares |

Persistencia cruda exigida para declarar vuelo filtrado: 0.120 s.

| Pata | Episodios acotados | Duración media | Duración máxima | Episodios que superan el umbral |
|---|---:|---:|---:|---:|
| fl | 1 | 0.015434 s | 0.015434 s | 0 |
| fr | 0 | sin episodios | sin episodios | 0 |
| rl | 0 | sin episodios | sin episodios | 0 |
| rr | 0 | sin episodios | sin episodios | 0 |

Un retardo positivo indica que la transición medida ocurrió después de la prevista; uno negativo indica que ocurrió antes. Los pares se buscan dentro de ±1,8 s. Los porcentajes están ponderados por tiempo, no por número de mensajes.

El análisis es descriptivo y no activa decisiones del supervisor.
