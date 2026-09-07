# Análisis automático de marcha paso

- Bolsa: `Experimentos/campanas_mujoco/paso_ajustado_5x20_20260903/rosbag2/paso_r5`.
- Ventana marcha paso--stand: 121.967521938 s.
- Duración nominal configurada por ciclo: 5.76 s.
- Duración observada media por ciclo: 5.760006 s.
- Ciclos completos analizados: 21.
- Activaciones verdaderas del supervisor: 0.

## Estadísticos entre ciclos

| Métrica | Media | Desv. estándar | Mínimo | Máximo |
|---|---:|---:|---:|---:|
| Avance por ciclo (m) | 0.010167 | 0.001396 | 0.009769 | 0.016256 |
| Velocidad media (m/s) | 0.001765 | 0.000242 | 0.001696 | 0.002822 |
| Excursión lateral (m) | 0.004937 | 0.000326 | 0.003518 | 0.005054 |
| Altura media (m) | 0.222101 | 0.000004 | 0.222093 | 0.222106 |
| Roll máximo absoluto (grados) | 1.510946 | 0.000045 | 1.510796 | 1.511002 |
| Pitch máximo absoluto (grados) | 3.171328 | 0.000025 | 3.171265 | 3.171377 |
| Salto articular máximo (rad) | 0.017196 | 0.002004 | 0.013149 | 0.020423 |

## Resultado

Los 21 ciclos completos acumularon 0.213499 m de avance medido entre la primera y última muestra de cada ciclo. 
No se cambiaron paso, elevación ni duración de muestra durante la ventana.

La continuidad articular se expresa como el mayor salto absoluto entre dos muestras consecutivas de una misma articulación. La velocidad articular máxima se obtiene del campo medido `joint_velocities_rad_s`.

Archivos generados:

- `metricas_por_ciclo.csv`
- `series_temporales.png`
- `resumen_por_ciclo.png`
- `INFORME_ANALISIS.md`
