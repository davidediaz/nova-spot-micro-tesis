# Análisis automático de marcha paso

- Bolsa: `/home/pavilion/Documentos/Cuadrupedo/Experimentos/campana_ppo_gazebo_20260903/ppo_gazebo_03`.
- Ventana marcha paso--stand: 61.008249094 s.
- Duración nominal configurada por ciclo: 5.76 s.
- Duración observada media por ciclo: 5.760076 s.
- Ciclos completos analizados: 10.
- Activaciones verdaderas del supervisor: 0.

## Estadísticos entre ciclos

| Métrica | Media | Desv. estándar | Mínimo | Máximo |
|---|---:|---:|---:|---:|
| Avance por ciclo (m) | 0.000906 | 0.001282 | -0.000875 | 0.002495 |
| Velocidad media (m/s) | 0.000157 | 0.000223 | -0.000152 | 0.000433 |
| Excursión lateral (m) | 0.009891 | 0.000608 | 0.009021 | 0.010698 |
| Altura media (m) | 0.225138 | 0.000226 | 0.224800 | 0.225428 |
| Roll máximo absoluto (grados) | 3.257114 | 0.140113 | 3.106546 | 3.519228 |
| Pitch máximo absoluto (grados) | 3.468501 | 0.129865 | 3.290235 | 3.675692 |
| Salto articular máximo (rad) | 0.007621 | 0.000135 | 0.007297 | 0.007791 |

## Resultado

Los 10 ciclos completos acumularon 0.009055 m de avance medido entre la primera y última muestra de cada ciclo. 
No se cambiaron paso, elevación ni duración de muestra durante la ventana.

La continuidad articular se expresa como el mayor salto absoluto entre dos muestras consecutivas de una misma articulación. La velocidad articular máxima se obtiene del campo medido `joint_velocities_rad_s`.

Archivos generados:

- `metricas_por_ciclo.csv`
- `series_temporales.png`
- `resumen_por_ciclo.png`
- `INFORME_ANALISIS.md`
