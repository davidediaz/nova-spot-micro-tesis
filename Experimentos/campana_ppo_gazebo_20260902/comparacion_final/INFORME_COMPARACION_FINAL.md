# Comparación final nominal–PPO en Gazebo

- Cuatro ensayos nominales válidos y cinco PPO; `nominal_03` se excluyó por cadencia inválida.
- El ciclo 1 se excluyó de los promedios por ser transitorio.

| Métrica | Nominal válido | PPO residual | Diferencia relativa |
|---|---:|---:|---:|
| Avance (m/ciclo) | 0.021935 | 0.016280 | -25.779 % |
| Velocidad (m/s) | 0.003808 | 0.002826 | -25.780 % |
| Roll máximo (°) | 1.279726 | 1.998084 | 56.134 % |
| Pitch máximo (°) | 2.506391 | 3.100022 | 23.685 % |
| Salto articular (rad) | 0.008354 | 0.007442 | -10.918 % |

Las diferencias describen esta campaña corta en Gazebo y no prueban transferencia al robot físico. La política usada fue la semilla 11 en las cinco corridas PPO; las demás semillas quedan disponibles para una selección bloqueada posterior.