# Análisis automático de marcha paso

- Bolsa: `Experimentos/campanas_mujoco/barrido_altura_paso_20260903/height_016/rosbag2/paso_r1`.
- Ventana marcha paso--stand: 29.469712661 s.
- Duración nominal configurada por ciclo: 5.76 s.
- Duración observada media por ciclo: 5.760055 s.
- Ciclos completos analizados: 5.
- Activaciones verdaderas del supervisor: 0.

## Estadísticos entre ciclos

| Métrica | Media | Desv. estándar | Mínimo | Máximo |
|---|---:|---:|---:|---:|
| Avance por ciclo (m) | 0.008531 | 0.002912 | 0.007213 | 0.013740 |
| Velocidad media (m/s) | 0.001481 | 0.000506 | 0.001252 | 0.002385 |
| Excursión lateral (m) | 0.004626 | 0.000271 | 0.004141 | 0.004757 |
| Altura media (m) | 0.220485 | 0.000003 | 0.220481 | 0.220488 |
| Roll máximo absoluto (grados) | 1.805026 | 0.000088 | 1.804936 | 1.805151 |
| Pitch máximo absoluto (grados) | 4.088097 | 0.000094 | 4.087974 | 4.088216 |
| Salto articular máximo (rad) | 0.023057 | 0.001236 | 0.021445 | 0.024290 |

## Resultado

Los 5 ciclos completos acumularon 0.042654 m de avance medido entre la primera y última muestra de cada ciclo. 
No se cambiaron paso, elevación ni duración de muestra durante la ventana.

La continuidad articular se expresa como el mayor salto absoluto entre dos muestras consecutivas de una misma articulación. La velocidad articular máxima se obtiene del campo medido `joint_velocities_rad_s`.

Archivos generados:

- `metricas_por_ciclo.csv`
- `series_temporales.png`
- `resumen_por_ciclo.png`
- `INFORME_ANALISIS.md`
