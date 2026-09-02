# Análisis automático de marcha paso

- Bolsa: `Experimentos/campana_ppo_gazebo_20260902/ppo_02`.
- Ventana marcha paso--stand: 22.109534137 s.
- Duración nominal configurada por ciclo: 5.76 s.
- Duración observada media por ciclo: 5.760134 s.
- Ciclos completos analizados: 3.
- Activaciones verdaderas del supervisor: 0.

## Estadísticos entre ciclos

| Métrica | Media | Desv. estándar | Mínimo | Máximo |
|---|---:|---:|---:|---:|
| Avance por ciclo (m) | 0.012610 | 0.004888 | 0.006980 | 0.015771 |
| Velocidad media (m/s) | 0.002189 | 0.000849 | 0.001212 | 0.002738 |
| Excursión lateral (m) | 0.005617 | 0.000780 | 0.004837 | 0.006398 |
| Altura media (m) | 0.223023 | 0.000189 | 0.222870 | 0.223234 |
| Roll máximo absoluto (grados) | 1.816857 | 0.122800 | 1.689052 | 1.933950 |
| Pitch máximo absoluto (grados) | 3.085334 | 0.043996 | 3.044175 | 3.131702 |
| Salto articular máximo (rad) | 0.007520 | 0.000019 | 0.007500 | 0.007539 |

## Resultado

Los 3 ciclos completos acumularon 0.037831 m de avance medido entre la primera y última muestra de cada ciclo. 
No se cambiaron paso, elevación ni duración de muestra durante la ventana.

La continuidad articular se expresa como el mayor salto absoluto entre dos muestras consecutivas de una misma articulación. La velocidad articular máxima se obtiene del campo medido `joint_velocities_rad_s`.

Archivos generados:

- `metricas_por_ciclo.csv`
- `series_temporales.png`
- `resumen_por_ciclo.png`
- `INFORME_ANALISIS.md`
