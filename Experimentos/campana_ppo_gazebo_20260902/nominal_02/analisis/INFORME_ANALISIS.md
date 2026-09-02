# Análisis automático de marcha paso

- Bolsa: `Experimentos/campana_ppo_gazebo_20260902/nominal_02`.
- Ventana marcha paso--stand: 20.999804143 s.
- Duración nominal configurada por ciclo: 5.76 s.
- Duración observada media por ciclo: 5.759951 s.
- Ciclos completos analizados: 3.
- Activaciones verdaderas del supervisor: 0.

## Estadísticos entre ciclos

| Métrica | Media | Desv. estándar | Mínimo | Máximo |
|---|---:|---:|---:|---:|
| Avance por ciclo (m) | 0.020312 | 0.002844 | 0.017054 | 0.022302 |
| Velocidad media (m/s) | 0.003526 | 0.000494 | 0.002961 | 0.003872 |
| Excursión lateral (m) | 0.005779 | 0.000037 | 0.005758 | 0.005822 |
| Altura media (m) | 0.224052 | 0.000118 | 0.223915 | 0.224124 |
| Roll máximo absoluto (grados) | 1.270939 | 0.014124 | 1.254717 | 1.280503 |
| Pitch máximo absoluto (grados) | 2.523940 | 0.018375 | 2.504945 | 2.541625 |
| Salto articular máximo (rad) | 0.008556 | 0.000351 | 0.008354 | 0.008962 |

## Resultado

Los 3 ciclos completos acumularon 0.060935 m de avance medido entre la primera y última muestra de cada ciclo. 
No se cambiaron paso, elevación ni duración de muestra durante la ventana.

La continuidad articular se expresa como el mayor salto absoluto entre dos muestras consecutivas de una misma articulación. La velocidad articular máxima se obtiene del campo medido `joint_velocities_rad_s`.

Archivos generados:

- `metricas_por_ciclo.csv`
- `series_temporales.png`
- `resumen_por_ciclo.png`
- `INFORME_ANALISIS.md`
