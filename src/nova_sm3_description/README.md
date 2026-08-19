# Modelo provisional NovaSM3

Este paquete describe el NovaSM3 para ROS 2. No es todavía un gemelo digital
validado. Usa las longitudes publicadas por el proyecto NovaSM3 v5.2b y una
masa total de referencia aproximada de 2,72 kg.

El URDF usado en Gazebo incorpora sensores de contacto de 100 Hz en los cuatro
pies. Sus flujos se puentean a ROS 2 y se consolidan mediante el paquete
`nova_gait_controller`. El MJCF todavía no expone contactos equivalentes ni una
pose corporal con el mismo contrato de métricas de Gazebo.

No se importó la calibración de los servomotores originales. Los límites,
velocidades, esfuerzos, secciones y distribución de masa son provisionales y
deben sustituirse por mediciones del robot con MG996R antes de validar dinámica
o transferir movimientos al hardware.

Visualización:

```bash
ros2 launch nova_sm3_description display.launch.py
```

MuJoCo con `ros2_control`:

```bash
ros2 launch nova_sm3_description mujoco_sim.launch.py
```

Gazebo Sim con `gz_ros2_control`:

```bash
ros2 launch nova_sm3_description sim.launch.py
```

La conversión añade una articulación libre al cuerpo raíz para permitir que el
robot caiga, apoye los pies y se desplace. El modelo usa geometría primitiva;
los STL oficiales se reservarán para visualización después de comprobar escala
y correspondencia con el ejemplar físico.

## Raspberry Pi 3

Después de grabar Ubuntu Server 22.04 ARM64 en la microSD, copiar el proyecto a
la Pi y ejecutar allí:

```bash
chmod +x scripts/preparar_raspberry_pi_ros2.sh scripts/verificar_raspberry_pi.sh
./scripts/preparar_raspberry_pi_ros2.sh
```

El script instala ROS 2 Humble, SSH, herramientas de compilación e I2C. No
controla todavía el PCA9685 ni debe utilizarse para energizar los MG996R.
