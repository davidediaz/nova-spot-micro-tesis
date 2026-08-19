# Comparación de reproducibilidad del gateo

Se comparan los primeros 13 ciclos completos de cada ensayo.
El ciclo 1 se conserva en los archivos y gráficas como transitorio de arranque;
los promedios comparativos siguientes usan los ciclos 2 al 13.

| Métrica | Ensayo 1 | Ensayo 2 | Diferencia relativa | RMSE ciclo a ciclo |
|---|---:|---:|---:|---:|
| Duración observada (s) | 4.320013 | 4.319959 | -0.001 % | 0.000331 |
| Avance (m/ciclo) | 0.023338 | 0.023384 | 0.194 % | 0.000477 |
| Velocidad media (m/s) | 0.005402 | 0.005413 | 0.195 % | 0.000111 |
| Excursión lateral (m) | 0.015133 | 0.015135 | 0.014 % | 0.000087 |
| Altura media (m) | 0.223836 | 0.223835 | -0.000 % | 0.000003 |
| Roll máximo absoluto (grados) | 2.233112 | 2.233795 | 0.031 % | 0.002323 |
| Pitch máximo absoluto (grados) | 4.365442 | 4.367038 | 0.037 % | 0.004414 |
| Salto articular máximo (rad) | 0.018336 | 0.018342 | 0.035 % | 0.000084 |

## Interpretación

La reproducibilidad se evalúa con la diferencia relativa entre medias y el RMSE ciclo a ciclo. No se declara equivalencia estadística formal con solo dos ensayos; estos resultados cuantifican repetibilidad en simulación bajo la misma configuración.
