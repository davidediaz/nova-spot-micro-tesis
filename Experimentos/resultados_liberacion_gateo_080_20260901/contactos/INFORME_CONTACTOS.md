# Análisis de contactos medidos durante gateo

- Bolsa: `Experimentos/rosbag2/liberacion_gateo_080_20260901`.
- Ventana gateo--stand: 79.444903 s.
- Ciclos completos según `/nova/gait_phase`: 18.
- Índices de ciclo completos: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17].
- Estados comprimidos analizados: 516.
- Coincidencia simultánea filtrada de las cuatro patas: 13.458 %.

## Resultado por pata

| Pata | Coincidencia | Retardo despegue medio | Retardo aterrizaje medio |
|---|---:|---:|---:|
| fl | 60.288 % | 0.261209 s | 0.537379 s |
| fr | 61.392 % | 0.258482 s | 0.544129 s |
| rl | 87.758 % | sin pares | sin pares |
| rr | 87.476 % | sin pares | sin pares |

## Comparación crudo frente a filtrado

- Coincidencia simultánea cruda: 20.380 %.
- Coincidencia simultánea filtrada: 13.458 %.

| Pata | Coincidencia cruda | Coincidencia filtrada |
|---|---:|---:|
| fl | 61.880 % | 60.288 % |
| fr | 62.757 % | 61.392 % |
| rl | 89.678 % | 87.758 % |
| rr | 89.563 % | 87.476 % |

| Pata | Transición | Retardo crudo medio | Retardo filtrado medio |
|---|---|---:|---:|
| fl | liftoff | 0.137710 s | 0.261209 s |
| fl | landing | 0.503815 s | 0.537379 s |
| fr | liftoff | 0.135022 s | 0.258482 s |
| fr | landing | 0.511076 s | 0.544129 s |
| rl | liftoff | 0.139677 s | sin pares |
| rl | landing | -0.315875 s | sin pares |
| rr | liftoff | 0.139495 s | sin pares |
| rr | landing | -0.312950 s | sin pares |

Persistencia cruda exigida para declarar vuelo filtrado: 0.120 s.

| Pata | Episodios acotados | Duración media | Duración máxima | Episodios que superan el umbral |
|---|---:|---:|---:|---:|
| fl | 38 | 0.926716 s | 0.995735 s | 38 |
| fr | 37 | 0.930930 s | 1.001150 s | 37 |
| rl | 18 | 0.084762 s | 0.092354 s | 0 |
| rr | 19 | 0.087241 s | 0.110865 s | 0 |

Un retardo positivo indica que la transición medida ocurrió después de la prevista; uno negativo indica que ocurrió antes. Los pares se buscan dentro de ±1,8 s. Los porcentajes están ponderados por tiempo, no por número de mensajes.

El análisis es descriptivo y no activa decisiones del supervisor.
