# Análisis automático de marcha paso

- Bolsa: `/home/pavilion/Documentos/Cuadrupedo/Experimentos/rosbag2/paso_exploratorio_20260814`.
- Ventana marcha paso--stand: 26.123082950 s.
- Duración nominal configurada por ciclo: 5.76 s.
- Duración observada media por ciclo: 5.759993 s.
- Ciclos completos analizados: 4.
- Activaciones verdaderas del supervisor: 0.

## Estadísticos entre ciclos

| Métrica | Media | Desv. estándar | Mínimo | Máximo |
|---|---:|---:|---:|---:|
| Avance por ciclo (m) | 0.020730 | 0.002471 | 0.017031 | 0.022155 |
| Velocidad media (m/s) | 0.003599 | 0.000429 | 0.002957 | 0.003847 |
| Excursión lateral (m) | 0.005490 | 0.000044 | 0.005432 | 0.005525 |
| Altura media (m) | 0.224065 | 0.000116 | 0.223891 | 0.224125 |
| Roll máximo absoluto (grados) | 1.275295 | 0.012168 | 1.257066 | 1.282097 |
| Pitch máximo absoluto (grados) | 2.496521 | 0.024834 | 2.483836 | 2.533770 |
| Salto articular máximo (rad) | 0.008528 | 0.000293 | 0.008354 | 0.008962 |

## Resultado

Los 4 ciclos completos acumularon 0.082921 m de avance medido entre la primera y última muestra de cada ciclo. 
No se cambiaron paso, elevación ni duración de muestra durante la ventana.

La continuidad articular se expresa como el mayor salto absoluto entre dos muestras consecutivas de una misma articulación. La velocidad articular máxima se obtiene del campo medido `joint_velocities_rad_s`.

Archivos generados:

- `metricas_por_ciclo.csv`
- `series_temporales.png`
- `resumen_por_ciclo.png`
- `INFORME_ANALISIS.md`
