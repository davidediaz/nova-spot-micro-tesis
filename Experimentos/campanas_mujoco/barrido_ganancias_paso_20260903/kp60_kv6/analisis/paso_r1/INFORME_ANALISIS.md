# Análisis automático de marcha paso

- Bolsa: `Experimentos/campanas_mujoco/barrido_ganancias_paso_20260903/kp60_kv6/rosbag2/paso_r1`.
- Ventana marcha paso--stand: 29.457295429 s.
- Duración nominal configurada por ciclo: 5.76 s.
- Duración observada media por ciclo: 5.760148 s.
- Ciclos completos analizados: 5.
- Activaciones verdaderas del supervisor: 0.

## Estadísticos entre ciclos

| Métrica | Media | Desv. estándar | Mínimo | Máximo |
|---|---:|---:|---:|---:|
| Avance por ciclo (m) | 0.010568 | 0.002914 | 0.009251 | 0.015781 |
| Velocidad media (m/s) | 0.001835 | 0.000506 | 0.001606 | 0.002740 |
| Excursión lateral (m) | 0.004189 | 0.000506 | 0.003284 | 0.004433 |
| Altura media (m) | 0.221591 | 0.000004 | 0.221586 | 0.221596 |
| Roll máximo absoluto (grados) | 1.378261 | 0.000030 | 1.378236 | 1.378307 |
| Pitch máximo absoluto (grados) | 2.968646 | 0.000009 | 2.968637 | 2.968661 |
| Salto articular máximo (rad) | 0.017276 | 0.001549 | 0.015629 | 0.019478 |

## Resultado

Los 5 ciclos completos acumularon 0.052842 m de avance medido entre la primera y última muestra de cada ciclo. 
No se cambiaron paso, elevación ni duración de muestra durante la ventana.

La continuidad articular se expresa como el mayor salto absoluto entre dos muestras consecutivas de una misma articulación. La velocidad articular máxima se obtiene del campo medido `joint_velocities_rad_s`.

Archivos generados:

- `metricas_por_ciclo.csv`
- `series_temporales.png`
- `resumen_por_ciclo.png`
- `INFORME_ANALISIS.md`
