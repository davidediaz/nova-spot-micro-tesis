# Análisis automático de marcha paso

- Bolsa: `Experimentos/campanas_mujoco/paso_5x20_20260902/rosbag2/paso_r1`.
- Ventana marcha paso--stand: 35.062513614 s.
- Duración nominal configurada por ciclo: 5.76 s.
- Duración observada media por ciclo: 5.760065 s.
- Ciclos completos analizados: 6.
- Activaciones verdaderas del supervisor: 0.

## Estadísticos entre ciclos

| Métrica | Media | Desv. estándar | Mínimo | Máximo |
|---|---:|---:|---:|---:|
| Avance por ciclo (m) | 0.002417 | 0.000708 | 0.000972 | 0.002714 |
| Velocidad media (m/s) | 0.000420 | 0.000123 | 0.000169 | 0.000471 |
| Excursión lateral (m) | 0.003577 | 0.000653 | 0.002243 | 0.003847 |
| Altura media (m) | 0.220826 | 0.000004 | 0.220820 | 0.220830 |
| Roll máximo absoluto (grados) | 0.646363 | 0.000112 | 0.646206 | 0.646540 |
| Pitch máximo absoluto (grados) | 1.787327 | 0.000335 | 1.786836 | 1.787716 |
| Salto articular máximo (rad) | 0.010648 | 0.001073 | 0.009080 | 0.012171 |

## Resultado

Los 6 ciclos completos acumularon 0.014499 m de avance medido entre la primera y última muestra de cada ciclo. 
No se cambiaron paso, elevación ni duración de muestra durante la ventana.

La continuidad articular se expresa como el mayor salto absoluto entre dos muestras consecutivas de una misma articulación. La velocidad articular máxima se obtiene del campo medido `joint_velocities_rad_s`.

Archivos generados:

- `metricas_por_ciclo.csv`
- `series_temporales.png`
- `resumen_por_ciclo.png`
- `INFORME_ANALISIS.md`
