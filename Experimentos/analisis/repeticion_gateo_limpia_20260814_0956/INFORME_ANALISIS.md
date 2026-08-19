# Análisis automático de la línea base de gateo

- Bolsa: `/home/pavilion/Documentos/Cuadrupedo/Experimentos/rosbag2/repeticion_gateo_limpia_20260814_0956`.
- Ventana gateo--stand: 174.706623946 s.
- Duración nominal configurada por ciclo: 4.32 s.
- Duración observada media por ciclo: 4.793341 s.
- Ciclos completos analizados: 36.
- Activaciones verdaderas del supervisor: 0.

## Estadísticos entre ciclos

| Métrica | Media | Desv. estándar | Mínimo | Máximo |
|---|---:|---:|---:|---:|
| Avance por ciclo (m) | 0.023332 | 0.002678 | 0.007767 | 0.024173 |
| Velocidad media (m/s) | 0.004868 | 0.000559 | 0.001618 | 0.005036 |
| Excursión lateral (m) | 0.014837 | 0.000803 | 0.010164 | 0.015096 |
| Altura media (m) | 0.223841 | 0.000045 | 0.223579 | 0.223853 |
| Roll máximo absoluto (grados) | 2.255411 | 0.001129 | 2.254505 | 2.261803 |
| Pitch máximo absoluto (grados) | 4.411172 | 0.003247 | 4.400767 | 4.425055 |
| Salto articular máximo (rad) | 0.018054 | 0.000264 | 0.017919 | 0.019530 |

## Resultado

Los 36 ciclos completos acumularon 0.839969 m de avance medido entre la primera y última muestra de cada ciclo. 
No se cambiaron paso, elevación ni duración de muestra durante la ventana.

La continuidad articular se expresa como el mayor salto absoluto entre dos muestras consecutivas de una misma articulación. La velocidad articular máxima se obtiene del campo medido `joint_velocities_rad_s`.

Archivos generados:

- `metricas_por_ciclo.csv`
- `series_temporales.png`
- `resumen_por_ciclo.png`
- `INFORME_ANALISIS.md`
