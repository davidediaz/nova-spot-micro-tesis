# Análisis de contactos medidos durante gateo

- Bolsa: `Experimentos/rosbag2/liberacion_gateo_080_altura125_r3_20260901`.
- Ventana gateo--stand: 79.153864 s.
- Ciclos completos según `/nova/gait_phase`: 18.
- Índices de ciclo completos: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17].
- Estados comprimidos analizados: 512.
- Coincidencia simultánea filtrada de las cuatro patas: 13.639 %.

## Resultado por pata

| Pata | Coincidencia | Retardo despegue medio | Retardo aterrizaje medio |
|---|---:|---:|---:|
| fl | 60.371 % | 0.259121 s | 0.536092 s |
| fr | 61.301 % | 0.257822 s | 0.543825 s |
| rl | 88.805 % | 0.253525 s | -0.238729 s |
| rr | 88.519 % | 0.253387 s | -0.237929 s |

## Comparación crudo frente a filtrado

- Coincidencia simultánea cruda: 20.547 %.
- Coincidencia simultánea filtrada: 13.639 %.

| Pata | Coincidencia cruda | Coincidencia filtrada |
|---|---:|---:|
| fl | 62.057 % | 60.371 % |
| fr | 62.651 % | 61.301 % |
| rl | 90.841 % | 88.805 % |
| rr | 90.820 % | 88.519 % |

| Pata | Transición | Retardo crudo medio | Retardo filtrado medio |
|---|---|---:|---:|
| fl | liftoff | 0.134546 s | 0.259121 s |
| fl | landing | 0.503198 s | 0.536092 s |
| fr | liftoff | 0.134719 s | 0.257822 s |
| fr | landing | 0.510923 s | 0.543825 s |
| rl | liftoff | 0.130401 s | 0.253525 s |
| rl | landing | -0.272322 s | -0.238729 s |
| rr | liftoff | 0.131631 s | 0.253387 s |
| rr | landing | -0.271996 s | -0.237929 s |

Persistencia cruda exigida para declarar vuelo filtrado: 0.120 s.

| Pata | Episodios acotados | Duración media | Duración máxima | Episodios que superan el umbral |
|---|---:|---:|---:|---:|
| fl | 37 | 0.926941 s | 1.003721 s | 37 |
| fr | 37 | 0.930491 s | 1.003630 s | 37 |
| rl | 18 | 0.137415 s | 0.147404 s | 18 |
| rr | 18 | 0.135786 s | 0.146749 s | 18 |

Un retardo positivo indica que la transición medida ocurrió después de la prevista; uno negativo indica que ocurrió antes. Los pares se buscan dentro de ±1,8 s. Los porcentajes están ponderados por tiempo, no por número de mensajes.

El análisis es descriptivo y no activa decisiones del supervisor.
