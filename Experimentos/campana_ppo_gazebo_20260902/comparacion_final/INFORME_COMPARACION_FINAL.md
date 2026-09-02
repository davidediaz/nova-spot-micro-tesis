# Comparación final nominal–PPO en Gazebo

- Cinco ensayos por condición; se analizaron al menos tres ciclos completos por ensayo.
- El ciclo 1 se excluyó de los promedios por ser transitorio.

| Métrica | Nominal | PPO residual | Diferencia relativa | RMSE pareado |
|---|---:|---:|---:|---:|
| Avance (m/ciclo) | 0.027761 | 0.016280 | -41.355 % | 0.015948 |
| Velocidad (m/s) | 0.006594 | 0.002826 | -57.139 % | 0.006641 |
| Roll máximo (°) | 1.276861 | 1.998084 | 56.484 % | 0.729752 |
| Pitch máximo (°) | 2.502183 | 3.100022 | 23.893 % | 0.598021 |
| Salto articular (rad) | 0.024014 | 0.007442 | -69.011 % | 0.035443 |

Las diferencias describen esta campaña corta en Gazebo y no prueban transferencia al robot físico. La política usada fue la semilla 11 en las cinco corridas PPO; las demás semillas quedan disponibles para una selección bloqueada posterior.