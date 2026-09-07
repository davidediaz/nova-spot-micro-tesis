# Análisis automático de marcha paso

- Bolsa: `Experimentos/campanas_mujoco/paso_ajustado_5x20_20260903/rosbag2/paso_r1`.
- Ventana marcha paso--stand: 121.462941015 s.
- Duración nominal configurada por ciclo: 5.76 s.
- Duración observada media por ciclo: 5.760017 s.
- Ciclos completos analizados: 21.
- Activaciones verdaderas del supervisor: 0.

## Estadísticos entre ciclos

| Métrica | Media | Desv. estándar | Mínimo | Máximo |
|---|---:|---:|---:|---:|
| Avance por ciclo (m) | 0.010183 | 0.001403 | 0.009819 | 0.016303 |
| Velocidad media (m/s) | 0.001768 | 0.000244 | 0.001705 | 0.002830 |
| Excursión lateral (m) | 0.004951 | 0.000323 | 0.003545 | 0.005070 |
| Altura media (m) | 0.222099 | 0.000004 | 0.222093 | 0.222105 |
| Roll máximo absoluto (grados) | 1.510933 | 0.000035 | 1.510872 | 1.510989 |
| Pitch máximo absoluto (grados) | 3.171321 | 0.000020 | 3.171291 | 3.171352 |
| Salto articular máximo (rad) | 0.015975 | 0.001941 | 0.013058 | 0.019515 |

## Resultado

Los 21 ciclos completos acumularon 0.213842 m de avance medido entre la primera y última muestra de cada ciclo. 
No se cambiaron paso, elevación ni duración de muestra durante la ventana.

La continuidad articular se expresa como el mayor salto absoluto entre dos muestras consecutivas de una misma articulación. La velocidad articular máxima se obtiene del campo medido `joint_velocities_rad_s`.

Archivos generados:

- `metricas_por_ciclo.csv`
- `series_temporales.png`
- `resumen_por_ciclo.png`
- `INFORME_ANALISIS.md`
