# Análisis de contactos medidos durante marcha paso

- Bolsa: `Experimentos/campanas_mujoco/perturbacion_empuje_paso_10N_20260903/rosbag2/paso_r1`.
- Ventana paso--stand: 29.455891 s.
- Ciclos completos según `/nova/gait_phase`: 5.
- Índices de ciclo completos: [0, 1, 2, 3, 4].
- Estados comprimidos analizados: 112.
- Coincidencia simultánea filtrada de las cuatro patas: 36.790 %.

## Resultado por pata

| Pata | Coincidencia | Retardo despegue medio | Retardo aterrizaje medio |
|---|---:|---:|---:|
| fl | 74.699 % | 0.250779 s | -0.147813 s |
| fr | 75.522 % | 0.252203 s | -0.149374 s |
| rl | 75.651 % | sin pares | sin pares |
| rr | 75.625 % | sin pares | sin pares |

## Comparación crudo frente a filtrado

- Coincidencia simultánea cruda: 37.608 %.
- Coincidencia simultánea filtrada: 36.790 %.

| Pata | Coincidencia cruda | Coincidencia filtrada |
|---|---:|---:|
| fl | 74.802 % | 74.699 % |
| fr | 75.518 % | 75.522 % |
| rl | 75.681 % | 75.651 % |
| rr | 75.703 % | 75.625 % |

| Pata | Transición | Retardo crudo medio | Retardo filtrado medio |
|---|---|---:|---:|
| fl | liftoff | 0.220462 s | 0.250779 s |
| fl | landing | -0.156408 s | -0.147813 s |
| fr | liftoff | 0.222236 s | 0.252203 s |
| fr | landing | -0.159751 s | -0.149374 s |
| rl | liftoff | 1.271588 s | sin pares |
| rl | landing | -0.160868 s | sin pares |
| rr | liftoff | 1.271657 s | sin pares |
| rr | landing | -0.159522 s | sin pares |

Persistencia cruda exigida para declarar vuelo filtrado: 0.120 s.

| Pata | Episodios acotados | Duración media | Duración máxima | Episodios que superan el umbral |
|---|---:|---:|---:|---:|
| fl | 10 | 1.064022 s | 1.072355 s | 10 |
| fr | 10 | 1.062259 s | 1.068739 s | 10 |
| rl | 2 | 0.004399 s | 0.005429 s | 0 |
| rr | 5 | 0.004601 s | 0.005856 s | 0 |

Un retardo positivo indica que la transición medida ocurrió después de la prevista; uno negativo indica que ocurrió antes. Los pares se buscan dentro de ±1,8 s. Los porcentajes están ponderados por tiempo, no por número de mensajes.

El análisis es descriptivo y no activa decisiones del supervisor.
