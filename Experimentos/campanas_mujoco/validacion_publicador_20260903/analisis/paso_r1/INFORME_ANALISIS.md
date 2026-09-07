# Análisis automático de marcha paso

- Bolsa: `Experimentos/campanas_mujoco/validacion_publicador_20260903/rosbag2/paso_r1`.
- Ventana marcha paso--stand: 18.288530502 s.
- Duración nominal configurada por ciclo: 5.76 s.
- Duración observada media por ciclo: 5.760437 s.
- Ciclos completos analizados: 3.
- Activaciones verdaderas del supervisor: 0.

## Estadísticos entre ciclos

| Métrica | Media | Desv. estándar | Mínimo | Máximo |
|---|---:|---:|---:|---:|
| Avance por ciclo (m) | 0.002468 | 0.000398 | 0.002009 | 0.002701 |
| Velocidad media (m/s) | 0.000429 | 0.000069 | 0.000349 | 0.000469 |
| Excursión lateral (m) | 0.003300 | 0.000938 | 0.002216 | 0.003846 |
| Altura media (m) | 0.220826 | 0.000003 | 0.220823 | 0.220830 |
| Roll máximo absoluto (grados) | 0.646318 | 0.000191 | 0.646188 | 0.646537 |
| Pitch máximo absoluto (grados) | 1.787100 | 0.000313 | 1.786871 | 1.787457 |
| Salto articular máximo (rad) | 0.012496 | 0.001739 | 0.010852 | 0.014316 |

## Resultado

Los 3 ciclos completos acumularon 0.007405 m de avance medido entre la primera y última muestra de cada ciclo. 
No se cambiaron paso, elevación ni duración de muestra durante la ventana.

La continuidad articular se expresa como el mayor salto absoluto entre dos muestras consecutivas de una misma articulación. La velocidad articular máxima se obtiene del campo medido `joint_velocities_rad_s`.

Archivos generados:

- `metricas_por_ciclo.csv`
- `series_temporales.png`
- `resumen_por_ciclo.png`
- `INFORME_ANALISIS.md`
