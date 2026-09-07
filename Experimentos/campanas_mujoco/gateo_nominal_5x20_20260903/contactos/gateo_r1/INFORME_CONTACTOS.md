# Análisis de contactos medidos durante gateo

- Bolsa: `Experimentos/campanas_mujoco/gateo_nominal_5x20_20260903/rosbag2/gateo_r1`.
- Ventana gateo--stand: 92.767633 s.
- Ciclos completos según `/nova/gait_phase`: 21.
- Índices de ciclo completos: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20].
- Estados comprimidos analizados: 551.
- Coincidencia simultánea filtrada de las cuatro patas: 68.773 %.

## Resultado por pata

| Pata | Coincidencia | Retardo despegue medio | Retardo aterrizaje medio |
|---|---:|---:|---:|
| fl | 85.723 % | 0.069784 s | 0.028875 s |
| fr | 86.346 % | 0.069342 s | 0.030418 s |
| rl | 87.779 % | sin pares | sin pares |
| rr | 87.173 % | sin pares | sin pares |

## Comparación crudo frente a filtrado

- Coincidencia simultánea cruda: 71.135 %.
- Coincidencia simultánea filtrada: 68.773 %.

| Pata | Coincidencia cruda | Coincidencia filtrada |
|---|---:|---:|
| fl | 86.171 % | 85.723 % |
| fr | 86.732 % | 86.346 % |
| rl | 87.812 % | 87.779 % |
| rr | 87.215 % | 87.173 % |

| Pata | Transición | Retardo crudo medio | Retardo filtrado medio |
|---|---|---:|---:|
| fl | liftoff | 0.036460 s | 0.069784 s |
| fl | landing | 0.020766 s | 0.028875 s |
| fr | liftoff | 0.036592 s | 0.069342 s |
| fr | landing | 0.021331 s | 0.030418 s |
| rl | liftoff | 0.041397 s | sin pares |
| rl | landing | -0.492680 s | sin pares |
| rr | liftoff | 0.044072 s | sin pares |
| rr | landing | -0.491342 s | sin pares |

Persistencia cruda exigida para declarar vuelo filtrado: 0.120 s.

| Pata | Episodios acotados | Duración media | Duración máxima | Episodios que superan el umbral |
|---|---:|---:|---:|---:|
| fl | 45 | 0.514173 s | 0.532042 s | 44 |
| fr | 44 | 0.503141 s | 0.534196 s | 42 |
| rl | 8 | 0.003786 s | 0.005991 s | 0 |
| rr | 9 | 0.004287 s | 0.007102 s | 0 |

Un retardo positivo indica que la transición medida ocurrió después de la prevista; uno negativo indica que ocurrió antes. Los pares se buscan dentro de ±1,8 s. Los porcentajes están ponderados por tiempo, no por número de mensajes.

El análisis es descriptivo y no activa decisiones del supervisor.
