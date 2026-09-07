# Análisis de contactos medidos durante marcha paso

- Bolsa: `Experimentos/campanas_mujoco/barrido_ganancias_paso_20260903/kp120_kv12/rosbag2/paso_r1`.
- Ventana paso--stand: 29.949845 s.
- Ciclos completos según `/nova/gait_phase`: 5.
- Índices de ciclo completos: [0, 1, 2, 3, 4].
- Estados comprimidos analizados: 139.
- Coincidencia simultánea filtrada de las cuatro patas: 37.714 %.

## Resultado por pata

| Pata | Coincidencia | Retardo despegue medio | Retardo aterrizaje medio |
|---|---:|---:|---:|
| fl | 74.506 % | 0.245153 s | -0.136380 s |
| fr | 76.032 % | 0.249900 s | -0.132147 s |
| rl | 75.983 % | sin pares | sin pares |
| rr | 75.988 % | sin pares | sin pares |

## Comparación crudo frente a filtrado

- Coincidencia simultánea cruda: 38.484 %.
- Coincidencia simultánea filtrada: 37.714 %.

| Pata | Coincidencia cruda | Coincidencia filtrada |
|---|---:|---:|
| fl | 74.600 % | 74.506 % |
| fr | 75.965 % | 76.032 % |
| rl | 76.154 % | 75.983 % |
| rr | 76.148 % | 75.988 % |

| Pata | Transición | Retardo crudo medio | Retardo filtrado medio |
|---|---|---:|---:|
| fl | liftoff | 0.213407 s | 0.245153 s |
| fl | landing | -0.144518 s | -0.136380 s |
| fr | liftoff | 0.216591 s | 0.249900 s |
| fr | landing | -0.145182 s | -0.132147 s |
| rl | liftoff | 1.184597 s | sin pares |
| rl | landing | -0.152039 s | sin pares |
| rr | liftoff | 0.856495 s | sin pares |
| rr | landing | -0.151072 s | sin pares |

Persistencia cruda exigida para declarar vuelo filtrado: 0.120 s.

| Pata | Episodios acotados | Duración media | Duración máxima | Episodios que superan el umbral |
|---|---:|---:|---:|---:|
| fl | 10 | 1.056017 s | 1.085939 s | 10 |
| fr | 10 | 1.078927 s | 1.083668 s | 10 |
| rl | 9 | 0.005693 s | 0.013932 s | 0 |
| rr | 11 | 0.004366 s | 0.008879 s | 0 |

Un retardo positivo indica que la transición medida ocurrió después de la prevista; uno negativo indica que ocurrió antes. Los pares se buscan dentro de ±1,8 s. Los porcentajes están ponderados por tiempo, no por número de mensajes.

El análisis es descriptivo y no activa decisiones del supervisor.
