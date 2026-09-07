# Análisis automático de marcha paso

- Bolsa: `Experimentos/campanas_mujoco/paso_5x20_aislada_r3_20260903/rosbag2/paso_r5`.
- Ventana marcha paso--stand: 121.454138278 s.
- Duración nominal configurada por ciclo: 5.76 s.
- Duración observada media por ciclo: 5.760002 s.
- Ciclos completos analizados: 21.
- Activaciones verdaderas del supervisor: 0.

## Estadísticos entre ciclos

| Métrica | Media | Desv. estándar | Mínimo | Máximo |
|---|---:|---:|---:|---:|
| Avance por ciclo (m) | 0.002667 | 0.000157 | 0.001981 | 0.002708 |
| Velocidad media (m/s) | 0.000463 | 0.000027 | 0.000344 | 0.000470 |
| Excursión lateral (m) | 0.003764 | 0.000354 | 0.002219 | 0.003847 |
| Altura media (m) | 0.220825 | 0.000006 | 0.220817 | 0.220842 |
| Roll máximo absoluto (grados) | 0.646297 | 0.000062 | 0.646160 | 0.646376 |
| Pitch máximo absoluto (grados) | 1.787337 | 0.000193 | 1.787057 | 1.787686 |
| Salto articular máximo (rad) | 0.011214 | 0.001236 | 0.008328 | 0.012555 |

## Resultado

Los 21 ciclos completos acumularon 0.056017 m de avance medido entre la primera y última muestra de cada ciclo. 
No se cambiaron paso, elevación ni duración de muestra durante la ventana.

La continuidad articular se expresa como el mayor salto absoluto entre dos muestras consecutivas de una misma articulación. La velocidad articular máxima se obtiene del campo medido `joint_velocities_rad_s`.

Archivos generados:

- `metricas_por_ciclo.csv`
- `series_temporales.png`
- `resumen_por_ciclo.png`
- `INFORME_ANALISIS.md`
