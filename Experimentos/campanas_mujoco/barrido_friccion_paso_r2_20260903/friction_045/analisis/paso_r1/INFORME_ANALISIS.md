# Análisis automático de marcha paso

- Bolsa: `Experimentos/campanas_mujoco/barrido_friccion_paso_r2_20260903/friction_045/rosbag2/paso_r1`.
- Ventana marcha paso--stand: 29.441028347 s.
- Duración nominal configurada por ciclo: 5.76 s.
- Duración observada media por ciclo: 5.760081 s.
- Ciclos completos analizados: 5.
- Activaciones verdaderas del supervisor: 0.

## Estadísticos entre ciclos

| Métrica | Media | Desv. estándar | Mínimo | Máximo |
|---|---:|---:|---:|---:|
| Avance por ciclo (m) | 0.008522 | 0.003002 | 0.007174 | 0.013893 |
| Velocidad media (m/s) | 0.001479 | 0.000521 | 0.001245 | 0.002412 |
| Excursión lateral (m) | 0.003462 | 0.000491 | 0.002584 | 0.003691 |
| Altura media (m) | 0.220629 | 0.000004 | 0.220625 | 0.220634 |
| Roll máximo absoluto (grados) | 1.107981 | 0.000035 | 1.107937 | 1.108011 |
| Pitch máximo absoluto (grados) | 2.580909 | 0.000201 | 2.580684 | 2.581166 |
| Salto articular máximo (rad) | 0.017511 | 0.001246 | 0.015721 | 0.018856 |

## Resultado

Los 5 ciclos completos acumularon 0.042609 m de avance medido entre la primera y última muestra de cada ciclo. 
No se cambiaron paso, elevación ni duración de muestra durante la ventana.

La continuidad articular se expresa como el mayor salto absoluto entre dos muestras consecutivas de una misma articulación. La velocidad articular máxima se obtiene del campo medido `joint_velocities_rad_s`.

Archivos generados:

- `metricas_por_ciclo.csv`
- `series_temporales.png`
- `resumen_por_ciclo.png`
- `INFORME_ANALISIS.md`
