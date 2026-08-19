# Instalación de Thonny en Raspberry Pi

La SD fue grabada con Ubuntu 22.04 Desktop ARM64 y se verificó la presencia de
`ubuntu-desktop`, GNOME y sesiones Xorg/Wayland. Falta ejecutar la instalación
en la Raspberry después del primer arranque y comprobar la interfaz gráfica.

## Instalación

En la Raspberry, abrir Terminal y ejecutar:

```bash
sudo apt update
sudo apt install -y thonny python3-pip python3-venv git openssh-server
```

Verificar:

```bash
thonny --version
python3 --version
uname -m
systemctl is-enabled ssh
systemctl is-active ssh
```

Abrir Thonny desde el menú o con `thonny`. La arquitectura esperada es
`aarch64`.

## Primera prueba sin hardware

Crear `prueba_raspberry.py` en Thonny:

```python
import platform
print(platform.platform())
print(platform.machine())
print("Thonny funciona en la Raspberry")
```

Ejecutarlo sin conectar servos.

## Evidencia

Registrar captura de Thonny, versiones, `uname -m`, fecha, IP, hostname y
confirmación de que no había servos energizados.
