# Análisis automático de marcha paso

- Bolsa: `Experimentos/campanas_mujoco/paso_5x20_aislada_r2_20260903/rosbag2/paso_r1`.
- Ventana marcha paso--stand: 121.870438106 s.
- Duración nominal configurada por ciclo: 5.76 s.
- Duración observada media por ciclo: 5.759978 s.
- Ciclos completos analizados: 21.
- Activaciones verdaderas del supervisor: 0.

## Estadísticos entre ciclos

| Métrica | Media | Desv. estándar | Mínimo | Máximo |
|---|---:|---:|---:|---:|
| Avance por ciclo (m) | 0.002681 | 0.000149 | 0.002032 | 0.002750 |
| Velocidad media (m/s) | 0.000465 | 0.000026 | 0.000353 | 0.000477 |
| Excursión lateral (m) | 0.003760 | 0.000355 | 0.002213 | 0.003858 |
| Altura media (m) | 0.220829 | 0.000009 | 0.220818 | 0.220852 |
| Roll máximo absoluto (grados) | 0.646377 | 0.000127 | 0.646090 | 0.646672 |
| Pitch máximo absoluto (grados) | 1.787315 | 0.000398 | 1.786835 | 1.788094 |
| Salto articular máximo (rad) | 0.011661 | 0.001785 | 0.009074 | 0.015308 |

## Resultado

Los 21 ciclos completos acumularon 0.056302 m de avance medido entre la primera y última muestra de cada ciclo. 
No se cambiaron paso, elevación ni duración de muestra durante la ventana.

La continuidad articular se expresa como el mayor salto absoluto entre dos muestras consecutivas de una misma articulación. La velocidad articular máxima se obtiene del campo medido `joint_velocities_rad_s`.

Archivos generados:

- `metricas_por_ciclo.csv`
- `series_temporales.png`
- `resumen_por_ciclo.png`
- `INFORME_ANALISIS.md`
