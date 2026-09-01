# Análisis automático de gateo

- Bolsa: `Experimentos/rosbag2/preload_gateo_150_20260901`.
- Ventana gateo--stand: 79.161569566 s.
- Duración nominal configurada por ciclo: 4.32 s.
- Duración observada media por ciclo: 4.319985 s.
- Ciclos completos analizados: 18.
- Activaciones verdaderas del supervisor: 0.

## Estadísticos entre ciclos

| Métrica | Media | Desv. estándar | Mínimo | Máximo |
|---|---:|---:|---:|---:|
| Avance por ciclo (m) | 0.023192 | 0.001990 | 0.015429 | 0.024385 |
| Velocidad media (m/s) | 0.005369 | 0.000461 | 0.003571 | 0.005644 |
| Excursión lateral (m) | 0.007166 | 0.000287 | 0.006090 | 0.007426 |
| Altura media (m) | 0.224191 | 0.000050 | 0.223990 | 0.224210 |
| Roll máximo absoluto (grados) | 2.096164 | 0.005707 | 2.083202 | 2.105917 |
| Pitch máximo absoluto (grados) | 4.167473 | 0.009135 | 4.155509 | 4.200784 |
| Salto articular máximo (rad) | 0.019615 | 0.000095 | 0.019254 | 0.019711 |

## Resultado

Los 18 ciclos completos acumularon 0.417454 m de avance medido entre la primera y última muestra de cada ciclo. 
No se cambiaron paso, elevación ni duración de muestra durante la ventana.

La continuidad articular se expresa como el mayor salto absoluto entre dos muestras consecutivas de una misma articulación. La velocidad articular máxima se obtiene del campo medido `joint_velocities_rad_s`.

Archivos generados:

- `metricas_por_ciclo.csv`
- `series_temporales.png`
- `resumen_por_ciclo.png`
- `INFORME_ANALISIS.md`
