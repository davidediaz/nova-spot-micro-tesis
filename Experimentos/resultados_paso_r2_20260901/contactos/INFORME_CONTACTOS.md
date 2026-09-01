# Análisis de contactos medidos durante marcha paso

- Bolsa: `Experimentos/rosbag2/cierre_paso_r2_20260901`.
- Ventana paso--stand: 131.922730 s.
- Ciclos completos según `/nova/gait_phase`: 22.
- Índices de ciclo completos: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21].
- Estados comprimidos analizados: 282.
- Coincidencia simultánea filtrada de las cuatro patas: 34.631 %.

## Resultado por pata

| Pata | Coincidencia | Retardo despegue medio | Retardo aterrizaje medio |
|---|---:|---:|---:|
| fl | 63.000 % | 0.456477 s | 1.638644 s |
| fr | 63.060 % | 0.457532 s | 1.641450 s |
| rl | 75.322 % | sin pares | sin pares |
| rr | 74.899 % | sin pares | sin pares |

## Comparación crudo frente a filtrado

- Coincidencia simultánea cruda: 38.879 %.
- Coincidencia simultánea filtrada: 34.631 %.

| Pata | Coincidencia cruda | Coincidencia filtrada |
|---|---:|---:|
| fl | 65.583 % | 63.000 % |
| fr | 65.647 % | 63.060 % |
| rl | 75.322 % | 75.322 % |
| rr | 74.899 % | 74.899 % |

| Pata | Transición | Retardo crudo medio | Retardo filtrado medio |
|---|---|---:|---:|
| fl | liftoff | 0.332618 s | 0.456477 s |
| fl | landing | 1.605101 s | 1.638644 s |
| fr | liftoff | 0.332382 s | 0.457532 s |
| fr | landing | 1.608103 s | 1.641450 s |
| rl | liftoff | sin pares | sin pares |
| rl | landing | sin pares | sin pares |
| rr | liftoff | sin pares | sin pares |
| rr | landing | sin pares | sin pares |

Persistencia cruda exigida para declarar vuelo filtrado: 0.120 s.

| Pata | Episodios acotados | Duración media | Duración máxima | Episodios que superan el umbral |
|---|---:|---:|---:|---:|
| fl | 24 | 2.662203 s | 2.807899 s | 24 |
| fr | 24 | 2.549353 s | 2.793685 s | 23 |
| rl | 0 | sin episodios | sin episodios | 0 |
| rr | 0 | sin episodios | sin episodios | 0 |

Un retardo positivo indica que la transición medida ocurrió después de la prevista; uno negativo indica que ocurrió antes. Los pares se buscan dentro de ±1,8 s. Los porcentajes están ponderados por tiempo, no por número de mensajes.

El análisis es descriptivo y no activa decisiones del supervisor.
