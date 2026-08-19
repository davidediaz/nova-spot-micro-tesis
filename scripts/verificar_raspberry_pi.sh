#!/usr/bin/env bash
set -euo pipefail

echo "Equipo: $(hostname)"
echo "Arquitectura: $(uname -m)"
echo "Sistema: $(. /etc/os-release && echo "$PRETTY_NAME")"
echo "ROS_DISTRO: ${ROS_DISTRO:-no cargado}"
echo "ROS_DOMAIN_ID: ${ROS_DOMAIN_ID:-no definido}"
echo "Interfaces I2C:"
ls -l /dev/i2c-* 2>/dev/null || echo "No hay interfaces I2C habilitadas."
echo "Paquetes esenciales:"
for package in controller_manager joint_trajectory_controller; do
  if ros2 pkg prefix "$package" >/dev/null 2>&1; then
    echo "  OK: $package"
  else
    echo "  FALTA: $package"
  fi
done

echo "La presencia del PCA9685 debe comprobarse después con i2cdetect."
echo "No ejecutar i2cdetect con cableado desconocido o potencia de servos activa."
