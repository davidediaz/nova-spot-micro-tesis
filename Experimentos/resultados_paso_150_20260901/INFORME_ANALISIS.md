# Análisis automático de marcha paso

- Bolsa: `Experimentos/rosbag2/velocidad_paso_150_20260901`.
- Ventana marcha paso--stand: 101.203232793 s.
- Duración nominal configurada por ciclo: 3.84 s.
- Duración observada media por ciclo: 3.840720 s.
- Ciclos completos analizados: 26.
- Activaciones verdaderas del supervisor: 0.

## Estadísticos entre ciclos

| Métrica | Media | Desv. estándar | Mínimo | Máximo |
|---|---:|---:|---:|---:|
| Avance por ciclo (m) | 0.020921 | 0.001952 | 0.011508 | 0.022016 |
| Velocidad media (m/s) | 0.005448 | 0.000511 | 0.002982 | 0.005733 |
| Excursión lateral (m) | 0.005111 | 0.000186 | 0.004961 | 0.005993 |
| Altura media (m) | 0.224095 | 0.000048 | 0.223859 | 0.224105 |
| Roll máximo absoluto (grados) | 1.233465 | 0.004594 | 1.211676 | 1.238311 |
| Pitch máximo absoluto (grados) | 2.416679 | 0.004724 | 2.414308 | 2.435757 |
| Salto articular máximo (rad) | 0.010987 | 0.000775 | 0.010835 | 0.014785 |

## Resultado

Los 26 ciclos completos acumularon 0.543943 m de avance medido entre la primera y última muestra de cada ciclo. 
No se cambiaron paso, elevación ni duración de muestra durante la ventana.

La continuidad articular se expresa como el mayor salto absoluto entre dos muestras consecutivas de una misma articulación. La velocidad articular máxima se obtiene del campo medido `joint_velocities_rad_s`.

Archivos generados:

- `metricas_por_ciclo.csv`
- `series_temporales.png`
- `resumen_por_ciclo.png`
- `INFORME_ANALISIS.md`
