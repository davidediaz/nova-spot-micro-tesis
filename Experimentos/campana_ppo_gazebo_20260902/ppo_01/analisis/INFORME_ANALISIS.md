# Análisis automático de marcha paso

- Bolsa: `Experimentos/campana_ppo_gazebo_20260902/ppo_01`.
- Ventana marcha paso--stand: 21.135507670 s.
- Duración nominal configurada por ciclo: 5.76 s.
- Duración observada media por ciclo: 5.759809 s.
- Ciclos completos analizados: 3.
- Activaciones verdaderas del supervisor: 0.

## Estadísticos entre ciclos

| Métrica | Media | Desv. estándar | Mínimo | Máximo |
|---|---:|---:|---:|---:|
| Avance por ciclo (m) | 0.015605 | 0.003331 | 0.011825 | 0.018111 |
| Velocidad media (m/s) | 0.002709 | 0.000578 | 0.002053 | 0.003144 |
| Excursión lateral (m) | 0.004956 | 0.000271 | 0.004644 | 0.005125 |
| Altura media (m) | 0.223957 | 0.000273 | 0.223661 | 0.224199 |
| Roll máximo absoluto (grados) | 2.107974 | 0.076008 | 2.023603 | 2.171099 |
| Pitch máximo absoluto (grados) | 3.084583 | 0.051768 | 3.032741 | 3.136277 |
| Salto articular máximo (rad) | 0.007482 | 0.000051 | 0.007424 | 0.007516 |

## Resultado

Los 3 ciclos completos acumularon 0.046816 m de avance medido entre la primera y última muestra de cada ciclo. 
No se cambiaron paso, elevación ni duración de muestra durante la ventana.

La continuidad articular se expresa como el mayor salto absoluto entre dos muestras consecutivas de una misma articulación. La velocidad articular máxima se obtiene del campo medido `joint_velocities_rad_s`.

Archivos generados:

- `metricas_por_ciclo.csv`
- `series_temporales.png`
- `resumen_por_ciclo.png`
- `INFORME_ANALISIS.md`
