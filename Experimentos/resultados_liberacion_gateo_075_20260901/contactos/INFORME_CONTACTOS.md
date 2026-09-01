# Análisis de contactos medidos durante gateo

- Bolsa: `Experimentos/rosbag2/liberacion_gateo_075_20260901`.
- Ventana gateo--stand: 79.199090 s.
- Ciclos completos según `/nova/gait_phase`: 18.
- Índices de ciclo completos: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17].
- Estados comprimidos analizados: 508.
- Coincidencia simultánea filtrada de las cuatro patas: 13.404 %.

## Resultado por pata

| Pata | Coincidencia | Retardo despegue medio | Retardo aterrizaje medio |
|---|---:|---:|---:|
| fl | 60.190 % | 0.261490 s | 0.535760 s |
| fr | 61.179 % | 0.260213 s | 0.547151 s |
| rl | 87.724 % | sin pares | sin pares |
| rr | 87.721 % | sin pares | sin pares |

## Comparación crudo frente a filtrado

- Coincidencia simultánea cruda: 20.321 %.
- Coincidencia simultánea filtrada: 13.404 %.

| Pata | Coincidencia cruda | Coincidencia filtrada |
|---|---:|---:|
| fl | 61.929 % | 60.190 % |
| fr | 62.604 % | 61.179 % |
| rl | 89.622 % | 87.724 % |
| rr | 89.642 % | 87.721 % |

| Pata | Transición | Retardo crudo medio | Retardo filtrado medio |
|---|---|---:|---:|
| fl | liftoff | 0.137657 s | 0.261490 s |
| fl | landing | 0.502986 s | 0.535760 s |
| fr | liftoff | 0.136900 s | 0.260213 s |
| fr | landing | 0.513440 s | 0.547151 s |
| rl | liftoff | 0.139968 s | sin pares |
| rl | landing | -0.316626 s | sin pares |
| rr | liftoff | 0.141187 s | sin pares |
| rr | landing | -0.314529 s | sin pares |

Persistencia cruda exigida para declarar vuelo filtrado: 0.120 s.

| Pata | Episodios acotados | Duración media | Duración máxima | Episodios que superan el umbral |
|---|---:|---:|---:|---:|
| fl | 38 | 0.925804 s | 1.003715 s | 38 |
| fr | 37 | 0.929691 s | 1.000120 s | 37 |
| rl | 18 | 0.083508 s | 0.090262 s | 0 |
| rr | 18 | 0.084515 s | 0.101201 s | 0 |

Un retardo positivo indica que la transición medida ocurrió después de la prevista; uno negativo indica que ocurrió antes. Los pares se buscan dentro de ±1,8 s. Los porcentajes están ponderados por tiempo, no por número de mensajes.

El análisis es descriptivo y no activa decisiones del supervisor.
