# Análisis automático de marcha paso

- Bolsa: `Experimentos/campana_ppo_gazebo_20260902/nominal_01`.
- Ventana marcha paso--stand: 22.653211013 s.
- Duración nominal configurada por ciclo: 5.76 s.
- Duración observada media por ciclo: 5.759940 s.
- Ciclos completos analizados: 3.
- Activaciones verdaderas del supervisor: 0.

## Estadísticos entre ciclos

| Métrica | Media | Desv. estándar | Mínimo | Máximo |
|---|---:|---:|---:|---:|
| Avance por ciclo (m) | 0.018904 | 0.005155 | 0.012954 | 0.022016 |
| Velocidad media (m/s) | 0.003282 | 0.000895 | 0.002249 | 0.003822 |
| Excursión lateral (m) | 0.005340 | 0.000743 | 0.004481 | 0.005788 |
| Altura media (m) | 0.224036 | 0.000146 | 0.223868 | 0.224125 |
| Roll máximo absoluto (grados) | 1.272211 | 0.012958 | 1.257271 | 1.280392 |
| Pitch máximo absoluto (grados) | 2.518939 | 0.020402 | 2.502794 | 2.541869 |
| Salto articular máximo (rad) | 0.008354 | 0.000000 | 0.008354 | 0.008354 |

## Resultado

Los 3 ciclos completos acumularon 0.056712 m de avance medido entre la primera y última muestra de cada ciclo. 
No se cambiaron paso, elevación ni duración de muestra durante la ventana.

La continuidad articular se expresa como el mayor salto absoluto entre dos muestras consecutivas de una misma articulación. La velocidad articular máxima se obtiene del campo medido `joint_velocities_rad_s`.

Archivos generados:

- `metricas_por_ciclo.csv`
- `series_temporales.png`
- `resumen_por_ciclo.png`
- `INFORME_ANALISIS.md`
