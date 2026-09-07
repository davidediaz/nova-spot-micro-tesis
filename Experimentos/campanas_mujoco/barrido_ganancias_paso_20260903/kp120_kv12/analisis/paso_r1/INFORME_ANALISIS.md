# Análisis automático de marcha paso

- Bolsa: `Experimentos/campanas_mujoco/barrido_ganancias_paso_20260903/kp120_kv12/rosbag2/paso_r1`.
- Ventana marcha paso--stand: 29.949844555 s.
- Duración nominal configurada por ciclo: 5.76 s.
- Duración observada media por ciclo: 5.760481 s.
- Ciclos completos analizados: 5.
- Activaciones verdaderas del supervisor: 0.

## Estadísticos entre ciclos

| Métrica | Media | Desv. estándar | Mínimo | Máximo |
|---|---:|---:|---:|---:|
| Avance por ciclo (m) | 0.012069 | 0.002827 | 0.010753 | 0.017125 |
| Velocidad media (m/s) | 0.002095 | 0.000491 | 0.001867 | 0.002973 |
| Excursión lateral (m) | 0.005506 | 0.000777 | 0.004116 | 0.005870 |
| Altura media (m) | 0.222621 | 0.000005 | 0.222611 | 0.222623 |
| Roll máximo absoluto (grados) | 1.641143 | 0.000019 | 1.641114 | 1.641164 |
| Pitch máximo absoluto (grados) | 3.365586 | 0.000017 | 3.365563 | 3.365607 |
| Salto articular máximo (rad) | 0.023197 | 0.011066 | 0.016895 | 0.042913 |

## Resultado

Los 5 ciclos completos acumularon 0.060344 m de avance medido entre la primera y última muestra de cada ciclo. 
No se cambiaron paso, elevación ni duración de muestra durante la ventana.

La continuidad articular se expresa como el mayor salto absoluto entre dos muestras consecutivas de una misma articulación. La velocidad articular máxima se obtiene del campo medido `joint_velocities_rad_s`.

Archivos generados:

- `metricas_por_ciclo.csv`
- `series_temporales.png`
- `resumen_por_ciclo.png`
- `INFORME_ANALISIS.md`
