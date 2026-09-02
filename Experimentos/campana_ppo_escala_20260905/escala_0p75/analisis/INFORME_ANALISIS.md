# Análisis automático de marcha paso

- Bolsa: `/home/pavilion/Documentos/Cuadrupedo/Experimentos/campana_ppo_escala_20260905/escala_0p75`.
- Ventana marcha paso--stand: 61.041246783 s.
- Duración nominal configurada por ciclo: 5.76 s.
- Duración observada media por ciclo: 5.760026 s.
- Ciclos completos analizados: 10.
- Activaciones verdaderas del supervisor: 0.

## Estadísticos entre ciclos

| Métrica | Media | Desv. estándar | Mínimo | Máximo |
|---|---:|---:|---:|---:|
| Avance por ciclo (m) | 0.005635 | 0.006022 | -0.004169 | 0.015941 |
| Velocidad media (m/s) | 0.000978 | 0.001046 | -0.000724 | 0.002768 |
| Excursión lateral (m) | 0.007221 | 0.001579 | 0.004547 | 0.009977 |
| Altura media (m) | 0.223352 | 0.000629 | 0.222437 | 0.224582 |
| Roll máximo absoluto (grados) | 3.888195 | 0.495423 | 2.978629 | 4.496573 |
| Pitch máximo absoluto (grados) | 3.661472 | 0.420063 | 3.185391 | 4.416546 |
| Salto articular máximo (rad) | 0.008988 | 0.001098 | 0.007493 | 0.011495 |

## Resultado

Los 10 ciclos completos acumularon 0.056351 m de avance medido entre la primera y última muestra de cada ciclo. 
No se cambiaron paso, elevación ni duración de muestra durante la ventana.

La continuidad articular se expresa como el mayor salto absoluto entre dos muestras consecutivas de una misma articulación. La velocidad articular máxima se obtiene del campo medido `joint_velocities_rad_s`.

Archivos generados:

- `metricas_por_ciclo.csv`
- `series_temporales.png`
- `resumen_por_ciclo.png`
- `INFORME_ANALISIS.md`
