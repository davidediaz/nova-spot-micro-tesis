# Análisis de contactos medidos durante marcha paso

- Bolsa: `Experimentos/campanas_mujoco/barrido_friccion_paso_r2_20260903/friction_09/rosbag2/paso_r1`.
- Ventana paso--stand: 29.769793 s.
- Ciclos completos según `/nova/gait_phase`: 5.
- Índices de ciclo completos: [0, 1, 2, 3, 4].
- Estados comprimidos analizados: 107.
- Coincidencia simultánea filtrada de las cuatro patas: 25.289 %.

## Resultado por pata

| Pata | Coincidencia | Retardo despegue medio | Retardo aterrizaje medio |
|---|---:|---:|---:|
| fl | 75.429 % | 0.426720 s | -0.311180 s |
| fr | 76.644 % | 0.428488 s | -0.318239 s |
| rl | 75.879 % | sin pares | sin pares |
| rr | 75.792 % | sin pares | sin pares |

## Comparación crudo frente a filtrado

- Coincidencia simultánea cruda: 26.202 %.
- Coincidencia simultánea filtrada: 25.289 %.

| Pata | Coincidencia cruda | Coincidencia filtrada |
|---|---:|---:|
| fl | 75.581 % | 75.429 % |
| fr | 76.703 % | 76.644 % |
| rl | 75.879 % | 75.879 % |
| rr | 75.792 % | 75.792 % |

| Pata | Transición | Retardo crudo medio | Retardo filtrado medio |
|---|---|---:|---:|
| fl | liftoff | 0.364035 s | 0.426720 s |
| fl | landing | -0.211662 s | -0.311180 s |
| fr | liftoff | 0.361150 s | 0.428488 s |
| fr | landing | -0.326035 s | -0.318239 s |
| rl | liftoff | sin pares | sin pares |
| rl | landing | sin pares | sin pares |
| rr | liftoff | sin pares | sin pares |
| rr | landing | sin pares | sin pares |

Persistencia cruda exigida para declarar vuelo filtrado: 0.120 s.

| Pata | Episodios acotados | Duración media | Duración máxima | Episodios que superan el umbral |
|---|---:|---:|---:|---:|
| fl | 12 | 0.575544 s | 0.727497 s | 10 |
| fr | 11 | 0.632589 s | 0.731653 s | 10 |
| rl | 0 | sin episodios | sin episodios | 0 |
| rr | 0 | sin episodios | sin episodios | 0 |

Un retardo positivo indica que la transición medida ocurrió después de la prevista; uno negativo indica que ocurrió antes. Los pares se buscan dentro de ±1,8 s. Los porcentajes están ponderados por tiempo, no por número de mensajes.

El análisis es descriptivo y no activa decisiones del supervisor.
