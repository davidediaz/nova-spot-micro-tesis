# Análisis de contactos medidos durante marcha paso

- Bolsa: `Experimentos/campanas_mujoco/perturbacion_empuje_paso_30N_20260903/rosbag2/paso_r1`.
- Ventana paso--stand: 29.434537 s.
- Ciclos completos según `/nova/gait_phase`: 5.
- Índices de ciclo completos: [0, 1, 2, 3, 4].
- Estados comprimidos analizados: 126.
- Coincidencia simultánea filtrada de las cuatro patas: 36.535 %.

## Resultado por pata

| Pata | Coincidencia | Retardo despegue medio | Retardo aterrizaje medio |
|---|---:|---:|---:|
| fl | 74.798 % | 0.249829 s | -0.142242 s |
| fr | 75.378 % | 0.254194 s | -0.144720 s |
| rl | 75.327 % | -1.168096 s | sin pares |
| rr | 75.539 % | sin pares | sin pares |

## Comparación crudo frente a filtrado

- Coincidencia simultánea cruda: 37.287 %.
- Coincidencia simultánea filtrada: 36.535 %.

| Pata | Coincidencia cruda | Coincidencia filtrada |
|---|---:|---:|
| fl | 74.832 % | 74.798 % |
| fr | 75.478 % | 75.378 % |
| rl | 75.382 % | 75.327 % |
| rr | 75.557 % | 75.539 % |

| Pata | Transición | Retardo crudo medio | Retardo filtrado medio |
|---|---|---:|---:|
| fl | liftoff | 0.219529 s | 0.249829 s |
| fl | landing | -0.152890 s | -0.142242 s |
| fr | liftoff | 0.222353 s | 0.254194 s |
| fr | landing | -0.154591 s | -0.144720 s |
| rl | liftoff | 0.310571 s | -1.168096 s |
| rl | landing | -0.162176 s | sin pares |
| rr | liftoff | 1.100653 s | sin pares |
| rr | landing | -0.160594 s | sin pares |

Persistencia cruda exigida para declarar vuelo filtrado: 0.120 s.

| Pata | Episodios acotados | Duración media | Duración máxima | Episodios que superan el umbral |
|---|---:|---:|---:|---:|
| fl | 10 | 1.064781 s | 1.070118 s | 10 |
| fr | 12 | 0.882415 s | 1.071770 s | 10 |
| rl | 8 | 0.015214 s | 0.087569 s | 0 |
| rr | 2 | 0.002661 s | 0.003461 s | 0 |

Un retardo positivo indica que la transición medida ocurrió después de la prevista; uno negativo indica que ocurrió antes. Los pares se buscan dentro de ±1,8 s. Los porcentajes están ponderados por tiempo, no por número de mensajes.

El análisis es descriptivo y no activa decisiones del supervisor.
