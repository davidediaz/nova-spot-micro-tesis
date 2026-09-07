# Análisis automático de marcha paso

- Bolsa: `Experimentos/campanas_mujoco/barrido_transferencia_paso_20260903/shift_004/rosbag2/paso_r1`.
- Ventana marcha paso--stand: 29.438403652 s.
- Duración nominal configurada por ciclo: 5.76 s.
- Duración observada media por ciclo: 5.760067 s.
- Ciclos completos analizados: 5.
- Activaciones verdaderas del supervisor: 0.

## Estadísticos entre ciclos

| Métrica | Media | Desv. estándar | Mínimo | Máximo |
|---|---:|---:|---:|---:|
| Avance por ciclo (m) | 0.003328 | 0.000590 | 0.003060 | 0.004384 |
| Velocidad media (m/s) | 0.000578 | 0.000103 | 0.000531 | 0.000761 |
| Excursión lateral (m) | 0.003674 | 0.000713 | 0.002399 | 0.003997 |
| Altura media (m) | 0.220865 | 0.000006 | 0.220858 | 0.220873 |
| Roll máximo absoluto (grados) | 0.647101 | 0.000075 | 0.647001 | 0.647186 |
| Pitch máximo absoluto (grados) | 1.694624 | 0.000162 | 1.694415 | 1.694787 |
| Salto articular máximo (rad) | 0.010014 | 0.001325 | 0.008241 | 0.011918 |

## Resultado

Los 5 ciclos completos acumularon 0.016639 m de avance medido entre la primera y última muestra de cada ciclo. 
No se cambiaron paso, elevación ni duración de muestra durante la ventana.

La continuidad articular se expresa como el mayor salto absoluto entre dos muestras consecutivas de una misma articulación. La velocidad articular máxima se obtiene del campo medido `joint_velocities_rad_s`.

Archivos generados:

- `metricas_por_ciclo.csv`
- `series_temporales.png`
- `resumen_por_ciclo.png`
- `INFORME_ANALISIS.md`
