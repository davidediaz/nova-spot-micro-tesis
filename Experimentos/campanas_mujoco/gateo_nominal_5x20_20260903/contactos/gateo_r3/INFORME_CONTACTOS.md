# Análisis de contactos medidos durante gateo

- Bolsa: `Experimentos/campanas_mujoco/gateo_nominal_5x20_20260903/rosbag2/gateo_r3`.
- Ventana gateo--stand: 92.529870 s.
- Ciclos completos según `/nova/gait_phase`: 21.
- Índices de ciclo completos: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20].
- Estados comprimidos analizados: 540.
- Coincidencia simultánea filtrada de las cuatro patas: 68.936 %.

## Resultado por pata

| Pata | Coincidencia | Retardo despegue medio | Retardo aterrizaje medio |
|---|---:|---:|---:|
| fl | 85.902 % | 0.069645 s | 0.030924 s |
| fr | 86.324 % | 0.069950 s | 0.029808 s |
| rl | 87.747 % | sin pares | sin pares |
| rr | 87.351 % | sin pares | sin pares |

## Comparación crudo frente a filtrado

- Coincidencia simultánea cruda: 71.181 %.
- Coincidencia simultánea filtrada: 68.936 %.

| Pata | Coincidencia cruda | Coincidencia filtrada |
|---|---:|---:|
| fl | 86.275 % | 85.902 % |
| fr | 86.690 % | 86.324 % |
| rl | 87.783 % | 87.747 % |
| rr | 87.380 % | 87.351 % |

| Pata | Transición | Retardo crudo medio | Retardo filtrado medio |
|---|---|---:|---:|
| fl | liftoff | 0.036293 s | 0.069645 s |
| fl | landing | 0.024860 s | 0.030924 s |
| fr | liftoff | 0.038106 s | 0.069950 s |
| fr | landing | 0.022023 s | 0.029808 s |
| rl | liftoff | 0.039326 s | sin pares |
| rl | landing | -0.494841 s | sin pares |
| rr | liftoff | 0.044002 s | sin pares |
| rr | landing | -0.493781 s | sin pares |

Persistencia cruda exigida para declarar vuelo filtrado: 0.120 s.

| Pata | Episodios acotados | Duración media | Duración máxima | Episodios que superan el umbral |
|---|---:|---:|---:|---:|
| fl | 47 | 0.482653 s | 0.541033 s | 43 |
| fr | 44 | 0.501681 s | 0.537845 s | 42 |
| rl | 7 | 0.004653 s | 0.008668 s | 0 |
| rr | 7 | 0.003929 s | 0.005868 s | 0 |

Un retardo positivo indica que la transición medida ocurrió después de la prevista; uno negativo indica que ocurrió antes. Los pares se buscan dentro de ±1,8 s. Los porcentajes están ponderados por tiempo, no por número de mensajes.

El análisis es descriptivo y no activa decisiones del supervisor.
