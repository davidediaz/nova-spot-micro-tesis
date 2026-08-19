# Análisis automático de marcha paso

- Bolsa: `/home/pavilion/Documentos/Cuadrupedo/Experimentos/rosbag2/paso_linea_base_20260814`.
- Ventana marcha paso--stand: 71.063355160 s.
- Duración nominal configurada por ciclo: 5.76 s.
- Duración observada media por ciclo: 5.760001 s.
- Ciclos completos analizados: 12.
- Activaciones verdaderas del supervisor: 0.

## Estadísticos entre ciclos

| Métrica | Media | Desv. estándar | Mínimo | Máximo |
|---|---:|---:|---:|---:|
| Avance por ciclo (m) | 0.021573 | 0.001607 | 0.016534 | 0.022317 |
| Velocidad media (m/s) | 0.003745 | 0.000279 | 0.002871 | 0.003874 |
| Excursión lateral (m) | 0.005452 | 0.000055 | 0.005371 | 0.005598 |
| Altura media (m) | 0.224105 | 0.000069 | 0.223888 | 0.224127 |
| Roll máximo absoluto (grados) | 1.279591 | 0.007590 | 1.255541 | 1.282169 |
| Pitch máximo absoluto (grados) | 2.487488 | 0.013021 | 2.483288 | 2.528820 |
| Salto articular máximo (rad) | 0.008405 | 0.000196 | 0.008299 | 0.009027 |

## Resultado

Los 12 ciclos completos acumularon 0.258880 m de avance medido entre la primera y última muestra de cada ciclo. 
No se cambiaron paso, elevación ni duración de muestra durante la ventana.

La continuidad articular se expresa como el mayor salto absoluto entre dos muestras consecutivas de una misma articulación. La velocidad articular máxima se obtiene del campo medido `joint_velocities_rad_s`.

Archivos generados:

- `metricas_por_ciclo.csv`
- `series_temporales.png`
- `resumen_por_ciclo.png`
- `INFORME_ANALISIS.md`
