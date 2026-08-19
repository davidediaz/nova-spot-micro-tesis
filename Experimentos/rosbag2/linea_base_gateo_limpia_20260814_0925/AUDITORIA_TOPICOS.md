# Auditoría de tópicos requeridos

Fuente: `metadata.yaml` de la bolsa válida
`linea_base_gateo_limpia_20260814_0925`.

| Dato requerido | Tópico | Tipo ROS 2 | Mensajes | Resultado |
|---|---|---|---:|---|
| Pose 3D | `/world/empty/dynamic_pose/info` | `tf2_msgs/msg/TFMessage` | 10.232 | Registrada |
| Transformaciones | `/tf` | `tf2_msgs/msg/TFMessage` | 17.372 | Registradas |
| Estados articulares | `/joint_states` | `sensor_msgs/msg/JointState` | 17.372 | Registrados |
| Estados articulares dinámicos | `/dynamic_joint_states` | `control_msgs/msg/DynamicJointState` | 17.372 | Registrados |
| Métricas JSON | `/nova/metrics/json` | `std_msgs/msg/String` | 10.231 | Registradas |
| Diagnósticos | `/nova/metrics/diagnostics` | `diagnostic_msgs/msg/DiagnosticArray` | 10.231 | Registrados |
| Órdenes de marcha | `/nova/gait_command` | `std_msgs/msg/String` | 2 | `gateo` y `stand` registradas |
| Activaciones del supervisor | `/nova/safety/triggered` | `std_msgs/msg/Bool` | 0 | Tópico incluido; no hubo activaciones |
| Referencias articulares | `/joint_trajectory_controller/joint_trajectory` | `trajectory_msgs/msg/JointTrajectory` | 629 | Registradas |

El tópico del supervisor formó parte explícita de la grabación. Un conteo cero
significa que no se produjo ningún evento de seguridad durante el ensayo; no
significa que el tópico haya sido omitido. Esto concuerda con la altura e
inclinación observadas dentro de los umbrales configurados.

Conclusión: el requisito de registrar pose 3D, estados articulares, métricas,
órdenes de marcha y activaciones del supervisor está cubierto por la bolsa.
