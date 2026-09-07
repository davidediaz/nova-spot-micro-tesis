# Análisis automático de gateo

- Bolsa: `Experimentos/campanas_mujoco/gateo_nominal_5x20_20260903/rosbag2/gateo_r1`.
- Ventana gateo--stand: 92.767632763 s.
- Duración nominal configurada por ciclo: 4.32 s.
- Duración observada media por ciclo: 4.320000 s.
- Ciclos completos analizados: 21.
- Activaciones verdaderas del supervisor: 0.

## Estadísticos entre ciclos

| Métrica | Media | Desv. estándar | Mínimo | Máximo |
|---|---:|---:|---:|---:|
| Avance por ciclo (m) | 0.006297 | 0.000087 | 0.005945 | 0.006373 |
| Velocidad media (m/s) | 0.001458 | 0.000020 | 0.001376 | 0.001475 |
| Excursión lateral (m) | 0.003143 | 0.000048 | 0.002941 | 0.003175 |
| Altura media (m) | 0.220965 | 0.000010 | 0.220945 | 0.220988 |
| Roll máximo absoluto (grados) | 1.535694 | 0.000310 | 1.535183 | 1.536185 |
| Pitch máximo absoluto (grados) | 3.605539 | 0.001455 | 3.602663 | 3.607596 |
| Salto articular máximo (rad) | 0.027894 | 0.002523 | 0.022669 | 0.031321 |

## Resultado

Los 21 ciclos completos acumularon 0.132234 m de avance medido entre la primera y última muestra de cada ciclo. 
No se cambiaron paso, elevación ni duración de muestra durante la ventana.

La continuidad articular se expresa como el mayor salto absoluto entre dos muestras consecutivas de una misma articulación. La velocidad articular máxima se obtiene del campo medido `joint_velocities_rad_s`.

Archivos generados:

- `metricas_por_ciclo.csv`
- `series_temporales.png`
- `resumen_por_ciclo.png`
- `INFORME_ANALISIS.md`
