# Análisis automático de marcha paso

- Bolsa: `Experimentos/campanas_mujoco/barrido_transferencia_paso_20260903/shift_008/rosbag2/paso_r1`.
- Ventana marcha paso--stand: 29.424514779 s.
- Duración nominal configurada por ciclo: 5.76 s.
- Duración observada media por ciclo: 5.760140 s.
- Ciclos completos analizados: 5.
- Activaciones verdaderas del supervisor: 0.

## Estadísticos entre ciclos

| Métrica | Media | Desv. estándar | Mínimo | Máximo |
|---|---:|---:|---:|---:|
| Avance por ciclo (m) | 0.004038 | 0.001483 | 0.003369 | 0.006691 |
| Velocidad media (m/s) | 0.000701 | 0.000257 | 0.000585 | 0.001162 |
| Excursión lateral (m) | 0.003795 | 0.000717 | 0.002512 | 0.004118 |
| Altura media (m) | 0.220906 | 0.000003 | 0.220904 | 0.220909 |
| Roll máximo absoluto (grados) | 0.648988 | 0.000053 | 0.648929 | 0.649073 |
| Pitch máximo absoluto (grados) | 1.617005 | 0.000048 | 1.616964 | 1.617076 |
| Salto articular máximo (rad) | 0.010880 | 0.000693 | 0.010184 | 0.012045 |

## Resultado

Los 5 ciclos completos acumularon 0.020190 m de avance medido entre la primera y última muestra de cada ciclo. 
No se cambiaron paso, elevación ni duración de muestra durante la ventana.

La continuidad articular se expresa como el mayor salto absoluto entre dos muestras consecutivas de una misma articulación. La velocidad articular máxima se obtiene del campo medido `joint_velocities_rad_s`.

Archivos generados:

- `metricas_por_ciclo.csv`
- `series_temporales.png`
- `resumen_por_ciclo.png`
- `INFORME_ANALISIS.md`
