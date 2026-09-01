# Análisis automático de gateo

- Bolsa: `Experimentos/rosbag2/liberacion_gateo_080_20260901`.
- Ventana gateo--stand: 79.444903400 s.
- Duración nominal configurada por ciclo: 4.32 s.
- Duración observada media por ciclo: 4.320025 s.
- Ciclos completos analizados: 18.
- Activaciones verdaderas del supervisor: 0.

## Estadísticos entre ciclos

| Métrica | Media | Desv. estándar | Mínimo | Máximo |
|---|---:|---:|---:|---:|
| Avance por ciclo (m) | 0.023597 | 0.001133 | 0.019461 | 0.024710 |
| Velocidad media (m/s) | 0.005462 | 0.000262 | 0.004505 | 0.005720 |
| Excursión lateral (m) | 0.005802 | 0.000225 | 0.005599 | 0.006601 |
| Altura media (m) | 0.224166 | 0.000031 | 0.224042 | 0.224176 |
| Roll máximo absoluto (grados) | 2.106043 | 0.004330 | 2.092981 | 2.109288 |
| Pitch máximo absoluto (grados) | 4.176105 | 0.002611 | 4.170083 | 4.179447 |
| Salto articular máximo (rad) | 0.020331 | 0.000118 | 0.020016 | 0.020429 |

## Resultado

Los 18 ciclos completos acumularon 0.424747 m de avance medido entre la primera y última muestra de cada ciclo. 
No se cambiaron paso, elevación ni duración de muestra durante la ventana.

La continuidad articular se expresa como el mayor salto absoluto entre dos muestras consecutivas de una misma articulación. La velocidad articular máxima se obtiene del campo medido `joint_velocities_rad_s`.

Archivos generados:

- `metricas_por_ciclo.csv`
- `series_temporales.png`
- `resumen_por_ciclo.png`
- `INFORME_ANALISIS.md`
