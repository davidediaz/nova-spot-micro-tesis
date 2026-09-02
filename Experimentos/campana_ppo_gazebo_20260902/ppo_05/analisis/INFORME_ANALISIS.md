# Análisis automático de marcha paso

- Bolsa: `Experimentos/campana_ppo_gazebo_20260902/ppo_05`.
- Ventana marcha paso--stand: 21.146850965 s.
- Duración nominal configurada por ciclo: 5.76 s.
- Duración observada media por ciclo: 5.760024 s.
- Ciclos completos analizados: 3.
- Activaciones verdaderas del supervisor: 0.

## Estadísticos entre ciclos

| Métrica | Media | Desv. estándar | Mínimo | Máximo |
|---|---:|---:|---:|---:|
| Avance por ciclo (m) | 0.013021 | 0.003965 | 0.008619 | 0.016313 |
| Velocidad media (m/s) | 0.002261 | 0.000688 | 0.001496 | 0.002832 |
| Excursión lateral (m) | 0.006372 | 0.000462 | 0.005870 | 0.006781 |
| Altura media (m) | 0.223379 | 0.000513 | 0.222979 | 0.223957 |
| Roll máximo absoluto (grados) | 1.934407 | 0.238404 | 1.709944 | 2.184656 |
| Pitch máximo absoluto (grados) | 3.122692 | 0.027833 | 3.090712 | 3.141451 |
| Salto articular máximo (rad) | 0.007488 | 0.000159 | 0.007318 | 0.007632 |

## Resultado

Los 3 ciclos completos acumularon 0.039063 m de avance medido entre la primera y última muestra de cada ciclo. 
No se cambiaron paso, elevación ni duración de muestra durante la ventana.

La continuidad articular se expresa como el mayor salto absoluto entre dos muestras consecutivas de una misma articulación. La velocidad articular máxima se obtiene del campo medido `joint_velocities_rad_s`.

Archivos generados:

- `metricas_por_ciclo.csv`
- `series_temporales.png`
- `resumen_por_ciclo.png`
- `INFORME_ANALISIS.md`
