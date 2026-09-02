# Análisis automático de marcha paso

- Bolsa: `/home/pavilion/Documentos/Cuadrupedo/Experimentos/campana_ppo_gazebo_20260902/nominal_05`.
- Ventana marcha paso--stand: 21.017195093 s.
- Duración nominal configurada por ciclo: 5.76 s.
- Duración observada media por ciclo: 5.759968 s.
- Ciclos completos analizados: 3.
- Activaciones verdaderas del supervisor: 0.

## Estadísticos entre ciclos

| Métrica | Media | Desv. estándar | Mínimo | Máximo |
|---|---:|---:|---:|---:|
| Avance por ciclo (m) | 0.020114 | 0.003174 | 0.016465 | 0.022237 |
| Velocidad media (m/s) | 0.003492 | 0.000551 | 0.002859 | 0.003861 |
| Excursión lateral (m) | 0.005772 | 0.000088 | 0.005672 | 0.005841 |
| Altura media (m) | 0.224038 | 0.000143 | 0.223873 | 0.224124 |
| Roll máximo absoluto (grados) | 1.272008 | 0.012179 | 1.257994 | 1.280033 |
| Pitch máximo absoluto (grados) | 2.526665 | 0.015747 | 2.510764 | 2.542254 |
| Salto articular máximo (rad) | 0.008578 | 0.000389 | 0.008354 | 0.009027 |

## Resultado

Los 3 ciclos completos acumularon 0.060343 m de avance medido entre la primera y última muestra de cada ciclo. 
No se cambiaron paso, elevación ni duración de muestra durante la ventana.

La continuidad articular se expresa como el mayor salto absoluto entre dos muestras consecutivas de una misma articulación. La velocidad articular máxima se obtiene del campo medido `joint_velocities_rad_s`.

Archivos generados:

- `metricas_por_ciclo.csv`
- `series_temporales.png`
- `resumen_por_ciclo.png`
- `INFORME_ANALISIS.md`
