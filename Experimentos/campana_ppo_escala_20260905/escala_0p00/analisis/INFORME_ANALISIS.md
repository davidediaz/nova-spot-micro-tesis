# Análisis automático de marcha paso

- Bolsa: `/home/pavilion/Documentos/Cuadrupedo/Experimentos/campana_ppo_escala_20260905/escala_0p00`.
- Ventana marcha paso--stand: 63.154170007 s.
- Duración nominal configurada por ciclo: 5.76 s.
- Duración observada media por ciclo: 5.760000 s.
- Ciclos completos analizados: 10.
- Activaciones verdaderas del supervisor: 0.

## Estadísticos entre ciclos

| Métrica | Media | Desv. estándar | Mínimo | Máximo |
|---|---:|---:|---:|---:|
| Avance por ciclo (m) | 0.021598 | 0.000897 | 0.019079 | 0.022136 |
| Velocidad media (m/s) | 0.003750 | 0.000156 | 0.003313 | 0.003843 |
| Excursión lateral (m) | 0.005404 | 0.000314 | 0.004512 | 0.005549 |
| Altura media (m) | 0.224129 | 0.000007 | 0.224122 | 0.224145 |
| Roll máximo absoluto (grados) | 1.280189 | 0.003837 | 1.274470 | 1.286291 |
| Pitch máximo absoluto (grados) | 2.503516 | 0.018077 | 2.476851 | 2.517546 |
| Salto articular máximo (rad) | 0.007423 | 0.000036 | 0.007409 | 0.007525 |

## Resultado

Los 10 ciclos completos acumularon 0.215984 m de avance medido entre la primera y última muestra de cada ciclo. 
No se cambiaron paso, elevación ni duración de muestra durante la ventana.

La continuidad articular se expresa como el mayor salto absoluto entre dos muestras consecutivas de una misma articulación. La velocidad articular máxima se obtiene del campo medido `joint_velocities_rad_s`.

Archivos generados:

- `metricas_por_ciclo.csv`
- `series_temporales.png`
- `resumen_por_ciclo.png`
- `INFORME_ANALISIS.md`
