# Análisis automático de gateo

- Bolsa: `Experimentos/rosbag2/velocidad_gateo_200_20260901`.
- Ventana gateo--stand: 73.480599220 s.
- Duración nominal configurada por ciclo: 2.16 s.
- Duración observada media por ciclo: 2.157641 s.
- Ciclos completos analizados: 34.
- Activaciones verdaderas del supervisor: 0.

## Estadísticos entre ciclos

| Métrica | Media | Desv. estándar | Mínimo | Máximo |
|---|---:|---:|---:|---:|
| Avance por ciclo (m) | 0.022160 | 0.001965 | 0.012061 | 0.024273 |
| Velocidad media (m/s) | 0.010266 | 0.000876 | 0.005799 | 0.011237 |
| Excursión lateral (m) | 0.006906 | 0.000274 | 0.006128 | 0.007235 |
| Altura media (m) | 0.224048 | 0.000038 | 0.223837 | 0.224072 |
| Roll máximo absoluto (grados) | 1.758665 | 0.016559 | 1.666548 | 1.768048 |
| Pitch máximo absoluto (grados) | 3.550226 | 0.013460 | 3.529067 | 3.612654 |
| Salto articular máximo (rad) | 0.025527 | 0.000086 | 0.025352 | 0.025831 |

## Resultado

Los 34 ciclos completos acumularon 0.753456 m de avance medido entre la primera y última muestra de cada ciclo. 
No se cambiaron paso, elevación ni duración de muestra durante la ventana.

La continuidad articular se expresa como el mayor salto absoluto entre dos muestras consecutivas de una misma articulación. La velocidad articular máxima se obtiene del campo medido `joint_velocities_rad_s`.

Archivos generados:

- `metricas_por_ciclo.csv`
- `series_temporales.png`
- `resumen_por_ciclo.png`
- `INFORME_ANALISIS.md`
