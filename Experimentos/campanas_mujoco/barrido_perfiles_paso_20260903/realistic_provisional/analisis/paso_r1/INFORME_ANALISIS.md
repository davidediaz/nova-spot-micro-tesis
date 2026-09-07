# Análisis automático de marcha paso

- Bolsa: `Experimentos/campanas_mujoco/barrido_perfiles_paso_20260903/realistic_provisional/rosbag2/paso_r1`.
- Ventana marcha paso--stand: 31.838301561 s.
- Duración nominal configurada por ciclo: 5.76 s.
- Duración observada media por ciclo: 5.760060 s.
- Ciclos completos analizados: 5.
- Activaciones verdaderas del supervisor: 0.

## Estadísticos entre ciclos

| Métrica | Media | Desv. estándar | Mínimo | Máximo |
|---|---:|---:|---:|---:|
| Avance por ciclo (m) | -0.000999 | 0.000072 | -0.001074 | -0.000917 |
| Velocidad media (m/s) | -0.000174 | 0.000012 | -0.000186 | -0.000159 |
| Excursión lateral (m) | 0.003105 | 0.000233 | 0.002689 | 0.003220 |
| Altura media (m) | 0.108596 | 0.000116 | 0.108473 | 0.108779 |
| Roll máximo absoluto (grados) | 1.822498 | 0.000177 | 1.822342 | 1.822770 |
| Pitch máximo absoluto (grados) | 41.397251 | 0.002253 | 41.393864 | 41.399727 |
| Salto articular máximo (rad) | 0.015134 | 0.001219 | 0.013439 | 0.016655 |

## Resultado

Los 5 ciclos completos acumularon -0.004997 m de avance medido entre la primera y última muestra de cada ciclo. 
No se cambiaron paso, elevación ni duración de muestra durante la ventana.

La continuidad articular se expresa como el mayor salto absoluto entre dos muestras consecutivas de una misma articulación. La velocidad articular máxima se obtiene del campo medido `joint_velocities_rad_s`.

Archivos generados:

- `metricas_por_ciclo.csv`
- `series_temporales.png`
- `resumen_por_ciclo.png`
- `INFORME_ANALISIS.md`
