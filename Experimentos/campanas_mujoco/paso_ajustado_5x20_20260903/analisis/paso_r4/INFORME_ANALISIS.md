# Análisis automático de marcha paso

- Bolsa: `Experimentos/campanas_mujoco/paso_ajustado_5x20_20260903/rosbag2/paso_r4`.
- Ventana marcha paso--stand: 122.410163924 s.
- Duración nominal configurada por ciclo: 5.76 s.
- Duración observada media por ciclo: 5.759997 s.
- Ciclos completos analizados: 21.
- Activaciones verdaderas del supervisor: 0.

## Estadísticos entre ciclos

| Métrica | Media | Desv. estándar | Mínimo | Máximo |
|---|---:|---:|---:|---:|
| Avance por ciclo (m) | 0.010161 | 0.001396 | 0.009776 | 0.016251 |
| Velocidad media (m/s) | 0.001764 | 0.000242 | 0.001697 | 0.002821 |
| Excursión lateral (m) | 0.004963 | 0.000318 | 0.003577 | 0.005089 |
| Altura media (m) | 0.222101 | 0.000005 | 0.222093 | 0.222111 |
| Roll máximo absoluto (grados) | 1.510930 | 0.000040 | 1.510833 | 1.510986 |
| Pitch máximo absoluto (grados) | 3.171323 | 0.000023 | 3.171251 | 3.171355 |
| Salto articular máximo (rad) | 0.017338 | 0.002142 | 0.013287 | 0.021326 |

## Resultado

Los 21 ciclos completos acumularon 0.213381 m de avance medido entre la primera y última muestra de cada ciclo. 
No se cambiaron paso, elevación ni duración de muestra durante la ventana.

La continuidad articular se expresa como el mayor salto absoluto entre dos muestras consecutivas de una misma articulación. La velocidad articular máxima se obtiene del campo medido `joint_velocities_rad_s`.

Archivos generados:

- `metricas_por_ciclo.csv`
- `series_temporales.png`
- `resumen_por_ciclo.png`
- `INFORME_ANALISIS.md`
