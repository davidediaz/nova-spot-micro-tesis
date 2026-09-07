# Análisis automático de marcha paso

- Bolsa: `Experimentos/campanas_mujoco/barrido_altura_paso_20260903/height_020/rosbag2/paso_r1`.
- Ventana marcha paso--stand: 31.942820649 s.
- Duración nominal configurada por ciclo: 5.76 s.
- Duración observada media por ciclo: 5.760012 s.
- Ciclos completos analizados: 5.
- Activaciones verdaderas del supervisor: 0.

## Estadísticos entre ciclos

| Métrica | Media | Desv. estándar | Mínimo | Máximo |
|---|---:|---:|---:|---:|
| Avance por ciclo (m) | 0.007858 | 0.002893 | 0.006498 | 0.013032 |
| Velocidad media (m/s) | 0.001364 | 0.000502 | 0.001128 | 0.002262 |
| Excursión lateral (m) | 0.007289 | 0.000298 | 0.006756 | 0.007445 |
| Altura media (m) | 0.220363 | 0.000011 | 0.220347 | 0.220374 |
| Roll máximo absoluto (grados) | 2.500317 | 0.000059 | 2.500233 | 2.500393 |
| Pitch máximo absoluto (grados) | 5.616760 | 0.000039 | 5.616728 | 5.616827 |
| Salto articular máximo (rad) | 0.028838 | 0.002492 | 0.024575 | 0.030838 |

## Resultado

Los 5 ciclos completos acumularon 0.039290 m de avance medido entre la primera y última muestra de cada ciclo. 
No se cambiaron paso, elevación ni duración de muestra durante la ventana.

La continuidad articular se expresa como el mayor salto absoluto entre dos muestras consecutivas de una misma articulación. La velocidad articular máxima se obtiene del campo medido `joint_velocities_rad_s`.

Archivos generados:

- `metricas_por_ciclo.csv`
- `series_temporales.png`
- `resumen_por_ciclo.png`
- `INFORME_ANALISIS.md`
