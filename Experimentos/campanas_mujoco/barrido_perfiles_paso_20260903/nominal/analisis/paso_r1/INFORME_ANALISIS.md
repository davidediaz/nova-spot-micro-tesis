# Análisis automático de marcha paso

- Bolsa: `Experimentos/campanas_mujoco/barrido_perfiles_paso_20260903/nominal/rosbag2/paso_r1`.
- Ventana marcha paso--stand: 29.448568788 s.
- Duración nominal configurada por ciclo: 5.76 s.
- Duración observada media por ciclo: 5.760072 s.
- Ciclos completos analizados: 5.
- Activaciones verdaderas del supervisor: 0.

## Estadísticos entre ciclos

| Métrica | Media | Desv. estándar | Mínimo | Máximo |
|---|---:|---:|---:|---:|
| Avance por ciclo (m) | -0.001345 | 0.000064 | -0.001457 | -0.001300 |
| Velocidad media (m/s) | -0.000233 | 0.000011 | -0.000253 | -0.000226 |
| Excursión lateral (m) | 0.004790 | 0.000122 | 0.004573 | 0.004870 |
| Altura media (m) | 0.135082 | 0.000073 | 0.135031 | 0.135208 |
| Roll máximo absoluto (grados) | 2.668890 | 0.000060 | 2.668825 | 2.668960 |
| Pitch máximo absoluto (grados) | 35.702134 | 0.000261 | 35.701901 | 35.702429 |
| Salto articular máximo (rad) | 0.017655 | 0.001911 | 0.016012 | 0.020700 |

## Resultado

Los 5 ciclos completos acumularon -0.006723 m de avance medido entre la primera y última muestra de cada ciclo. 
No se cambiaron paso, elevación ni duración de muestra durante la ventana.

La continuidad articular se expresa como el mayor salto absoluto entre dos muestras consecutivas de una misma articulación. La velocidad articular máxima se obtiene del campo medido `joint_velocities_rad_s`.

Archivos generados:

- `metricas_por_ciclo.csv`
- `series_temporales.png`
- `resumen_por_ciclo.png`
- `INFORME_ANALISIS.md`
