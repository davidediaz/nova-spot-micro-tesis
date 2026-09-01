# Análisis de contactos medidos durante gateo

- Bolsa: `Experimentos/rosbag2/cierre_gateo_r1_20260901`.
- Ventana gateo--stand: 126.025836 s.
- Ciclos completos según `/nova/gait_phase`: 29.
- Índices de ciclo completos: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28].
- Estados comprimidos analizados: 807.
- Coincidencia simultánea filtrada de las cuatro patas: 13.455 %.

## Resultado por pata

| Pata | Coincidencia | Retardo despegue medio | Retardo aterrizaje medio |
|---|---:|---:|---:|
| fl | 60.813 % | 0.261454 s | 0.541590 s |
| fr | 60.771 % | 0.258814 s | 0.545568 s |
| rl | 87.568 % | sin pares | sin pares |
| rr | 87.572 % | sin pares | sin pares |

## Comparación crudo frente a filtrado

- Coincidencia simultánea cruda: 20.425 %.
- Coincidencia simultánea filtrada: 13.455 %.

| Pata | Coincidencia cruda | Coincidencia filtrada |
|---|---:|---:|
| fl | 62.458 % | 60.813 % |
| fr | 62.252 % | 60.771 % |
| rl | 89.299 % | 87.568 % |
| rr | 89.317 % | 87.572 % |

| Pata | Transición | Retardo crudo medio | Retardo filtrado medio |
|---|---|---:|---:|
| fl | liftoff | 0.138099 s | 0.261454 s |
| fl | landing | 0.508097 s | 0.541590 s |
| fr | liftoff | 0.135565 s | 0.258814 s |
| fr | landing | 0.512874 s | 0.545568 s |
| rl | liftoff | 0.139535 s | sin pares |
| rl | landing | -0.325480 s | sin pares |
| rr | liftoff | 0.140932 s | sin pares |
| rr | landing | -0.323290 s | sin pares |

Persistencia cruda exigida para declarar vuelo filtrado: 0.120 s.

| Pata | Episodios acotados | Duración media | Duración máxima | Episodios que superan el umbral |
|---|---:|---:|---:|---:|
| fl | 58 | 0.945032 s | 1.000776 s | 58 |
| fr | 59 | 0.937958 s | 1.002328 s | 58 |
| rl | 29 | 0.075217 s | 0.080615 s | 0 |
| rr | 29 | 0.075810 s | 0.088292 s | 0 |

Un retardo positivo indica que la transición medida ocurrió después de la prevista; uno negativo indica que ocurrió antes. Los pares se buscan dentro de ±1,8 s. Los porcentajes están ponderados por tiempo, no por número de mensajes.

El análisis es descriptivo y no activa decisiones del supervisor.
