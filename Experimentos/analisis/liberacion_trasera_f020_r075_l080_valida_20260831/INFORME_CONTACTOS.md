# Análisis de contactos medidos durante gateo

- Bolsa: `Experimentos/rosbag2/liberacion_trasera_f020_r075_l080_valida_20260831`.
- Ventana gateo--stand: 65.633846 s.
- Ciclos completos según `/nova/gait_phase`: 15.
- Índices de ciclo completos: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14].
- Estados comprimidos analizados: 292.
- Coincidencia simultánea de las cuatro patas: 23.644 %.

## Resultado por pata

| Pata | Coincidencia | Retardo despegue medio | Retardo aterrizaje medio |
|---|---:|---:|---:|
| fl | 64.010 % | 0.136447 s | 0.444341 s |
| fr | 63.872 % | 0.134717 s | 0.457778 s |
| rl | 89.861 % | 0.138183 s | -0.305102 s |
| rr | 89.868 % | 0.134114 s | -0.309170 s |

Un retardo positivo indica que la transición medida ocurrió después de la prevista; uno negativo indica que ocurrió antes. Los pares se buscan dentro de ±1,8 s. Los porcentajes están ponderados por tiempo, no por número de mensajes.

El análisis es descriptivo y no activa decisiones del supervisor.
