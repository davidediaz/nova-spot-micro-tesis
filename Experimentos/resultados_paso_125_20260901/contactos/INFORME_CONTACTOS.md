# Análisis de contactos medidos durante marcha paso

- Bolsa: `Experimentos/rosbag2/velocidad_paso_125_20260901`.
- Ventana paso--stand: 119.195430 s.
- Ciclos completos según `/nova/gait_phase`: 25.
- Índices de ciclo completos: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24].
- Estados comprimidos analizados: 314.
- Coincidencia simultánea filtrada de las cuatro patas: 31.999 %.

## Resultado por pata

| Pata | Coincidencia | Retardo despegue medio | Retardo aterrizaje medio |
|---|---:|---:|---:|
| fl | 61.044 % | 0.427633 s | 1.342198 s |
| fr | 61.064 % | 0.427134 s | 1.391182 s |
| rl | 75.397 % | sin pares | sin pares |
| rr | 74.889 % | sin pares | sin pares |

## Comparación crudo frente a filtrado

- Coincidencia simultánea cruda: 37.292 %.
- Coincidencia simultánea filtrada: 31.999 %.

| Pata | Coincidencia cruda | Coincidencia filtrada |
|---|---:|---:|
| fl | 64.269 % | 61.044 % |
| fr | 64.403 % | 61.064 % |
| rl | 75.397 % | 75.397 % |
| rr | 74.889 % | 74.889 % |

| Pata | Transición | Retardo crudo medio | Retardo filtrado medio |
|---|---|---:|---:|
| fl | liftoff | 0.304286 s | 0.427633 s |
| fl | landing | 1.309564 s | 1.342198 s |
| fr | liftoff | 0.303090 s | 0.427134 s |
| fr | landing | 1.358347 s | 1.391182 s |
| rl | liftoff | sin pares | sin pares |
| rl | landing | sin pares | sin pares |
| rr | liftoff | sin pares | sin pares |
| rr | landing | sin pares | sin pares |

Persistencia cruda exigida para declarar vuelo filtrado: 0.120 s.

| Pata | Episodios acotados | Duración media | Duración máxima | Episodios que superan el umbral |
|---|---:|---:|---:|---:|
| fl | 27 | 2.123955 s | 2.224525 s | 27 |
| fr | 26 | 2.125184 s | 2.245219 s | 25 |
| rl | 0 | sin episodios | sin episodios | 0 |
| rr | 0 | sin episodios | sin episodios | 0 |

Un retardo positivo indica que la transición medida ocurrió después de la prevista; uno negativo indica que ocurrió antes. Los pares se buscan dentro de ±1,8 s. Los porcentajes están ponderados por tiempo, no por número de mensajes.

El análisis es descriptivo y no activa decisiones del supervisor.
