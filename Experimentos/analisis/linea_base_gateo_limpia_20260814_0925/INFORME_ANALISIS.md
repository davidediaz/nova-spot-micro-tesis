# Análisis automático de la línea base de gateo

- Bolsa: `/home/pavilion/Documentos/Cuadrupedo/Experimentos/rosbag2/linea_base_gateo_limpia_20260814_0925`.
- Ventana gateo--stand: 98.978769031 s.
- Duración nominal configurada por ciclo: 4.32 s.
- Duración observada media por ciclo: 4.797996 s.
- Ciclos completos analizados: 20.
- Activaciones verdaderas del supervisor: 0.

## Estadísticos entre ciclos

| Métrica | Media | Desv. estándar | Mínimo | Máximo |
|---|---:|---:|---:|---:|
| Avance por ciclo (m) | 0.022908 | 0.003978 | 0.006028 | 0.024129 |
| Velocidad media (m/s) | 0.004775 | 0.000829 | 0.001256 | 0.005027 |
| Excursión lateral (m) | 0.014667 | 0.001296 | 0.009167 | 0.015058 |
| Altura media (m) | 0.223835 | 0.000070 | 0.223537 | 0.223856 |
| Roll máximo absoluto (grados) | 2.255235 | 0.000178 | 2.254719 | 2.255451 |
| Pitch máximo absoluto (grados) | 4.410611 | 0.002573 | 4.401102 | 4.412489 |
| Salto articular máximo (rad) | 0.018005 | 0.000066 | 0.017919 | 0.018131 |

## Resultado

Los 20 ciclos completos acumularon 0.458163 m de avance medido entre la primera y última muestra de cada ciclo. 
No se cambiaron paso, elevación ni duración de muestra durante la ventana.

La continuidad articular se expresa como el mayor salto absoluto entre dos muestras consecutivas de una misma articulación. La velocidad articular máxima se obtiene del campo medido `joint_velocities_rad_s`.

Archivos generados:

- `metricas_por_ciclo.csv`
- `series_temporales.png`
- `resumen_por_ciclo.png`
- `INFORME_ANALISIS.md`
