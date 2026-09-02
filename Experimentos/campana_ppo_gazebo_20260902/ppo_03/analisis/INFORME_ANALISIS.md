# Análisis automático de marcha paso

- Bolsa: `Experimentos/campana_ppo_gazebo_20260902/ppo_03`.
- Ventana marcha paso--stand: 21.104337655 s.
- Duración nominal configurada por ciclo: 5.76 s.
- Duración observada media por ciclo: 5.759927 s.
- Ciclos completos analizados: 3.
- Activaciones verdaderas del supervisor: 0.

## Estadísticos entre ciclos

| Métrica | Media | Desv. estándar | Mínimo | Máximo |
|---|---:|---:|---:|---:|
| Avance por ciclo (m) | 0.015632 | 0.003305 | 0.011885 | 0.018131 |
| Velocidad media (m/s) | 0.002714 | 0.000574 | 0.002063 | 0.003148 |
| Excursión lateral (m) | 0.004970 | 0.000280 | 0.004650 | 0.005169 |
| Altura media (m) | 0.223956 | 0.000271 | 0.223663 | 0.224198 |
| Roll máximo absoluto (grados) | 2.104636 | 0.072604 | 2.022990 | 2.161944 |
| Pitch máximo absoluto (grados) | 3.079850 | 0.052554 | 3.032496 | 3.136392 |
| Salto articular máximo (rad) | 0.007466 | 0.000078 | 0.007418 | 0.007556 |

## Resultado

Los 3 ciclos completos acumularon 0.046897 m de avance medido entre la primera y última muestra de cada ciclo. 
No se cambiaron paso, elevación ni duración de muestra durante la ventana.

La continuidad articular se expresa como el mayor salto absoluto entre dos muestras consecutivas de una misma articulación. La velocidad articular máxima se obtiene del campo medido `joint_velocities_rad_s`.

Archivos generados:

- `metricas_por_ciclo.csv`
- `series_temporales.png`
- `resumen_por_ciclo.png`
- `INFORME_ANALISIS.md`
