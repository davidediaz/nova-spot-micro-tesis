# Análisis automático de marcha paso

- Bolsa: `/home/pavilion/Documentos/Cuadrupedo/Experimentos/campana_ppo_semillas_20260906/semilla_11`.
- Ventana marcha paso--stand: 63.172166342 s.
- Duración nominal configurada por ciclo: 5.76 s.
- Duración observada media por ciclo: 5.760026 s.
- Ciclos completos analizados: 10.
- Activaciones verdaderas del supervisor: 0.

## Estadísticos entre ciclos

| Métrica | Media | Desv. estándar | Mínimo | Máximo |
|---|---:|---:|---:|---:|
| Avance por ciclo (m) | 0.016459 | 0.005478 | 0.004173 | 0.021355 |
| Velocidad media (m/s) | 0.002857 | 0.000951 | 0.000724 | 0.003707 |
| Excursión lateral (m) | 0.006107 | 0.001373 | 0.004428 | 0.009613 |
| Altura media (m) | 0.224734 | 0.001188 | 0.223020 | 0.225963 |
| Roll máximo absoluto (grados) | 2.169517 | 0.130904 | 1.847869 | 2.279359 |
| Pitch máximo absoluto (grados) | 2.507367 | 0.052251 | 2.458326 | 2.637625 |
| Salto articular máximo (rad) | 0.007479 | 0.000105 | 0.007398 | 0.007752 |

## Resultado

Los 10 ciclos completos acumularon 0.164590 m de avance medido entre la primera y última muestra de cada ciclo. 
No se cambiaron paso, elevación ni duración de muestra durante la ventana.

La continuidad articular se expresa como el mayor salto absoluto entre dos muestras consecutivas de una misma articulación. La velocidad articular máxima se obtiene del campo medido `joint_velocities_rad_s`.

Archivos generados:

- `metricas_por_ciclo.csv`
- `series_temporales.png`
- `resumen_por_ciclo.png`
- `INFORME_ANALISIS.md`
