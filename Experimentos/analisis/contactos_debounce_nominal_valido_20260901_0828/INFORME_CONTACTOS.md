# Análisis de contactos medidos durante gateo

- Bolsa: `Experimentos/rosbag2/contactos_debounce_nominal_valido_20260901_0828`.
- Ventana gateo--stand: 105.522328 s.
- Ciclos completos según `/nova/gait_phase`: 24.
- Índices de ciclo completos: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23].
- Estados comprimidos analizados: 679.
- Coincidencia simultánea filtrada de las cuatro patas: 13.621 %.

## Resultado por pata

| Pata | Coincidencia | Retardo despegue medio | Retardo aterrizaje medio |
|---|---:|---:|---:|
| fl | 60.747 % | 0.258905 s | 0.535164 s |
| fr | 61.290 % | 0.258326 s | 0.546356 s |
| rl | 87.717 % | sin pares | sin pares |
| rr | 87.339 % | sin pares | sin pares |

## Comparación crudo frente a filtrado

- Coincidencia simultánea cruda: 20.639 %.
- Coincidencia simultánea filtrada: 13.621 %.

| Pata | Coincidencia cruda | Coincidencia filtrada |
|---|---:|---:|
| fl | 62.304 % | 60.747 % |
| fr | 62.731 % | 61.290 % |
| rl | 89.414 % | 87.717 % |
| rr | 89.088 % | 87.339 % |

| Pata | Transición | Retardo crudo medio | Retardo filtrado medio |
|---|---|---:|---:|
| fl | liftoff | 0.134708 s | 0.258905 s |
| fl | landing | 0.501924 s | 0.535164 s |
| fr | liftoff | 0.134015 s | 0.258326 s |
| fr | landing | 0.513175 s | 0.546356 s |
| rl | liftoff | 0.139133 s | sin pares |
| rl | landing | -0.326257 s | sin pares |
| rr | liftoff | 0.139656 s | sin pares |
| rr | landing | -0.244079 s | sin pares |

Persistencia cruda exigida para declarar vuelo filtrado: 0.120 s.

| Pata | Episodios acotados | Duración media | Duración máxima | Episodios que superan el umbral |
|---|---:|---:|---:|---:|
| fl | 49 | 0.944766 s | 0.999304 s | 49 |
| fr | 49 | 0.935656 s | 0.994892 s | 48 |
| rl | 24 | 0.074645 s | 0.089805 s | 0 |
| rr | 25 | 0.073803 s | 0.089396 s | 0 |

Un retardo positivo indica que la transición medida ocurrió después de la prevista; uno negativo indica que ocurrió antes. Los pares se buscan dentro de ±1,8 s. Los porcentajes están ponderados por tiempo, no por número de mensajes.

El análisis es descriptivo y no activa decisiones del supervisor.
