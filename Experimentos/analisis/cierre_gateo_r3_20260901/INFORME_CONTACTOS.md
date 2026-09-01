# Análisis de contactos medidos durante gateo

- Bolsa: `Experimentos/rosbag2/cierre_gateo_r3_20260901`.
- Ventana gateo--stand: 220.731955 s.
- Ciclos completos según `/nova/gait_phase`: 50.
- Índices de ciclo completos: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49].
- Estados comprimidos analizados: 1419.
- Coincidencia simultánea filtrada de las cuatro patas: 13.099 %.

## Resultado por pata

| Pata | Coincidencia | Retardo despegue medio | Retardo aterrizaje medio |
|---|---:|---:|---:|
| fl | 60.642 % | 0.260769 s | 0.540675 s |
| fr | 60.700 % | 0.258920 s | 0.545994 s |
| rl | 87.267 % | sin pares | sin pares |
| rr | 87.522 % | sin pares | sin pares |

## Comparación crudo frente a filtrado

- Coincidencia simultánea cruda: 20.046 %.
- Coincidencia simultánea filtrada: 13.099 %.

| Pata | Coincidencia cruda | Coincidencia filtrada |
|---|---:|---:|
| fl | 62.137 % | 60.642 % |
| fr | 62.198 % | 60.700 % |
| rl | 89.004 % | 87.267 % |
| rr | 89.269 % | 87.522 % |

| Pata | Transición | Retardo crudo medio | Retardo filtrado medio |
|---|---|---:|---:|
| fl | liftoff | 0.136866 s | 0.260769 s |
| fl | landing | 0.507559 s | 0.540675 s |
| fr | liftoff | 0.135306 s | 0.258920 s |
| fr | landing | 0.513122 s | 0.545994 s |
| rl | liftoff | 0.139569 s | sin pares |
| rl | landing | -0.325444 s | sin pares |
| rr | liftoff | 0.139351 s | sin pares |
| rr | landing | -0.325064 s | sin pares |

Persistencia cruda exigida para declarar vuelo filtrado: 0.120 s.

| Pata | Episodios acotados | Duración media | Duración máxima | Episodios que superan el umbral |
|---|---:|---:|---:|---:|
| fl | 103 | 0.941724 s | 1.001417 s | 103 |
| fr | 103 | 0.943415 s | 1.001816 s | 103 |
| rl | 51 | 0.075179 s | 0.096427 s | 0 |
| rr | 51 | 0.075609 s | 0.087604 s | 0 |

Un retardo positivo indica que la transición medida ocurrió después de la prevista; uno negativo indica que ocurrió antes. Los pares se buscan dentro de ±1,8 s. Los porcentajes están ponderados por tiempo, no por número de mensajes.

El análisis es descriptivo y no activa decisiones del supervisor.
