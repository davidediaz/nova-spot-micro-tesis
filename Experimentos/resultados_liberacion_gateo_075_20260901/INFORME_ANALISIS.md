# Análisis automático de gateo

- Bolsa: `Experimentos/rosbag2/liberacion_gateo_075_20260901`.
- Ventana gateo--stand: 79.199089862 s.
- Duración nominal configurada por ciclo: 4.32 s.
- Duración observada media por ciclo: 4.319997 s.
- Ciclos completos analizados: 18.
- Activaciones verdaderas del supervisor: 0.

## Estadísticos entre ciclos

| Métrica | Media | Desv. estándar | Mínimo | Máximo |
|---|---:|---:|---:|---:|
| Avance por ciclo (m) | 0.023685 | 0.001141 | 0.019443 | 0.025033 |
| Velocidad media (m/s) | 0.005483 | 0.000264 | 0.004501 | 0.005794 |
| Excursión lateral (m) | 0.005766 | 0.000229 | 0.005540 | 0.006555 |
| Altura media (m) | 0.224168 | 0.000031 | 0.224044 | 0.224178 |
| Roll máximo absoluto (grados) | 2.087504 | 0.003562 | 2.074079 | 2.090537 |
| Pitch máximo absoluto (grados) | 4.131782 | 0.004070 | 4.119911 | 4.135741 |
| Salto articular máximo (rad) | 0.019653 | 0.000040 | 0.019541 | 0.019752 |

## Resultado

Los 18 ciclos completos acumularon 0.426325 m de avance medido entre la primera y última muestra de cada ciclo. 
No se cambiaron paso, elevación ni duración de muestra durante la ventana.

La continuidad articular se expresa como el mayor salto absoluto entre dos muestras consecutivas de una misma articulación. La velocidad articular máxima se obtiene del campo medido `joint_velocities_rad_s`.

Archivos generados:

- `metricas_por_ciclo.csv`
- `series_temporales.png`
- `resumen_por_ciclo.png`
- `INFORME_ANALISIS.md`
