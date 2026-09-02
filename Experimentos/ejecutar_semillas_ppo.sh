#!/usr/bin/env bash
set -euo pipefail
root="$(cd "$(dirname "$0")/.." && pwd)"
campaign="${CAMPAIGN_DIR:-campana_ppo_semillas_20260906}"
scale="${RESIDUAL_SCALE:-0.25}"
for seed in 11 23 37 53 71; do
  setsid ros2 launch nova_gait_controller ppo_gazebo.launch.py policy_path:="$root/Experimentos/ppo_residual_20260903/politica_semilla_${seed}.npz" residual_scale:="$scale" >"/tmp/ppo_seed_${seed}.log" 2>&1 & lp=$!
  sleep 12
  CAMPAIGN_DIR="$campaign" WAIT_SECONDS=60 bash "$root/Experimentos/ejecutar_ensayo_gazebo.sh" "semilla_${seed}" ppo
  kill -INT -- -"$lp" 2>/dev/null || true
  sleep 5
  pkill -TERM -f 'ros2 launch nova_gait_controller' 2>/dev/null || true
  pkill -TERM -f '/nova_gait_controller/lib/nova_gait_controller/' 2>/dev/null || true
  pkill -TERM -f 'ign gazebo' 2>/dev/null || true
  sleep 3
done
python3 "$root/Experimentos/comparar_semillas_ppo.py" "$campaign"
