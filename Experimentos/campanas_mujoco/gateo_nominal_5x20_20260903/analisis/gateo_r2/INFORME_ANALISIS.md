# Análisis automático de gateo

- Bolsa: `Experimentos/campanas_mujoco/gateo_nominal_5x20_20260903/rosbag2/gateo_r2`.
- Ventana gateo--stand: 92.482363374 s.
- Duración nominal configurada por ciclo: 4.32 s.
- Duración observada media por ciclo: 4.320002 s.
- Ciclos completos analizados: 21.
- Activaciones verdaderas del supervisor: 0.

## Estadísticos entre ciclos

| Métrica | Media | Desv. estándar | Mínimo | Máximo |
|---|---:|---:|---:|---:|
| Avance por ciclo (m) | 0.006285 | 0.000100 | 0.005881 | 0.006374 |
| Velocidad media (m/s) | 0.001455 | 0.000023 | 0.001361 | 0.001475 |
| Excursión lateral (m) | 0.003139 | 0.000061 | 0.002883 | 0.003183 |
| Altura media (m) | 0.220965 | 0.000010 | 0.220947 | 0.220985 |
| Roll máximo absoluto (grados) | 1.535596 | 0.000253 | 1.535224 | 1.535972 |
| Pitch máximo absoluto (grados) | 3.605197 | 0.001204 | 3.603362 | 3.607264 |
| Salto articular máximo (rad) | 0.027933 | 0.002038 | 0.022027 | 0.030636 |

## Resultado

Los 21 ciclos completos acumularon 0.131977 m de avance medido entre la primera y última muestra de cada ciclo. 
No se cambiaron paso, elevación ni duración de muestra durante la ventana.

La continuidad articular se expresa como el mayor salto absoluto entre dos muestras consecutivas de una misma articulación. La velocidad articular máxima se obtiene del campo medido `joint_velocities_rad_s`.

Archivos generados:

- `metricas_por_ciclo.csv`
- `series_temporales.png`
- `resumen_por_ciclo.png`
- `INFORME_ANALISIS.md`
