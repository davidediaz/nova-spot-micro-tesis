# Análisis de contactos medidos durante marcha paso

- Bolsa: `Experimentos/campanas_mujoco/barrido_ganancias_paso_20260903/kp80_kv8/rosbag2/paso_r1`.
- Ventana paso--stand: 29.989232 s.
- Ciclos completos según `/nova/gait_phase`: 5.
- Índices de ciclo completos: [0, 1, 2, 3, 4].
- Estados comprimidos analizados: 111.
- Coincidencia simultánea filtrada de las cuatro patas: 38.022 %.

## Resultado por pata

| Pata | Coincidencia | Retardo despegue medio | Retardo aterrizaje medio |
|---|---:|---:|---:|
| fl | 75.314 % | 0.252130 s | -0.139558 s |
| fr | 76.217 % | 0.247816 s | -0.141570 s |
| rl | 75.987 % | sin pares | sin pares |
| rr | 75.924 % | sin pares | sin pares |

## Comparación crudo frente a filtrado

- Coincidencia simultánea cruda: 38.899 %.
- Coincidencia simultánea filtrada: 38.022 %.

| Pata | Coincidencia cruda | Coincidencia filtrada |
|---|---:|---:|
| fl | 75.360 % | 75.314 % |
| fr | 76.255 % | 76.217 % |
| rl | 76.067 % | 75.987 % |
| rr | 75.934 % | 75.924 % |

| Pata | Transición | Retardo crudo medio | Retardo filtrado medio |
|---|---|---:|---:|
| fl | liftoff | 0.219901 s | 0.252130 s |
| fl | landing | -0.151894 s | -0.139558 s |
| fr | liftoff | 0.213712 s | 0.247816 s |
| fr | landing | -0.151320 s | -0.141570 s |
| rl | liftoff | 0.932263 s | sin pares |
| rl | landing | -0.462014 s | sin pares |
| rr | liftoff | 1.103040 s | sin pares |
| rr | landing | -0.335135 s | sin pares |

Persistencia cruda exigida para declarar vuelo filtrado: 0.120 s.

| Pata | Episodios acotados | Duración media | Duración máxima | Episodios que superan el umbral |
|---|---:|---:|---:|---:|
| fl | 10 | 1.065791 s | 1.073898 s | 10 |
| fr | 10 | 1.064062 s | 1.071455 s | 10 |
| rl | 5 | 0.004822 s | 0.007606 s | 0 |
| rr | 1 | 0.002912 s | 0.002912 s | 0 |

Un retardo positivo indica que la transición medida ocurrió después de la prevista; uno negativo indica que ocurrió antes. Los pares se buscan dentro de ±1,8 s. Los porcentajes están ponderados por tiempo, no por número de mensajes.

El análisis es descriptivo y no activa decisiones del supervisor.
