# Análisis automático de marcha paso

- Bolsa: `/home/pavilion/Documentos/Cuadrupedo/Experimentos/campana_ppo_escala_20260905/escala_1p00`.
- Ventana marcha paso--stand: 61.512359922 s.
- Duración nominal configurada por ciclo: 5.76 s.
- Duración observada media por ciclo: 5.759960 s.
- Ciclos completos analizados: 10.
- Activaciones verdaderas del supervisor: 0.

## Estadísticos entre ciclos

| Métrica | Media | Desv. estándar | Mínimo | Máximo |
|---|---:|---:|---:|---:|
| Avance por ciclo (m) | 0.004558 | 0.003663 | -0.001123 | 0.011604 |
| Velocidad media (m/s) | 0.000791 | 0.000636 | -0.000195 | 0.002015 |
| Excursión lateral (m) | 0.008561 | 0.003300 | 0.001258 | 0.012350 |
| Altura media (m) | 0.222546 | 0.000327 | 0.222020 | 0.223127 |
| Roll máximo absoluto (grados) | 4.425475 | 0.452968 | 3.782492 | 5.036271 |
| Pitch máximo absoluto (grados) | 3.744527 | 0.599284 | 2.390601 | 4.433177 |
| Salto articular máximo (rad) | 0.008807 | 0.002098 | 0.004988 | 0.011593 |

## Resultado

Los 10 ciclos completos acumularon 0.045577 m de avance medido entre la primera y última muestra de cada ciclo. 
No se cambiaron paso, elevación ni duración de muestra durante la ventana.

La continuidad articular se expresa como el mayor salto absoluto entre dos muestras consecutivas de una misma articulación. La velocidad articular máxima se obtiene del campo medido `joint_velocities_rad_s`.

Archivos generados:

- `metricas_por_ciclo.csv`
- `series_temporales.png`
- `resumen_por_ciclo.png`
- `INFORME_ANALISIS.md`
