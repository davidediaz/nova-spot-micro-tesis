# Análisis de contactos medidos durante gateo

- Bolsa: `Experimentos/rosbag2/velocidad_gateo_200_20260901`.
- Ventana gateo--stand: 73.480599 s.
- Ciclos completos según `/nova/gait_phase`: 34.
- Índices de ciclo completos: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33].
- Estados comprimidos analizados: 816.
- Coincidencia simultánea filtrada de las cuatro patas: 1.097 %.

## Resultado por pata

| Pata | Coincidencia | Retardo despegue medio | Retardo aterrizaje medio |
|---|---:|---:|---:|
| fl | 46.994 % | 0.253732 s | 0.884925 s |
| fr | 46.935 % | 0.267560 s | 0.902362 s |
| rl | 87.535 % | 0.223774 s | 0.045616 s |
| rr | 87.678 % | 0.222932 s | 0.043547 s |

## Comparación crudo frente a filtrado

- Coincidencia simultánea cruda: 10.916 %.
- Coincidencia simultánea filtrada: 1.097 %.

| Pata | Coincidencia cruda | Coincidencia filtrada |
|---|---:|---:|
| fl | 53.256 % | 46.994 % |
| fr | 53.390 % | 46.935 % |
| rl | 94.764 % | 87.535 % |
| rr | 94.797 % | 87.678 % |

| Pata | Transición | Retardo crudo medio | Retardo filtrado medio |
|---|---|---:|---:|
| fl | liftoff | 0.158895 s | 0.253732 s |
| fl | landing | 0.851872 s | 0.884925 s |
| fr | liftoff | 0.144458 s | 0.267560 s |
| fr | landing | 0.869084 s | 0.902362 s |
| rl | liftoff | 0.100759 s | 0.223774 s |
| rl | landing | 0.012319 s | 0.045616 s |
| rr | liftoff | 0.101238 s | 0.222932 s |
| rr | landing | 0.010864 s | 0.043547 s |

Persistencia cruda exigida para declarar vuelo filtrado: 0.120 s.

| Pata | Episodios acotados | Duración media | Duración máxima | Episodios que superan el umbral |
|---|---:|---:|---:|---:|
| fl | 35 | 0.963298 s | 0.997331 s | 35 |
| fr | 33 | 0.984182 s | 0.996821 s | 33 |
| rl | 34 | 0.171643 s | 0.183456 s | 34 |
| rr | 35 | 0.164624 s | 0.181896 s | 33 |

Un retardo positivo indica que la transición medida ocurrió después de la prevista; uno negativo indica que ocurrió antes. Los pares se buscan dentro de ±1,8 s. Los porcentajes están ponderados por tiempo, no por número de mensajes.

El análisis es descriptivo y no activa decisiones del supervisor.
