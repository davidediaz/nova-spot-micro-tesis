# Análisis de contactos medidos durante marcha paso

- Bolsa: `Experimentos/campanas_mujoco/barrido_altura_paso_20260903/height_012/rosbag2/paso_r1`.
- Ventana paso--stand: 29.439824 s.
- Ciclos completos según `/nova/gait_phase`: 5.
- Índices de ciclo completos: [0, 1, 2, 3, 4].
- Estados comprimidos analizados: 104.
- Coincidencia simultánea filtrada de las cuatro patas: 24.501 %.

## Resultado por pata

| Pata | Coincidencia | Retardo despegue medio | Retardo aterrizaje medio |
|---|---:|---:|---:|
| fl | 75.121 % | 0.429056 s | -0.312320 s |
| fr | 76.619 % | 0.422177 s | -0.312278 s |
| rl | 75.550 % | sin pares | sin pares |
| rr | 75.488 % | sin pares | sin pares |

## Comparación crudo frente a filtrado

- Coincidencia simultánea cruda: 25.305 %.
- Coincidencia simultánea filtrada: 24.501 %.

| Pata | Coincidencia cruda | Coincidencia filtrada |
|---|---:|---:|
| fl | 75.175 % | 75.121 % |
| fr | 76.589 % | 76.619 % |
| rl | 75.550 % | 75.550 % |
| rr | 75.488 % | 75.488 % |

| Pata | Transición | Retardo crudo medio | Retardo filtrado medio |
|---|---|---:|---:|
| fl | liftoff | 0.398545 s | 0.429056 s |
| fl | landing | -0.212452 s | -0.312320 s |
| fr | liftoff | 0.390718 s | 0.422177 s |
| fr | landing | -0.322055 s | -0.312278 s |
| rl | liftoff | sin pares | sin pares |
| rl | landing | sin pares | sin pares |
| rr | liftoff | sin pares | sin pares |
| rr | landing | sin pares | sin pares |

Persistencia cruda exigida para declarar vuelo filtrado: 0.120 s.

| Pata | Episodios acotados | Duración media | Duración máxima | Episodios que superan el umbral |
|---|---:|---:|---:|---:|
| fl | 11 | 0.625722 s | 0.726695 s | 10 |
| fr | 10 | 0.695319 s | 0.726923 s | 10 |
| rl | 0 | sin episodios | sin episodios | 0 |
| rr | 0 | sin episodios | sin episodios | 0 |

Un retardo positivo indica que la transición medida ocurrió después de la prevista; uno negativo indica que ocurrió antes. Los pares se buscan dentro de ±1,8 s. Los porcentajes están ponderados por tiempo, no por número de mensajes.

El análisis es descriptivo y no activa decisiones del supervisor.
