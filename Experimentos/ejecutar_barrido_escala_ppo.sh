#!/usr/bin/env bash
set -euo pipefail
root="$(cd "$(dirname "$0")/.." && pwd)"
campaign="${CAMPAIGN_DIR:-campana_ppo_escala_20260904}"
policy="${POLICY_PATH:-$root/Experimentos/ppo_residual_20260903/politica_semilla_11.npz}"
for scale in 0.00 0.25 0.50 0.75 1.00; do
  label="escala_${scale//./p}"
  setsid ros2 launch nova_gait_controller ppo_gazebo.launch.py policy_path:="$policy" residual_scale:="$scale" >"/tmp/ppo_scale_${label}.log" 2>&1 & launch_pid=$!
  sleep 12
  if ! ros2 node list | grep -qx '/ppo_residual_node'; then
    echo "No inició PPO en escala $scale" >&2; kill -TERM "$launch_pid" 2>/dev/null || true; exit 1
  fi
  CAMPAIGN_DIR="$campaign" WAIT_SECONDS=60 bash "$root/Experimentos/ejecutar_ensayo_gazebo.sh" "$label" ppo
  kill -INT -- -"$launch_pid" 2>/dev/null || true
  sleep 5
  pkill -TERM -f 'ros2 launch nova_gait_controller' 2>/dev/null || true
  pkill -TERM -f '/nova_gait_controller/lib/nova_gait_controller/' 2>/dev/null || true
  pkill -TERM -f 'ign gazebo' 2>/dev/null || true
  sleep 3
done
python3 "$root/Experimentos/comparar_escala_ppo.py" "$campaign"
