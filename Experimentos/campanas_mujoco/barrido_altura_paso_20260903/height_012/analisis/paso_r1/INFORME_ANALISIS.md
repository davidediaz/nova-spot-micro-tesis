# Análisis automático de marcha paso

- Bolsa: `Experimentos/campanas_mujoco/barrido_altura_paso_20260903/height_012/rosbag2/paso_r1`.
- Ventana marcha paso--stand: 29.439823683 s.
- Duración nominal configurada por ciclo: 5.76 s.
- Duración observada media por ciclo: 5.760074 s.
- Ciclos completos analizados: 5.
- Activaciones verdaderas del supervisor: 0.

## Estadísticos entre ciclos

| Métrica | Media | Desv. estándar | Mínimo | Máximo |
|---|---:|---:|---:|---:|
| Avance por ciclo (m) | 0.008518 | 0.002988 | 0.007178 | 0.013864 |
| Velocidad media (m/s) | 0.001479 | 0.000519 | 0.001246 | 0.002407 |
| Excursión lateral (m) | 0.003465 | 0.000494 | 0.002581 | 0.003690 |
| Altura media (m) | 0.220631 | 0.000007 | 0.220622 | 0.220642 |
| Roll máximo absoluto (grados) | 1.107984 | 0.000046 | 1.107924 | 1.108031 |
| Pitch máximo absoluto (grados) | 2.580923 | 0.000225 | 2.580711 | 2.581199 |
| Salto articular máximo (rad) | 0.015672 | 0.001218 | 0.014302 | 0.017436 |

## Resultado

Los 5 ciclos completos acumularon 0.042590 m de avance medido entre la primera y última muestra de cada ciclo. 
No se cambiaron paso, elevación ni duración de muestra durante la ventana.

La continuidad articular se expresa como el mayor salto absoluto entre dos muestras consecutivas de una misma articulación. La velocidad articular máxima se obtiene del campo medido `joint_velocities_rad_s`.

Archivos generados:

- `metricas_por_ciclo.csv`
- `series_temporales.png`
- `resumen_por_ciclo.png`
- `INFORME_ANALISIS.md`
