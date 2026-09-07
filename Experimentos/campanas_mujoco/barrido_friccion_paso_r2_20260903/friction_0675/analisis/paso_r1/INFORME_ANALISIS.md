# Análisis automático de marcha paso

- Bolsa: `Experimentos/campanas_mujoco/barrido_friccion_paso_r2_20260903/friction_0675/rosbag2/paso_r1`.
- Ventana marcha paso--stand: 29.736689191 s.
- Duración nominal configurada por ciclo: 5.76 s.
- Duración observada media por ciclo: 5.760488 s.
- Ciclos completos analizados: 5.
- Activaciones verdaderas del supervisor: 0.

## Estadísticos entre ciclos

| Métrica | Media | Desv. estándar | Mínimo | Máximo |
|---|---:|---:|---:|---:|
| Avance por ciclo (m) | 0.008530 | 0.002999 | 0.007181 | 0.013894 |
| Velocidad media (m/s) | 0.001481 | 0.000521 | 0.001247 | 0.002412 |
| Excursión lateral (m) | 0.003467 | 0.000491 | 0.002588 | 0.003692 |
| Altura media (m) | 0.220627 | 0.000006 | 0.220616 | 0.220631 |
| Roll máximo absoluto (grados) | 1.107987 | 0.000018 | 1.107965 | 1.108011 |
| Pitch máximo absoluto (grados) | 2.580889 | 0.000088 | 2.580806 | 2.580986 |
| Salto articular máximo (rad) | 0.017940 | 0.001051 | 0.016467 | 0.019120 |

## Resultado

Los 5 ciclos completos acumularon 0.042649 m de avance medido entre la primera y última muestra de cada ciclo. 
No se cambiaron paso, elevación ni duración de muestra durante la ventana.

La continuidad articular se expresa como el mayor salto absoluto entre dos muestras consecutivas de una misma articulación. La velocidad articular máxima se obtiene del campo medido `joint_velocities_rad_s`.

Archivos generados:

- `metricas_por_ciclo.csv`
- `series_temporales.png`
- `resumen_por_ciclo.png`
- `INFORME_ANALISIS.md`
