# Análisis automático de gateo

- Bolsa: `Experimentos/rosbag2/cierre_gateo_r6_20260901`.
- Ventana gateo--stand: 158.385185280 s.
- Duración nominal configurada por ciclo: 4.32 s.
- Duración observada media por ciclo: 4.320000 s.
- Ciclos completos analizados: 36.
- Activaciones verdaderas del supervisor: 0.

## Estadísticos entre ciclos

| Métrica | Media | Desv. estándar | Mínimo | Máximo |
|---|---:|---:|---:|---:|
| Avance por ciclo (m) | 0.023850 | 0.000823 | 0.019658 | 0.024644 |
| Velocidad media (m/s) | 0.005521 | 0.000190 | 0.004551 | 0.005705 |
| Excursión lateral (m) | 0.005691 | 0.000165 | 0.005526 | 0.006495 |
| Altura media (m) | 0.224174 | 0.000026 | 0.224024 | 0.224181 |
| Roll máximo absoluto (grados) | 2.072494 | 0.002129 | 2.063698 | 2.075014 |
| Pitch máximo absoluto (grados) | 4.095909 | 0.001727 | 4.092652 | 4.102441 |
| Salto articular máximo (rad) | 0.019584 | 0.000139 | 0.019130 | 0.019631 |

## Resultado

Los 36 ciclos completos acumularon 0.858603 m de avance medido entre la primera y última muestra de cada ciclo. 
No se cambiaron paso, elevación ni duración de muestra durante la ventana.

La continuidad articular se expresa como el mayor salto absoluto entre dos muestras consecutivas de una misma articulación. La velocidad articular máxima se obtiene del campo medido `joint_velocities_rad_s`.

Archivos generados:

- `metricas_por_ciclo.csv`
- `series_temporales.png`
- `resumen_por_ciclo.png`
- `INFORME_ANALISIS.md`
