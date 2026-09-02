# Análisis automático de marcha paso

- Bolsa: `/home/pavilion/Documentos/Cuadrupedo/Experimentos/campana_ppo_escala_20260905/escala_0p50`.
- Ventana marcha paso--stand: 61.052537452 s.
- Duración nominal configurada por ciclo: 5.76 s.
- Duración observada media por ciclo: 5.760044 s.
- Ciclos completos analizados: 10.
- Activaciones verdaderas del supervisor: 0.

## Estadísticos entre ciclos

| Métrica | Media | Desv. estándar | Mínimo | Máximo |
|---|---:|---:|---:|---:|
| Avance por ciclo (m) | -0.000440 | 0.006084 | -0.016458 | 0.006817 |
| Velocidad media (m/s) | -0.000076 | 0.001056 | -0.002857 | 0.001183 |
| Excursión lateral (m) | 0.006261 | 0.001469 | 0.005072 | 0.010243 |
| Altura media (m) | 0.222905 | 0.000312 | 0.222496 | 0.223430 |
| Roll máximo absoluto (grados) | 3.376773 | 0.419265 | 3.130956 | 4.269834 |
| Pitch máximo absoluto (grados) | 3.266233 | 0.494512 | 2.940830 | 4.596856 |
| Salto articular máximo (rad) | 0.008071 | 0.001165 | 0.007403 | 0.011262 |

## Resultado

Los 10 ciclos completos acumularon -0.004399 m de avance medido entre la primera y última muestra de cada ciclo. 
No se cambiaron paso, elevación ni duración de muestra durante la ventana.

La continuidad articular se expresa como el mayor salto absoluto entre dos muestras consecutivas de una misma articulación. La velocidad articular máxima se obtiene del campo medido `joint_velocities_rad_s`.

Archivos generados:

- `metricas_por_ciclo.csv`
- `series_temporales.png`
- `resumen_por_ciclo.png`
- `INFORME_ANALISIS.md`
