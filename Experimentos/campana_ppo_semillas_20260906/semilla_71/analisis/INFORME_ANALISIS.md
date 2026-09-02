# Análisis automático de marcha paso

- Bolsa: `/home/pavilion/Documentos/Cuadrupedo/Experimentos/campana_ppo_semillas_20260906/semilla_71`.
- Ventana marcha paso--stand: 61.067210596 s.
- Duración nominal configurada por ciclo: 5.76 s.
- Duración observada media por ciclo: 5.760024 s.
- Ciclos completos analizados: 10.
- Activaciones verdaderas del supervisor: 0.

## Estadísticos entre ciclos

| Métrica | Media | Desv. estándar | Mínimo | Máximo |
|---|---:|---:|---:|---:|
| Avance por ciclo (m) | 0.018831 | 0.003298 | 0.009705 | 0.021328 |
| Velocidad media (m/s) | 0.003269 | 0.000572 | 0.001685 | 0.003703 |
| Excursión lateral (m) | 0.004942 | 0.000555 | 0.003434 | 0.005259 |
| Altura media (m) | 0.224389 | 0.000733 | 0.222711 | 0.224865 |
| Roll máximo absoluto (grados) | 1.287571 | 0.161696 | 0.922651 | 1.424061 |
| Pitch máximo absoluto (grados) | 3.211210 | 0.075732 | 3.116260 | 3.294521 |
| Salto articular máximo (rad) | 0.008369 | 0.003074 | 0.007308 | 0.017117 |

## Resultado

Los 10 ciclos completos acumularon 0.188305 m de avance medido entre la primera y última muestra de cada ciclo. 
No se cambiaron paso, elevación ni duración de muestra durante la ventana.

La continuidad articular se expresa como el mayor salto absoluto entre dos muestras consecutivas de una misma articulación. La velocidad articular máxima se obtiene del campo medido `joint_velocities_rad_s`.

Archivos generados:

- `metricas_por_ciclo.csv`
- `series_temporales.png`
- `resumen_por_ciclo.png`
- `INFORME_ANALISIS.md`
