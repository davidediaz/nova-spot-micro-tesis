# Análisis de contactos medidos durante marcha paso

- Bolsa: `Experimentos/campanas_mujoco/barrido_friccion_paso_r2_20260903/friction_045/rosbag2/paso_r1`.
- Ventana paso--stand: 29.441028 s.
- Ciclos completos según `/nova/gait_phase`: 5.
- Índices de ciclo completos: [0, 1, 2, 3, 4].
- Estados comprimidos analizados: 107.
- Coincidencia simultánea filtrada de las cuatro patas: 24.459 %.

## Resultado por pata

| Pata | Coincidencia | Retardo despegue medio | Retardo aterrizaje medio |
|---|---:|---:|---:|
| fl | 75.189 % | 0.424949 s | -0.314321 s |
| fr | 76.513 % | 0.427574 s | -0.313717 s |
| rl | 75.518 % | sin pares | sin pares |
| rr | 75.548 % | sin pares | sin pares |

## Comparación crudo frente a filtrado

- Coincidencia simultánea cruda: 25.362 %.
- Coincidencia simultánea filtrada: 24.459 %.

| Pata | Coincidencia cruda | Coincidencia filtrada |
|---|---:|---:|
| fl | 75.304 % | 75.189 % |
| fr | 76.631 % | 76.513 % |
| rl | 75.518 % | 75.518 % |
| rr | 75.548 % | 75.548 % |

| Pata | Transición | Retardo crudo medio | Retardo filtrado medio |
|---|---|---:|---:|
| fl | liftoff | 0.360381 s | 0.424949 s |
| fl | landing | -0.321310 s | -0.314321 s |
| fr | liftoff | 0.362173 s | 0.427574 s |
| fr | landing | -0.324891 s | -0.313717 s |
| rl | liftoff | sin pares | sin pares |
| rl | landing | sin pares | sin pares |
| rr | liftoff | sin pares | sin pares |
| rr | landing | sin pares | sin pares |

Persistencia cruda exigida para declarar vuelo filtrado: 0.120 s.

| Pata | Episodios acotados | Duración media | Duración máxima | Episodios que superan el umbral |
|---|---:|---:|---:|---:|
| fl | 11 | 0.627876 s | 0.730155 s | 10 |
| fr | 11 | 0.627397 s | 0.725961 s | 10 |
| rl | 0 | sin episodios | sin episodios | 0 |
| rr | 0 | sin episodios | sin episodios | 0 |

Un retardo positivo indica que la transición medida ocurrió después de la prevista; uno negativo indica que ocurrió antes. Los pares se buscan dentro de ±1,8 s. Los porcentajes están ponderados por tiempo, no por número de mensajes.

El análisis es descriptivo y no activa decisiones del supervisor.
