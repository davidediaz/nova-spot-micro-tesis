# Análisis automático de marcha paso

- Bolsa: `Experimentos/campana_ppo_gazebo_20260902/nominal_03`.
- Ventana marcha paso--stand: 21.469685324 s.
- Duración nominal configurada por ciclo: 5.76 s.
- Duración observada media por ciclo: 2.880666 s.
- Ciclos completos analizados: 7.
- Activaciones verdaderas del supervisor: 0.

## Estadísticos entre ciclos

| Métrica | Media | Desv. estándar | Mínimo | Máximo |
|---|---:|---:|---:|---:|
| Avance por ciclo (m) | 0.043769 | 0.214272 | -0.317600 | 0.317600 |
| Velocidad media (m/s) | 0.015205 | 0.074407 | -0.110269 | 0.110294 |
| Excursión lateral (m) | 0.008244 | 0.001795 | 0.005889 | 0.010847 |
| Altura media (m) | 0.223223 | 0.000027 | 0.223164 | 0.223238 |
| Roll máximo absoluto (grados) | 1.260842 | 0.013037 | 1.233485 | 1.274529 |
| Pitch máximo absoluto (grados) | 2.488262 | 0.010921 | 2.478407 | 2.505729 |
| Salto articular máximo (rad) | 0.086754 | 0.000667 | 0.085736 | 0.087454 |

## Resultado

Los 7 ciclos completos acumularon 0.306382 m de avance medido entre la primera y última muestra de cada ciclo. 
No se cambiaron paso, elevación ni duración de muestra durante la ventana.

La continuidad articular se expresa como el mayor salto absoluto entre dos muestras consecutivas de una misma articulación. La velocidad articular máxima se obtiene del campo medido `joint_velocities_rad_s`.

Archivos generados:

- `metricas_por_ciclo.csv`
- `series_temporales.png`
- `resumen_por_ciclo.png`
- `INFORME_ANALISIS.md`
