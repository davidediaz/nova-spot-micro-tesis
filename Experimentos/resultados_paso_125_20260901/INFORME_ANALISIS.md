# Análisis automático de marcha paso

- Bolsa: `Experimentos/rosbag2/velocidad_paso_125_20260901`.
- Ventana marcha paso--stand: 119.195429501 s.
- Duración nominal configurada por ciclo: 4.61 s.
- Duración observada media por ciclo: 4.607986 s.
- Ciclos completos analizados: 25.
- Activaciones verdaderas del supervisor: 0.

## Estadísticos entre ciclos

| Métrica | Media | Desv. estándar | Mínimo | Máximo |
|---|---:|---:|---:|---:|
| Avance por ciclo (m) | 0.021302 | 0.001704 | 0.013481 | 0.022427 |
| Velocidad media (m/s) | 0.004623 | 0.000367 | 0.002931 | 0.004854 |
| Excursión lateral (m) | 0.005329 | 0.000417 | 0.005112 | 0.007301 |
| Altura media (m) | 0.224109 | 0.000051 | 0.223862 | 0.224123 |
| Roll máximo absoluto (grados) | 1.259694 | 0.006325 | 1.231139 | 1.263139 |
| Pitch máximo absoluto (grados) | 2.456898 | 0.011588 | 2.447221 | 2.507069 |
| Salto articular máximo (rad) | 0.009755 | 0.000260 | 0.009582 | 0.010966 |

## Resultado

Los 25 ciclos completos acumularon 0.532555 m de avance medido entre la primera y última muestra de cada ciclo. 
No se cambiaron paso, elevación ni duración de muestra durante la ventana.

La continuidad articular se expresa como el mayor salto absoluto entre dos muestras consecutivas de una misma articulación. La velocidad articular máxima se obtiene del campo medido `joint_velocities_rad_s`.

Archivos generados:

- `metricas_por_ciclo.csv`
- `series_temporales.png`
- `resumen_por_ciclo.png`
- `INFORME_ANALISIS.md`
