# Análisis de contactos medidos durante gateo

- Bolsa: `Experimentos/rosbag2/cierre_gateo_r4_20260901`.
- Ventana gateo--stand: 226.207642 s.
- Ciclos completos según `/nova/gait_phase`: 52.
- Índices de ciclo completos: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51].
- Estados comprimidos analizados: 1454.
- Coincidencia simultánea filtrada de las cuatro patas: 13.434 %.

## Resultado por pata

| Pata | Coincidencia | Retardo despegue medio | Retardo aterrizaje medio |
|---|---:|---:|---:|
| fl | 60.270 % | 0.258131 s | 0.538989 s |
| fr | 61.178 % | 0.274038 s | 0.562283 s |
| rl | 87.602 % | sin pares | sin pares |
| rr | 87.552 % | sin pares | sin pares |

## Comparación crudo frente a filtrado

- Coincidencia simultánea cruda: 20.328 %.
- Coincidencia simultánea filtrada: 13.434 %.

| Pata | Coincidencia cruda | Coincidencia filtrada |
|---|---:|---:|
| fl | 61.907 % | 60.270 % |
| fr | 62.626 % | 61.178 % |
| rl | 89.295 % | 87.602 % |
| rr | 89.174 % | 87.552 % |

| Pata | Transición | Retardo crudo medio | Retardo filtrado medio |
|---|---|---:|---:|
| fl | liftoff | 0.133580 s | 0.258131 s |
| fl | landing | 0.506156 s | 0.538989 s |
| fr | liftoff | 0.135440 s | 0.274038 s |
| fr | landing | 0.498593 s | 0.562283 s |
| rl | liftoff | 0.140015 s | sin pares |
| rl | landing | -0.322592 s | sin pares |
| rr | liftoff | 0.140508 s | sin pares |
| rr | landing | -0.322982 s | sin pares |

Persistencia cruda exigida para declarar vuelo filtrado: 0.120 s.

| Pata | Episodios acotados | Duración media | Duración máxima | Episodios que superan el umbral |
|---|---:|---:|---:|---:|
| fl | 106 | 0.950775 s | 1.789181 s | 106 |
| fr | 105 | 0.934697 s | 1.014626 s | 104 |
| rl | 53 | 0.078300 s | 0.159530 s | 1 |
| rr | 53 | 0.079921 s | 0.284148 s | 1 |

Un retardo positivo indica que la transición medida ocurrió después de la prevista; uno negativo indica que ocurrió antes. Los pares se buscan dentro de ±1,8 s. Los porcentajes están ponderados por tiempo, no por número de mensajes.

El análisis es descriptivo y no activa decisiones del supervisor.
