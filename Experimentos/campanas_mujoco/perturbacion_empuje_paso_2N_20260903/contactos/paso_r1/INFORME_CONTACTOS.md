# Análisis de contactos medidos durante marcha paso

- Bolsa: `Experimentos/campanas_mujoco/perturbacion_empuje_paso_2N_20260903/rosbag2/paso_r1`.
- Ventana paso--stand: 31.979430 s.
- Ciclos completos según `/nova/gait_phase`: 5.
- Índices de ciclo completos: [0, 1, 2, 3, 4].
- Estados comprimidos analizados: 132.
- Coincidencia simultánea filtrada de las cuatro patas: 36.712 %.

## Resultado por pata

| Pata | Coincidencia | Retardo despegue medio | Retardo aterrizaje medio |
|---|---:|---:|---:|
| fl | 73.047 % | 0.249565 s | -0.146210 s |
| fr | 77.504 % | 0.253457 s | -0.144637 s |
| rl | 78.329 % | 0.865157 s | -0.302728 s |
| rr | 73.003 % | sin pares | sin pares |

## Comparación crudo frente a filtrado

- Coincidencia simultánea cruda: 37.555 %.
- Coincidencia simultánea filtrada: 36.712 %.

| Pata | Coincidencia cruda | Coincidencia filtrada |
|---|---:|---:|
| fl | 73.099 % | 73.047 % |
| fr | 77.528 % | 77.504 % |
| rl | 78.461 % | 78.329 % |
| rr | 73.046 % | 73.003 % |

| Pata | Transición | Retardo crudo medio | Retardo filtrado medio |
|---|---|---:|---:|
| fl | liftoff | 0.219347 s | 0.249565 s |
| fl | landing | -0.153159 s | -0.146210 s |
| fr | liftoff | 0.220819 s | 0.253457 s |
| fr | landing | -0.154099 s | -0.144637 s |
| rl | liftoff | 1.117662 s | 0.865157 s |
| rl | landing | -0.224966 s | -0.302728 s |
| rr | liftoff | 1.230721 s | sin pares |
| rr | landing | -0.203821 s | sin pares |

Persistencia cruda exigida para declarar vuelo filtrado: 0.120 s.

| Pata | Episodios acotados | Duración media | Duración máxima | Episodios que superan el umbral |
|---|---:|---:|---:|---:|
| fl | 12 | 1.061810 s | 1.077441 s | 12 |
| fr | 11 | 0.947374 s | 1.068422 s | 11 |
| rl | 6 | 0.052432 s | 0.295972 s | 1 |
| rr | 4 | 0.003397 s | 0.004586 s | 0 |

Un retardo positivo indica que la transición medida ocurrió después de la prevista; uno negativo indica que ocurrió antes. Los pares se buscan dentro de ±1,8 s. Los porcentajes están ponderados por tiempo, no por número de mensajes.

El análisis es descriptivo y no activa decisiones del supervisor.
