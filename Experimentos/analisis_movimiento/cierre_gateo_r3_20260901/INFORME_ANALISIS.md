# Análisis automático de gateo

- Bolsa: `Experimentos/rosbag2/cierre_gateo_r3_20260901`.
- Ventana gateo--stand: 220.731954961 s.
- Duración nominal configurada por ciclo: 4.32 s.
- Duración observada media por ciclo: 4.319977 s.
- Ciclos completos analizados: 50.
- Activaciones verdaderas del supervisor: 0.

## Estadísticos entre ciclos

| Métrica | Media | Desv. estándar | Mínimo | Máximo |
|---|---:|---:|---:|---:|
| Avance por ciclo (m) | 0.023899 | 0.000760 | 0.019233 | 0.024875 |
| Velocidad media (m/s) | 0.005532 | 0.000176 | 0.004453 | 0.005758 |
| Excursión lateral (m) | 0.005681 | 0.000166 | 0.005471 | 0.006591 |
| Altura media (m) | 0.224176 | 0.000018 | 0.224048 | 0.224181 |
| Roll máximo absoluto (grados) | 2.072785 | 0.002579 | 2.060555 | 2.074621 |
| Pitch máximo absoluto (grados) | 4.096269 | 0.002430 | 4.086089 | 4.101861 |
| Salto articular máximo (rad) | 0.019630 | 0.000019 | 0.019612 | 0.019688 |

## Resultado

Los 50 ciclos completos acumularon 1.194965 m de avance medido entre la primera y última muestra de cada ciclo. 
No se cambiaron paso, elevación ni duración de muestra durante la ventana.

La continuidad articular se expresa como el mayor salto absoluto entre dos muestras consecutivas de una misma articulación. La velocidad articular máxima se obtiene del campo medido `joint_velocities_rad_s`.

Archivos generados:

- `metricas_por_ciclo.csv`
- `series_temporales.png`
- `resumen_por_ciclo.png`
- `INFORME_ANALISIS.md`
