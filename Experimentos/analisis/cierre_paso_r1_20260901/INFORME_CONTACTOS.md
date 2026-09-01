# Análisis de contactos medidos durante marcha paso

- Bolsa: `Experimentos/rosbag2/cierre_paso_r1_20260901`.
- Ventana paso--stand: 122.092760 s.
- Ciclos completos según `/nova/gait_phase`: 21.
- Índices de ciclo completos: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20].
- Estados comprimidos analizados: 263.
- Coincidencia simultánea filtrada de las cuatro patas: 34.787 %.

## Resultado por pata

| Pata | Coincidencia | Retardo despegue medio | Retardo aterrizaje medio |
|---|---:|---:|---:|
| fl | 63.204 % | 0.456674 s | 1.630902 s |
| fr | 63.027 % | 0.454396 s | 1.636729 s |
| rl | 75.233 % | sin pares | sin pares |
| rr | 75.226 % | sin pares | sin pares |

## Comparación crudo frente a filtrado

- Coincidencia simultánea cruda: 39.067 %.
- Coincidencia simultánea filtrada: 34.787 %.

| Pata | Coincidencia cruda | Coincidencia filtrada |
|---|---:|---:|
| fl | 65.854 % | 63.204 % |
| fr | 65.562 % | 63.027 % |
| rl | 75.233 % | 75.233 % |
| rr | 75.226 % | 75.226 % |

| Pata | Transición | Retardo crudo medio | Retardo filtrado medio |
|---|---|---:|---:|
| fl | liftoff | 0.331155 s | 0.456674 s |
| fl | landing | 1.598118 s | 1.630902 s |
| fr | liftoff | 0.331107 s | 0.454396 s |
| fr | landing | 1.602801 s | 1.636729 s |
| rl | liftoff | sin pares | sin pares |
| rl | landing | sin pares | sin pares |
| rr | liftoff | sin pares | sin pares |
| rr | landing | sin pares | sin pares |

Persistencia cruda exigida para declarar vuelo filtrado: 0.120 s.

| Pata | Episodios acotados | Duración media | Duración máxima | Episodios que superan el umbral |
|---|---:|---:|---:|---:|
| fl | 22 | 2.653545 s | 2.794540 s | 22 |
| fr | 23 | 2.537896 s | 2.795060 s | 22 |
| rl | 0 | sin episodios | sin episodios | 0 |
| rr | 0 | sin episodios | sin episodios | 0 |

Un retardo positivo indica que la transición medida ocurrió después de la prevista; uno negativo indica que ocurrió antes. Los pares se buscan dentro de ±1,8 s. Los porcentajes están ponderados por tiempo, no por número de mensajes.

El análisis es descriptivo y no activa decisiones del supervisor.
