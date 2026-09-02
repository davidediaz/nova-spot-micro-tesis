# Análisis automático de marcha paso

- Bolsa: `/home/pavilion/Documentos/Cuadrupedo/Experimentos/campana_ppo_semillas_20260906/semilla_53`.
- Ventana marcha paso--stand: 60.987313012 s.
- Duración nominal configurada por ciclo: 5.76 s.
- Duración observada media por ciclo: 5.760001 s.
- Ciclos completos analizados: 10.
- Activaciones verdaderas del supervisor: 0.

## Estadísticos entre ciclos

| Métrica | Media | Desv. estándar | Mínimo | Máximo |
|---|---:|---:|---:|---:|
| Avance por ciclo (m) | 0.014150 | 0.001417 | 0.011149 | 0.015568 |
| Velocidad media (m/s) | 0.002457 | 0.000246 | 0.001936 | 0.002703 |
| Excursión lateral (m) | 0.006608 | 0.001000 | 0.004491 | 0.007599 |
| Altura media (m) | 0.224959 | 0.000410 | 0.223799 | 0.225130 |
| Roll máximo absoluto (grados) | 1.126456 | 0.026516 | 1.089717 | 1.193098 |
| Pitch máximo absoluto (grados) | 2.657225 | 0.056745 | 2.568799 | 2.734343 |
| Salto articular máximo (rad) | 0.007626 | 0.000424 | 0.007330 | 0.008621 |

## Resultado

Los 10 ciclos completos acumularon 0.141495 m de avance medido entre la primera y última muestra de cada ciclo. 
No se cambiaron paso, elevación ni duración de muestra durante la ventana.

La continuidad articular se expresa como el mayor salto absoluto entre dos muestras consecutivas de una misma articulación. La velocidad articular máxima se obtiene del campo medido `joint_velocities_rad_s`.

Archivos generados:

- `metricas_por_ciclo.csv`
- `series_temporales.png`
- `resumen_por_ciclo.png`
- `INFORME_ANALISIS.md`
