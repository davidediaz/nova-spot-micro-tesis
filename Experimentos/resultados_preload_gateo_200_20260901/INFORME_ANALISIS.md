# Análisis automático de gateo

- Bolsa: `Experimentos/rosbag2/preload_gateo_200_20260901`.
- Ventana gateo--stand: 79.149822027 s.
- Duración nominal configurada por ciclo: 4.32 s.
- Duración observada media por ciclo: 4.320007 s.
- Ciclos completos analizados: 18.
- Activaciones verdaderas del supervisor: 0.

## Estadísticos entre ciclos

| Métrica | Media | Desv. estándar | Mínimo | Máximo |
|---|---:|---:|---:|---:|
| Avance por ciclo (m) | 0.021662 | 0.001127 | 0.017286 | 0.022473 |
| Velocidad media (m/s) | 0.005014 | 0.000261 | 0.004001 | 0.005202 |
| Excursión lateral (m) | 0.008810 | 0.000164 | 0.008655 | 0.009368 |
| Altura media (m) | 0.224212 | 0.000028 | 0.224101 | 0.224222 |
| Roll máximo absoluto (grados) | 2.156779 | 0.006092 | 2.149583 | 2.176877 |
| Pitch máximo absoluto (grados) | 4.261714 | 0.011071 | 4.245135 | 4.296749 |
| Salto articular máximo (rad) | 0.019679 | 0.000017 | 0.019659 | 0.019728 |

## Resultado

Los 18 ciclos completos acumularon 0.389910 m de avance medido entre la primera y última muestra de cada ciclo. 
No se cambiaron paso, elevación ni duración de muestra durante la ventana.

La continuidad articular se expresa como el mayor salto absoluto entre dos muestras consecutivas de una misma articulación. La velocidad articular máxima se obtiene del campo medido `joint_velocities_rad_s`.

Archivos generados:

- `metricas_por_ciclo.csv`
- `series_temporales.png`
- `resumen_por_ciclo.png`
- `INFORME_ANALISIS.md`
