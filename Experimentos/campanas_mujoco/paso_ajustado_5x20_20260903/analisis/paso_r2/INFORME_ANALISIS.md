# Análisis automático de marcha paso

- Bolsa: `Experimentos/campanas_mujoco/paso_ajustado_5x20_20260903/rosbag2/paso_r2`.
- Ventana marcha paso--stand: 122.679147445 s.
- Duración nominal configurada por ciclo: 5.76 s.
- Duración observada media por ciclo: 5.760006 s.
- Ciclos completos analizados: 21.
- Activaciones verdaderas del supervisor: 0.

## Estadísticos entre ciclos

| Métrica | Media | Desv. estándar | Mínimo | Máximo |
|---|---:|---:|---:|---:|
| Avance por ciclo (m) | 0.010176 | 0.001389 | 0.009798 | 0.016238 |
| Velocidad media (m/s) | 0.001767 | 0.000241 | 0.001701 | 0.002819 |
| Excursión lateral (m) | 0.004957 | 0.000327 | 0.003533 | 0.005063 |
| Altura media (m) | 0.222101 | 0.000003 | 0.222095 | 0.222107 |
| Roll máximo absoluto (grados) | 1.510930 | 0.000035 | 1.510843 | 1.510985 |
| Pitch máximo absoluto (grados) | 3.171319 | 0.000023 | 3.171268 | 3.171358 |
| Salto articular máximo (rad) | 0.016628 | 0.001406 | 0.013915 | 0.019456 |

## Resultado

Los 21 ciclos completos acumularon 0.213692 m de avance medido entre la primera y última muestra de cada ciclo. 
No se cambiaron paso, elevación ni duración de muestra durante la ventana.

La continuidad articular se expresa como el mayor salto absoluto entre dos muestras consecutivas de una misma articulación. La velocidad articular máxima se obtiene del campo medido `joint_velocities_rad_s`.

Archivos generados:

- `metricas_por_ciclo.csv`
- `series_temporales.png`
- `resumen_por_ciclo.png`
- `INFORME_ANALISIS.md`
