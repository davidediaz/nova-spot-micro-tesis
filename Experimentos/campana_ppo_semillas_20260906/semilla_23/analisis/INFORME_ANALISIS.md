# Análisis automático de marcha paso

- Bolsa: `/home/pavilion/Documentos/Cuadrupedo/Experimentos/campana_ppo_semillas_20260906/semilla_23`.
- Ventana marcha paso--stand: 63.645840190 s.
- Duración nominal configurada por ciclo: 5.76 s.
- Duración observada media por ciclo: 5.769962 s.
- Ciclos completos analizados: 11.
- Activaciones verdaderas del supervisor: 0.

## Estadísticos entre ciclos

| Métrica | Media | Desv. estándar | Mínimo | Máximo |
|---|---:|---:|---:|---:|
| Avance por ciclo (m) | 0.016607 | 0.002257 | 0.011781 | 0.018539 |
| Velocidad media (m/s) | 0.002880 | 0.000400 | 0.002007 | 0.003219 |
| Excursión lateral (m) | 0.005850 | 0.000181 | 0.005719 | 0.006366 |
| Altura media (m) | 0.224259 | 0.000119 | 0.224090 | 0.224395 |
| Roll máximo absoluto (grados) | 2.189145 | 0.140869 | 1.766829 | 2.249928 |
| Pitch máximo absoluto (grados) | 2.649646 | 0.244947 | 1.925589 | 2.781440 |
| Salto articular máximo (rad) | 0.007418 | 0.000064 | 0.007309 | 0.007576 |

## Resultado

Los 11 ciclos completos acumularon 0.182674 m de avance medido entre la primera y última muestra de cada ciclo. 
No se cambiaron paso, elevación ni duración de muestra durante la ventana.

La continuidad articular se expresa como el mayor salto absoluto entre dos muestras consecutivas de una misma articulación. La velocidad articular máxima se obtiene del campo medido `joint_velocities_rad_s`.

Archivos generados:

- `metricas_por_ciclo.csv`
- `series_temporales.png`
- `resumen_por_ciclo.png`
- `INFORME_ANALISIS.md`
