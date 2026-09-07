# Análisis de contactos medidos durante marcha paso

- Bolsa: `Experimentos/campanas_mujoco/paso_ajustado_5x20_20260903/rosbag2/paso_r4`.
- Ventana paso--stand: 122.410164 s.
- Ciclos completos según `/nova/gait_phase`: 21.
- Índices de ciclo completos: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20].
- Estados comprimidos analizados: 475.
- Coincidencia simultánea filtrada de las cuatro patas: 36.711 %.

## Resultado por pata

| Pata | Coincidencia | Retardo despegue medio | Retardo aterrizaje medio |
|---|---:|---:|---:|
| fl | 75.102 % | 0.252323 s | -0.141903 s |
| fr | 75.423 % | 0.251152 s | -0.143854 s |
| rl | 75.292 % | sin pares | sin pares |
| rr | 75.283 % | sin pares | sin pares |

## Comparación crudo frente a filtrado

- Coincidencia simultánea cruda: 37.483 %.
- Coincidencia simultánea filtrada: 36.711 %.

| Pata | Coincidencia cruda | Coincidencia filtrada |
|---|---:|---:|
| fl | 75.131 % | 75.102 % |
| fr | 75.374 % | 75.423 % |
| rl | 75.342 % | 75.292 % |
| rr | 75.332 % | 75.283 % |

| Pata | Transición | Retardo crudo medio | Retardo filtrado medio |
|---|---|---:|---:|
| fl | liftoff | 0.219146 s | 0.252323 s |
| fl | landing | -0.152192 s | -0.141903 s |
| fr | liftoff | 0.220627 s | 0.251152 s |
| fr | landing | -0.153853 s | -0.143854 s |
| rl | liftoff | 1.114824 s | sin pares |
| rl | landing | -0.188649 s | sin pares |
| rr | liftoff | 1.088018 s | sin pares |
| rr | landing | -0.174808 s | sin pares |

Persistencia cruda exigida para declarar vuelo filtrado: 0.120 s.

| Pata | Episodios acotados | Duración media | Duración máxima | Episodios que superan el umbral |
|---|---:|---:|---:|---:|
| fl | 43 | 1.064324 s | 1.078530 s | 43 |
| fr | 42 | 1.063202 s | 1.070995 s | 42 |
| rl | 18 | 0.003390 s | 0.009598 s | 0 |
| rr | 17 | 0.003532 s | 0.005697 s | 0 |

Un retardo positivo indica que la transición medida ocurrió después de la prevista; uno negativo indica que ocurrió antes. Los pares se buscan dentro de ±1,8 s. Los porcentajes están ponderados por tiempo, no por número de mensajes.

El análisis es descriptivo y no activa decisiones del supervisor.
