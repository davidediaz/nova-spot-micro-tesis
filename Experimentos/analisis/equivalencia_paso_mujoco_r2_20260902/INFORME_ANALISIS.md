# Análisis automático de marcha paso

- Bolsa: `Experimentos/rosbag2/equivalencia_paso_mujoco_r2_20260902`.
- Ventana marcha paso--stand: 68.072372399 s.
- Duración nominal configurada por ciclo: 5.76 s.
- Duración observada media por ciclo: 5.760009 s.
- Ciclos completos analizados: 11.
- Activaciones verdaderas del supervisor: 0.

## Estadísticos entre ciclos

| Métrica | Media | Desv. estándar | Mínimo | Máximo |
|---|---:|---:|---:|---:|
| Avance por ciclo (m) | 0.000870 | 0.000951 | -0.001997 | 0.001160 |
| Velocidad media (m/s) | 0.000151 | 0.000165 | -0.000347 | 0.000201 |
| Excursión lateral (m) | 0.003489 | 0.000398 | 0.002290 | 0.003611 |
| Altura media (m) | 0.220887 | 0.000001 | 0.220886 | 0.220889 |
| Roll máximo absoluto (grados) | 0.624951 | 0.000004 | 0.624949 | 0.624960 |
| Pitch máximo absoluto (grados) | 1.738556 | 0.000141 | 1.738131 | 1.738609 |
| Salto articular máximo (rad) | 0.007864 | 0.000081 | 0.007742 | 0.007967 |

## Resultado

Los 11 ciclos completos acumularon 0.009575 m de avance medido entre la primera y última muestra de cada ciclo. 
No se cambiaron paso, elevación ni duración de muestra durante la ventana.

La continuidad articular se expresa como el mayor salto absoluto entre dos muestras consecutivas de una misma articulación. La velocidad articular máxima se obtiene del campo medido `joint_velocities_rad_s`.

Archivos generados:

- `metricas_por_ciclo.csv`
- `series_temporales.png`
- `resumen_por_ciclo.png`
- `INFORME_ANALISIS.md`
