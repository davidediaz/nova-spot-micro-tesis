# Análisis automático de gateo

- Bolsa: `Experimentos/campanas_mujoco/gateo_nominal_5x20_20260903/rosbag2/gateo_r4`.
- Ventana gateo--stand: 95.024202143 s.
- Duración nominal configurada por ciclo: 4.32 s.
- Duración observada media por ciclo: 4.320009 s.
- Ciclos completos analizados: 21.
- Activaciones verdaderas del supervisor: 0.

## Estadísticos entre ciclos

| Métrica | Media | Desv. estándar | Mínimo | Máximo |
|---|---:|---:|---:|---:|
| Avance por ciclo (m) | 0.006281 | 0.000137 | 0.005700 | 0.006358 |
| Velocidad media (m/s) | 0.001454 | 0.000032 | 0.001319 | 0.001472 |
| Excursión lateral (m) | 0.003139 | 0.000054 | 0.002909 | 0.003168 |
| Altura media (m) | 0.220962 | 0.000012 | 0.220927 | 0.220979 |
| Roll máximo absoluto (grados) | 1.535645 | 0.000196 | 1.535248 | 1.535975 |
| Pitch máximo absoluto (grados) | 3.605412 | 0.000827 | 3.603850 | 3.606667 |
| Salto articular máximo (rad) | 0.028134 | 0.002868 | 0.023063 | 0.033844 |

## Resultado

Los 21 ciclos completos acumularon 0.131910 m de avance medido entre la primera y última muestra de cada ciclo. 
No se cambiaron paso, elevación ni duración de muestra durante la ventana.

La continuidad articular se expresa como el mayor salto absoluto entre dos muestras consecutivas de una misma articulación. La velocidad articular máxima se obtiene del campo medido `joint_velocities_rad_s`.

Archivos generados:

- `metricas_por_ciclo.csv`
- `series_temporales.png`
- `resumen_por_ciclo.png`
- `INFORME_ANALISIS.md`
