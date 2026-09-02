# Revalidación dinámica nominal–PPO en Gazebo

- Cuatro ensayos nominales válidos y cinco PPO; `nominal_03` se excluyó por cadencia inválida.
- PPO: política reentrenada con contactos, IMU y altura corporal; semilla 11.
- La comparación es descriptiva y no emparejada.

| Métrica | Nominal válido | PPO reentrenada | Diferencia relativa |
|---|---:|---:|---:|
| Avance (m/ciclo) | 0.021935 | 0.000910 | -95.850 % |
| Velocidad (m/s) | 0.003808 | 0.000158 | -95.850 % |
| Roll máximo (°) | 1.279726 | 3.216878 | 151.372 % |
| Pitch máximo (°) | 2.506391 | 3.427771 | 36.761 % |
| Salto articular (rad) | 0.008354 | 0.008037 | -3.789 % |

Estos resultados son evidencia de simulación dinámica en Gazebo y no implican transferencia al robot físico. La mejora locomotora solo se afirmará si avance y velocidad aumentan sin degradar estabilidad.