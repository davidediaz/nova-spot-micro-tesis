# Análisis de contactos medidos durante marcha paso

- Bolsa: `Experimentos/campanas_mujoco/paso_ajustado_5x20_20260903/rosbag2/paso_r1`.
- Ventana paso--stand: 121.462941 s.
- Ciclos completos según `/nova/gait_phase`: 21.
- Índices de ciclo completos: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20].
- Estados comprimidos analizados: 479.
- Coincidencia simultánea filtrada de las cuatro patas: 36.293 %.

## Resultado por pata

| Pata | Coincidencia | Retardo despegue medio | Retardo aterrizaje medio |
|---|---:|---:|---:|
| fl | 74.986 % | 0.251543 s | -0.145904 s |
| fr | 75.214 % | 0.250122 s | -0.144842 s |
| rl | 75.107 % | sin pares | sin pares |
| rr | 75.098 % | sin pares | sin pares |

## Comparación crudo frente a filtrado

- Coincidencia simultánea cruda: 37.130 %.
- Coincidencia simultánea filtrada: 36.293 %.

| Pata | Coincidencia cruda | Coincidencia filtrada |
|---|---:|---:|
| fl | 75.016 % | 74.986 % |
| fr | 75.210 % | 75.214 % |
| rl | 75.187 % | 75.107 % |
| rr | 75.140 % | 75.098 % |

| Pata | Transición | Retardo crudo medio | Retardo filtrado medio |
|---|---|---:|---:|
| fl | liftoff | 0.219123 s | 0.251543 s |
| fl | landing | -0.155122 s | -0.145904 s |
| fr | liftoff | 0.218887 s | 0.250122 s |
| fr | landing | -0.153258 s | -0.144842 s |
| rl | liftoff | 0.875436 s | sin pares |
| rl | landing | -0.313722 s | sin pares |
| rr | liftoff | 1.167763 s | sin pares |
| rr | landing | -0.189897 s | sin pares |

Persistencia cruda exigida para declarar vuelo filtrado: 0.120 s.

| Pata | Episodios acotados | Duración media | Duración máxima | Episodios que superan el umbral |
|---|---:|---:|---:|---:|
| fl | 42 | 1.063503 s | 1.074765 s | 42 |
| fr | 42 | 1.064264 s | 1.090063 s | 42 |
| rl | 23 | 0.004206 s | 0.010686 s | 0 |
| rr | 14 | 0.003622 s | 0.005481 s | 0 |

Un retardo positivo indica que la transición medida ocurrió después de la prevista; uno negativo indica que ocurrió antes. Los pares se buscan dentro de ±1,8 s. Los porcentajes están ponderados por tiempo, no por número de mensajes.

El análisis es descriptivo y no activa decisiones del supervisor.
