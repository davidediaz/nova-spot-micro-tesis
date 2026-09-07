# Análisis de contactos medidos durante marcha paso

- Bolsa: `Experimentos/campanas_mujoco/barrido_altura_paso_20260903/height_020/rosbag2/paso_r1`.
- Ventana paso--stand: 31.942821 s.
- Ciclos completos según `/nova/gait_phase`: 5.
- Índices de ciclo completos: [0, 1, 2, 3, 4].
- Estados comprimidos analizados: 111.
- Coincidencia simultánea filtrada de las cuatro patas: 35.820 %.

## Resultado por pata

| Pata | Coincidencia | Retardo despegue medio | Retardo aterrizaje medio |
|---|---:|---:|---:|
| fl | 72.860 % | 0.251035 s | -0.147706 s |
| fr | 76.725 % | 0.248967 s | -0.149913 s |
| rl | 77.452 % | sin pares | sin pares |
| rr | 72.915 % | sin pares | sin pares |

## Comparación crudo frente a filtrado

- Coincidencia simultánea cruda: 36.803 %.
- Coincidencia simultánea filtrada: 35.820 %.

| Pata | Coincidencia cruda | Coincidencia filtrada |
|---|---:|---:|
| fl | 72.909 % | 72.860 % |
| fr | 76.864 % | 76.725 % |
| rl | 77.452 % | 77.452 % |
| rr | 72.915 % | 72.915 % |

| Pata | Transición | Retardo crudo medio | Retardo filtrado medio |
|---|---|---:|---:|
| fl | liftoff | 0.219720 s | 0.251035 s |
| fl | landing | -0.155986 s | -0.147706 s |
| fr | liftoff | 0.214298 s | 0.248967 s |
| fr | landing | -0.156820 s | -0.149913 s |
| rl | liftoff | sin pares | sin pares |
| rl | landing | sin pares | sin pares |
| rr | liftoff | sin pares | sin pares |
| rr | landing | sin pares | sin pares |

Persistencia cruda exigida para declarar vuelo filtrado: 0.120 s.

| Pata | Episodios acotados | Duración media | Duración máxima | Episodios que superan el umbral |
|---|---:|---:|---:|---:|
| fl | 12 | 1.064972 s | 1.076868 s | 12 |
| fr | 10 | 1.065526 s | 1.076895 s | 10 |
| rl | 0 | sin episodios | sin episodios | 0 |
| rr | 0 | sin episodios | sin episodios | 0 |

Un retardo positivo indica que la transición medida ocurrió después de la prevista; uno negativo indica que ocurrió antes. Los pares se buscan dentro de ±1,8 s. Los porcentajes están ponderados por tiempo, no por número de mensajes.

El análisis es descriptivo y no activa decisiones del supervisor.
