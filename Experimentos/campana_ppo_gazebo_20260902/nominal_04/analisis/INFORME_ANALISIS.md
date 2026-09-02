# Análisis automático de marcha paso

- Bolsa: `/home/pavilion/Documentos/Cuadrupedo/Experimentos/campana_ppo_gazebo_20260902/nominal_04`.
- Ventana marcha paso--stand: 21.170256345 s.
- Duración nominal configurada por ciclo: 5.76 s.
- Duración observada media por ciclo: 5.759995 s.
- Ciclos completos analizados: 3.
- Activaciones verdaderas del supervisor: 0.

## Estadísticos entre ciclos

| Métrica | Media | Desv. estándar | Mínimo | Máximo |
|---|---:|---:|---:|---:|
| Avance por ciclo (m) | 0.020082 | 0.003308 | 0.016283 | 0.022330 |
| Velocidad media (m/s) | 0.003486 | 0.000574 | 0.002827 | 0.003877 |
| Excursión lateral (m) | 0.005363 | 0.000173 | 0.005164 | 0.005475 |
| Altura media (m) | 0.224047 | 0.000131 | 0.223896 | 0.224126 |
| Roll máximo absoluto (grados) | 1.273864 | 0.012645 | 1.259279 | 1.281747 |
| Pitch máximo absoluto (grados) | 2.500270 | 0.027969 | 2.483717 | 2.532562 |
| Salto articular máximo (rad) | 0.008567 | 0.000370 | 0.008354 | 0.008994 |

## Resultado

Los 3 ciclos completos acumularon 0.060246 m de avance medido entre la primera y última muestra de cada ciclo. 
No se cambiaron paso, elevación ni duración de muestra durante la ventana.

La continuidad articular se expresa como el mayor salto absoluto entre dos muestras consecutivas de una misma articulación. La velocidad articular máxima se obtiene del campo medido `joint_velocities_rad_s`.

Archivos generados:

- `metricas_por_ciclo.csv`
- `series_temporales.png`
- `resumen_por_ciclo.png`
- `INFORME_ANALISIS.md`
