# Campaña emparejada nominal–PPO en Gazebo

La conexión quedó disponible mediante:

```bash
ros2 launch nova_gait_controller ppo_gazebo.launch.py \
  policy_path:=/ruta/ppo_residual_20260902/politica_semilla_11.npz
```

Para la condición nominal se usa `demo.launch.py` sin el nodo PPO. Para la
condición PPO se publica la referencia nominal en `/nova/nominal_trajectory` y
`ppo_residual_node` entrega la referencia corregida al controlador. Se deben
ejecutar cinco pares con semillas de evaluación `11, 23, 37, 53, 71`, misma
marcha, duración y ventana de ciclos. Cada bolsa debe conservarse con la
configuración YAML, hash de la política y registro de activaciones del
supervisor.

La campaña no se ejecutó automáticamente en esta iteración: requiere lanzar
Gazebo y mantener cada proceso durante la duración completa. Hasta completar
los diez ensayos, el resultado se considera conexión e integración, no mejora
demostrada frente a la línea base.
