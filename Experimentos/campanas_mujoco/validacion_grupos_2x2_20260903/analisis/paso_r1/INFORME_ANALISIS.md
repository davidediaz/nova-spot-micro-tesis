# Análisis automático de marcha paso

- Bolsa: `Experimentos/campanas_mujoco/validacion_grupos_2x2_20260903/rosbag2/paso_r1`.
- Ventana marcha paso--stand: 17.930697507 s.
- Duración nominal configurada por ciclo: 5.76 s.
- Duración observada media por ciclo: 5.759993 s.
- Ciclos completos analizados: 3.
- Activaciones verdaderas del supervisor: 0.

## Estadísticos entre ciclos

| Métrica | Media | Desv. estándar | Mínimo | Máximo |
|---|---:|---:|---:|---:|
| Avance por ciclo (m) | 0.002471 | 0.000403 | 0.002005 | 0.002705 |
| Velocidad media (m/s) | 0.000429 | 0.000070 | 0.000348 | 0.000470 |
| Excursión lateral (m) | 0.003297 | 0.000943 | 0.002208 | 0.003842 |
| Altura media (m) | 0.220826 | 0.000002 | 0.220824 | 0.220829 |
| Roll máximo absoluto (grados) | 0.646286 | 0.000053 | 0.646253 | 0.646348 |
| Pitch máximo absoluto (grados) | 1.787327 | 0.000172 | 1.787129 | 1.787438 |
| Salto articular máximo (rad) | 0.010772 | 0.001542 | 0.009857 | 0.012552 |

## Resultado

Los 3 ciclos completos acumularon 0.007412 m de avance medido entre la primera y última muestra de cada ciclo. 
No se cambiaron paso, elevación ni duración de muestra durante la ventana.

La continuidad articular se expresa como el mayor salto absoluto entre dos muestras consecutivas de una misma articulación. La velocidad articular máxima se obtiene del campo medido `joint_velocities_rad_s`.

Archivos generados:

- `metricas_por_ciclo.csv`
- `series_temporales.png`
- `resumen_por_ciclo.png`
- `INFORME_ANALISIS.md`
