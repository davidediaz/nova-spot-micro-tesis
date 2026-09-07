# Análisis automático de marcha paso

- Bolsa: `Experimentos/campanas_mujoco/paso_5x20_r2_20260902/rosbag2/paso_r1`.
- Ventana marcha paso--stand: 121.178754359 s.
- Duración nominal configurada por ciclo: 5.76 s.
- Duración observada media por ciclo: 5.759997 s.
- Ciclos completos analizados: 21.
- Activaciones verdaderas del supervisor: 0.

## Estadísticos entre ciclos

| Métrica | Media | Desv. estándar | Mínimo | Máximo |
|---|---:|---:|---:|---:|
| Avance por ciclo (m) | 0.002665 | 0.000516 | 0.000958 | 0.003551 |
| Velocidad media (m/s) | 0.000463 | 0.000090 | 0.000166 | 0.000616 |
| Excursión lateral (m) | 0.003884 | 0.000453 | 0.002254 | 0.004521 |
| Altura media (m) | 0.220829 | 0.000008 | 0.220811 | 0.220845 |
| Roll máximo absoluto (grados) | 0.646547 | 0.000499 | 0.646150 | 0.647602 |
| Pitch máximo absoluto (grados) | 1.788112 | 0.001174 | 1.787104 | 1.790349 |
| Salto articular máximo (rad) | 0.023433 | 0.007128 | 0.007110 | 0.033764 |

## Resultado

Los 21 ciclos completos acumularon 0.055971 m de avance medido entre la primera y última muestra de cada ciclo. 
No se cambiaron paso, elevación ni duración de muestra durante la ventana.

La continuidad articular se expresa como el mayor salto absoluto entre dos muestras consecutivas de una misma articulación. La velocidad articular máxima se obtiene del campo medido `joint_velocities_rad_s`.

Archivos generados:

- `metricas_por_ciclo.csv`
- `series_temporales.png`
- `resumen_por_ciclo.png`
- `INFORME_ANALISIS.md`
