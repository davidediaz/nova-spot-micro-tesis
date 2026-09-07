# Análisis automático de marcha paso

- Bolsa: `Experimentos/campanas_mujoco/paso_ajustado_5x20_20260903/rosbag2/paso_r3`.
- Ventana marcha paso--stand: 122.138814144 s.
- Duración nominal configurada por ciclo: 5.76 s.
- Duración observada media por ciclo: 5.760006 s.
- Ciclos completos analizados: 21.
- Activaciones verdaderas del supervisor: 0.

## Estadísticos entre ciclos

| Métrica | Media | Desv. estándar | Mínimo | Máximo |
|---|---:|---:|---:|---:|
| Avance por ciclo (m) | 0.010173 | 0.001382 | 0.009808 | 0.016201 |
| Velocidad media (m/s) | 0.001766 | 0.000240 | 0.001703 | 0.002813 |
| Excursión lateral (m) | 0.004957 | 0.000327 | 0.003535 | 0.005080 |
| Altura media (m) | 0.222098 | 0.000004 | 0.222092 | 0.222106 |
| Roll máximo absoluto (grados) | 1.510940 | 0.000030 | 1.510870 | 1.510981 |
| Pitch máximo absoluto (grados) | 3.171337 | 0.000019 | 3.171307 | 3.171379 |
| Salto articular máximo (rad) | 0.016726 | 0.003040 | 0.013513 | 0.028367 |

## Resultado

Los 21 ciclos completos acumularon 0.213639 m de avance medido entre la primera y última muestra de cada ciclo. 
No se cambiaron paso, elevación ni duración de muestra durante la ventana.

La continuidad articular se expresa como el mayor salto absoluto entre dos muestras consecutivas de una misma articulación. La velocidad articular máxima se obtiene del campo medido `joint_velocities_rad_s`.

Archivos generados:

- `metricas_por_ciclo.csv`
- `series_temporales.png`
- `resumen_por_ciclo.png`
- `INFORME_ANALISIS.md`
