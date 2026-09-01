# Análisis automático de gateo

- Bolsa: `Experimentos/rosbag2/cierre_gateo_r1_20260901`.
- Ventana gateo--stand: 126.025835947 s.
- Duración nominal configurada por ciclo: 4.32 s.
- Duración observada media por ciclo: 4.319985 s.
- Ciclos completos analizados: 29.
- Activaciones verdaderas del supervisor: 0.

## Estadísticos entre ciclos

| Métrica | Media | Desv. estándar | Mínimo | Máximo |
|---|---:|---:|---:|---:|
| Avance por ciclo (m) | 0.023658 | 0.001619 | 0.015528 | 0.024934 |
| Velocidad media (m/s) | 0.005476 | 0.000375 | 0.003595 | 0.005772 |
| Excursión lateral (m) | 0.005659 | 0.000232 | 0.004620 | 0.005972 |
| Altura media (m) | 0.224169 | 0.000047 | 0.223923 | 0.224181 |
| Roll máximo absoluto (grados) | 2.072463 | 0.003501 | 2.058707 | 2.074400 |
| Pitch máximo absoluto (grados) | 4.096528 | 0.004000 | 4.084262 | 4.103068 |
| Salto articular máximo (rad) | 0.019621 | 0.000098 | 0.019130 | 0.019688 |

## Resultado

Los 29 ciclos completos acumularon 0.686089 m de avance medido entre la primera y última muestra de cada ciclo. 
No se cambiaron paso, elevación ni duración de muestra durante la ventana.

La continuidad articular se expresa como el mayor salto absoluto entre dos muestras consecutivas de una misma articulación. La velocidad articular máxima se obtiene del campo medido `joint_velocities_rad_s`.

Archivos generados:

- `metricas_por_ciclo.csv`
- `series_temporales.png`
- `resumen_por_ciclo.png`
- `INFORME_ANALISIS.md`
