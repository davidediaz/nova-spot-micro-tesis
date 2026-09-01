# Análisis automático de marcha paso

- Bolsa: `Experimentos/rosbag2/cierre_paso_r1_20260901`.
- Ventana marcha paso--stand: 122.092760058 s.
- Duración nominal configurada por ciclo: 5.76 s.
- Duración observada media por ciclo: 5.760859 s.
- Ciclos completos analizados: 21.
- Activaciones verdaderas del supervisor: 0.

## Estadísticos entre ciclos

| Métrica | Media | Desv. estándar | Mínimo | Máximo |
|---|---:|---:|---:|---:|
| Avance por ciclo (m) | 0.021663 | 0.001541 | 0.014971 | 0.022301 |
| Velocidad media (m/s) | 0.003760 | 0.000269 | 0.002591 | 0.003872 |
| Excursión lateral (m) | 0.005553 | 0.000585 | 0.005384 | 0.008107 |
| Altura media (m) | 0.224115 | 0.000050 | 0.223897 | 0.224127 |
| Roll máximo absoluto (grados) | 1.280799 | 0.004926 | 1.259369 | 1.282188 |
| Pitch máximo absoluto (grados) | 2.485997 | 0.010791 | 2.482666 | 2.533070 |
| Salto articular máximo (rad) | 0.008427 | 0.000337 | 0.008354 | 0.009900 |

## Resultado

Los 21 ciclos completos acumularon 0.454915 m de avance medido entre la primera y última muestra de cada ciclo. 
No se cambiaron paso, elevación ni duración de muestra durante la ventana.

La continuidad articular se expresa como el mayor salto absoluto entre dos muestras consecutivas de una misma articulación. La velocidad articular máxima se obtiene del campo medido `joint_velocities_rad_s`.

Archivos generados:

- `metricas_por_ciclo.csv`
- `series_temporales.png`
- `resumen_por_ciclo.png`
- `INFORME_ANALISIS.md`
