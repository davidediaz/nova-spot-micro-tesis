# Revalidación dinámica nominal–PPO en Gazebo

- Cinco ensayos válidos por condición; se excluyó el ciclo 1 transitorio y se promediaron los ciclos restantes.
- PPO: política reentrenada con contactos, IMU y altura corporal; semilla 11.
- La comparación usa la campaña nominal independiente anterior como referencia.

| Métrica | Nominal | PPO reentrenada | Diferencia relativa | RMSE pareado |
|---|---:|---:|---:|---:|
| Avance (m/ciclo) | 0.027761 | 0.000910 | -96.721 % | 0.029294 |
| Velocidad (m/s) | 0.006594 | 0.000158 | -97.603 % | 0.008520 |
| Roll máximo (°) | 1.276861 | 3.216878 | 151.936 % | 1.940343 |
| Pitch máximo (°) | 2.502183 | 3.427771 | 36.991 % | 0.926756 |
| Salto articular (rad) | 0.024014 | 0.008037 | -66.531 % | 0.035350 |

Estos resultados son evidencia de simulación dinámica en Gazebo y no implican transferencia al robot físico. La mejora locomotora solo se afirmará si avance y velocidad aumentan sin degradar estabilidad.