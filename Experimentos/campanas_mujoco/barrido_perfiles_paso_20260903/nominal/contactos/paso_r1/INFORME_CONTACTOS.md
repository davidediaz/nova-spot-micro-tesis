# Análisis de contactos medidos durante marcha paso

- Bolsa: `Experimentos/campanas_mujoco/barrido_perfiles_paso_20260903/nominal/rosbag2/paso_r1`.
- Ventana paso--stand: 29.448569 s.
- Ciclos completos según `/nova/gait_phase`: 5.
- Índices de ciclo completos: [0, 1, 2, 3, 4].
- Estados comprimidos analizados: 545.
- Coincidencia simultánea filtrada de las cuatro patas: 0.000 %.

## Resultado por pata

| Pata | Coincidencia | Retardo despegue medio | Retardo aterrizaje medio |
|---|---:|---:|---:|
| fl | 30.284 % | 0.050629 s | 0.322179 s |
| fr | 30.312 % | 0.039801 s | 0.321148 s |
| rl | 75.570 % | sin pares | sin pares |
| rr | 75.375 % | sin pares | sin pares |

## Comparación crudo frente a filtrado

- Coincidencia simultánea cruda: 0.000 %.
- Coincidencia simultánea filtrada: 0.000 %.

| Pata | Coincidencia cruda | Coincidencia filtrada |
|---|---:|---:|
| fl | 29.751 % | 30.284 % |
| fr | 29.840 % | 30.312 % |
| rl | 75.477 % | 75.570 % |
| rr | 75.375 % | 75.375 % |

| Pata | Transición | Retardo crudo medio | Retardo filtrado medio |
|---|---|---:|---:|
| fl | liftoff | 0.017791 s | 0.050629 s |
| fl | landing | -0.060337 s | 0.322179 s |
| fr | liftoff | 0.011231 s | 0.039801 s |
| fr | landing | -0.060760 s | 0.321148 s |
| rl | liftoff | -1.597611 s | sin pares |
| rl | landing | sin pares | sin pares |
| rr | liftoff | sin pares | sin pares |
| rr | landing | sin pares | sin pares |

Persistencia cruda exigida para declarar vuelo filtrado: 0.120 s.

| Pata | Episodios acotados | Duración media | Duración máxima | Episodios que superan el umbral |
|---|---:|---:|---:|---:|
| fl | 113 | 0.127261 s | 1.828972 s | 15 |
| fr | 103 | 0.133914 s | 1.829008 s | 15 |
| rl | 3 | 0.009087 s | 0.014801 s | 0 |
| rr | 0 | sin episodios | sin episodios | 0 |

Un retardo positivo indica que la transición medida ocurrió después de la prevista; uno negativo indica que ocurrió antes. Los pares se buscan dentro de ±1,8 s. Los porcentajes están ponderados por tiempo, no por número de mensajes.

El análisis es descriptivo y no activa decisiones del supervisor.
