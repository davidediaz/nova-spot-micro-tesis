#!/usr/bin/env bash
set -euo pipefail
label="$1"
mode="$2"
root="$(cd "$(dirname "$0")/.." && pwd)"
out="$root/Experimentos/campana_ppo_gazebo_20260902/$label"
rm -rf "$out"; mkdir -p "$out"
recdir="$(mktemp -d /tmp/gz_campaign_XXXX)"
topics=(/nova/gait_command /nova/metrics/json /nova/safety/triggered /joint_trajectory_controller/joint_trajectory /joint_states /world/empty/dynamic_pose/info /nova/imu /nova/contact_diagnostics /nova/stability)
ros2 bag record -o "$recdir/bag" "${topics[@]}" >"$recdir/record.log" 2>&1 & rec=$!
sleep 5
ros2 topic pub -r 2 /nova/gait_command std_msgs/msg/String '{data: paso}' >"$recdir/start.log" 2>&1 & starter=$!
sleep 2; kill "$starter" 2>/dev/null || true
sleep 20
ros2 topic pub -r 2 /nova/gait_command std_msgs/msg/String '{data: stand}' >"$recdir/stop.log" 2>&1 & stopper=$!
sleep 3; kill "$stopper" 2>/dev/null || true
kill -INT "$rec" 2>/dev/null || true; wait "$rec" || true
cp -a "$recdir/bag/." "$out/"
python3 "$root/Experimentos/analizar_gateo_rosbag.py" "$out" "$out/analisis" --start-command paso --samples-per-cycle 32 --phase-duration 0.18
