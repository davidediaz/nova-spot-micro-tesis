# Análisis automático de marcha paso

- Bolsa: `Experimentos/campanas_mujoco/paso_5x20_aislada_r2_20260903/rosbag2/paso_r2`.
- Ventana marcha paso--stand: 122.281352914 s.
- Duración nominal configurada por ciclo: 5.76 s.
- Duración observada media por ciclo: 5.759383 s.
- Ciclos completos analizados: 21.
- Activaciones verdaderas del supervisor: 0.

## Estadísticos entre ciclos

| Métrica | Media | Desv. estándar | Mínimo | Máximo |
|---|---:|---:|---:|---:|
| Avance por ciclo (m) | -0.009228 | 0.042749 | -0.106961 | 0.063068 |
| Velocidad media (m/s) | -0.001601 | 0.007425 | -0.018571 | 0.010950 |
| Excursión lateral (m) | 0.003400 | 0.000700 | 0.002179 | 0.004153 |
| Altura media (m) | 0.221401 | 0.000015 | 0.221368 | 0.221426 |
| Roll máximo absoluto (grados) | 0.646914 | 0.000736 | 0.645122 | 0.648055 |
| Pitch máximo absoluto (grados) | 1.788930 | 0.001745 | 1.785118 | 1.792422 |
| Salto articular máximo (rad) | 0.102885 | 0.000089 | 0.102734 | 0.103067 |

## Resultado

Los 21 ciclos completos acumularon -0.193785 m de avance medido entre la primera y última muestra de cada ciclo. 
No se cambiaron paso, elevación ni duración de muestra durante la ventana.

La continuidad articular se expresa como el mayor salto absoluto entre dos muestras consecutivas de una misma articulación. La velocidad articular máxima se obtiene del campo medido `joint_velocities_rad_s`.

Archivos generados:

- `metricas_por_ciclo.csv`
- `series_temporales.png`
- `resumen_por_ciclo.png`
- `INFORME_ANALISIS.md`
