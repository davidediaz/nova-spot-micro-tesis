# Análisis automático de marcha paso

- Bolsa: `/home/pavilion/Documentos/Cuadrupedo/Experimentos/campana_ppo_gazebo_20260903/ppo_gazebo_05`.
- Ventana marcha paso--stand: 63.470874810 s.
- Duración nominal configurada por ciclo: 5.76 s.
- Duración observada media por ciclo: 5.760081 s.
- Ciclos completos analizados: 10.
- Activaciones verdaderas del supervisor: 0.

## Estadísticos entre ciclos

| Métrica | Media | Desv. estándar | Mínimo | Máximo |
|---|---:|---:|---:|---:|
| Avance por ciclo (m) | 0.001805 | 0.001132 | 0.000293 | 0.003775 |
| Velocidad media (m/s) | 0.000313 | 0.000197 | 0.000051 | 0.000655 |
| Excursión lateral (m) | 0.009135 | 0.001068 | 0.007776 | 0.010551 |
| Altura media (m) | 0.225626 | 0.000292 | 0.224940 | 0.225984 |
| Roll máximo absoluto (grados) | 3.175967 | 0.076638 | 3.102828 | 3.324276 |
| Pitch máximo absoluto (grados) | 3.411310 | 0.104122 | 3.319569 | 3.563214 |
| Salto articular máximo (rad) | 0.008698 | 0.001659 | 0.007314 | 0.011884 |

## Resultado

Los 10 ciclos completos acumularon 0.018048 m de avance medido entre la primera y última muestra de cada ciclo. 
No se cambiaron paso, elevación ni duración de muestra durante la ventana.

La continuidad articular se expresa como el mayor salto absoluto entre dos muestras consecutivas de una misma articulación. La velocidad articular máxima se obtiene del campo medido `joint_velocities_rad_s`.

Archivos generados:

- `metricas_por_ciclo.csv`
- `series_temporales.png`
- `resumen_por_ciclo.png`
- `INFORME_ANALISIS.md`
