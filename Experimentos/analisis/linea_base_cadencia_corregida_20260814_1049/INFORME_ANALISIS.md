# Análisis automático de la línea base de gateo

- Bolsa: `/home/pavilion/Documentos/Cuadrupedo/Experimentos/rosbag2/linea_base_cadencia_corregida_20260814_1049`.
- Ventana gateo--stand: 57.014709063 s.
- Duración nominal configurada por ciclo: 4.32 s.
- Duración observada media por ciclo: 4.320013 s.
- Ciclos completos analizados: 13.
- Activaciones verdaderas del supervisor: 0.

## Estadísticos entre ciclos

| Métrica | Media | Desv. estándar | Mínimo | Máximo |
|---|---:|---:|---:|---:|
| Avance por ciclo (m) | 0.022053 | 0.004644 | 0.006622 | 0.023720 |
| Velocidad media (m/s) | 0.005105 | 0.001075 | 0.001533 | 0.005491 |
| Excursión lateral (m) | 0.014740 | 0.001418 | 0.010022 | 0.015194 |
| Altura media (m) | 0.223818 | 0.000067 | 0.223593 | 0.223841 |
| Roll máximo absoluto (grados) | 2.233075 | 0.002086 | 2.226301 | 2.234086 |
| Pitch máximo absoluto (grados) | 4.364926 | 0.004356 | 4.353124 | 4.367932 |
| Salto articular máximo (rad) | 0.018589 | 0.000912 | 0.018238 | 0.021620 |

## Resultado

Los 13 ciclos completos acumularon 0.286683 m de avance medido entre la primera y última muestra de cada ciclo. 
No se cambiaron paso, elevación ni duración de muestra durante la ventana.

La continuidad articular se expresa como el mayor salto absoluto entre dos muestras consecutivas de una misma articulación. La velocidad articular máxima se obtiene del campo medido `joint_velocities_rad_s`.

Archivos generados:

- `metricas_por_ciclo.csv`
- `series_temporales.png`
- `resumen_por_ciclo.png`
- `INFORME_ANALISIS.md`
