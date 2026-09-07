# Análisis automático de marcha paso

- Bolsa: `Experimentos/campanas_mujoco/barrido_friccion_paso_r2_20260903/friction_09/rosbag2/paso_r1`.
- Ventana marcha paso--stand: 29.769792630 s.
- Duración nominal configurada por ciclo: 5.76 s.
- Duración observada media por ciclo: 5.760021 s.
- Ciclos completos analizados: 5.
- Activaciones verdaderas del supervisor: 0.

## Estadísticos entre ciclos

| Métrica | Media | Desv. estándar | Mínimo | Máximo |
|---|---:|---:|---:|---:|
| Avance por ciclo (m) | 0.008509 | 0.002975 | 0.007170 | 0.013830 |
| Velocidad media (m/s) | 0.001477 | 0.000516 | 0.001245 | 0.002401 |
| Excursión lateral (m) | 0.003465 | 0.000497 | 0.002576 | 0.003693 |
| Altura media (m) | 0.220631 | 0.000009 | 0.220619 | 0.220643 |
| Roll máximo absoluto (grados) | 1.107972 | 0.000029 | 1.107926 | 1.107999 |
| Pitch máximo absoluto (grados) | 2.580683 | 0.000155 | 2.580485 | 2.580842 |
| Salto articular máximo (rad) | 0.015155 | 0.000900 | 0.013897 | 0.016006 |

## Resultado

Los 5 ciclos completos acumularon 0.042544 m de avance medido entre la primera y última muestra de cada ciclo. 
No se cambiaron paso, elevación ni duración de muestra durante la ventana.

La continuidad articular se expresa como el mayor salto absoluto entre dos muestras consecutivas de una misma articulación. La velocidad articular máxima se obtiene del campo medido `joint_velocities_rad_s`.

Archivos generados:

- `metricas_por_ciclo.csv`
- `series_temporales.png`
- `resumen_por_ciclo.png`
- `INFORME_ANALISIS.md`
