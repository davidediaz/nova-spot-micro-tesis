# Análisis automático de marcha paso

- Bolsa: `Experimentos/campanas_mujoco/validacion_cierre_20260903/rosbag2/paso_r1`.
- Ventana marcha paso--stand: 11.272469723 s.
- Duración nominal configurada por ciclo: 5.76 s.
- Duración observada media por ciclo: 5.759327 s.
- Ciclos completos analizados: 1.
- Activaciones verdaderas del supervisor: 0.

## Estadísticos entre ciclos

| Métrica | Media | Desv. estándar | Mínimo | Máximo |
|---|---:|---:|---:|---:|
| Avance por ciclo (m) | 0.002076 | nan | 0.002076 | 0.002076 |
| Velocidad media (m/s) | 0.000360 | nan | 0.000360 | 0.000360 |
| Excursión lateral (m) | 0.002216 | nan | 0.002216 | 0.002216 |
| Altura media (m) | 0.220825 | nan | 0.220825 | 0.220825 |
| Roll máximo absoluto (grados) | 0.646338 | nan | 0.646338 | 0.646338 |
| Pitch máximo absoluto (grados) | 1.787352 | nan | 1.787352 | 1.787352 |
| Salto articular máximo (rad) | 0.009171 | nan | 0.009171 | 0.009171 |

## Resultado

Los 1 ciclos completos acumularon 0.002076 m de avance medido entre la primera y última muestra de cada ciclo. 
No se cambiaron paso, elevación ni duración de muestra durante la ventana.

La continuidad articular se expresa como el mayor salto absoluto entre dos muestras consecutivas de una misma articulación. La velocidad articular máxima se obtiene del campo medido `joint_velocities_rad_s`.

Archivos generados:

- `metricas_por_ciclo.csv`
- `series_temporales.png`
- `resumen_por_ciclo.png`
- `INFORME_ANALISIS.md`
