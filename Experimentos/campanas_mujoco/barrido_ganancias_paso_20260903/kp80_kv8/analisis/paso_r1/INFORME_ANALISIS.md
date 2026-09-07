# Análisis automático de marcha paso

- Bolsa: `Experimentos/campanas_mujoco/barrido_ganancias_paso_20260903/kp80_kv8/rosbag2/paso_r1`.
- Ventana marcha paso--stand: 29.989231773 s.
- Duración nominal configurada por ciclo: 5.76 s.
- Duración observada media por ciclo: 5.759995 s.
- Ciclos completos analizados: 5.
- Activaciones verdaderas del supervisor: 0.

## Estadísticos entre ciclos

| Métrica | Media | Desv. estándar | Mínimo | Máximo |
|---|---:|---:|---:|---:|
| Avance por ciclo (m) | 0.011193 | 0.002903 | 0.009853 | 0.016386 |
| Velocidad media (m/s) | 0.001943 | 0.000504 | 0.001711 | 0.002845 |
| Excursión lateral (m) | 0.004743 | 0.000659 | 0.003565 | 0.005068 |
| Altura media (m) | 0.222100 | 0.000005 | 0.222095 | 0.222107 |
| Roll máximo absoluto (grados) | 1.510939 | 0.000024 | 1.510900 | 1.510964 |
| Pitch máximo absoluto (grados) | 3.171321 | 0.000019 | 3.171299 | 3.171346 |
| Salto articular máximo (rad) | 0.016495 | 0.002697 | 0.012106 | 0.019487 |

## Resultado

Los 5 ciclos completos acumularon 0.055966 m de avance medido entre la primera y última muestra de cada ciclo. 
No se cambiaron paso, elevación ni duración de muestra durante la ventana.

La continuidad articular se expresa como el mayor salto absoluto entre dos muestras consecutivas de una misma articulación. La velocidad articular máxima se obtiene del campo medido `joint_velocities_rad_s`.

Archivos generados:

- `metricas_por_ciclo.csv`
- `series_temporales.png`
- `resumen_por_ciclo.png`
- `INFORME_ANALISIS.md`
