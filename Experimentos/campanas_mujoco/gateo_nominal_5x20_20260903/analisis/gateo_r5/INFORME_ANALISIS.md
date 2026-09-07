# Análisis automático de gateo

- Bolsa: `Experimentos/campanas_mujoco/gateo_nominal_5x20_20260903/rosbag2/gateo_r5`.
- Ventana gateo--stand: 92.441498874 s.
- Duración nominal configurada por ciclo: 4.32 s.
- Duración observada media por ciclo: 4.312382 s.
- Ciclos completos analizados: 21.
- Activaciones verdaderas del supervisor: 0.

## Estadísticos entre ciclos

| Métrica | Media | Desv. estándar | Mínimo | Máximo |
|---|---:|---:|---:|---:|
| Avance por ciclo (m) | 0.006191 | 0.000423 | 0.004348 | 0.006321 |
| Velocidad media (m/s) | 0.001435 | 0.000090 | 0.001045 | 0.001463 |
| Excursión lateral (m) | 0.004176 | 0.000249 | 0.003091 | 0.004271 |
| Altura media (m) | 0.220968 | 0.000011 | 0.220941 | 0.220986 |
| Roll máximo absoluto (grados) | 1.535680 | 0.000253 | 1.535374 | 1.536137 |
| Pitch máximo absoluto (grados) | 3.605597 | 0.000997 | 3.603888 | 3.607944 |
| Salto articular máximo (rad) | 0.028137 | 0.002589 | 0.022592 | 0.031046 |

## Resultado

Los 21 ciclos completos acumularon 0.130016 m de avance medido entre la primera y última muestra de cada ciclo. 
No se cambiaron paso, elevación ni duración de muestra durante la ventana.

La continuidad articular se expresa como el mayor salto absoluto entre dos muestras consecutivas de una misma articulación. La velocidad articular máxima se obtiene del campo medido `joint_velocities_rad_s`.

Archivos generados:

- `metricas_por_ciclo.csv`
- `series_temporales.png`
- `resumen_por_ciclo.png`
- `INFORME_ANALISIS.md`
