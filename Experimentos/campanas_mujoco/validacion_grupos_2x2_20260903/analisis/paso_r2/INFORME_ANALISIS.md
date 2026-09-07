# Análisis automático de marcha paso

- Bolsa: `Experimentos/campanas_mujoco/validacion_grupos_2x2_20260903/rosbag2/paso_r2`.
- Ventana marcha paso--stand: 17.748337269 s.
- Duración nominal configurada por ciclo: 5.76 s.
- Duración observada media por ciclo: 5.760003 s.
- Ciclos completos analizados: 3.
- Activaciones verdaderas del supervisor: 0.

## Estadísticos entre ciclos

| Métrica | Media | Desv. estándar | Mínimo | Máximo |
|---|---:|---:|---:|---:|
| Avance por ciclo (m) | 0.002471 | 0.000398 | 0.002011 | 0.002702 |
| Velocidad media (m/s) | 0.000429 | 0.000069 | 0.000349 | 0.000469 |
| Excursión lateral (m) | 0.003297 | 0.000944 | 0.002207 | 0.003842 |
| Altura media (m) | 0.220828 | 0.000013 | 0.220816 | 0.220841 |
| Roll máximo absoluto (grados) | 0.646322 | 0.000048 | 0.646268 | 0.646362 |
| Pitch máximo absoluto (grados) | 1.787070 | 0.000049 | 1.787019 | 1.787117 |
| Salto articular máximo (rad) | 0.011688 | 0.000450 | 0.011292 | 0.012177 |

## Resultado

Los 3 ciclos completos acumularon 0.007413 m de avance medido entre la primera y última muestra de cada ciclo. 
No se cambiaron paso, elevación ni duración de muestra durante la ventana.

La continuidad articular se expresa como el mayor salto absoluto entre dos muestras consecutivas de una misma articulación. La velocidad articular máxima se obtiene del campo medido `joint_velocities_rad_s`.

Archivos generados:

- `metricas_por_ciclo.csv`
- `series_temporales.png`
- `resumen_por_ciclo.png`
- `INFORME_ANALISIS.md`
