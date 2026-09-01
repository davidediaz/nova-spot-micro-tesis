# Análisis automático de gateo

- Bolsa: `Experimentos/rosbag2/cierre_gateo_r4_20260901`.
- Ventana gateo--stand: 226.207641513 s.
- Duración nominal configurada por ciclo: 4.32 s.
- Duración observada media por ciclo: 4.320382 s.
- Ciclos completos analizados: 52.
- Activaciones verdaderas del supervisor: 0.

## Estadísticos entre ciclos

| Métrica | Media | Desv. estándar | Mínimo | Máximo |
|---|---:|---:|---:|---:|
| Avance por ciclo (m) | 0.023834 | 0.001068 | 0.020326 | 0.026030 |
| Velocidad media (m/s) | 0.005516 | 0.000242 | 0.004700 | 0.005998 |
| Excursión lateral (m) | 0.005729 | 0.000289 | 0.005224 | 0.006944 |
| Altura media (m) | 0.224176 | 0.000019 | 0.224048 | 0.224187 |
| Roll máximo absoluto (grados) | 2.079294 | 0.017460 | 2.043962 | 2.113055 |
| Pitch máximo absoluto (grados) | 4.111040 | 0.036446 | 4.040909 | 4.173451 |
| Salto articular máximo (rad) | 0.019624 | 0.000118 | 0.019130 | 0.019787 |

## Resultado

Los 52 ciclos completos acumularon 1.239358 m de avance medido entre la primera y última muestra de cada ciclo. 
No se cambiaron paso, elevación ni duración de muestra durante la ventana.

La continuidad articular se expresa como el mayor salto absoluto entre dos muestras consecutivas de una misma articulación. La velocidad articular máxima se obtiene del campo medido `joint_velocities_rad_s`.

Archivos generados:

- `metricas_por_ciclo.csv`
- `series_temporales.png`
- `resumen_por_ciclo.png`
- `INFORME_ANALISIS.md`
