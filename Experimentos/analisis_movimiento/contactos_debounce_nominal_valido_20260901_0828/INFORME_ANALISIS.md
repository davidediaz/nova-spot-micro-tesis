# Análisis automático de gateo

- Bolsa: `Experimentos/rosbag2/contactos_debounce_nominal_valido_20260901_0828`.
- Ventana gateo--stand: 105.522327958 s.
- Duración nominal configurada por ciclo: 4.32 s.
- Duración observada media por ciclo: 4.319990 s.
- Ciclos completos analizados: 24.
- Activaciones verdaderas del supervisor: 0.

## Estadísticos entre ciclos

| Métrica | Media | Desv. estándar | Mínimo | Máximo |
|---|---:|---:|---:|---:|
| Avance por ciclo (m) | 0.023558 | 0.002051 | 0.014070 | 0.024518 |
| Velocidad media (m/s) | 0.005453 | 0.000475 | 0.003257 | 0.005675 |
| Excursión lateral (m) | 0.005615 | 0.000266 | 0.004460 | 0.005878 |
| Altura media (m) | 0.224174 | 0.000022 | 0.224069 | 0.224180 |
| Roll máximo absoluto (grados) | 2.074511 | 0.004044 | 2.056439 | 2.077704 |
| Pitch máximo absoluto (grados) | 4.102216 | 0.001528 | 4.098950 | 4.105285 |
| Salto articular máximo (rad) | 0.019584 | 0.000140 | 0.019130 | 0.019631 |

## Resultado

Los 24 ciclos completos acumularon 0.565401 m de avance medido entre la primera y última muestra de cada ciclo. 
No se cambiaron paso, elevación ni duración de muestra durante la ventana.

La continuidad articular se expresa como el mayor salto absoluto entre dos muestras consecutivas de una misma articulación. La velocidad articular máxima se obtiene del campo medido `joint_velocities_rad_s`.

Archivos generados:

- `metricas_por_ciclo.csv`
- `series_temporales.png`
- `resumen_por_ciclo.png`
- `INFORME_ANALISIS.md`
