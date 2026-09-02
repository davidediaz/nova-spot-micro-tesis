# Análisis automático de marcha paso

- Bolsa: `/home/pavilion/Documentos/Cuadrupedo/Experimentos/campana_ppo_gazebo_20260903/ppo_gazebo_02`.
- Ventana marcha paso--stand: 60.999224851 s.
- Duración nominal configurada por ciclo: 5.76 s.
- Duración observada media por ciclo: 5.759990 s.
- Ciclos completos analizados: 10.
- Activaciones verdaderas del supervisor: 0.

## Estadísticos entre ciclos

| Métrica | Media | Desv. estándar | Mínimo | Máximo |
|---|---:|---:|---:|---:|
| Avance por ciclo (m) | 0.000962 | 0.001369 | -0.000739 | 0.003109 |
| Velocidad media (m/s) | 0.000167 | 0.000238 | -0.000128 | 0.000540 |
| Excursión lateral (m) | 0.009544 | 0.000649 | 0.008268 | 0.010336 |
| Altura media (m) | 0.225282 | 0.000315 | 0.224832 | 0.225842 |
| Roll máximo absoluto (grados) | 3.196453 | 0.076016 | 3.089701 | 3.288174 |
| Pitch máximo absoluto (grados) | 3.485513 | 0.142362 | 3.284039 | 3.651007 |
| Salto articular máximo (rad) | 0.008004 | 0.000497 | 0.007582 | 0.009023 |

## Resultado

Los 10 ciclos completos acumularon 0.009624 m de avance medido entre la primera y última muestra de cada ciclo. 
No se cambiaron paso, elevación ni duración de muestra durante la ventana.

La continuidad articular se expresa como el mayor salto absoluto entre dos muestras consecutivas de una misma articulación. La velocidad articular máxima se obtiene del campo medido `joint_velocities_rad_s`.

Archivos generados:

- `metricas_por_ciclo.csv`
- `series_temporales.png`
- `resumen_por_ciclo.png`
- `INFORME_ANALISIS.md`
