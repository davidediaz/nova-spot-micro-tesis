# Análisis automático de marcha paso

- Bolsa: `Experimentos/campanas_mujoco/paso_5x20_aislada_r3_20260903/rosbag2/paso_r1`.
- Ventana marcha paso--stand: 122.539419654 s.
- Duración nominal configurada por ciclo: 5.76 s.
- Duración observada media por ciclo: 5.760005 s.
- Ciclos completos analizados: 21.
- Activaciones verdaderas del supervisor: 0.

## Estadísticos entre ciclos

| Métrica | Media | Desv. estándar | Mínimo | Máximo |
|---|---:|---:|---:|---:|
| Avance por ciclo (m) | 0.002669 | 0.000151 | 0.002009 | 0.002709 |
| Velocidad media (m/s) | 0.000463 | 0.000026 | 0.000349 | 0.000470 |
| Excursión lateral (m) | 0.003763 | 0.000357 | 0.002206 | 0.003848 |
| Altura media (m) | 0.220823 | 0.000007 | 0.220808 | 0.220835 |
| Roll máximo absoluto (grados) | 0.646324 | 0.000065 | 0.646232 | 0.646465 |
| Pitch máximo absoluto (grados) | 1.787231 | 0.000228 | 1.786900 | 1.787808 |
| Salto articular máximo (rad) | 0.010847 | 0.001254 | 0.008890 | 0.013155 |

## Resultado

Los 21 ciclos completos acumularon 0.056052 m de avance medido entre la primera y última muestra de cada ciclo. 
No se cambiaron paso, elevación ni duración de muestra durante la ventana.

La continuidad articular se expresa como el mayor salto absoluto entre dos muestras consecutivas de una misma articulación. La velocidad articular máxima se obtiene del campo medido `joint_velocities_rad_s`.

Archivos generados:

- `metricas_por_ciclo.csv`
- `series_temporales.png`
- `resumen_por_ciclo.png`
- `INFORME_ANALISIS.md`
