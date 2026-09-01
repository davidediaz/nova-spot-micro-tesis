# Análisis automático de marcha paso

- Bolsa: `Experimentos/rosbag2/cierre_paso_r2_20260901`.
- Ventana marcha paso--stand: 131.922729715 s.
- Duración nominal configurada por ciclo: 5.76 s.
- Duración observada media por ciclo: 5.760001 s.
- Ciclos completos analizados: 22.
- Activaciones verdaderas del supervisor: 0.

## Estadísticos entre ciclos

| Métrica | Media | Desv. estándar | Mínimo | Máximo |
|---|---:|---:|---:|---:|
| Avance por ciclo (m) | 0.021670 | 0.001481 | 0.015080 | 0.022223 |
| Velocidad media (m/s) | 0.003762 | 0.000257 | 0.002618 | 0.003858 |
| Excursión lateral (m) | 0.005541 | 0.000571 | 0.005369 | 0.008093 |
| Altura media (m) | 0.224115 | 0.000050 | 0.223893 | 0.224126 |
| Roll máximo absoluto (grados) | 1.280899 | 0.004858 | 1.259411 | 1.283791 |
| Pitch máximo absoluto (grados) | 2.486195 | 0.010536 | 2.483173 | 2.533247 |
| Salto articular máximo (rad) | 0.008411 | 0.000253 | 0.008302 | 0.009539 |

## Resultado

Los 22 ciclos completos acumularon 0.476734 m de avance medido entre la primera y última muestra de cada ciclo. 
No se cambiaron paso, elevación ni duración de muestra durante la ventana.

La continuidad articular se expresa como el mayor salto absoluto entre dos muestras consecutivas de una misma articulación. La velocidad articular máxima se obtiene del campo medido `joint_velocities_rad_s`.

Archivos generados:

- `metricas_por_ciclo.csv`
- `series_temporales.png`
- `resumen_por_ciclo.png`
- `INFORME_ANALISIS.md`
