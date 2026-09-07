# Análisis de contactos medidos durante marcha paso

- Bolsa: `Experimentos/campanas_mujoco/barrido_ganancias_paso_20260903/kp30_kv3/rosbag2/paso_r1`.
- Ventana paso--stand: 32.140084 s.
- Ciclos completos según `/nova/gait_phase`: 5.
- Índices de ciclo completos: [0, 1, 2, 3, 4].
- Estados comprimidos analizados: 165.
- Coincidencia simultánea filtrada de las cuatro patas: 12.015 %.

## Resultado por pata

| Pata | Coincidencia | Retardo despegue medio | Retardo aterrizaje medio |
|---|---:|---:|---:|
| fl | 79.652 % | 0.600553 s | -0.488043 s |
| fr | 81.604 % | 0.574551 s | -0.492922 s |
| rl | 77.660 % | sin pares | sin pares |
| rr | 73.100 % | sin pares | sin pares |

## Comparación crudo frente a filtrado

- Coincidencia simultánea cruda: 13.306 %.
- Coincidencia simultánea filtrada: 12.015 %.

| Pata | Coincidencia cruda | Coincidencia filtrada |
|---|---:|---:|
| fl | 80.070 % | 79.652 % |
| fr | 81.920 % | 81.604 % |
| rl | 77.660 % | 77.660 % |
| rr | 73.100 % | 73.100 % |

| Pata | Transición | Retardo crudo medio | Retardo filtrado medio |
|---|---|---:|---:|
| fl | liftoff | 0.415752 s | 0.600553 s |
| fl | landing | 0.103558 s | -0.488043 s |
| fr | liftoff | 0.416514 s | 0.574551 s |
| fr | landing | -0.139842 s | -0.492922 s |
| rl | liftoff | sin pares | sin pares |
| rl | landing | sin pares | sin pares |
| rr | liftoff | sin pares | sin pares |
| rr | landing | sin pares | sin pares |

Persistencia cruda exigida para declarar vuelo filtrado: 0.120 s.

| Pata | Episodios acotados | Duración media | Duración máxima | Episodios que superan el umbral |
|---|---:|---:|---:|---:|
| fl | 35 | 0.068772 s | 0.378601 s | 6 |
| fr | 24 | 0.083402 s | 0.378139 s | 5 |
| rl | 0 | sin episodios | sin episodios | 0 |
| rr | 0 | sin episodios | sin episodios | 0 |

Un retardo positivo indica que la transición medida ocurrió después de la prevista; uno negativo indica que ocurrió antes. Los pares se buscan dentro de ±1,8 s. Los porcentajes están ponderados por tiempo, no por número de mensajes.

El análisis es descriptivo y no activa decisiones del supervisor.
