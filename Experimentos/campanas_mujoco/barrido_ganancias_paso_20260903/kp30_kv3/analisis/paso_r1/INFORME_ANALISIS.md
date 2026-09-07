# Análisis automático de marcha paso

- Bolsa: `Experimentos/campanas_mujoco/barrido_ganancias_paso_20260903/kp30_kv3/rosbag2/paso_r1`.
- Ventana marcha paso--stand: 32.140084398 s.
- Duración nominal configurada por ciclo: 5.76 s.
- Duración observada media por ciclo: 5.760332 s.
- Ciclos completos analizados: 5.
- Activaciones verdaderas del supervisor: 0.

## Estadísticos entre ciclos

| Métrica | Media | Desv. estándar | Mínimo | Máximo |
|---|---:|---:|---:|---:|
| Avance por ciclo (m) | 0.006414 | 0.003169 | 0.004996 | 0.012084 |
| Velocidad media (m/s) | 0.001114 | 0.000550 | 0.000867 | 0.002098 |
| Excursión lateral (m) | 0.003171 | 0.000554 | 0.002180 | 0.003421 |
| Altura media (m) | 0.219761 | 0.000011 | 0.219744 | 0.219771 |
| Roll máximo absoluto (grados) | 0.925350 | 0.000112 | 0.925216 | 0.925509 |
| Pitch máximo absoluto (grados) | 2.356910 | 0.000028 | 2.356867 | 2.356942 |
| Salto articular máximo (rad) | 0.017287 | 0.000541 | 0.016767 | 0.018166 |

## Resultado

Los 5 ciclos completos acumularon 0.032072 m de avance medido entre la primera y última muestra de cada ciclo. 
No se cambiaron paso, elevación ni duración de muestra durante la ventana.

La continuidad articular se expresa como el mayor salto absoluto entre dos muestras consecutivas de una misma articulación. La velocidad articular máxima se obtiene del campo medido `joint_velocities_rad_s`.

Archivos generados:

- `metricas_por_ciclo.csv`
- `series_temporales.png`
- `resumen_por_ciclo.png`
- `INFORME_ANALISIS.md`
