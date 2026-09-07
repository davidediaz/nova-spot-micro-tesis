# Análisis de contactos medidos durante marcha paso

- Bolsa: `Experimentos/campanas_mujoco/barrido_ganancias_paso_20260903/kp60_kv6/rosbag2/paso_r1`.
- Ventana paso--stand: 29.457295 s.
- Ciclos completos según `/nova/gait_phase`: 5.
- Índices de ciclo completos: [0, 1, 2, 3, 4].
- Estados comprimidos analizados: 147.
- Coincidencia simultánea filtrada de las cuatro patas: 32.933 %.

## Resultado por pata

| Pata | Coincidencia | Retardo despegue medio | Retardo aterrizaje medio |
|---|---:|---:|---:|
| fl | 77.831 % | 0.258725 s | -0.251599 s |
| fr | 78.770 % | 0.255436 s | -0.250415 s |
| rl | 75.570 % | sin pares | sin pares |
| rr | 75.491 % | sin pares | sin pares |

## Comparación crudo frente a filtrado

- Coincidencia simultánea cruda: 33.827 %.
- Coincidencia simultánea filtrada: 32.933 %.

| Pata | Coincidencia cruda | Coincidencia filtrada |
|---|---:|---:|
| fl | 77.737 % | 77.831 % |
| fr | 78.536 % | 78.770 % |
| rl | 75.570 % | 75.570 % |
| rr | 75.491 % | 75.491 % |

| Pata | Transición | Retardo crudo medio | Retardo filtrado medio |
|---|---|---:|---:|
| fl | liftoff | 0.227070 s | 0.258725 s |
| fl | landing | -0.024587 s | -0.251599 s |
| fr | liftoff | 0.221183 s | 0.255436 s |
| fr | landing | 0.053343 s | -0.250415 s |
| rl | liftoff | sin pares | sin pares |
| rl | landing | sin pares | sin pares |
| rr | liftoff | sin pares | sin pares |
| rr | landing | sin pares | sin pares |

Persistencia cruda exigida para declarar vuelo filtrado: 0.120 s.

| Pata | Episodios acotados | Duración media | Duración máxima | Episodios que superan el umbral |
|---|---:|---:|---:|---:|
| fl | 22 | 0.393859 s | 0.956579 s | 10 |
| fr | 20 | 0.433679 s | 0.954508 s | 10 |
| rl | 0 | sin episodios | sin episodios | 0 |
| rr | 0 | sin episodios | sin episodios | 0 |

Un retardo positivo indica que la transición medida ocurrió después de la prevista; uno negativo indica que ocurrió antes. Los pares se buscan dentro de ±1,8 s. Los porcentajes están ponderados por tiempo, no por número de mensajes.

El análisis es descriptivo y no activa decisiones del supervisor.
