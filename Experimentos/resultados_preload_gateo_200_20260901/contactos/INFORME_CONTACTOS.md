# Análisis de contactos medidos durante gateo

- Bolsa: `Experimentos/rosbag2/preload_gateo_200_20260901`.
- Ventana gateo--stand: 79.149822 s.
- Ciclos completos según `/nova/gait_phase`: 18.
- Índices de ciclo completos: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17].
- Estados comprimidos analizados: 535.
- Coincidencia simultánea filtrada de las cuatro patas: 19.356 %.

## Resultado por pata

| Pata | Coincidencia | Retardo despegue medio | Retardo aterrizaje medio |
|---|---:|---:|---:|
| fl | 64.916 % | 0.194289 s | 0.521048 s |
| fr | 65.880 % | 0.195777 s | 0.530288 s |
| rl | 92.572 % | 0.252917 s | -0.073674 s |
| rr | 92.564 % | 0.253182 s | -0.073742 s |

## Comparación crudo frente a filtrado

- Coincidencia simultánea cruda: 28.184 %.
- Coincidencia simultánea filtrada: 19.356 %.

| Pata | Coincidencia cruda | Coincidencia filtrada |
|---|---:|---:|
| fl | 66.667 % | 64.916 % |
| fr | 67.395 % | 65.880 % |
| rl | 94.609 % | 92.572 % |
| rr | 94.602 % | 92.564 % |

| Pata | Transición | Retardo crudo medio | Retardo filtrado medio |
|---|---|---:|---:|
| fl | liftoff | 0.070413 s | 0.194289 s |
| fl | landing | 0.487775 s | 0.521048 s |
| fr | liftoff | 0.073058 s | 0.195777 s |
| fr | landing | 0.497190 s | 0.530288 s |
| rl | liftoff | 0.130748 s | 0.252917 s |
| rl | landing | -0.106282 s | -0.073674 s |
| rr | liftoff | 0.130704 s | 0.253182 s |
| rr | landing | -0.106611 s | -0.073742 s |

Persistencia cruda exigida para declarar vuelo filtrado: 0.120 s.

| Pata | Episodios acotados | Duración media | Duración máxima | Episodios que superan el umbral |
|---|---:|---:|---:|---:|
| fl | 37 | 0.892209 s | 0.996342 s | 37 |
| fr | 37 | 0.889182 s | 1.003939 s | 36 |
| rl | 18 | 0.302978 s | 0.311543 s | 18 |
| rr | 18 | 0.303423 s | 0.319684 s | 18 |

Un retardo positivo indica que la transición medida ocurrió después de la prevista; uno negativo indica que ocurrió antes. Los pares se buscan dentro de ±1,8 s. Los porcentajes están ponderados por tiempo, no por número de mensajes.

El análisis es descriptivo y no activa decisiones del supervisor.
