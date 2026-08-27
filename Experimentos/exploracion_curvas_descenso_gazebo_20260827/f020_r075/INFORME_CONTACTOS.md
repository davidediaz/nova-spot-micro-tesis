# Análisis de contactos medidos durante gateo

- Bolsa: `Experimentos/rosbag2/curva_descenso_f020_r075_robusta_20260827`.
- Ventana gateo--stand: 47.093324 s.
- Ciclos completos según `/nova/gait_phase`: 10.
- Índices de ciclo completos: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9].
- Estados comprimidos analizados: 218.
- Coincidencia simultánea de las cuatro patas: 23.855 %.

## Resultado por pata

| Pata | Coincidencia | Retardo despegue medio | Retardo aterrizaje medio |
|---|---:|---:|---:|
| fl | 63.544 % | 0.139431 s | 0.436068 s |
| fr | 64.768 % | 0.135283 s | 0.460010 s |
| rl | 89.617 % | 0.142308 s | -0.326231 s |
| rr | 89.150 % | 0.143420 s | -0.321033 s |

Un retardo positivo indica que la transición medida ocurrió después de la prevista; uno negativo indica que ocurrió antes. Los pares se buscan dentro de ±1,8 s. Los porcentajes están ponderados por tiempo, no por número de mensajes.

El análisis es descriptivo y no activa decisiones del supervisor.
