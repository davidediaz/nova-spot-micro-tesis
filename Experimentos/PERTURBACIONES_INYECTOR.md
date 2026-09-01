# Inyector reproducible de perturbaciones

Se implementó `perturbation_injector`, un nodo ROS 2 que conserva la telemetría
nominal y publica copias perturbadas en `/nova/perturbed/*`.

Ejemplo (ruido, retardo y pérdida de paquetes de contacto):

```bash
ros2 launch nova_gait_controller perturbation_injector.launch.py \
  delay_ms:=50 pose_noise_std_m:=0.002 \
  imu_accel_noise_std:=0.08 imu_gyro_noise_std:=0.015 \
  contact_dropout_probability:=0.05 noise_seed:=20260901
```

El mismo `noise_seed` produce la misma secuencia. El retardo se mide con reloj
monotónico y no depende de pausas del simulador. Para usar los datos en un
ensayo, se remapean los consumidores, por ejemplo:

```bash
ros2 run nova_gait_controller stability_monitor --ros-args \
  -r /tf:=/nova/perturbed/tf -r /nova/imu:=/nova/perturbed/imu
```

El nodo también publica un empuje horizontal temporizado como
`ros_gz_interfaces/msg/EntityWrench`:

```bash
ros2 launch nova_gait_controller perturbation_injector.launch.py \
  push_force_x:=2.0 push_start_s:=8.0 push_duration_s:=0.10
```

Ese canal debe enlazarse en `ros_gz_bridge` con el servicio/tópico de wrench de
la versión de Gazebo instalada. Si el bridge no ofrece esa interfaz, el evento
queda registrado sin afectar la simulación y se marca como pendiente en la
bitácora, evitando confundir un ensayo nominal con uno perturbado.

La fricción del suelo se mantiene como variante del mundo SDF (25 %, 50 % y
75 % del valor nominal); cada variante debe conservarse con su archivo SDF y
su hash en la carpeta de resultados antes de comparar métricas.
