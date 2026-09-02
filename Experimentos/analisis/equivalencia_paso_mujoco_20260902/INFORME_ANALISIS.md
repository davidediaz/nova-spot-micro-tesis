# Análisis automático de marcha paso

- Bolsa: `Experimentos/rosbag2/equivalencia_paso_mujoco_20260902`.
- Ventana marcha paso--stand: 73.034777518 s.
- Duración nominal configurada por ciclo: 5.76 s.
- Duración observada media por ciclo: 5.759994 s.
- Ciclos completos analizados: 12.
- Activaciones verdaderas del supervisor: 0.

## Estadísticos entre ciclos

| Métrica | Media | Desv. estándar | Mínimo | Máximo |
|---|---:|---:|---:|---:|
| Avance por ciclo (m) | 0.000001 | 0.000000 | 0.000001 | 0.000001 |
| Velocidad media (m/s) | 0.000000 | 0.000000 | 0.000000 | 0.000000 |
| Excursión lateral (m) | 0.000012 | 0.000001 | 0.000007 | 0.000012 |
| Altura media (m) | 0.037405 | 0.000000 | 0.037405 | 0.037405 |
| Roll máximo absoluto (grados) | 180.000000 | 0.000000 | 180.000000 | 180.000000 |
| Pitch máximo absoluto (grados) | 0.004406 | 0.000022 | 0.004336 | 0.004422 |
| Salto articular máximo (rad) | 0.008094 | 0.000315 | 0.007862 | 0.009085 |

## Resultado

Los 12 ciclos completos acumularon 0.000012 m de avance medido entre la primera y última muestra de cada ciclo. 
No se cambiaron paso, elevación ni duración de muestra durante la ventana.

La continuidad articular se expresa como el mayor salto absoluto entre dos muestras consecutivas de una misma articulación. La velocidad articular máxima se obtiene del campo medido `joint_velocities_rad_s`.

Archivos generados:

- `metricas_por_ciclo.csv`
- `series_temporales.png`
- `resumen_por_ciclo.png`
- `INFORME_ANALISIS.md`
