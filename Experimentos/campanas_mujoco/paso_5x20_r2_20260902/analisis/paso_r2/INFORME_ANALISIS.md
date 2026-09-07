# Análisis automático de marcha paso

- Bolsa: `Experimentos/campanas_mujoco/paso_5x20_r2_20260902/rosbag2/paso_r2`.
- Ventana marcha paso--stand: 121.149912337 s.
- Duración nominal configurada por ciclo: 5.76 s.
- Duración observada media por ciclo: 5.759995 s.
- Ciclos completos analizados: 21.
- Activaciones verdaderas del supervisor: 0.

## Estadísticos entre ciclos

| Métrica | Media | Desv. estándar | Mínimo | Máximo |
|---|---:|---:|---:|---:|
| Avance por ciclo (m) | -0.023702 | 0.041519 | -0.054812 | 0.058104 |
| Velocidad media (m/s) | -0.004115 | 0.007208 | -0.009516 | 0.010088 |
| Excursión lateral (m) | 0.004905 | 0.000960 | 0.003134 | 0.006147 |
| Altura media (m) | 0.220829 | 0.000008 | 0.220812 | 0.220846 |
| Roll máximo absoluto (grados) | 0.646439 | 0.000358 | 0.646227 | 0.647581 |
| Pitch máximo absoluto (grados) | 1.787560 | 0.000691 | 1.786860 | 1.790200 |
| Salto articular máximo (rad) | 0.021892 | 0.007047 | 0.008307 | 0.033277 |

## Resultado

Los 21 ciclos completos acumularon -0.497739 m de avance medido entre la primera y última muestra de cada ciclo. 
No se cambiaron paso, elevación ni duración de muestra durante la ventana.

La continuidad articular se expresa como el mayor salto absoluto entre dos muestras consecutivas de una misma articulación. La velocidad articular máxima se obtiene del campo medido `joint_velocities_rad_s`.

Archivos generados:

- `metricas_por_ciclo.csv`
- `series_temporales.png`
- `resumen_por_ciclo.png`
- `INFORME_ANALISIS.md`
