# Análisis automático de gateo

- Bolsa: `Experimentos/campanas_mujoco/gateo_nominal_5x20_20260903/rosbag2/gateo_r3`.
- Ventana gateo--stand: 92.529869847 s.
- Duración nominal configurada por ciclo: 4.32 s.
- Duración observada media por ciclo: 4.320000 s.
- Ciclos completos analizados: 21.
- Activaciones verdaderas del supervisor: 0.

## Estadísticos entre ciclos

| Métrica | Media | Desv. estándar | Mínimo | Máximo |
|---|---:|---:|---:|---:|
| Avance por ciclo (m) | 0.006290 | 0.000077 | 0.005977 | 0.006375 |
| Velocidad media (m/s) | 0.001456 | 0.000018 | 0.001384 | 0.001476 |
| Excursión lateral (m) | 0.003141 | 0.000035 | 0.003002 | 0.003182 |
| Altura media (m) | 0.220964 | 0.000012 | 0.220935 | 0.220982 |
| Roll máximo absoluto (grados) | 1.535562 | 0.000288 | 1.535076 | 1.536107 |
| Pitch máximo absoluto (grados) | 3.605311 | 0.001398 | 3.603043 | 3.608306 |
| Salto articular máximo (rad) | 0.028008 | 0.002020 | 0.022506 | 0.030180 |

## Resultado

Los 21 ciclos completos acumularon 0.132098 m de avance medido entre la primera y última muestra de cada ciclo. 
No se cambiaron paso, elevación ni duración de muestra durante la ventana.

La continuidad articular se expresa como el mayor salto absoluto entre dos muestras consecutivas de una misma articulación. La velocidad articular máxima se obtiene del campo medido `joint_velocities_rad_s`.

Archivos generados:

- `metricas_por_ciclo.csv`
- `series_temporales.png`
- `resumen_por_ciclo.png`
- `INFORME_ANALISIS.md`
