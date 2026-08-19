# Comparación de reproducibilidad de marcha paso

Se comparan los primeros 12 ciclos completos de cada ensayo.
El ciclo 1 se conserva en los archivos y gráficas como transitorio de arranque;
los promedios comparativos siguientes usan los ciclos 2 al 12.

| Métrica | Ensayo 1 | Ensayo 2 | Diferencia relativa | RMSE ciclo a ciclo |
|---|---:|---:|---:|---:|
| Duración observada (s) | 5.759993 | 5.760010 | 0.000 % | 0.000251 |
| Avance (m/ciclo) | 0.022031 | 0.022001 | -0.136 % | 0.000374 |
| Velocidad media (m/s) | 0.003825 | 0.003820 | -0.136 % | 0.000065 |
| Excursión lateral (m) | 0.005438 | 0.005417 | -0.399 % | 0.000052 |
| Altura media (m) | 0.224125 | 0.224125 | 0.000 % | 0.000001 |
| Roll máximo absoluto (grados) | 1.281777 | 1.281816 | 0.003 % | 0.000219 |
| Pitch máximo absoluto (grados) | 2.483731 | 2.483831 | 0.004 % | 0.000549 |
| Salto articular máximo (rad) | 0.008349 | 0.008362 | 0.161 % | 0.000032 |

## Interpretación

La reproducibilidad se evalúa con la diferencia relativa entre medias y el RMSE ciclo a ciclo. No se declara equivalencia estadística formal con solo dos ensayos; estos resultados cuantifican repetibilidad en simulación bajo la misma configuración.
