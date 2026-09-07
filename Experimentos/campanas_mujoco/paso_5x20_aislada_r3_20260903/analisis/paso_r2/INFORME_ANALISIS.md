# Análisis automático de marcha paso

- Bolsa: `Experimentos/campanas_mujoco/paso_5x20_aislada_r3_20260903/rosbag2/paso_r2`.
- Ventana marcha paso--stand: 121.439017666 s.
- Duración nominal configurada por ciclo: 5.76 s.
- Duración observada media por ciclo: 5.759999 s.
- Ciclos completos analizados: 21.
- Activaciones verdaderas del supervisor: 0.

## Estadísticos entre ciclos

| Métrica | Media | Desv. estándar | Mínimo | Máximo |
|---|---:|---:|---:|---:|
| Avance por ciclo (m) | 0.002668 | 0.000160 | 0.001970 | 0.002713 |
| Velocidad media (m/s) | 0.000463 | 0.000028 | 0.000342 | 0.000471 |
| Excursión lateral (m) | 0.003763 | 0.000352 | 0.002226 | 0.003851 |
| Altura media (m) | 0.220825 | 0.000009 | 0.220814 | 0.220850 |
| Roll máximo absoluto (grados) | 0.646333 | 0.000074 | 0.646184 | 0.646454 |
| Pitch máximo absoluto (grados) | 1.787253 | 0.000194 | 1.786867 | 1.787511 |
| Salto articular máximo (rad) | 0.010900 | 0.001188 | 0.009031 | 0.012560 |

## Resultado

Los 21 ciclos completos acumularon 0.056023 m de avance medido entre la primera y última muestra de cada ciclo. 
No se cambiaron paso, elevación ni duración de muestra durante la ventana.

La continuidad articular se expresa como el mayor salto absoluto entre dos muestras consecutivas de una misma articulación. La velocidad articular máxima se obtiene del campo medido `joint_velocities_rad_s`.

Archivos generados:

- `metricas_por_ciclo.csv`
- `series_temporales.png`
- `resumen_por_ciclo.png`
- `INFORME_ANALISIS.md`
