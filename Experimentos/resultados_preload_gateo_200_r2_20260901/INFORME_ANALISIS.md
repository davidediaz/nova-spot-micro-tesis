# Análisis automático de gateo

- Bolsa: `Experimentos/rosbag2/preload_gateo_200_r2_20260901`.
- Ventana gateo--stand: 79.218224902 s.
- Duración nominal configurada por ciclo: 4.32 s.
- Duración observada media por ciclo: 4.320014 s.
- Ciclos completos analizados: 18.
- Activaciones verdaderas del supervisor: 0.

## Estadísticos entre ciclos

| Métrica | Media | Desv. estándar | Mínimo | Máximo |
|---|---:|---:|---:|---:|
| Avance por ciclo (m) | 0.021639 | 0.000851 | 0.018481 | 0.022392 |
| Velocidad media (m/s) | 0.005009 | 0.000197 | 0.004278 | 0.005183 |
| Excursión lateral (m) | 0.008824 | 0.000223 | 0.008644 | 0.009620 |
| Altura media (m) | 0.224213 | 0.000026 | 0.224109 | 0.224221 |
| Roll máximo absoluto (grados) | 2.153787 | 0.004354 | 2.145127 | 2.159750 |
| Pitch máximo absoluto (grados) | 4.261194 | 0.007990 | 4.249156 | 4.273553 |
| Salto articular máximo (rad) | 0.019684 | 0.000043 | 0.019656 | 0.019833 |

## Resultado

Los 18 ciclos completos acumularon 0.389496 m de avance medido entre la primera y última muestra de cada ciclo. 
No se cambiaron paso, elevación ni duración de muestra durante la ventana.

La continuidad articular se expresa como el mayor salto absoluto entre dos muestras consecutivas de una misma articulación. La velocidad articular máxima se obtiene del campo medido `joint_velocities_rad_s`.

Archivos generados:

- `metricas_por_ciclo.csv`
- `series_temporales.png`
- `resumen_por_ciclo.png`
- `INFORME_ANALISIS.md`
