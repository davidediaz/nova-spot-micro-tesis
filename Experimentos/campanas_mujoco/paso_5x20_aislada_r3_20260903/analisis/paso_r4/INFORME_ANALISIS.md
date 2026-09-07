# Análisis automático de marcha paso

- Bolsa: `Experimentos/campanas_mujoco/paso_5x20_aislada_r3_20260903/rosbag2/paso_r4`.
- Ventana marcha paso--stand: 121.962568367 s.
- Duración nominal configurada por ciclo: 5.76 s.
- Duración observada media por ciclo: 5.760012 s.
- Ciclos completos analizados: 21.
- Activaciones verdaderas del supervisor: 0.

## Estadísticos entre ciclos

| Métrica | Media | Desv. estándar | Mínimo | Máximo |
|---|---:|---:|---:|---:|
| Avance por ciclo (m) | 0.002666 | 0.000163 | 0.001953 | 0.002708 |
| Velocidad media (m/s) | 0.000463 | 0.000028 | 0.000339 | 0.000470 |
| Excursión lateral (m) | 0.003764 | 0.000352 | 0.002229 | 0.003845 |
| Altura media (m) | 0.220823 | 0.000008 | 0.220801 | 0.220832 |
| Roll máximo absoluto (grados) | 0.646295 | 0.000066 | 0.646169 | 0.646396 |
| Pitch máximo absoluto (grados) | 1.787184 | 0.000194 | 1.786867 | 1.787586 |
| Salto articular máximo (rad) | 0.010861 | 0.001138 | 0.009526 | 0.013653 |

## Resultado

Los 21 ciclos completos acumularon 0.055979 m de avance medido entre la primera y última muestra de cada ciclo. 
No se cambiaron paso, elevación ni duración de muestra durante la ventana.

La continuidad articular se expresa como el mayor salto absoluto entre dos muestras consecutivas de una misma articulación. La velocidad articular máxima se obtiene del campo medido `joint_velocities_rad_s`.

Archivos generados:

- `metricas_por_ciclo.csv`
- `series_temporales.png`
- `resumen_por_ciclo.png`
- `INFORME_ANALISIS.md`
