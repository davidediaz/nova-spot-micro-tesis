# Análisis automático de gateo

- Bolsa: `Experimentos/rosbag2/velocidad_gateo_150_20260901`.
- Ventana gateo--stand: 83.199698316 s.
- Duración nominal configurada por ciclo: 2.88 s.
- Duración observada media por ciclo: 2.880002 s.
- Ciclos completos analizados: 28.
- Activaciones verdaderas del supervisor: 0.

## Estadísticos entre ciclos

| Métrica | Media | Desv. estándar | Mínimo | Máximo |
|---|---:|---:|---:|---:|
| Avance por ciclo (m) | 0.022174 | 0.003236 | 0.005965 | 0.024479 |
| Velocidad media (m/s) | 0.007699 | 0.001124 | 0.002071 | 0.008500 |
| Excursión lateral (m) | 0.005729 | 0.000144 | 0.005499 | 0.006119 |
| Altura media (m) | 0.224112 | 0.000011 | 0.224076 | 0.224131 |
| Roll máximo absoluto (grados) | 1.830374 | 0.015919 | 1.806335 | 1.868418 |
| Pitch máximo absoluto (grados) | 3.771698 | 0.013336 | 3.751046 | 3.803884 |
| Salto articular máximo (rad) | 0.023257 | 0.000227 | 0.022288 | 0.023447 |

## Resultado

Los 28 ciclos completos acumularon 0.620882 m de avance medido entre la primera y última muestra de cada ciclo. 
No se cambiaron paso, elevación ni duración de muestra durante la ventana.

La continuidad articular se expresa como el mayor salto absoluto entre dos muestras consecutivas de una misma articulación. La velocidad articular máxima se obtiene del campo medido `joint_velocities_rad_s`.

Archivos generados:

- `metricas_por_ciclo.csv`
- `series_temporales.png`
- `resumen_por_ciclo.png`
- `INFORME_ANALISIS.md`
