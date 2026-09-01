# Análisis de contactos medidos durante gateo

- Bolsa: `Experimentos/rosbag2/velocidad_gateo_125_20260901`.
- Ventana gateo--stand: 93.135209 s.
- Ciclos completos según `/nova/gait_phase`: 26.
- Índices de ciclo completos: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25].
- Estados comprimidos analizados: 588.
- Coincidencia simultánea filtrada de las cuatro patas: 9.914 %.

## Resultado por pata

| Pata | Coincidencia | Retardo despegue medio | Retardo aterrizaje medio |
|---|---:|---:|---:|
| fl | 54.115 % | 0.264994 s | 1.111524 s |
| fr | 54.231 % | 0.266777 s | 1.172011 s |
| rl | 87.524 % | sin pares | sin pares |
| rr | 87.488 % | sin pares | sin pares |

## Comparación crudo frente a filtrado

- Coincidencia simultánea cruda: 17.211 %.
- Coincidencia simultánea filtrada: 9.914 %.

| Pata | Coincidencia cruda | Coincidencia filtrada |
|---|---:|---:|
| fl | 57.918 % | 54.115 % |
| fr | 58.153 % | 54.231 % |
| rl | 90.552 % | 87.524 % |
| rr | 90.593 % | 87.488 % |

| Pata | Transición | Retardo crudo medio | Retardo filtrado medio |
|---|---|---:|---:|
| fl | liftoff | 0.141595 s | 0.264994 s |
| fl | landing | 1.078928 s | 1.111524 s |
| fr | liftoff | 0.142274 s | 0.266777 s |
| fr | landing | 1.038812 s | 1.172011 s |
| rl | liftoff | 0.124103 s | sin pares |
| rl | landing | -0.203361 s | sin pares |
| rr | liftoff | 0.123035 s | sin pares |
| rr | landing | -0.201467 s | sin pares |

Persistencia cruda exigida para declarar vuelo filtrado: 0.120 s.

| Pata | Episodios acotados | Duración media | Duración máxima | Episodios que superan el umbral |
|---|---:|---:|---:|---:|
| fl | 36 | 1.199026 s | 1.648965 s | 35 |
| fr | 33 | 1.268247 s | 1.651538 s | 32 |
| rl | 27 | 0.104448 s | 0.120473 s | 2 |
| rr | 27 | 0.107077 s | 0.127362 s | 5 |

Un retardo positivo indica que la transición medida ocurrió después de la prevista; uno negativo indica que ocurrió antes. Los pares se buscan dentro de ±1,8 s. Los porcentajes están ponderados por tiempo, no por número de mensajes.

El análisis es descriptivo y no activa decisiones del supervisor.
