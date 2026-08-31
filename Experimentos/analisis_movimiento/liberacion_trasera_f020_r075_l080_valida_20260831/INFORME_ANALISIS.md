# Análisis automático de gateo

- Bolsa: `Experimentos/rosbag2/liberacion_trasera_f020_r075_l080_valida_20260831`.
- Ventana gateo--stand: 65.633845928 s.
- Duración nominal configurada por ciclo: 4.32 s.
- Duración observada media por ciclo: 4.320000 s.
- Ciclos completos analizados: 15.
- Activaciones verdaderas del supervisor: 0.

## Estadísticos entre ciclos

| Métrica | Media | Desv. estándar | Mínimo | Máximo |
|---|---:|---:|---:|---:|
| Avance por ciclo (m) | 0.023090 | 0.002269 | 0.014957 | 0.024179 |
| Velocidad media (m/s) | 0.005345 | 0.000525 | 0.003462 | 0.005597 |
| Excursión lateral (m) | 0.005901 | 0.000120 | 0.005545 | 0.006053 |
| Altura media (m) | 0.224170 | 0.000027 | 0.224075 | 0.224180 |
| Roll máximo absoluto (grados) | 2.122867 | 0.011774 | 2.080682 | 2.127195 |
| Pitch máximo absoluto (grados) | 4.194693 | 0.004702 | 4.180151 | 4.202143 |
| Salto articular máximo (rad) | 0.020569 | 0.000092 | 0.020244 | 0.020607 |

## Resultado

Los 15 ciclos completos acumularon 0.346351 m de avance medido entre la primera y última muestra de cada ciclo.
No se cambiaron paso, elevación ni duración de muestra durante la ventana.

La continuidad articular se expresa como el mayor salto absoluto entre dos muestras consecutivas de una misma articulación. La velocidad articular máxima se obtiene del campo medido `joint_velocities_rad_s`.

Archivos generados:

- `metricas_por_ciclo.csv`
- `series_temporales.png`
- `resumen_por_ciclo.png`
- `INFORME_ANALISIS.md`
