# Análisis de contactos medidos durante marcha paso

- Bolsa: `Experimentos/campanas_mujoco/barrido_altura_paso_20260903/height_016/rosbag2/paso_r1`.
- Ventana paso--stand: 29.469713 s.
- Ciclos completos según `/nova/gait_phase`: 5.
- Índices de ciclo completos: [0, 1, 2, 3, 4].
- Estados comprimidos analizados: 198.
- Coincidencia simultánea filtrada de las cuatro patas: 29.619 %.

## Resultado por pata

| Pata | Coincidencia | Retardo despegue medio | Retardo aterrizaje medio |
|---|---:|---:|---:|
| fl | 75.976 % | 0.255775 s | -0.277547 s |
| fr | 77.309 % | 0.250768 s | -0.278978 s |
| rl | 75.617 % | sin pares | sin pares |
| rr | 75.540 % | sin pares | sin pares |

## Comparación crudo frente a filtrado

- Coincidencia simultánea cruda: 31.376 %.
- Coincidencia simultánea filtrada: 29.619 %.

| Pata | Coincidencia cruda | Coincidencia filtrada |
|---|---:|---:|
| fl | 76.307 % | 75.976 % |
| fr | 77.301 % | 77.309 % |
| rl | 75.617 % | 75.617 % |
| rr | 75.540 % | 75.540 % |

| Pata | Transición | Retardo crudo medio | Retardo filtrado medio |
|---|---|---:|---:|
| fl | liftoff | 0.223612 s | 0.255775 s |
| fl | landing | 0.231140 s | -0.277547 s |
| fr | liftoff | 0.221990 s | 0.250768 s |
| fr | landing | 0.153321 s | -0.278978 s |
| rl | liftoff | sin pares | sin pares |
| rl | landing | sin pares | sin pares |
| rr | liftoff | sin pares | sin pares |
| rr | landing | sin pares | sin pares |

Persistencia cruda exigida para declarar vuelo filtrado: 0.120 s.

| Pata | Episodios acotados | Duración media | Duración máxima | Episodios que superan el umbral |
|---|---:|---:|---:|---:|
| fl | 29 | 0.292121 s | 0.787451 s | 10 |
| fr | 29 | 0.287551 s | 0.781398 s | 11 |
| rl | 0 | sin episodios | sin episodios | 0 |
| rr | 0 | sin episodios | sin episodios | 0 |

Un retardo positivo indica que la transición medida ocurrió después de la prevista; uno negativo indica que ocurrió antes. Los pares se buscan dentro de ±1,8 s. Los porcentajes están ponderados por tiempo, no por número de mensajes.

El análisis es descriptivo y no activa decisiones del supervisor.
