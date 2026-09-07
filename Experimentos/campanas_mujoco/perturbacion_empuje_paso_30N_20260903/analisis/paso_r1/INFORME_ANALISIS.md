# Análisis automático de marcha paso

- Bolsa: `Experimentos/campanas_mujoco/perturbacion_empuje_paso_30N_20260903/rosbag2/paso_r1`.
- Ventana marcha paso--stand: 29.434536859 s.
- Duración nominal configurada por ciclo: 5.76 s.
- Duración observada media por ciclo: 5.760059 s.
- Ciclos completos analizados: 5.
- Activaciones verdaderas del supervisor: 0.

## Estadísticos entre ciclos

| Métrica | Media | Desv. estándar | Mínimo | Máximo |
|---|---:|---:|---:|---:|
| Avance por ciclo (m) | 0.012034 | 0.003083 | 0.009850 | 0.016418 |
| Velocidad media (m/s) | 0.002089 | 0.000535 | 0.001710 | 0.002850 |
| Excursión lateral (m) | 0.004752 | 0.000667 | 0.003561 | 0.005103 |
| Altura media (m) | 0.222102 | 0.000005 | 0.222096 | 0.222106 |
| Roll máximo absoluto (grados) | 1.510914 | 0.000033 | 1.510876 | 1.510964 |
| Pitch máximo absoluto (grados) | 3.171315 | 0.000018 | 3.171301 | 3.171345 |
| Salto articular máximo (rad) | 0.017932 | 0.000825 | 0.017305 | 0.019311 |

## Resultado

Los 5 ciclos completos acumularon 0.060168 m de avance medido entre la primera y última muestra de cada ciclo. 
No se cambiaron paso, elevación ni duración de muestra durante la ventana.

La continuidad articular se expresa como el mayor salto absoluto entre dos muestras consecutivas de una misma articulación. La velocidad articular máxima se obtiene del campo medido `joint_velocities_rad_s`.

Archivos generados:

- `metricas_por_ciclo.csv`
- `series_temporales.png`
- `resumen_por_ciclo.png`
- `INFORME_ANALISIS.md`
