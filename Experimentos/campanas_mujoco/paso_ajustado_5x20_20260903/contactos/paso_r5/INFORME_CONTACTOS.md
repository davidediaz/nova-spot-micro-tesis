# Análisis de contactos medidos durante marcha paso

- Bolsa: `Experimentos/campanas_mujoco/paso_ajustado_5x20_20260903/rosbag2/paso_r5`.
- Ventana paso--stand: 121.967522 s.
- Ciclos completos según `/nova/gait_phase`: 21.
- Índices de ciclo completos: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20].
- Estados comprimidos analizados: 465.
- Coincidencia simultánea filtrada de las cuatro patas: 36.592 %.

## Resultado por pata

| Pata | Coincidencia | Retardo despegue medio | Retardo aterrizaje medio |
|---|---:|---:|---:|
| fl | 75.130 % | 0.250946 s | -0.143786 s |
| fr | 75.342 % | 0.250264 s | -0.143887 s |
| rl | 75.190 % | sin pares | sin pares |
| rr | 75.198 % | sin pares | sin pares |

## Comparación crudo frente a filtrado

- Coincidencia simultánea cruda: 37.416 %.
- Coincidencia simultánea filtrada: 36.592 %.

| Pata | Coincidencia cruda | Coincidencia filtrada |
|---|---:|---:|
| fl | 75.120 % | 75.130 % |
| fr | 75.352 % | 75.342 % |
| rl | 75.243 % | 75.190 % |
| rr | 75.247 % | 75.198 % |

| Pata | Transición | Retardo crudo medio | Retardo filtrado medio |
|---|---|---:|---:|
| fl | liftoff | 0.219636 s | 0.250946 s |
| fl | landing | -0.153193 s | -0.143786 s |
| fr | liftoff | 0.218129 s | 0.250264 s |
| fr | landing | -0.152369 s | -0.143887 s |
| rl | liftoff | 1.154894 s | sin pares |
| rl | landing | -0.254639 s | sin pares |
| rr | liftoff | 1.087368 s | sin pares |
| rr | landing | -0.242685 s | sin pares |

Persistencia cruda exigida para declarar vuelo filtrado: 0.120 s.

| Pata | Episodios acotados | Duración media | Duración máxima | Episodios que superan el umbral |
|---|---:|---:|---:|---:|
| fl | 42 | 1.063985 s | 1.082334 s | 42 |
| fr | 42 | 1.064768 s | 1.088367 s | 42 |
| rl | 16 | 0.004019 s | 0.009407 s | 0 |
| rr | 16 | 0.003739 s | 0.009993 s | 0 |

Un retardo positivo indica que la transición medida ocurrió después de la prevista; uno negativo indica que ocurrió antes. Los pares se buscan dentro de ±1,8 s. Los porcentajes están ponderados por tiempo, no por número de mensajes.

El análisis es descriptivo y no activa decisiones del supervisor.
