# Análisis de contactos medidos durante marcha paso

- Bolsa: `Experimentos/campanas_mujoco/validacion_aislamiento_r4_20260903/rosbag2/paso_r1`.
- Ventana paso--stand: 17.300915 s.
- Ciclos completos según `/nova/gait_phase`: 3.
- Índices de ciclo completos: [0, 1, 2].
- Estados comprimidos analizados: 13.
- Coincidencia simultánea filtrada de las cuatro patas: 0.000 %.

## Resultado por pata

| Pata | Coincidencia | Retardo despegue medio | Retardo aterrizaje medio |
|---|---:|---:|---:|
| fl | 74.889 % | sin pares | sin pares |
| fr | 75.057 % | sin pares | sin pares |
| rl | 75.023 % | sin pares | sin pares |
| rr | 75.030 % | sin pares | sin pares |

## Comparación crudo frente a filtrado

- Coincidencia simultánea cruda: 0.000 %.
- Coincidencia simultánea filtrada: 0.000 %.

| Pata | Coincidencia cruda | Coincidencia filtrada |
|---|---:|---:|
| fl | 74.889 % | 74.889 % |
| fr | 75.057 % | 75.057 % |
| rl | 75.023 % | 75.023 % |
| rr | 75.030 % | 75.030 % |

| Pata | Transición | Retardo crudo medio | Retardo filtrado medio |
|---|---|---:|---:|
| fl | liftoff | sin pares | sin pares |
| fl | landing | sin pares | sin pares |
| fr | liftoff | sin pares | sin pares |
| fr | landing | sin pares | sin pares |
| rl | liftoff | sin pares | sin pares |
| rl | landing | sin pares | sin pares |
| rr | liftoff | sin pares | sin pares |
| rr | landing | sin pares | sin pares |

Persistencia cruda exigida para declarar vuelo filtrado: 0.120 s.

| Pata | Episodios acotados | Duración media | Duración máxima | Episodios que superan el umbral |
|---|---:|---:|---:|---:|
| fl | 0 | sin episodios | sin episodios | 0 |
| fr | 0 | sin episodios | sin episodios | 0 |
| rl | 0 | sin episodios | sin episodios | 0 |
| rr | 0 | sin episodios | sin episodios | 0 |

Un retardo positivo indica que la transición medida ocurrió después de la prevista; uno negativo indica que ocurrió antes. Los pares se buscan dentro de ±1,8 s. Los porcentajes están ponderados por tiempo, no por número de mensajes.

El análisis es descriptivo y no activa decisiones del supervisor.
