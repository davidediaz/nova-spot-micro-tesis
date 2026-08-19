#!/usr/bin/env bash
set -euo pipefail

# Reinstalación deliberadamente destructiva de la memoria de la Raspberry Pi.
# No ejecutar apuntando al SSD interno.
TARGET=/dev/sda
IMAGE="${1:-$HOME/Descargas/ubuntu-22.04.5-preinstalled-desktop-arm64+raspi.img.xz}"
EXPECTED_SHA=74764944dd4a96bdddd30cf1ffc133ecbe5ebb1d1f2eaa34cd5f8fbb57211c86

if [[ $EUID -ne 0 ]]; then
  echo "Ejecuta con sudo: sudo $0 [ruta-imagen.img.xz]" >&2
  exit 1
fi
[[ -b "$TARGET" ]] || { echo "No existe $TARGET; conecta la memoria y vuelve a verificarla." >&2; exit 1; }
MODEL=$(lsblk -dn -o MODEL "$TARGET" | xargs)
SIZE_BYTES=$(blockdev --getsize64 "$TARGET")
SIZE_GIB=$((SIZE_BYTES / 1024 / 1024 / 1024))
if [[ "$MODEL" != "Storage Device" || "$SIZE_GIB" -lt 20 || "$SIZE_GIB" -gt 40 ]]; then
  echo "Dispositivo inesperado: $TARGET | modelo='$MODEL' | tamaño=${SIZE_GIB}GiB" >&2
  echo "Se detiene para proteger el SSD interno." >&2
  exit 1
fi
[[ -f "$IMAGE" ]] || { echo "No existe la imagen: $IMAGE" >&2; exit 1; }

echo "Se BORRARÁ TODO el contenido de $TARGET ($MODEL, ${SIZE_GIB} GiB)."
echo "El SSD interno nvme0n1 NO será tocado."
read -r -p "Escribe exactamente BORRAR-SDA para continuar: " CONFIRM
[[ "$CONFIRM" == "BORRAR-SDA" ]] || { echo "Cancelado."; exit 1; }

ACTUAL_SHA=$(sha256sum "$IMAGE" | awk '{print $1}')
[[ "$ACTUAL_SHA" == "$EXPECTED_SHA" ]] || { echo "SHA-256 de imagen no coincide." >&2; exit 1; }
for part in "${TARGET}1" "${TARGET}2"; do
  umount "$part" 2>/dev/null || true
done
sync
echo "Grabando Ubuntu 22.04 Desktop ARM64 en $TARGET..."
xzcat "$IMAGE" | dd of="$TARGET" bs=4M status=progress conv=fsync
sync
echo "Proceso terminado. Retira y vuelve a insertar la memoria para comprobarla."
lsblk -o NAME,SIZE,MODEL,FSTYPE,MOUNTPOINTS "$TARGET"
