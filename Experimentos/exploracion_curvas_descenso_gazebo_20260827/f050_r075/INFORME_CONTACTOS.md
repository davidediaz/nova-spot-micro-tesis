# Análisis de contactos medidos durante gateo

- Bolsa: `Experimentos/rosbag2/curva_descenso_f050_r075_20260827`.
- Ventana gateo--stand: 47.679699 s.
- Ciclos completos según `/nova/gait_phase`: 11.
- Índices de ciclo completos: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10].
- Estados comprimidos analizados: 213.
- Coincidencia simultánea de las cuatro patas: 21.728 %.

## Resultado por pata

| Pata | Coincidencia | Retardo despegue medio | Retardo aterrizaje medio |
|---|---:|---:|---:|
| fl | 63.354 % | 0.133251 s | 0.474507 s |
| fr | 62.748 % | 0.132274 s | 0.498197 s |
| rl | 89.305 % | 0.137653 s | -0.325862 s |
| rr | 89.277 % | 0.137636 s | -0.327101 s |

Un retardo positivo indica que la transición medida ocurrió después de la prevista; uno negativo indica que ocurrió antes. Los pares se buscan dentro de ±1,8 s. Los porcentajes están ponderados por tiempo, no por número de mensajes.

El análisis es descriptivo y no activa decisiones del supervisor.
