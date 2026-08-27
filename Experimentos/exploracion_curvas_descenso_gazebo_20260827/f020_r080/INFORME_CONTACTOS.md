# Análisis de contactos medidos durante gateo

- Bolsa: `Experimentos/rosbag2/curva_descenso_f020_r080_20260827`.
- Ventana gateo--stand: 47.066173 s.
- Ciclos completos según `/nova/gait_phase`: 10.
- Índices de ciclo completos: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9].
- Estados comprimidos analizados: 217.
- Coincidencia simultánea de las cuatro patas: 23.721 %.

## Resultado por pata

| Pata | Coincidencia | Retardo despegue medio | Retardo aterrizaje medio |
|---|---:|---:|---:|
| fl | 63.293 % | 0.137465 s | 0.445507 s |
| fr | 64.787 % | 0.136060 s | 0.459791 s |
| rl | 89.703 % | 0.141181 s | -0.324589 s |
| rr | 89.090 % | 0.141263 s | -0.325523 s |

Un retardo positivo indica que la transición medida ocurrió después de la prevista; uno negativo indica que ocurrió antes. Los pares se buscan dentro de ±1,8 s. Los porcentajes están ponderados por tiempo, no por número de mensajes.

El análisis es descriptivo y no activa decisiones del supervisor.
