#!/usr/bin/env bash
set -euo pipefail
for i in 1 2 3 4 5; do
  CAMPAIGN_DIR=campana_ppo_gazebo_20260903 bash "$(dirname "$0")/ejecutar_ensayo_gazebo.sh" "ppo_gazebo_0${i}" ppo
done
