# Análisis de contactos medidos durante gateo

- Bolsa: `Experimentos/rosbag2/preload_gateo_150_20260901`.
- Ventana gateo--stand: 79.161570 s.
- Ciclos completos según `/nova/gait_phase`: 18.
- Índices de ciclo completos: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17].
- Estados comprimidos analizados: 533.
- Coincidencia simultánea filtrada de las cuatro patas: 14.527 %.

## Resultado por pata

| Pata | Coincidencia | Retardo despegue medio | Retardo aterrizaje medio |
|---|---:|---:|---:|
| fl | 61.277 % | 0.258864 s | 0.514643 s |
| fr | 61.817 % | 0.256964 s | 0.526693 s |
| rl | 89.002 % | 0.260228 s | -0.223351 s |
| rr | 88.817 % | 0.258439 s | -0.226835 s |

## Comparación crudo frente a filtrado

- Coincidencia simultánea cruda: 21.858 %.
- Coincidencia simultánea filtrada: 14.527 %.

| Pata | Coincidencia cruda | Coincidencia filtrada |
|---|---:|---:|
| fl | 62.953 % | 61.277 % |
| fr | 63.343 % | 61.817 % |
| rl | 91.064 % | 89.002 % |
| rr | 90.950 % | 88.817 % |

| Pata | Transición | Retardo crudo medio | Retardo filtrado medio |
|---|---|---:|---:|
| fl | liftoff | 0.135305 s | 0.258864 s |
| fl | landing | 0.481962 s | 0.514643 s |
| fr | liftoff | 0.133345 s | 0.256964 s |
| fr | landing | 0.492795 s | 0.526693 s |
| rl | liftoff | 0.136575 s | 0.260228 s |
| rl | landing | -0.256357 s | -0.223351 s |
| rr | liftoff | 0.136740 s | 0.258439 s |
| rr | landing | -0.261181 s | -0.226835 s |

Persistencia cruda exigida para declarar vuelo filtrado: 0.120 s.

| Pata | Episodios acotados | Duración media | Duración máxima | Episodios que superan el umbral |
|---|---:|---:|---:|---:|
| fl | 36 | 0.931596 s | 0.995180 s | 36 |
| fr | 36 | 0.942141 s | 0.993907 s | 36 |
| rl | 18 | 0.147173 s | 0.159323 s | 18 |
| rr | 18 | 0.142499 s | 0.157044 s | 18 |

Un retardo positivo indica que la transición medida ocurrió después de la prevista; uno negativo indica que ocurrió antes. Los pares se buscan dentro de ±1,8 s. Los porcentajes están ponderados por tiempo, no por número de mensajes.

El análisis es descriptivo y no activa decisiones del supervisor.
