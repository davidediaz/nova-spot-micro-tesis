# Análisis de contactos medidos durante gateo

- Bolsa: `Experimentos/rosbag2/cierre_gateo_r7_20260901`.
- Ventana gateo--stand: 125.568453 s.
- Ciclos completos según `/nova/gait_phase`: 29.
- Índices de ciclo completos: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28].
- Estados comprimidos analizados: 800.
- Coincidencia simultánea filtrada de las cuatro patas: 13.260 %.

## Resultado por pata

| Pata | Coincidencia | Retardo despegue medio | Retardo aterrizaje medio |
|---|---:|---:|---:|
| fl | 60.714 % | 0.258800 s | 0.536980 s |
| fr | 60.860 % | 0.257815 s | 0.544703 s |
| rl | 87.519 % | sin pares | sin pares |
| rr | 87.534 % | sin pares | sin pares |

## Comparación crudo frente a filtrado

- Coincidencia simultánea cruda: 20.220 %.
- Coincidencia simultánea filtrada: 13.260 %.

| Pata | Coincidencia cruda | Coincidencia filtrada |
|---|---:|---:|
| fl | 62.300 % | 60.714 % |
| fr | 62.281 % | 60.860 % |
| rl | 89.272 % | 87.519 % |
| rr | 89.236 % | 87.534 % |

| Pata | Transición | Retardo crudo medio | Retardo filtrado medio |
|---|---|---:|---:|
| fl | liftoff | 0.134741 s | 0.258800 s |
| fl | landing | 0.504083 s | 0.536980 s |
| fr | liftoff | 0.134566 s | 0.257815 s |
| fr | landing | 0.511518 s | 0.544703 s |
| rl | liftoff | 0.140850 s | sin pares |
| rl | landing | -0.323649 s | sin pares |
| rr | liftoff | 0.140154 s | sin pares |
| rr | landing | -0.325897 s | sin pares |

Persistencia cruda exigida para declarar vuelo filtrado: 0.120 s.

| Pata | Episodios acotados | Duración media | Duración máxima | Episodios que superan el umbral |
|---|---:|---:|---:|---:|
| fl | 59 | 0.935287 s | 0.995472 s | 59 |
| fr | 58 | 0.937072 s | 0.998361 s | 58 |
| rl | 29 | 0.075887 s | 0.104992 s | 0 |
| rr | 29 | 0.073691 s | 0.086108 s | 0 |

Un retardo positivo indica que la transición medida ocurrió después de la prevista; uno negativo indica que ocurrió antes. Los pares se buscan dentro de ±1,8 s. Los porcentajes están ponderados por tiempo, no por número de mensajes.

El análisis es descriptivo y no activa decisiones del supervisor.
