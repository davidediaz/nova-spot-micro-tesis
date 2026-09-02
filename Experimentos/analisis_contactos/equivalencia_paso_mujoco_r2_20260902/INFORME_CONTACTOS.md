# Análisis de contactos medidos durante marcha paso

- Bolsa: `Experimentos/rosbag2/equivalencia_paso_mujoco_r2_20260902`.
- Ventana paso--stand: 68.072372 s.
- Ciclos completos según `/nova/gait_phase`: 11.
- Índices de ciclo completos: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10].
- Estados comprimidos analizados: 180.
- Coincidencia simultánea filtrada de las cuatro patas: 0.000 %.

## Resultado por pata

| Pata | Coincidencia | Retardo despegue medio | Retardo aterrizaje medio |
|---|---:|---:|---:|
| fl | 74.605 % | sin pares | sin pares |
| fr | 74.626 % | sin pares | sin pares |
| rl | 76.171 % | sin pares | sin pares |
| rr | 74.598 % | sin pares | sin pares |

## Comparación crudo frente a filtrado

- Coincidencia simultánea cruda: 0.000 %.
- Coincidencia simultánea filtrada: 0.000 %.

| Pata | Coincidencia cruda | Coincidencia filtrada |
|---|---:|---:|
| fl | 74.105 % | 74.605 % |
| fr | 74.175 % | 74.626 % |
| rl | 76.171 % | 76.171 % |
| rr | 74.598 % | 74.598 % |

| Pata | Transición | Retardo crudo medio | Retardo filtrado medio |
|---|---|---:|---:|
| fl | liftoff | sin pares | sin pares |
| fl | landing | 0.565048 s | sin pares |
| fr | liftoff | sin pares | sin pares |
| fr | landing | 0.565554 s | sin pares |
| rl | liftoff | sin pares | sin pares |
| rl | landing | sin pares | sin pares |
| rr | liftoff | sin pares | sin pares |
| rr | landing | sin pares | sin pares |

Persistencia cruda exigida para declarar vuelo filtrado: 0.120 s.

| Pata | Episodios acotados | Duración media | Duración máxima | Episodios que superan el umbral |
|---|---:|---:|---:|---:|
| fl | 35 | 0.009729 s | 0.015210 s | 0 |
| fr | 31 | 0.009898 s | 0.016141 s | 0 |
| rl | 0 | sin episodios | sin episodios | 0 |
| rr | 0 | sin episodios | sin episodios | 0 |

Un retardo positivo indica que la transición medida ocurrió después de la prevista; uno negativo indica que ocurrió antes. Los pares se buscan dentro de ±1,8 s. Los porcentajes están ponderados por tiempo, no por número de mensajes.

El análisis es descriptivo y no activa decisiones del supervisor.
