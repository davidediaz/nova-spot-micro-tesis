#!/usr/bin/env bash
set -euo pipefail

source /opt/ros/humble/setup.bash
source install/setup.bash

RESULTADOS=${1:-Experimentos/pruebas_dinamicas_supervisor}
export ROS_DOMAIN_ID=${ROS_DOMAIN_ID:-93}
mkdir -p "$RESULTADOS"

run_scenario() {
  local scenario=$1
  shift
  timeout 7s ros2 run nova_gait_controller safety_supervisor --ros-args "$@" \
    > "$RESULTADOS/supervisor_${scenario}.log" 2>&1 &
  local supervisor_pid=$!
  sleep 1
  ros2 run nova_gait_controller safety_test_node \
    --scenario "$scenario" --output "$RESULTADOS/${scenario}.json"
  wait "$supervisor_pid" || test $? -eq 124
}

run_scenario margin -p enable_stability_stop:=true \
  -p stability_topic:=/nova/stability_test -p startup_grace_period:=0.0
run_scenario contact -p enable_contact_stop:=true \
  -p contact_diagnostics_topic:=/nova/contact_diagnostics_test \
  -p startup_grace_period:=0.0
run_scenario timeout -p enable_data_timeout_stop:=true \
  -p startup_grace_period:=2.0 -p data_timeout:=0.5
run_scenario low_height -p pose_topic:=/nova/pose_test -p startup_grace_period:=0.0
run_scenario high_height -p pose_topic:=/nova/pose_test -p startup_grace_period:=0.0
run_scenario roll -p pose_topic:=/nova/pose_test -p startup_grace_period:=0.0
run_scenario pitch -p pose_topic:=/nova/pose_test -p startup_grace_period:=0.0
run_scenario joint_limit -p trajectory_topic:=/nova/joint_trajectory_test \
  -p startup_grace_period:=0.0
run_scenario discontinuity -p trajectory_topic:=/nova/joint_trajectory_test \
  -p startup_grace_period:=0.0

python3 Experimentos/validar_pruebas_dinamicas_supervisor.py "$RESULTADOS"
