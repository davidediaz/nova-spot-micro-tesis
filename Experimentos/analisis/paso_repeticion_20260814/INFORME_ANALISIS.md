# Análisis automático de marcha paso

- Bolsa: `/home/pavilion/Documentos/Cuadrupedo/Experimentos/rosbag2/paso_repeticion_20260814`.
- Ventana marcha paso--stand: 71.058031710 s.
- Duración nominal configurada por ciclo: 5.76 s.
- Duración observada media por ciclo: 5.759997 s.
- Ciclos completos analizados: 12.
- Activaciones verdaderas del supervisor: 0.

## Estadísticos entre ciclos

| Métrica | Media | Desv. estándar | Mínimo | Máximo |
|---|---:|---:|---:|---:|
| Avance por ciclo (m) | 0.021540 | 0.001608 | 0.016467 | 0.022421 |
| Velocidad media (m/s) | 0.003740 | 0.000279 | 0.002859 | 0.003893 |
| Excursión lateral (m) | 0.005429 | 0.000051 | 0.005371 | 0.005572 |
| Altura media (m) | 0.224105 | 0.000068 | 0.223890 | 0.224126 |
| Roll máximo absoluto (grados) | 1.279899 | 0.006662 | 1.258808 | 1.282174 |
| Pitch máximo absoluto (grados) | 2.487937 | 0.014227 | 2.483443 | 2.533106 |
| Salto articular máximo (rad) | 0.008418 | 0.000193 | 0.008354 | 0.009027 |

## Resultado

Los 12 ciclos completos acumularon 0.258483 m de avance medido entre la primera y última muestra de cada ciclo. 
No se cambiaron paso, elevación ni duración de muestra durante la ventana.

La continuidad articular se expresa como el mayor salto absoluto entre dos muestras consecutivas de una misma articulación. La velocidad articular máxima se obtiene del campo medido `joint_velocities_rad_s`.

Archivos generados:

- `metricas_por_ciclo.csv`
- `series_temporales.png`
- `resumen_por_ciclo.png`
- `INFORME_ANALISIS.md`
