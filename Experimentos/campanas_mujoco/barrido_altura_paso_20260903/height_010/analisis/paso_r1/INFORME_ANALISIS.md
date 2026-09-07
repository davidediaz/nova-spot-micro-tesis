# Análisis automático de marcha paso

- Bolsa: `Experimentos/campanas_mujoco/barrido_altura_paso_20260903/height_010/rosbag2/paso_r1`.
- Ventana marcha paso--stand: 29.658021080 s.
- Duración nominal configurada por ciclo: 5.76 s.
- Duración observada media por ciclo: 5.760162 s.
- Ciclos completos analizados: 5.
- Activaciones verdaderas del supervisor: 0.

## Estadísticos entre ciclos

| Métrica | Media | Desv. estándar | Mínimo | Máximo |
|---|---:|---:|---:|---:|
| Avance por ciclo (m) | 0.008099 | 0.003001 | 0.006753 | 0.013467 |
| Velocidad media (m/s) | 0.001406 | 0.000521 | 0.001172 | 0.002338 |
| Excursión lateral (m) | 0.003598 | 0.000586 | 0.002550 | 0.003866 |
| Altura media (m) | 0.220743 | 0.000003 | 0.220739 | 0.220747 |
| Roll máximo absoluto (grados) | 0.781651 | 0.000089 | 0.781523 | 0.781753 |
| Pitch máximo absoluto (grados) | 1.877460 | 0.000273 | 1.877087 | 1.877714 |
| Salto articular máximo (rad) | 0.014266 | 0.001089 | 0.012703 | 0.015667 |

## Resultado

Los 5 ciclos completos acumularon 0.040495 m de avance medido entre la primera y última muestra de cada ciclo. 
No se cambiaron paso, elevación ni duración de muestra durante la ventana.

La continuidad articular se expresa como el mayor salto absoluto entre dos muestras consecutivas de una misma articulación. La velocidad articular máxima se obtiene del campo medido `joint_velocities_rad_s`.

Archivos generados:

- `metricas_por_ciclo.csv`
- `series_temporales.png`
- `resumen_por_ciclo.png`
- `INFORME_ANALISIS.md`
