# Protocolo de comunicación con la Raspberry Pi

## Objetivo

Definir cómo administrar la Raspberry, transferir código y comunicar ROS 2 con
el computador de Gazebo sin energizar servos accidentalmente.

## Canal principal: Wi-Fi + SSH

1. Conectar Raspberry y computador a la misma red Wi-Fi privada. La Raspberry
   Pi 4 puede usar 2,4 o 5 GHz; mantener desactivado el aislamiento entre
   clientes del router.
2. En la Raspberry consultar la dirección:

   ```bash
   hostname -I
   ip -br addr
   ```

3. Desde el computador comprobar y abrir la sesión:

   ```bash
   ping -c 3 IP_DE_LA_RASPBERRY
   ssh pavilion@IP_DE_LA_RASPBERRY
   ```

4. La primera sesión solo verifica Ubuntu, red, reloj, SSH, ROS 2 e I2C sin
   actuadores.

Registro actual: Raspberry Pi 4 Model B, Ubuntu 22.04.5 LTS ARM64, Wi-Fi
`192.168.0.101`, SSH instalado y acceso remoto verificado el 20 de agosto de
2026. La prueba DDS `talker/listener` todavía está pendiente.

## Transferencia de código

```bash
git clone https://github.com/davidediaz/nova-spot-micro-tesis.git
cd nova-spot-micro-tesis
git pull --ff-only
```

No copiar credenciales, claves privadas ni configuraciones PWM no revisadas.

## Canal ROS 2/DDS

Después de instalar ROS 2 Humble en Ubuntu 22.04 ARM64:

```bash
source /opt/ros/humble/setup.bash
export ROS_DOMAIN_ID=42
ros2 node list
ros2 topic list
```

Ambos equipos deben usar el mismo `ROS_DOMAIN_ID`, una red alcanzable y relojes
razonablemente sincronizados. Primero se probarán mensajes de diagnóstico; no
se publicarán referencias a servos hasta cerrar seguridad y calibración.

## Canal de respaldo: USB-serial

Usar únicamente una consola de 3,3 V conectada a GND/TX/RX, nunca 5 V:

```bash
ls /dev/ttyUSB* /dev/ttyACM* 2>/dev/null
screen /dev/ttyUSB0 115200
```

## Reglas de seguridad

- No conectar ni energizar servos durante la instalación de Thonny o ROS 2.
- No usar `sudo` para ejecutar el controlador del robot.
- Registrar IP, fecha, versiones y resultado de cada prueba en `CONTINUIDAD.md`.
- Si se pierde comunicación, mantener las salidas PWM deshabilitadas.
