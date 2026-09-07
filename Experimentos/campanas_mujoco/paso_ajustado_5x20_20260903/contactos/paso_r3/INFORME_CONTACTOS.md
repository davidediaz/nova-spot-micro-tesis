# Análisis de contactos medidos durante marcha paso

- Bolsa: `Experimentos/campanas_mujoco/paso_ajustado_5x20_20260903/rosbag2/paso_r3`.
- Ventana paso--stand: 122.138814 s.
- Ciclos completos según `/nova/gait_phase`: 21.
- Índices de ciclo completos: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20].
- Estados comprimidos analizados: 471.
- Coincidencia simultánea filtrada de las cuatro patas: 36.646 %.

## Resultado por pata

| Pata | Coincidencia | Retardo despegue medio | Retardo aterrizaje medio |
|---|---:|---:|---:|
| fl | 75.112 % | 0.252691 s | -0.144004 s |
| fr | 75.337 % | 0.252686 s | -0.143246 s |
| rl | 75.244 % | sin pares | sin pares |
| rr | 75.252 % | sin pares | sin pares |

## Comparación crudo frente a filtrado

- Coincidencia simultánea cruda: 37.472 %.
- Coincidencia simultánea filtrada: 36.646 %.

| Pata | Coincidencia cruda | Coincidencia filtrada |
|---|---:|---:|
| fl | 75.165 % | 75.112 % |
| fr | 75.323 % | 75.337 % |
| rl | 75.299 % | 75.244 % |
| rr | 75.309 % | 75.252 % |

| Pata | Transición | Retardo crudo medio | Retardo filtrado medio |
|---|---|---:|---:|
| fl | liftoff | 0.220237 s | 0.252691 s |
| fl | landing | -0.153579 s | -0.144004 s |
| fr | liftoff | 0.220940 s | 0.252686 s |
| fr | landing | -0.151899 s | -0.143246 s |
| rl | liftoff | 1.078448 s | sin pares |
| rl | landing | -0.183664 s | sin pares |
| rr | liftoff | 1.100828 s | sin pares |
| rr | landing | -0.191026 s | sin pares |

Persistencia cruda exigida para declarar vuelo filtrado: 0.120 s.

| Pata | Episodios acotados | Duración media | Duración máxima | Episodios que superan el umbral |
|---|---:|---:|---:|---:|
| fl | 42 | 1.063378 s | 1.074119 s | 42 |
| fr | 42 | 1.064719 s | 1.079137 s | 42 |
| rl | 18 | 0.003771 s | 0.006018 s | 0 |
| rr | 16 | 0.004283 s | 0.008656 s | 0 |

Un retardo positivo indica que la transición medida ocurrió después de la prevista; uno negativo indica que ocurrió antes. Los pares se buscan dentro de ±1,8 s. Los porcentajes están ponderados por tiempo, no por número de mensajes.

El análisis es descriptivo y no activa decisiones del supervisor.
