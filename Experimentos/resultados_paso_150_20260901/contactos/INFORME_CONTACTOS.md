# Análisis de contactos medidos durante marcha paso

- Bolsa: `Experimentos/rosbag2/velocidad_paso_150_20260901`.
- Ventana paso--stand: 101.203233 s.
- Ciclos completos según `/nova/gait_phase`: 26.
- Índices de ciclo completos: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25].
- Estados comprimidos analizados: 322.
- Coincidencia simultánea filtrada de las cuatro patas: 29.110 %.

## Resultado por pata

| Pata | Coincidencia | Retardo despegue medio | Retardo aterrizaje medio |
|---|---:|---:|---:|
| fl | 58.828 % | 0.407699 s | 1.140415 s |
| fr | 59.313 % | 0.404715 s | 1.178967 s |
| rl | 75.332 % | sin pares | sin pares |
| rr | 74.964 % | sin pares | sin pares |

## Comparación crudo frente a filtrado

- Coincidencia simultánea cruda: 35.527 %.
- Coincidencia simultánea filtrada: 29.110 %.

| Pata | Coincidencia cruda | Coincidencia filtrada |
|---|---:|---:|
| fl | 62.860 % | 58.828 % |
| fr | 63.319 % | 59.313 % |
| rl | 75.332 % | 75.332 % |
| rr | 74.964 % | 74.964 % |

| Pata | Transición | Retardo crudo medio | Retardo filtrado medio |
|---|---|---:|---:|
| fl | liftoff | 0.283438 s | 0.407699 s |
| fl | landing | 1.107570 s | 1.140415 s |
| fr | liftoff | 0.282555 s | 0.404715 s |
| fr | landing | 1.145204 s | 1.178967 s |
| rl | liftoff | sin pares | sin pares |
| rl | landing | sin pares | sin pares |
| rr | liftoff | sin pares | sin pares |
| rr | landing | sin pares | sin pares |

Persistencia cruda exigida para declarar vuelo filtrado: 0.120 s.

| Pata | Episodios acotados | Duración media | Duración máxima | Episodios que superan el umbral |
|---|---:|---:|---:|---:|
| fl | 28 | 1.687815 s | 1.833425 s | 27 |
| fr | 26 | 1.822871 s | 1.849483 s | 26 |
| rl | 0 | sin episodios | sin episodios | 0 |
| rr | 0 | sin episodios | sin episodios | 0 |

Un retardo positivo indica que la transición medida ocurrió después de la prevista; uno negativo indica que ocurrió antes. Los pares se buscan dentro de ±1,8 s. Los porcentajes están ponderados por tiempo, no por número de mensajes.

El análisis es descriptivo y no activa decisiones del supervisor.
