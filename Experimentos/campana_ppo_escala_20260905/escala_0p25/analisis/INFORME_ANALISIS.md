# Análisis automático de marcha paso

- Bolsa: `/home/pavilion/Documentos/Cuadrupedo/Experimentos/campana_ppo_escala_20260905/escala_0p25`.
- Ventana marcha paso--stand: 61.016695621 s.
- Duración nominal configurada por ciclo: 5.76 s.
- Duración observada media por ciclo: 5.761897 s.
- Ciclos completos analizados: 10.
- Activaciones verdaderas del supervisor: 0.

## Estadísticos entre ciclos

| Métrica | Media | Desv. estándar | Mínimo | Máximo |
|---|---:|---:|---:|---:|
| Avance por ciclo (m) | 0.016679 | 0.005116 | 0.004902 | 0.021206 |
| Velocidad media (m/s) | 0.002895 | 0.000889 | 0.000848 | 0.003682 |
| Excursión lateral (m) | 0.005695 | 0.000482 | 0.005060 | 0.006573 |
| Altura media (m) | 0.224669 | 0.001170 | 0.223059 | 0.225931 |
| Roll máximo absoluto (grados) | 2.163882 | 0.143149 | 1.821978 | 2.273704 |
| Pitch máximo absoluto (grados) | 2.551656 | 0.110319 | 2.447937 | 2.800285 |
| Salto articular máximo (rad) | 0.007476 | 0.000116 | 0.007346 | 0.007732 |

## Resultado

Los 10 ciclos completos acumularon 0.166794 m de avance medido entre la primera y última muestra de cada ciclo. 
No se cambiaron paso, elevación ni duración de muestra durante la ventana.

La continuidad articular se expresa como el mayor salto absoluto entre dos muestras consecutivas de una misma articulación. La velocidad articular máxima se obtiene del campo medido `joint_velocities_rad_s`.

Archivos generados:

- `metricas_por_ciclo.csv`
- `series_temporales.png`
- `resumen_por_ciclo.png`
- `INFORME_ANALISIS.md`
