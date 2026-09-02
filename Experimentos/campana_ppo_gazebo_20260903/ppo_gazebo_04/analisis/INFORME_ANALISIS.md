# Análisis automático de marcha paso

- Bolsa: `/home/pavilion/Documentos/Cuadrupedo/Experimentos/campana_ppo_gazebo_20260903/ppo_gazebo_04`.
- Ventana marcha paso--stand: 62.970607659 s.
- Duración nominal configurada por ciclo: 5.76 s.
- Duración observada media por ciclo: 5.759969 s.
- Ciclos completos analizados: 10.
- Activaciones verdaderas del supervisor: 0.

## Estadísticos entre ciclos

| Métrica | Media | Desv. estándar | Mínimo | Máximo |
|---|---:|---:|---:|---:|
| Avance por ciclo (m) | 0.000397 | 0.000798 | -0.001078 | 0.001439 |
| Velocidad media (m/s) | 0.000069 | 0.000139 | -0.000187 | 0.000250 |
| Excursión lateral (m) | 0.009855 | 0.000663 | 0.008933 | 0.011230 |
| Altura media (m) | 0.225059 | 0.000146 | 0.224789 | 0.225266 |
| Roll máximo absoluto (grados) | 3.225011 | 0.043051 | 3.166878 | 3.285423 |
| Pitch máximo absoluto (grados) | 3.442334 | 0.141601 | 3.260503 | 3.611786 |
| Salto articular máximo (rad) | 0.007693 | 0.000145 | 0.007451 | 0.007911 |

## Resultado

Los 10 ciclos completos acumularon 0.003971 m de avance medido entre la primera y última muestra de cada ciclo. 
No se cambiaron paso, elevación ni duración de muestra durante la ventana.

La continuidad articular se expresa como el mayor salto absoluto entre dos muestras consecutivas de una misma articulación. La velocidad articular máxima se obtiene del campo medido `joint_velocities_rad_s`.

Archivos generados:

- `metricas_por_ciclo.csv`
- `series_temporales.png`
- `resumen_por_ciclo.png`
- `INFORME_ANALISIS.md`
