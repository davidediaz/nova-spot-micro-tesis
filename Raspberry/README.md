# Control de marchas Nova desde Raspberry Pi

Esta carpeta reúne los archivos que se pueden abrir en Thonny para conocer y
ordenar las marchas del proyecto. Estos programas publican órdenes ROS 2; **no
generan PWM ni controlan directamente el PCA9685 o los MG996R**.

## Contenido

- `AVANCES_PCA9685_2026-08-24.md`: estado comprobado de la integración entre
  Arduino Mega 2560, PCA9685 y servos MG996R en la Raspberry Pi 4.
- `codigo/panel_marchas.py`: ventana con botones para postura, gateo y paso.
- `codigo/control_marchas_ros2.py`: publica una orden en `/nova/gait_command`.
- `marchas/tipos_de_marcha.py`: catálogo legible de las marchas disponibles.
- `configuracion/marchas.yaml`: parámetros nominales congelados.
- `configuracion/servos.yaml`: canales y calibraciones, bloqueadas inicialmente.
- `codigo/pca9685_seguro.py`: controlador PWM con `OE` y apagado global.
- `codigo/interfaz_pwm_ros2.py`: conversión de trayectorias ROS 2 a PWM.
- `CONEXIONES.md`: tabla de cableado y asignación de los doce servos.
- `DIAGRAMA_CABLEADO_PI4_PCA9685_LM2596.pdf`: diagrama de pines y separación
  entre lógica I²C, potencia externa y servos; usarlo antes de cablear.
- `DIAGRAMA_CABLEADO_PI4_PCA9685_LM2596.svg`: misma lámina en formato vectorial
  editable.
- `CONEXIONES_ELECTRONICAS_NOVASM3.pdf`: guía ilustrada de pines, materiales,
  alimentación, sensores y secuencia segura de puesta en marcha.
- `diagrama_conexion_servos.svg`: imagen vectorial revisada del cableado.
- `vista_cuadrupedo_servos.png`: seis vistas del robot con los canales CH0--CH11.
- `vista_cuadrupedo_servos_novasm3.png`: versión fiel al Nova Spot Micro 3
  amarillo y morado conservado en las referencias del proyecto.
- `mapa_articulaciones_novasm3_corregido.svg`: mapa autoritativo de los ejes,
  construido desde la cadena cinemática del URDF para evitar puntos ambiguos.
- `configuracion/calibracion_servos.csv`: hoja para registrar PWM, velocidad y torque.
- `seguridad/ANTES_DE_CONECTAR_SERVOS.md`: requisitos obligatorios de hardware.

El generador matemático utilizado realmente por ROS 2 permanece en
`../src/nova_gait_controller/nova_gait_controller/kinematics.py`, evitando
mantener dos copias que puedan divergir.

## Abrir en Thonny

En el computador actual:

```bash
cd /home/pavilion/Documentos/Cuadrupedo
source /opt/ros/humble/setup.bash
source install/setup.bash
thonny Raspberry/codigo/panel_marchas.py
```

En la Raspberry Pi, cambia la primera ruta por aquella donde copies el
proyecto. Selecciona el intérprete **Python 3 del sistema** en Thonny.

Para probar solamente el catálogo, sin ROS 2 ni movimiento:

```bash
python3 Raspberry/marchas/tipos_de_marcha.py
```

## Estado actual del hardware

El planificador `gateo` y `paso` funciona en simulación. En la Raspberry Pi 4 se
instaló Arduino IDE 1.8.19 ARM64 y se verificó un Arduino Mega 2560 en
`/dev/ttyACM0`. El Mega detecta el PCA9685 en `0x40`; después de corregir la
inversión de SDA y SCL se probaron progresivamente servos MG996R y el sketch
actual mueve `CH5`--`CH10` entre 1300 y 1700 microsegundos. Los demás canales
se mantienen en `FULL_OFF`.

Esta prueba confirma comunicación y movimiento, pero no completa la puesta en
marcha. Todavía se deben identificar las articulaciones, calibrar mínimo,
centro, máximo y sentido por canal, verificar la fuente bajo carga y añadir una
parada física mediante OE con pull-up. La interfaz PWM de ROS 2 permanece
bloqueada hasta completar las doce calibraciones y cambiar explícitamente
`hardware_ready` a `true`; aún debe integrarse como hardware `ros2_control`.

Para lanzar la interfaz en una Raspberry ya preparada:

```bash
source /opt/ros/humble/setup.bash
source install/setup.bash
python3 Raspberry/codigo/interfaz_pwm_ros2.py
```

La habilitación posterior se publica separadamente y solo será aceptada tras
completar la configuración:

```bash
ros2 topic pub --once /nova/hardware/enable std_msgs/msg/Bool "{data: true}"
```
