# Análisis de contactos medidos durante gateo

- Bolsa: `Experimentos/campanas_mujoco/gateo_nominal_5x20_20260903/rosbag2/gateo_r5`.
- Ventana gateo--stand: 92.441499 s.
- Ciclos completos según `/nova/gait_phase`: 21.
- Índices de ciclo completos: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20].
- Estados comprimidos analizados: 442.
- Coincidencia simultánea filtrada de las cuatro patas: 61.942 %.

## Resultado por pata

| Pata | Coincidencia | Retardo despegue medio | Retardo aterrizaje medio |
|---|---:|---:|---:|
| fl | 83.705 % | 0.118997 s | 0.077675 s |
| fr | 83.948 % | 0.121858 s | 0.080734 s |
| rl | 87.703 % | sin pares | sin pares |
| rr | 87.440 % | sin pares | sin pares |

## Comparación crudo frente a filtrado

- Coincidencia simultánea cruda: 64.265 %.
- Coincidencia simultánea filtrada: 61.942 %.

| Pata | Coincidencia cruda | Coincidencia filtrada |
|---|---:|---:|
| fl | 84.007 % | 83.705 % |
| fr | 84.424 % | 83.948 % |
| rl | 87.742 % | 87.703 % |
| rr | 87.445 % | 87.440 % |

| Pata | Transición | Retardo crudo medio | Retardo filtrado medio |
|---|---|---:|---:|
| fl | liftoff | 0.087153 s | 0.118997 s |
| fl | landing | 0.072277 s | 0.077675 s |
| fr | liftoff | 0.086005 s | 0.121858 s |
| fr | landing | 0.071420 s | 0.080734 s |
| rl | liftoff | 0.079155 s | sin pares |
| rl | landing | -0.422253 s | sin pares |
| rr | liftoff | 0.079325 s | sin pares |
| rr | landing | -0.459299 s | sin pares |

Persistencia cruda exigida para declarar vuelo filtrado: 0.120 s.

| Pata | Episodios acotados | Duración media | Duración máxima | Episodios que superan el umbral |
|---|---:|---:|---:|---:|
| fl | 43 | 0.526166 s | 0.570795 s | 43 |
| fr | 42 | 0.527103 s | 0.563437 s | 42 |
| rl | 1 | 0.036322 s | 0.036322 s | 0 |
| rr | 3 | 0.001414 s | 0.002145 s | 0 |

Un retardo positivo indica que la transición medida ocurrió después de la prevista; uno negativo indica que ocurrió antes. Los pares se buscan dentro de ±1,8 s. Los porcentajes están ponderados por tiempo, no por número de mensajes.

El análisis es descriptivo y no activa decisiones del supervisor.
