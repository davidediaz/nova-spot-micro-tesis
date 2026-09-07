# Análisis automático de marcha paso

- Bolsa: `Experimentos/campanas_mujoco/barrido_transferencia_paso_20260903/shift_012/rosbag2/paso_r1`.
- Ventana marcha paso--stand: 29.765948285 s.
- Duración nominal configurada por ciclo: 5.76 s.
- Duración observada media por ciclo: 5.760140 s.
- Ciclos completos analizados: 5.
- Activaciones verdaderas del supervisor: 0.

## Estadísticos entre ciclos

| Métrica | Media | Desv. estándar | Mínimo | Máximo |
|---|---:|---:|---:|---:|
| Avance por ciclo (m) | 0.004763 | 0.002362 | 0.003702 | 0.008988 |
| Velocidad media (m/s) | 0.000827 | 0.000410 | 0.000643 | 0.001560 |
| Excursión lateral (m) | 0.003907 | 0.000716 | 0.002626 | 0.004231 |
| Altura media (m) | 0.220933 | 0.000008 | 0.220920 | 0.220941 |
| Roll máximo absoluto (grados) | 0.650803 | 0.000104 | 0.650694 | 0.650963 |
| Pitch máximo absoluto (grados) | 1.544142 | 0.000168 | 1.543989 | 1.544338 |
| Salto articular máximo (rad) | 0.010886 | 0.001823 | 0.007721 | 0.012356 |

## Resultado

Los 5 ciclos completos acumularon 0.023815 m de avance medido entre la primera y última muestra de cada ciclo. 
No se cambiaron paso, elevación ni duración de muestra durante la ventana.

La continuidad articular se expresa como el mayor salto absoluto entre dos muestras consecutivas de una misma articulación. La velocidad articular máxima se obtiene del campo medido `joint_velocities_rad_s`.

Archivos generados:

- `metricas_por_ciclo.csv`
- `series_temporales.png`
- `resumen_por_ciclo.png`
- `INFORME_ANALISIS.md`
