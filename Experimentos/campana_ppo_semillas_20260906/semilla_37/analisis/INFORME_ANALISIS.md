# Análisis automático de marcha paso

- Bolsa: `/home/pavilion/Documentos/Cuadrupedo/Experimentos/campana_ppo_semillas_20260906/semilla_37`.
- Ventana marcha paso--stand: 60.959480243 s.
- Duración nominal configurada por ciclo: 5.76 s.
- Duración observada media por ciclo: 5.744053 s.
- Ciclos completos analizados: 10.
- Activaciones verdaderas del supervisor: 0.

## Estadísticos entre ciclos

| Métrica | Media | Desv. estándar | Mínimo | Máximo |
|---|---:|---:|---:|---:|
| Avance por ciclo (m) | 0.001915 | 0.001379 | -0.001502 | 0.003421 |
| Velocidad media (m/s) | 0.000332 | 0.000242 | -0.000268 | 0.000594 |
| Excursión lateral (m) | 0.005634 | 0.000480 | 0.004576 | 0.006289 |
| Altura media (m) | 0.218723 | 0.000184 | 0.218306 | 0.218910 |
| Roll máximo absoluto (grados) | 0.810778 | 0.018922 | 0.791649 | 0.853517 |
| Pitch máximo absoluto (grados) | 4.900983 | 0.058373 | 4.816245 | 5.011150 |
| Salto articular máximo (rad) | 0.010359 | 0.001112 | 0.007461 | 0.011194 |

## Resultado

Los 10 ciclos completos acumularon 0.019149 m de avance medido entre la primera y última muestra de cada ciclo. 
No se cambiaron paso, elevación ni duración de muestra durante la ventana.

La continuidad articular se expresa como el mayor salto absoluto entre dos muestras consecutivas de una misma articulación. La velocidad articular máxima se obtiene del campo medido `joint_velocities_rad_s`.

Archivos generados:

- `metricas_por_ciclo.csv`
- `series_temporales.png`
- `resumen_por_ciclo.png`
- `INFORME_ANALISIS.md`
