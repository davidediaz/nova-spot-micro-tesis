# Análisis automático de marcha paso

- Bolsa: `Experimentos/campanas_mujoco/barrido_friccion_paso_r2_20260903/friction_12/rosbag2/paso_r1`.
- Ventana marcha paso--stand: 29.440953479 s.
- Duración nominal configurada por ciclo: 5.76 s.
- Duración observada media por ciclo: 5.760640 s.
- Ciclos completos analizados: 5.
- Activaciones verdaderas del supervisor: 0.

## Estadísticos entre ciclos

| Métrica | Media | Desv. estándar | Mínimo | Máximo |
|---|---:|---:|---:|---:|
| Avance por ciclo (m) | 0.008147 | 0.002968 | 0.006805 | 0.013457 |
| Velocidad media (m/s) | 0.001414 | 0.000515 | 0.001181 | 0.002336 |
| Excursión lateral (m) | 0.003245 | 0.000633 | 0.002113 | 0.003531 |
| Altura media (m) | 0.220126 | 0.000007 | 0.220115 | 0.220135 |
| Roll máximo absoluto (grados) | 0.999159 | 0.000071 | 0.999101 | 0.999281 |
| Pitch máximo absoluto (grados) | 2.420408 | 0.000206 | 2.420194 | 2.420747 |
| Salto articular máximo (rad) | 0.014850 | 0.001468 | 0.013019 | 0.016488 |

## Resultado

Los 5 ciclos completos acumularon 0.040735 m de avance medido entre la primera y última muestra de cada ciclo. 
No se cambiaron paso, elevación ni duración de muestra durante la ventana.

La continuidad articular se expresa como el mayor salto absoluto entre dos muestras consecutivas de una misma articulación. La velocidad articular máxima se obtiene del campo medido `joint_velocities_rad_s`.

Archivos generados:

- `metricas_por_ciclo.csv`
- `series_temporales.png`
- `resumen_por_ciclo.png`
- `INFORME_ANALISIS.md`
