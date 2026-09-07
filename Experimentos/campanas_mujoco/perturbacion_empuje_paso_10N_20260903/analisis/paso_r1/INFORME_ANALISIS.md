# Análisis automático de marcha paso

- Bolsa: `Experimentos/campanas_mujoco/perturbacion_empuje_paso_10N_20260903/rosbag2/paso_r1`.
- Ventana marcha paso--stand: 29.455891238 s.
- Duración nominal configurada por ciclo: 5.76 s.
- Duración observada media por ciclo: 5.760034 s.
- Ciclos completos analizados: 5.
- Activaciones verdaderas del supervisor: 0.

## Estadísticos entre ciclos

| Métrica | Media | Desv. estándar | Mínimo | Máximo |
|---|---:|---:|---:|---:|
| Avance por ciclo (m) | 0.011462 | 0.002811 | 0.009824 | 0.016350 |
| Velocidad media (m/s) | 0.001990 | 0.000488 | 0.001706 | 0.002838 |
| Excursión lateral (m) | 0.004729 | 0.000654 | 0.003558 | 0.005035 |
| Altura media (m) | 0.222099 | 0.000004 | 0.222094 | 0.222103 |
| Roll máximo absoluto (grados) | 1.510950 | 0.000028 | 1.510915 | 1.510976 |
| Pitch máximo absoluto (grados) | 3.171324 | 0.000012 | 3.171307 | 3.171337 |
| Salto articular máximo (rad) | 0.016466 | 0.001253 | 0.014722 | 0.018227 |

## Resultado

Los 5 ciclos completos acumularon 0.057309 m de avance medido entre la primera y última muestra de cada ciclo. 
No se cambiaron paso, elevación ni duración de muestra durante la ventana.

La continuidad articular se expresa como el mayor salto absoluto entre dos muestras consecutivas de una misma articulación. La velocidad articular máxima se obtiene del campo medido `joint_velocities_rad_s`.

Archivos generados:

- `metricas_por_ciclo.csv`
- `series_temporales.png`
- `resumen_por_ciclo.png`
- `INFORME_ANALISIS.md`
