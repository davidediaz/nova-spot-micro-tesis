# Análisis automático de marcha paso

- Bolsa: `Experimentos/campanas_mujoco/barrido_transferencia_paso_20260903/shift_015/rosbag2/paso_r1`.
- Ventana marcha paso--stand: 29.756879566 s.
- Duración nominal configurada por ciclo: 5.76 s.
- Duración observada media por ciclo: 5.760044 s.
- Ciclos completos analizados: 5.
- Activaciones verdaderas del supervisor: 0.

## Estadísticos entre ciclos

| Métrica | Media | Desv. estándar | Mínimo | Máximo |
|---|---:|---:|---:|---:|
| Avance por ciclo (m) | 0.005484 | 0.003047 | 0.004114 | 0.010934 |
| Velocidad media (m/s) | 0.000952 | 0.000529 | 0.000714 | 0.001898 |
| Excursión lateral (m) | 0.003993 | 0.000708 | 0.002726 | 0.004313 |
| Altura media (m) | 0.220954 | 0.000003 | 0.220950 | 0.220957 |
| Roll máximo absoluto (grados) | 0.652064 | 0.000028 | 0.652025 | 0.652103 |
| Pitch máximo absoluto (grados) | 1.490726 | 0.000106 | 1.490601 | 1.490840 |
| Salto articular máximo (rad) | 0.011309 | 0.000982 | 0.010663 | 0.013008 |

## Resultado

Los 5 ciclos completos acumularon 0.027420 m de avance medido entre la primera y última muestra de cada ciclo. 
No se cambiaron paso, elevación ni duración de muestra durante la ventana.

La continuidad articular se expresa como el mayor salto absoluto entre dos muestras consecutivas de una misma articulación. La velocidad articular máxima se obtiene del campo medido `joint_velocities_rad_s`.

Archivos generados:

- `metricas_por_ciclo.csv`
- `series_temporales.png`
- `resumen_por_ciclo.png`
- `INFORME_ANALISIS.md`
