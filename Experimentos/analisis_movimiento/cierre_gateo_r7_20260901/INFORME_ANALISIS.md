# Análisis automático de gateo

- Bolsa: `Experimentos/rosbag2/cierre_gateo_r7_20260901`.
- Ventana gateo--stand: 125.568453168 s.
- Duración nominal configurada por ciclo: 4.32 s.
- Duración observada media por ciclo: 4.320002 s.
- Ciclos completos analizados: 29.
- Activaciones verdaderas del supervisor: 0.

## Estadísticos entre ciclos

| Métrica | Media | Desv. estándar | Mínimo | Máximo |
|---|---:|---:|---:|---:|
| Avance por ciclo (m) | 0.023824 | 0.000998 | 0.019751 | 0.025820 |
| Velocidad media (m/s) | 0.005515 | 0.000231 | 0.004572 | 0.005977 |
| Excursión lateral (m) | 0.005745 | 0.000232 | 0.005531 | 0.006544 |
| Altura media (m) | 0.224174 | 0.000023 | 0.224053 | 0.224181 |
| Roll máximo absoluto (grados) | 2.072533 | 0.003381 | 2.060111 | 2.074620 |
| Pitch máximo absoluto (grados) | 4.097013 | 0.001646 | 4.093064 | 4.101246 |
| Salto articular máximo (rad) | 0.019556 | 0.000174 | 0.019130 | 0.019632 |

## Resultado

Los 29 ciclos completos acumularon 0.690906 m de avance medido entre la primera y última muestra de cada ciclo. 
No se cambiaron paso, elevación ni duración de muestra durante la ventana.

La continuidad articular se expresa como el mayor salto absoluto entre dos muestras consecutivas de una misma articulación. La velocidad articular máxima se obtiene del campo medido `joint_velocities_rad_s`.

Archivos generados:

- `metricas_por_ciclo.csv`
- `series_temporales.png`
- `resumen_por_ciclo.png`
- `INFORME_ANALISIS.md`
