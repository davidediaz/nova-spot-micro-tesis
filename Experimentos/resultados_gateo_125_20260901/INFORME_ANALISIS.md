# Análisis automático de gateo

- Bolsa: `Experimentos/rosbag2/velocidad_gateo_125_20260901`.
- Ventana gateo--stand: 93.135209091 s.
- Duración nominal configurada por ciclo: 3.46 s.
- Duración observada media por ciclo: 3.456152 s.
- Ciclos completos analizados: 26.
- Activaciones verdaderas del supervisor: 0.

## Estadísticos entre ciclos

| Métrica | Media | Desv. estándar | Mínimo | Máximo |
|---|---:|---:|---:|---:|
| Avance por ciclo (m) | 0.023286 | 0.002158 | 0.013124 | 0.024939 |
| Velocidad media (m/s) | 0.006738 | 0.000622 | 0.003793 | 0.007208 |
| Excursión lateral (m) | 0.005772 | 0.000349 | 0.004264 | 0.006095 |
| Altura media (m) | 0.224163 | 0.000025 | 0.224043 | 0.224172 |
| Roll máximo absoluto (grados) | 1.973388 | 0.018797 | 1.945446 | 2.006261 |
| Pitch máximo absoluto (grados) | 3.943259 | 0.042053 | 3.888023 | 3.995295 |
| Salto articular máximo (rad) | 0.021762 | 0.000232 | 0.021291 | 0.022001 |

## Resultado

Los 26 ciclos completos acumularon 0.605449 m de avance medido entre la primera y última muestra de cada ciclo. 
No se cambiaron paso, elevación ni duración de muestra durante la ventana.

La continuidad articular se expresa como el mayor salto absoluto entre dos muestras consecutivas de una misma articulación. La velocidad articular máxima se obtiene del campo medido `joint_velocities_rad_s`.

Archivos generados:

- `metricas_por_ciclo.csv`
- `series_temporales.png`
- `resumen_por_ciclo.png`
- `INFORME_ANALISIS.md`
