# Análisis automático de marcha paso

- Bolsa: `Experimentos/campanas_mujoco/perturbacion_empuje_paso_2N_20260903/rosbag2/paso_r1`.
- Ventana marcha paso--stand: 31.979430142 s.
- Duración nominal configurada por ciclo: 5.76 s.
- Duración observada media por ciclo: 5.760030 s.
- Ciclos completos analizados: 5.
- Activaciones verdaderas del supervisor: 0.

## Estadísticos entre ciclos

| Métrica | Media | Desv. estándar | Mínimo | Máximo |
|---|---:|---:|---:|---:|
| Avance por ciclo (m) | 0.011954 | 0.002964 | 0.009804 | 0.016182 |
| Velocidad media (m/s) | 0.002075 | 0.000515 | 0.001702 | 0.002809 |
| Excursión lateral (m) | 0.004782 | 0.000706 | 0.003525 | 0.005148 |
| Altura media (m) | 0.222101 | 0.000004 | 0.222095 | 0.222105 |
| Roll máximo absoluto (grados) | 1.510939 | 0.000036 | 1.510890 | 1.510979 |
| Pitch máximo absoluto (grados) | 3.171345 | 0.000040 | 3.171316 | 3.171411 |
| Salto articular máximo (rad) | 0.017282 | 0.000405 | 0.016868 | 0.017951 |

## Resultado

Los 5 ciclos completos acumularon 0.059771 m de avance medido entre la primera y última muestra de cada ciclo. 
No se cambiaron paso, elevación ni duración de muestra durante la ventana.

La continuidad articular se expresa como el mayor salto absoluto entre dos muestras consecutivas de una misma articulación. La velocidad articular máxima se obtiene del campo medido `joint_velocities_rad_s`.

Archivos generados:

- `metricas_por_ciclo.csv`
- `series_temporales.png`
- `resumen_por_ciclo.png`
- `INFORME_ANALISIS.md`
