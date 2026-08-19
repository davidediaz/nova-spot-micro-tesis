# Análisis de contactos medidos durante gateo

- Bolsa: `Experimentos/rosbag2/contactos_gateo_validado_20260814_1410`.
- Ventana gateo--stand: 329.856750 s.
- Ciclos completos según `/nova/gait_phase`: 76.
- Índices de ciclo completos: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75].
- Estados comprimidos analizados: 610.
- Coincidencia simultánea de las cuatro patas: 32.550 %.

## Resultado por pata

| Pata | Coincidencia | Retardo despegue medio | Retardo aterrizaje medio |
|---|---:|---:|---:|
| fl | 59.671 % | 0.380297 s | 1.364317 s |
| fr | 59.788 % | 0.381066 s | 1.364194 s |
| rl | 75.121 % | sin pares | sin pares |
| rr | 74.972 % | sin pares | sin pares |

Un retardo positivo indica que la transición medida ocurrió después de la prevista; uno negativo indica que ocurrió antes. Los pares se buscan dentro de ±1,8 s. Los porcentajes están ponderados por tiempo, no por número de mensajes.

El análisis es descriptivo y no activa decisiones del supervisor.
