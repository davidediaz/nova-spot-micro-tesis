# Análisis automático de marcha paso

- Bolsa: `Experimentos/campanas_mujoco/validacion_aislamiento_r4_20260903/rosbag2/paso_r1`.
- Ventana marcha paso--stand: 17.300915427 s.
- Duración nominal configurada por ciclo: 5.76 s.
- Duración observada media por ciclo: 5.759925 s.
- Ciclos completos analizados: 3.
- Activaciones verdaderas del supervisor: 0.

## Estadísticos entre ciclos

| Métrica | Media | Desv. estándar | Mínimo | Máximo |
|---|---:|---:|---:|---:|
| Avance por ciclo (m) | 0.002465 | 0.000409 | 0.001992 | 0.002705 |
| Velocidad media (m/s) | 0.000428 | 0.000071 | 0.000346 | 0.000470 |
| Excursión lateral (m) | 0.003293 | 0.000943 | 0.002205 | 0.003839 |
| Altura media (m) | 0.220829 | 0.000008 | 0.220822 | 0.220837 |
| Roll máximo absoluto (grados) | 0.646269 | 0.000102 | 0.646190 | 0.646385 |
| Pitch máximo absoluto (grados) | 1.787251 | 0.000355 | 1.786886 | 1.787595 |
| Salto articular máximo (rad) | 0.011657 | 0.001368 | 0.010354 | 0.013081 |

## Resultado

Los 3 ciclos completos acumularon 0.007394 m de avance medido entre la primera y última muestra de cada ciclo. 
No se cambiaron paso, elevación ni duración de muestra durante la ventana.

La continuidad articular se expresa como el mayor salto absoluto entre dos muestras consecutivas de una misma articulación. La velocidad articular máxima se obtiene del campo medido `joint_velocities_rad_s`.

Archivos generados:

- `metricas_por_ciclo.csv`
- `series_temporales.png`
- `resumen_por_ciclo.png`
- `INFORME_ANALISIS.md`
