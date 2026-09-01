# Análisis automático de gateo

- Bolsa: `Experimentos/rosbag2/liberacion_gateo_080_altura125_r3_20260901`.
- Ventana gateo--stand: 79.153863687 s.
- Duración nominal configurada por ciclo: 4.32 s.
- Duración observada media por ciclo: 4.319999 s.
- Ciclos completos analizados: 18.
- Activaciones verdaderas del supervisor: 0.

## Estadísticos entre ciclos

| Métrica | Media | Desv. estándar | Mínimo | Máximo |
|---|---:|---:|---:|---:|
| Avance por ciclo (m) | 0.022662 | 0.001779 | 0.016380 | 0.024527 |
| Velocidad media (m/s) | 0.005246 | 0.000412 | 0.003792 | 0.005678 |
| Excursión lateral (m) | 0.008455 | 0.000263 | 0.007749 | 0.009119 |
| Altura media (m) | 0.224093 | 0.000033 | 0.223960 | 0.224103 |
| Roll máximo absoluto (grados) | 2.627563 | 0.002801 | 2.619479 | 2.633044 |
| Pitch máximo absoluto (grados) | 5.216466 | 0.002563 | 5.211881 | 5.219823 |
| Salto articular máximo (rad) | 0.025376 | 0.000113 | 0.025207 | 0.025475 |

## Resultado

Los 18 ciclos completos acumularon 0.407921 m de avance medido entre la primera y última muestra de cada ciclo. 
No se cambiaron paso, elevación ni duración de muestra durante la ventana.

La continuidad articular se expresa como el mayor salto absoluto entre dos muestras consecutivas de una misma articulación. La velocidad articular máxima se obtiene del campo medido `joint_velocities_rad_s`.

Archivos generados:

- `metricas_por_ciclo.csv`
- `series_temporales.png`
- `resumen_por_ciclo.png`
- `INFORME_ANALISIS.md`
