# Análisis de contactos medidos durante gateo

- Bolsa: `Experimentos/rosbag2/curva_descenso_nominal_20260827`.
- Ventana gateo--stand: 56.439321 s.
- Ciclos completos según `/nova/gait_phase`: 13.
- Índices de ciclo completos: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12].
- Estados comprimidos analizados: 253.
- Coincidencia simultánea de las cuatro patas: 20.949 %.

## Resultado por pata

| Pata | Coincidencia | Retardo despegue medio | Retardo aterrizaje medio |
|---|---:|---:|---:|
| fl | 62.954 % | 0.136826 s | 0.497227 s |
| fr | 62.474 % | 0.137179 s | 0.512263 s |
| rl | 89.333 % | 0.139378 s | -0.323550 s |
| rr | 89.262 % | 0.141574 s | -0.324463 s |

Un retardo positivo indica que la transición medida ocurrió después de la prevista; uno negativo indica que ocurrió antes. Los pares se buscan dentro de ±1,8 s. Los porcentajes están ponderados por tiempo, no por número de mensajes.

El análisis es descriptivo y no activa decisiones del supervisor.
