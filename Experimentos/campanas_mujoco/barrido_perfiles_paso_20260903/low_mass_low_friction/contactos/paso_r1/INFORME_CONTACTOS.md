# Análisis de contactos medidos durante marcha paso

- Bolsa: `Experimentos/campanas_mujoco/barrido_perfiles_paso_20260903/low_mass_low_friction/rosbag2/paso_r1`.
- Ventana paso--stand: 30.080948 s.
- Ciclos completos según `/nova/gait_phase`: 5.
- Índices de ciclo completos: [0, 1, 2, 3, 4].
- Estados comprimidos analizados: 410.
- Coincidencia simultánea filtrada de las cuatro patas: 0.000 %.

## Resultado por pata

| Pata | Coincidencia | Retardo despegue medio | Retardo aterrizaje medio |
|---|---:|---:|---:|
| fl | 35.092 % | -0.991174 s | 0.274602 s |
| fr | 36.326 % | -0.990771 s | 0.275547 s |
| rl | 76.056 % | sin pares | sin pares |
| rr | 76.063 % | sin pares | sin pares |

## Comparación crudo frente a filtrado

- Coincidencia simultánea cruda: 0.000 %.
- Coincidencia simultánea filtrada: 0.000 %.

| Pata | Coincidencia cruda | Coincidencia filtrada |
|---|---:|---:|
| fl | 33.625 % | 35.092 % |
| fr | 34.792 % | 36.326 % |
| rl | 76.028 % | 76.056 % |
| rr | 76.002 % | 76.063 % |

| Pata | Transición | Retardo crudo medio | Retardo filtrado medio |
|---|---|---:|---:|
| fl | liftoff | -0.112428 s | -0.991174 s |
| fl | landing | 0.011599 s | 0.274602 s |
| fr | liftoff | -0.006625 s | -0.990771 s |
| fr | landing | 0.011883 s | 0.275547 s |
| rl | liftoff | -0.994549 s | sin pares |
| rl | landing | -1.220264 s | sin pares |
| rr | liftoff | -0.695684 s | sin pares |
| rr | landing | -0.325987 s | sin pares |

Persistencia cruda exigida para declarar vuelo filtrado: 0.120 s.

| Pata | Episodios acotados | Duración media | Duración máxima | Episodios que superan el umbral |
|---|---:|---:|---:|---:|
| fl | 82 | 0.142978 s | 1.684448 s | 15 |
| fr | 82 | 0.153925 s | 1.681559 s | 16 |
| rl | 6 | 0.004394 s | 0.006708 s | 0 |
| rr | 8 | 0.005658 s | 0.012985 s | 0 |

Un retardo positivo indica que la transición medida ocurrió después de la prevista; uno negativo indica que ocurrió antes. Los pares se buscan dentro de ±1,8 s. Los porcentajes están ponderados por tiempo, no por número de mensajes.

El análisis es descriptivo y no activa decisiones del supervisor.
