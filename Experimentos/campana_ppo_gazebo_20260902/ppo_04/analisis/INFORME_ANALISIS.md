# Análisis automático de marcha paso

- Bolsa: `Experimentos/campana_ppo_gazebo_20260902/ppo_04`.
- Ventana marcha paso--stand: 21.108743097 s.
- Duración nominal configurada por ciclo: 5.76 s.
- Duración observada media por ciclo: 5.760133 s.
- Ciclos completos analizados: 3.
- Activaciones verdaderas del supervisor: 0.

## Estadísticos entre ciclos

| Métrica | Media | Desv. estándar | Mínimo | Máximo |
|---|---:|---:|---:|---:|
| Avance por ciclo (m) | 0.012802 | 0.005367 | 0.006900 | 0.017388 |
| Velocidad media (m/s) | 0.002222 | 0.000932 | 0.001198 | 0.003019 |
| Excursión lateral (m) | 0.005524 | 0.001317 | 0.004555 | 0.007024 |
| Altura media (m) | 0.223264 | 0.000591 | 0.222787 | 0.223926 |
| Roll máximo absoluto (grados) | 1.891270 | 0.329135 | 1.625491 | 2.259427 |
| Pitch máximo absoluto (grados) | 3.082927 | 0.050244 | 3.034693 | 3.134966 |
| Salto articular máximo (rad) | 0.007389 | 0.000015 | 0.007376 | 0.007406 |

## Resultado

Los 3 ciclos completos acumularon 0.038406 m de avance medido entre la primera y última muestra de cada ciclo. 
No se cambiaron paso, elevación ni duración de muestra durante la ventana.

La continuidad articular se expresa como el mayor salto absoluto entre dos muestras consecutivas de una misma articulación. La velocidad articular máxima se obtiene del campo medido `joint_velocities_rad_s`.

Archivos generados:

- `metricas_por_ciclo.csv`
- `series_temporales.png`
- `resumen_por_ciclo.png`
- `INFORME_ANALISIS.md`
