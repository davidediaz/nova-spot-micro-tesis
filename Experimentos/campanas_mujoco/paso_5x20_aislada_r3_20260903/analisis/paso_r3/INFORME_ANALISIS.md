# Análisis automático de marcha paso

- Bolsa: `Experimentos/campanas_mujoco/paso_5x20_aislada_r3_20260903/rosbag2/paso_r3`.
- Ventana marcha paso--stand: 121.975640067 s.
- Duración nominal configurada por ciclo: 5.76 s.
- Duración observada media por ciclo: 5.759997 s.
- Ciclos completos analizados: 21.
- Activaciones verdaderas del supervisor: 0.

## Estadísticos entre ciclos

| Métrica | Media | Desv. estándar | Mínimo | Máximo |
|---|---:|---:|---:|---:|
| Avance por ciclo (m) | 0.002667 | 0.000158 | 0.001977 | 0.002706 |
| Velocidad media (m/s) | 0.000463 | 0.000027 | 0.000343 | 0.000470 |
| Excursión lateral (m) | 0.003763 | 0.000354 | 0.002218 | 0.003845 |
| Altura media (m) | 0.220827 | 0.000008 | 0.220809 | 0.220840 |
| Roll máximo absoluto (grados) | 0.646326 | 0.000062 | 0.646210 | 0.646458 |
| Pitch máximo absoluto (grados) | 1.787268 | 0.000224 | 1.786953 | 1.787636 |
| Salto articular máximo (rad) | 0.010886 | 0.001292 | 0.008498 | 0.013251 |

## Resultado

Los 21 ciclos completos acumularon 0.056010 m de avance medido entre la primera y última muestra de cada ciclo. 
No se cambiaron paso, elevación ni duración de muestra durante la ventana.

La continuidad articular se expresa como el mayor salto absoluto entre dos muestras consecutivas de una misma articulación. La velocidad articular máxima se obtiene del campo medido `joint_velocities_rad_s`.

Archivos generados:

- `metricas_por_ciclo.csv`
- `series_temporales.png`
- `resumen_por_ciclo.png`
- `INFORME_ANALISIS.md`
