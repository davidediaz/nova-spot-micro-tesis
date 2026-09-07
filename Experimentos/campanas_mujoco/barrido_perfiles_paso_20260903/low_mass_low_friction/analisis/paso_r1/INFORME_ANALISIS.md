# Análisis automático de marcha paso

- Bolsa: `Experimentos/campanas_mujoco/barrido_perfiles_paso_20260903/low_mass_low_friction/rosbag2/paso_r1`.
- Ventana marcha paso--stand: 30.080947944 s.
- Duración nominal configurada por ciclo: 5.76 s.
- Duración observada media por ciclo: 5.760050 s.
- Ciclos completos analizados: 5.
- Activaciones verdaderas del supervisor: 1.

## Estadísticos entre ciclos

| Métrica | Media | Desv. estándar | Mínimo | Máximo |
|---|---:|---:|---:|---:|
| Avance por ciclo (m) | -0.001391 | 0.000034 | -0.001422 | -0.001336 |
| Velocidad media (m/s) | -0.000242 | 0.000006 | -0.000247 | -0.000232 |
| Excursión lateral (m) | 0.004662 | 0.000140 | 0.004418 | 0.004761 |
| Altura media (m) | 0.134950 | 0.000024 | 0.134927 | 0.134988 |
| Roll máximo absoluto (grados) | 2.634735 | 0.000062 | 2.634675 | 2.634818 |
| Pitch máximo absoluto (grados) | 35.619524 | 0.000122 | 35.619365 | 35.619635 |
| Salto articular máximo (rad) | 0.018737 | 0.002738 | 0.015723 | 0.021333 |

## Resultado

Los 5 ciclos completos acumularon -0.006957 m de avance medido entre la primera y última muestra de cada ciclo. 
No se cambiaron paso, elevación ni duración de muestra durante la ventana.

La continuidad articular se expresa como el mayor salto absoluto entre dos muestras consecutivas de una misma articulación. La velocidad articular máxima se obtiene del campo medido `joint_velocities_rad_s`.

Archivos generados:

- `metricas_por_ciclo.csv`
- `series_temporales.png`
- `resumen_por_ciclo.png`
- `INFORME_ANALISIS.md`
