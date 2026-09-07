# Análisis de contactos medidos durante marcha paso

- Bolsa: `Experimentos/campanas_mujoco/barrido_friccion_paso_r2_20260903/friction_0675/rosbag2/paso_r1`.
- Ventana paso--stand: 29.736689 s.
- Ciclos completos según `/nova/gait_phase`: 5.
- Índices de ciclo completos: [0, 1, 2, 3, 4].
- Estados comprimidos analizados: 111.
- Coincidencia simultánea filtrada de las cuatro patas: 25.070 %.

## Resultado por pata

| Pata | Coincidencia | Retardo despegue medio | Retardo aterrizaje medio |
|---|---:|---:|---:|
| fl | 75.383 % | 0.426542 s | -0.314916 s |
| fr | 76.772 % | 0.433023 s | -0.311499 s |
| rl | 75.784 % | sin pares | sin pares |
| rr | 75.738 % | sin pares | sin pares |

## Comparación crudo frente a filtrado

- Coincidencia simultánea cruda: 26.107 %.
- Coincidencia simultánea filtrada: 25.070 %.

| Pata | Coincidencia cruda | Coincidencia filtrada |
|---|---:|---:|
| fl | 75.425 % | 75.383 % |
| fr | 76.886 % | 76.772 % |
| rl | 75.784 % | 75.784 % |
| rr | 75.738 % | 75.738 % |

| Pata | Transición | Retardo crudo medio | Retardo filtrado medio |
|---|---|---:|---:|
| fl | liftoff | 0.331796 s | 0.426542 s |
| fl | landing | -0.321391 s | -0.314916 s |
| fr | liftoff | 0.325557 s | 0.433023 s |
| fr | landing | -0.213147 s | -0.311499 s |
| rl | liftoff | sin pares | sin pares |
| rl | landing | sin pares | sin pares |
| rr | liftoff | sin pares | sin pares |
| rr | landing | sin pares | sin pares |

Persistencia cruda exigida para declarar vuelo filtrado: 0.120 s.

| Pata | Episodios acotados | Duración media | Duración máxima | Episodios que superan el umbral |
|---|---:|---:|---:|---:|
| fl | 12 | 0.578073 s | 0.733406 s | 10 |
| fr | 13 | 0.532380 s | 0.724535 s | 10 |
| rl | 0 | sin episodios | sin episodios | 0 |
| rr | 0 | sin episodios | sin episodios | 0 |

Un retardo positivo indica que la transición medida ocurrió después de la prevista; uno negativo indica que ocurrió antes. Los pares se buscan dentro de ±1,8 s. Los porcentajes están ponderados por tiempo, no por número de mensajes.

El análisis es descriptivo y no activa decisiones del supervisor.
