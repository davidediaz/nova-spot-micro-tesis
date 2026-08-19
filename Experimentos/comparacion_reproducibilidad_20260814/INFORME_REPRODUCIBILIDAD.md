# Comparación de reproducibilidad del gateo

Se comparan los primeros 20 ciclos completos de cada ensayo.
El ciclo 1 se conserva en los archivos y gráficas como transitorio de arranque;
los promedios comparativos siguientes usan los ciclos 2 al 20.

| Métrica | Ensayo 1 | Ensayo 2 | Diferencia relativa | RMSE ciclo a ciclo |
|---|---:|---:|---:|---:|
| Duración observada (s) | 4.797889 | 4.794744 | -0.066 % | 0.010241 |
| Avance (m/ciclo) | 0.023797 | 0.023772 | -0.102 % | 0.000233 |
| Velocidad media (m/s) | 0.004960 | 0.004958 | -0.036 % | 0.000047 |
| Excursión lateral (m) | 0.014956 | 0.014985 | 0.193 % | 0.000063 |
| Altura media (m) | 0.223850 | 0.223848 | -0.001 % | 0.000003 |
| Roll máximo absoluto (grados) | 2.255263 | 2.255255 | -0.000 % | 0.000244 |
| Pitch máximo absoluto (grados) | 4.411111 | 4.411041 | -0.002 % | 0.001765 |
| Salto articular máximo (rad) | 0.018007 | 0.018014 | 0.037 % | 0.000117 |

## Interpretación

La reproducibilidad se evalúa con la diferencia relativa entre medias y el RMSE ciclo a ciclo. No se declara equivalencia estadística formal con solo dos ensayos; estos resultados cuantifican repetibilidad en simulación bajo la misma configuración.
