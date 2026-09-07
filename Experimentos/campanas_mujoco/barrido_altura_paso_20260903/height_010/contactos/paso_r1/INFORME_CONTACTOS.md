# Análisis de contactos medidos durante marcha paso

- Bolsa: `Experimentos/campanas_mujoco/barrido_altura_paso_20260903/height_010/rosbag2/paso_r1`.
- Ventana paso--stand: 29.658021 s.
- Ciclos completos según `/nova/gait_phase`: 5.
- Índices de ciclo completos: [0, 1, 2, 3, 4].
- Estados comprimidos analizados: 166.
- Coincidencia simultánea filtrada de las cuatro patas: 18.088 %.

## Resultado por pata

| Pata | Coincidencia | Retardo despegue medio | Retardo aterrizaje medio |
|---|---:|---:|---:|
| fl | 79.530 % | 0.437185 s | -0.456386 s |
| fr | 81.208 % | 0.438590 s | -0.454823 s |
| rl | 75.701 % | sin pares | sin pares |
| rr | 75.739 % | sin pares | sin pares |

## Comparación crudo frente a filtrado

- Coincidencia simultánea cruda: 19.581 %.
- Coincidencia simultánea filtrada: 18.088 %.

| Pata | Coincidencia cruda | Coincidencia filtrada |
|---|---:|---:|
| fl | 80.043 % | 79.530 % |
| fr | 81.617 % | 81.208 % |
| rl | 75.701 % | 75.701 % |
| rr | 75.739 % | 75.739 % |

| Pata | Transición | Retardo crudo medio | Retardo filtrado medio |
|---|---|---:|---:|
| fl | liftoff | 0.404119 s | 0.437185 s |
| fl | landing | -0.119359 s | -0.456386 s |
| fr | liftoff | 0.407306 s | 0.438590 s |
| fr | landing | -0.466252 s | -0.454823 s |
| rl | liftoff | sin pares | sin pares |
| rl | landing | sin pares | sin pares |
| rr | liftoff | sin pares | sin pares |
| rr | landing | sin pares | sin pares |

Persistencia cruda exigida para declarar vuelo filtrado: 0.120 s.

| Pata | Episodios acotados | Duración media | Duración máxima | Episodios que superan el umbral |
|---|---:|---:|---:|---:|
| fl | 23 | 0.164029 s | 0.419075 s | 16 |
| fr | 18 | 0.204209 s | 0.568930 s | 13 |
| rl | 0 | sin episodios | sin episodios | 0 |
| rr | 0 | sin episodios | sin episodios | 0 |

Un retardo positivo indica que la transición medida ocurrió después de la prevista; uno negativo indica que ocurrió antes. Los pares se buscan dentro de ±1,8 s. Los porcentajes están ponderados por tiempo, no por número de mensajes.

El análisis es descriptivo y no activa decisiones del supervisor.
