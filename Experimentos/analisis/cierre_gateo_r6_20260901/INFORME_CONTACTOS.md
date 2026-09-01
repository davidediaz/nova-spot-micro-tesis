# Análisis de contactos medidos durante gateo

- Bolsa: `Experimentos/rosbag2/cierre_gateo_r6_20260901`.
- Ventana gateo--stand: 158.385185 s.
- Ciclos completos según `/nova/gait_phase`: 36.
- Índices de ciclo completos: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35].
- Estados comprimidos analizados: 1010.
- Coincidencia simultánea filtrada de las cuatro patas: 13.163 %.

## Resultado por pata

| Pata | Coincidencia | Retardo despegue medio | Retardo aterrizaje medio |
|---|---:|---:|---:|
| fl | 60.100 % | 0.262171 s | 0.540530 s |
| fr | 61.262 % | 0.251465 s | 0.546606 s |
| rl | 87.734 % | sin pares | sin pares |
| rr | 87.389 % | sin pares | sin pares |

## Comparación crudo frente a filtrado

- Coincidencia simultánea cruda: 20.054 %.
- Coincidencia simultánea filtrada: 13.163 %.

| Pata | Coincidencia cruda | Coincidencia filtrada |
|---|---:|---:|
| fl | 61.678 % | 60.100 % |
| fr | 62.704 % | 61.262 % |
| rl | 89.441 % | 87.734 % |
| rr | 89.157 % | 87.389 % |

| Pata | Transición | Retardo crudo medio | Retardo filtrado medio |
|---|---|---:|---:|
| fl | liftoff | 0.137726 s | 0.262171 s |
| fl | landing | 0.507396 s | 0.540530 s |
| fr | liftoff | 0.130827 s | 0.251465 s |
| fr | landing | 0.513930 s | 0.546606 s |
| rl | liftoff | 0.140375 s | sin pares |
| rl | landing | -0.324158 s | sin pares |
| rr | liftoff | 0.139872 s | sin pares |
| rr | landing | -0.324268 s | sin pares |

Persistencia cruda exigida para declarar vuelo filtrado: 0.120 s.

| Pata | Episodios acotados | Duración media | Duración máxima | Episodios que superan el umbral |
|---|---:|---:|---:|---:|
| fl | 75 | 0.939878 s | 1.183664 s | 75 |
| fr | 73 | 0.942964 s | 0.998425 s | 73 |
| rl | 36 | 0.075128 s | 0.096626 s | 0 |
| rr | 37 | 0.075684 s | 0.095777 s | 0 |

Un retardo positivo indica que la transición medida ocurrió después de la prevista; uno negativo indica que ocurrió antes. Los pares se buscan dentro de ±1,8 s. Los porcentajes están ponderados por tiempo, no por número de mensajes.

El análisis es descriptivo y no activa decisiones del supervisor.
