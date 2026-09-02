# Análisis automático de marcha paso

- Bolsa: `/home/pavilion/Documentos/Cuadrupedo/Experimentos/campana_ppo_gazebo_20260903/ppo_gazebo_01`.
- Ventana marcha paso--stand: 61.016543127 s.
- Duración nominal configurada por ciclo: 5.76 s.
- Duración observada media por ciclo: 5.760120 s.
- Ciclos completos analizados: 10.
- Activaciones verdaderas del supervisor: 0.

## Estadísticos entre ciclos

| Métrica | Media | Desv. estándar | Mínimo | Máximo |
|---|---:|---:|---:|---:|
| Avance por ciclo (m) | 0.000431 | 0.001316 | -0.001770 | 0.002318 |
| Velocidad media (m/s) | 0.000075 | 0.000228 | -0.000307 | 0.000403 |
| Excursión lateral (m) | 0.007873 | 0.001362 | 0.005916 | 0.009796 |
| Altura media (m) | 0.225122 | 0.000533 | 0.224012 | 0.225709 |
| Roll máximo absoluto (grados) | 3.261671 | 0.118688 | 3.124493 | 3.457843 |
| Pitch máximo absoluto (grados) | 3.359791 | 0.152084 | 3.206397 | 3.611024 |
| Salto articular máximo (rad) | 0.008146 | 0.001469 | 0.007331 | 0.012239 |

## Resultado

Los 10 ciclos completos acumularon 0.004308 m de avance medido entre la primera y última muestra de cada ciclo. 
No se cambiaron paso, elevación ni duración de muestra durante la ventana.

La continuidad articular se expresa como el mayor salto absoluto entre dos muestras consecutivas de una misma articulación. La velocidad articular máxima se obtiene del campo medido `joint_velocities_rad_s`.

Archivos generados:

- `metricas_por_ciclo.csv`
- `series_temporales.png`
- `resumen_por_ciclo.png`
- `INFORME_ANALISIS.md`
