#!/usr/bin/env bash
set -eo pipefail

source /opt/ros/humble/setup.bash
source install/setup.bash
set -u

MARCHA=${1:-paso}
REPETICIONES=${2:-5}
CICLOS=${3:-20}
SALIDA=${4:-Experimentos/campanas_mujoco/${MARCHA}}
FACTOR=${SIM_SPEED_FACTOR:-4.0}
STEP_FORE_AFT_SHIFT=${STEP_FORE_AFT_SHIFT:-0.0}
STEP_HEIGHT=${STEP_HEIGHT:-0.008}
GROUND_FRICTION=${GROUND_FRICTION:-0.9}
ACTUATOR_KP=${ACTUATOR_KP:-40.0}
ACTUATOR_KV=${ACTUATOR_KV:-4.0}
MUJOCO_MODEL=${MUJOCO_MODEL:-}
PUSH_FORCE_X=${PUSH_FORCE_X:-0.0}
PUSH_DELAY_S=${PUSH_DELAY_S:-10.0}
PUSH_PID=""
INICIO_REP=${INICIO_REP:-1}
export ROS_DOMAIN_ID=${ROS_DOMAIN_ID:-102}

if [[ "$MARCHA" == "paso" ]]; then
  MUESTRAS=32
  FASE=0.18
else
  MARCHA=gateo
  MUESTRAS=24
  FASE=0.18
fi
CICLO_SIM=$(awk -v n="$MUESTRAS" -v d="$FASE" 'BEGIN {print n*d}')
# Los temporizadores del controlador siguen el ritmo de ejecución ROS observado;
# acelerar la física no debe acortar la ventana ni reducir el número de referencias.
ESPERA=$(awk -v c="$CICLOS" -v t="$CICLO_SIM" 'BEGIN {print int(c*t+5)}')
mkdir -p "$SALIDA"

LAUNCH_PID=""
BAG_PID=""
stop_launch() {
  [[ -n "$LAUNCH_PID" ]] || return 0
  # El launch se inicia con setsid: la señal negativa alcanza también todos
  # sus nodos hijos y evita dejar simuladores huérfanos entre repeticiones.
  kill -INT -- "-$LAUNCH_PID" 2>/dev/null || true
  for _ in $(seq 1 40); do
    kill -0 -- "-$LAUNCH_PID" 2>/dev/null || {
      wait "$LAUNCH_PID" 2>/dev/null || true
      LAUNCH_PID=""
      return 0
    }
    sleep 0.25
  done
  kill -TERM -- "-$LAUNCH_PID" 2>/dev/null || true
  sleep 1
  kill -KILL -- "-$LAUNCH_PID" 2>/dev/null || true
  wait "$LAUNCH_PID" 2>/dev/null || true
  LAUNCH_PID=""
}
stop_push() {
  if [[ -n "$PUSH_PID" ]]; then
    kill "$PUSH_PID" 2>/dev/null || true
    wait "$PUSH_PID" 2>/dev/null || true
    PUSH_PID=""
  fi
}
cleanup() {
  stop_push
  if [[ -n "$BAG_PID" ]]; then
    kill -INT "$BAG_PID" 2>/dev/null || true
    wait "$BAG_PID" 2>/dev/null || true
  fi
  stop_launch
}
trap cleanup EXIT

wait_for_log() {
  local file=$1
  local pattern=$2
  local description=$3
  for _ in $(seq 1 120); do
    if grep -Fq "$pattern" "$file" 2>/dev/null; then
      return 0
    fi
    sleep 0.25
  done
  echo "Tiempo agotado esperando $description" >&2
  return 1
}

publish_marker() {
  local command=$1
  # Esperar grabador + controlador evita que el publicador efímero enlace solo
  # con rosbag y pierda la orden de marcha durante el descubrimiento DDS.
  ros2 topic pub --times 3 --rate 5 --wait-matching-subscriptions 2 \
    --qos-durability volatile --keep-alive 0.5 /nova/gait_command \
    std_msgs/msg/String "{data: $command}" >/dev/null
}

publish_friction() {
  ros2 topic pub --times 3 --rate 5 --wait-matching-subscriptions 2 \
    --qos-durability volatile --keep-alive 0.5 /nova/mujoco/ground_friction \
    std_msgs/msg/Float64 "{data: $GROUND_FRICTION}" >/dev/null
}

publish_scalar_parameter() {
  local topic=$1
  local value=$2
  ros2 topic pub --times 3 --rate 5 --wait-matching-subscriptions 2 \
    --qos-durability volatile --keep-alive 0.5 "$topic" \
    std_msgs/msg/Float64 "{data: $value}" >/dev/null
}

publish_push_after_delay() {
  sleep "$PUSH_DELAY_S"
  ros2 topic pub --times 5 --rate 20 --wait-matching-subscriptions 2 \
    --qos-durability volatile --keep-alive 0.5 /nova/mujoco/external_wrench \
    geometry_msgs/msg/WrenchStamped "{wrench: {force: {x: $PUSH_FORCE_X, y: 0.0, z: 0.0}}}" \
    >/dev/null
}

ULTIMA_REP=$((INICIO_REP + REPETICIONES - 1))
for REP in $(seq "$INICIO_REP" "$ULTIMA_REP"); do
  NOMBRE="${MARCHA}_r${REP}"
  BAG="$SALIDA/rosbag2/$NOMBRE"
  ANALISIS="$SALIDA/analisis/$NOMBRE"
  CONTACTOS="$SALIDA/contactos/$NOMBRE"
  ARTICULACIONES="$SALIDA/articulaciones/$NOMBRE"

  if [[ -e "$BAG" ]]; then
    echo "Ya existe $BAG; no se sobrescribe" >&2
    exit 1
  fi

  # Una instancia nueva por ensayo mantiene /clock monótono y aísla el estado.
  LAUNCH_ARGS=(headless:=true sim_speed_factor:="$FACTOR"
    step_fore_aft_shift:="$STEP_FORE_AFT_SHIFT" step_height:="$STEP_HEIGHT")
  if [[ -n "$MUJOCO_MODEL" ]]; then
    LAUNCH_ARGS+=(mujoco_model:="$MUJOCO_MODEL")
  fi
  setsid ros2 launch nova_gait_controller mujoco_demo.launch.py \
    "${LAUNCH_ARGS[@]}" > "$SALIDA/mujoco_${NOMBRE}.log" 2>&1 &
  LAUNCH_PID=$!
  for _ in $(seq 1 60); do
    ros2 service type /mujoco_ros2_control_node/reset_world >/dev/null 2>&1 && break
    sleep 0.5
  done
  ros2 service type /mujoco_ros2_control_node/reset_world >/dev/null 2>&1 || {
    echo "MuJoCo no quedó disponible para $NOMBRE" >&2
    exit 1
  }
  wait_for_log "$SALIDA/mujoco_${NOMBRE}.log" \
    'Control discreto listo.' "el controlador de marcha"
  ros2 bag record -o "$BAG" /clock /joint_states \
    /joint_trajectory_controller/joint_trajectory /nova/gait_command \
    /nova/gait_phase /nova/imu /nova/foot_contacts /nova/contact_diagnostics \
    /nova/stability /nova/metrics/json /nova/safety/triggered \
    /nova/mujoco/ground_friction \
    /nova/mujoco/actuator_kp /nova/mujoco/actuator_kv \
    /nova/mujoco/external_wrench \
    /world/empty/dynamic_pose/info > "$SALIDA/rosbag_${NOMBRE}.log" 2>&1 &
  BAG_PID=$!
  wait_for_log "$SALIDA/rosbag_${NOMBRE}.log" \
    "Subscribed to topic '/nova/gait_command'" "la suscripción del grabador a comandos"
  wait_for_log "$SALIDA/rosbag_${NOMBRE}.log" \
    "Subscribed to topic '/nova/gait_phase'" "la suscripción del grabador a fases"
  publish_marker stand
  publish_friction
  publish_scalar_parameter /nova/mujoco/actuator_kp "$ACTUATOR_KP"
  publish_scalar_parameter /nova/mujoco/actuator_kv "$ACTUATOR_KV"
  if [[ "$PUSH_FORCE_X" != "0.0" && "$PUSH_FORCE_X" != "0" ]]; then
    publish_push_after_delay &
    PUSH_PID=$!
  fi
  sleep 1
  publish_marker "$MARCHA"
  sleep "$ESPERA"
  publish_marker stand
  sleep 1
  kill -INT "$BAG_PID"
  wait "$BAG_PID"
  BAG_PID=""
  stop_push
  python3 Experimentos/analizar_gateo_rosbag.py "$BAG" "$ANALISIS" \
    --start-command "$MARCHA" --samples-per-cycle "$MUESTRAS" --phase-duration "$FASE"
  python3 Experimentos/analizar_contactos_rosbag.py "$BAG" "$CONTACTOS"
  python3 Experimentos/analizar_mujoco_articulaciones.py "$BAG" "$ARTICULACIONES" \
    --samples-per-cycle "$MUESTRAS" --start-command "$MARCHA"

  stop_launch
done

python3 Experimentos/resumir_campana_mujoco.py "$SALIDA" --expected "$ULTIMA_REP" \
  --minimum-cycles "$CICLOS"
