# Análisis automático de la línea base de gateo

- Bolsa: `/home/pavilion/Documentos/Cuadrupedo/Experimentos/rosbag2/repeticion_cadencia_corregida_20260814_1100`.
- Ventana gateo--stand: 57.121500323 s.
- Duración nominal configurada por ciclo: 4.32 s.
- Duración observada media por ciclo: 4.320003 s.
- Ciclos completos analizados: 13.
- Activaciones verdaderas del supervisor: 0.

## Estadísticos entre ciclos

| Métrica | Media | Desv. estándar | Mínimo | Máximo |
|---|---:|---:|---:|---:|
| Avance por ciclo (m) | 0.022101 | 0.004635 | 0.006712 | 0.023847 |
| Velocidad media (m/s) | 0.005116 | 0.001073 | 0.001553 | 0.005521 |
| Excursión lateral (m) | 0.014745 | 0.001409 | 0.010060 | 0.015234 |
| Altura media (m) | 0.223816 | 0.000069 | 0.223586 | 0.223839 |
| Roll máximo absoluto (grados) | 2.233728 | 0.000402 | 2.232918 | 2.234169 |
| Pitch máximo absoluto (grados) | 4.366448 | 0.002355 | 4.359374 | 4.368325 |
| Salto articular máximo (rad) | 0.018582 | 0.000866 | 0.018238 | 0.021455 |

## Resultado

Los 13 ciclos completos acumularon 0.287317 m de avance medido entre la primera y última muestra de cada ciclo. 
No se cambiaron paso, elevación ni duración de muestra durante la ventana.

La continuidad articular se expresa como el mayor salto absoluto entre dos muestras consecutivas de una misma articulación. La velocidad articular máxima se obtiene del campo medido `joint_velocities_rad_s`.

Archivos generados:

- `metricas_por_ciclo.csv`
- `series_temporales.png`
- `resumen_por_ciclo.png`
- `INFORME_ANALISIS.md`
