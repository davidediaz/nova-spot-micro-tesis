# Análisis de contactos medidos durante gateo

- Bolsa: `Experimentos/rosbag2/contactos_gateo_valido_20260814_1350`.
- Ventana gateo--stand: 63.356320 s.
- Ciclos completos según `/nova/gait_phase`: 14.
- Índices de ciclo completos: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13].
- Estados comprimidos analizados: 30.
- Coincidencia simultánea de las cuatro patas: 0.000 %.

## Resultado por pata

| Pata | Coincidencia | Retardo despegue medio | Retardo aterrizaje medio |
|---|---:|---:|---:|
| fl | 48.614 % | sin pares | sin pares |
| fr | 51.386 % | sin pares | sin pares |
| rl | 100.000 % | sin pares | sin pares |
| rr | 100.000 % | sin pares | sin pares |

Un retardo positivo indica que la transición medida ocurrió después de la prevista; uno negativo indica que ocurrió antes. Los pares se buscan dentro de ±0,8 s. Los porcentajes están ponderados por tiempo, no por número de mensajes.

El análisis es descriptivo y no activa decisiones del supervisor.
