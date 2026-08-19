# Análisis automático de gateo

- Bolsa: `Experimentos/rosbag2/contactos_gateo_validado_20260814_1410`.
- Ventana gateo--stand: 329.856750034 s.
- Duración nominal configurada por ciclo: 4.32 s.
- Duración observada media por ciclo: 4.320002 s.
- Ciclos completos analizados: 76.
- Activaciones verdaderas del supervisor: 0.

## Estadísticos entre ciclos

| Métrica | Media | Desv. estándar | Mínimo | Máximo |
|---|---:|---:|---:|---:|
| Avance por ciclo (m) | 0.022970 | 0.001753 | 0.008179 | 0.023892 |
| Velocidad media (m/s) | 0.005317 | 0.000406 | 0.001893 | 0.005531 |
| Excursión lateral (m) | 0.014916 | 0.000680 | 0.009148 | 0.015207 |
| Altura media (m) | 0.223819 | 0.000018 | 0.223676 | 0.223831 |
| Roll máximo absoluto (grados) | 2.232345 | 0.002090 | 2.225050 | 2.239508 |
| Pitch máximo absoluto (grados) | 4.396561 | 0.013249 | 4.360100 | 4.417602 |
| Salto articular máximo (rad) | 0.018374 | 0.000269 | 0.018238 | 0.020633 |

## Resultado

Los 76 ciclos completos acumularon 1.745713 m de avance medido entre la primera y última muestra de cada ciclo. 
No se cambiaron paso, elevación ni duración de muestra durante la ventana.

La continuidad articular se expresa como el mayor salto absoluto entre dos muestras consecutivas de una misma articulación. La velocidad articular máxima se obtiene del campo medido `joint_velocities_rad_s`.

Archivos generados:

- `metricas_por_ciclo.csv`
- `series_temporales.png`
- `resumen_por_ciclo.png`
- `INFORME_ANALISIS.md`
