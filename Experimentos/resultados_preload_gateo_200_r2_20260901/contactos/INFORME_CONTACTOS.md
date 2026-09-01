# Análisis de contactos medidos durante gateo

- Bolsa: `Experimentos/rosbag2/preload_gateo_200_r2_20260901`.
- Ventana gateo--stand: 79.218225 s.
- Ciclos completos según `/nova/gait_phase`: 18.
- Índices de ciclo completos: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17].
- Estados comprimidos analizados: 527.
- Coincidencia simultánea filtrada de las cuatro patas: 19.738 %.

## Resultado por pata

| Pata | Coincidencia | Retardo despegue medio | Retardo aterrizaje medio |
|---|---:|---:|---:|
| fl | 65.193 % | 0.184430 s | 0.519969 s |
| fr | 66.085 % | 0.190163 s | 0.529735 s |
| rl | 92.523 % | 0.254557 s | -0.074480 s |
| rr | 92.557 % | 0.255041 s | -0.072506 s |

## Comparación crudo frente a filtrado

- Coincidencia simultánea cruda: 28.552 %.
- Coincidencia simultánea filtrada: 19.738 %.

| Pata | Coincidencia cruda | Coincidencia filtrada |
|---|---:|---:|
| fl | 66.887 % | 65.193 % |
| fr | 67.572 % | 66.085 % |
| rl | 94.574 % | 92.523 % |
| rr | 94.638 % | 92.557 % |

| Pata | Transición | Retardo crudo medio | Retardo filtrado medio |
|---|---|---:|---:|
| fl | liftoff | 0.061794 s | 0.184430 s |
| fl | landing | 0.487402 s | 0.519969 s |
| fr | liftoff | 0.067322 s | 0.190163 s |
| fr | landing | 0.496515 s | 0.529735 s |
| rl | liftoff | 0.130527 s | 0.254557 s |
| rl | landing | -0.108267 s | -0.074480 s |
| rr | liftoff | 0.130660 s | 0.255041 s |
| rr | landing | -0.105306 s | -0.072506 s |

Persistencia cruda exigida para declarar vuelo filtrado: 0.120 s.

| Pata | Episodios acotados | Duración media | Duración máxima | Episodios que superan el umbral |
|---|---:|---:|---:|---:|
| fl | 38 | 0.898108 s | 1.000941 s | 38 |
| fr | 36 | 0.916136 s | 1.001129 s | 36 |
| rl | 18 | 0.301978 s | 0.311157 s | 18 |
| rr | 18 | 0.304325 s | 0.348080 s | 18 |

Un retardo positivo indica que la transición medida ocurrió después de la prevista; uno negativo indica que ocurrió antes. Los pares se buscan dentro de ±1,8 s. Los porcentajes están ponderados por tiempo, no por número de mensajes.

El análisis es descriptivo y no activa decisiones del supervisor.
