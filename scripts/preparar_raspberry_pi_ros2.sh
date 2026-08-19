#!/usr/bin/env bash
set -euo pipefail

# Ejecutar DENTRO de la Raspberry Pi con Ubuntu Server 22.04 ARM64.
# Instala el entorno ROS 2 y herramientas de desarrollo. No energiza servos,
# no configura pulsos PWM y no reemplaza la parada física de emergencia.

if [[ "$(uname -m)" != "aarch64" ]]; then
  echo "Error: se requiere Ubuntu ARM64 (aarch64). Arquitectura: $(uname -m)" >&2
  exit 1
fi

if ! grep -q 'VERSION_ID="22.04"' /etc/os-release; then
  echo "Error: este instalador está preparado para Ubuntu 22.04." >&2
  exit 1
fi

sudo apt-get update
sudo apt-get install -y locales software-properties-common curl gnupg lsb-release \
  openssh-server avahi-daemon git i2c-tools python3-pip python3-smbus
sudo apt-get install -y python3-rpi.gpio python3-yaml

sudo locale-gen en_US en_US.UTF-8
sudo update-locale LC_ALL=en_US.UTF-8 LANG=en_US.UTF-8
sudo add-apt-repository -y universe

sudo mkdir -p /usr/share/keyrings
curl -fsSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.key \
  | sudo gpg --dearmor -o /usr/share/keyrings/ros-archive-keyring.gpg

echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] http://packages.ros.org/ros2/ubuntu $(. /etc/os-release && echo "$UBUNTU_CODENAME") main" \
  | sudo tee /etc/apt/sources.list.d/ros2.list >/dev/null

sudo apt-get update
sudo apt-get install -y ros-humble-ros-base ros-dev-tools \
  ros-humble-ros2-control ros-humble-ros2-controllers

sudo systemctl enable --now ssh avahi-daemon
sudo usermod -aG dialout,i2c "$USER"

profile_file="$HOME/.bashrc"
grep -qxF 'source /opt/ros/humble/setup.bash' "$profile_file" \
  || echo 'source /opt/ros/humble/setup.bash' >> "$profile_file"
grep -qxF 'export ROS_DOMAIN_ID=30' "$profile_file" \
  || echo 'export ROS_DOMAIN_ID=30' >> "$profile_file"
grep -qxF 'export ROS_LOCALHOST_ONLY=0' "$profile_file" \
  || echo 'export ROS_LOCALHOST_ONLY=0' >> "$profile_file"

echo
echo "ROS 2 Humble y acceso remoto instalados."
echo "Reinicie la Raspberry Pi para aplicar los grupos i2c/dialout."
echo "Después verifique: ros2 doctor --report"
echo "No conecte todavía la potencia de los MG996R."
