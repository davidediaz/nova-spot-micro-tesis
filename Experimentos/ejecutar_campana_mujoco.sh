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
  kill -INT "$LAUNCH_PID" 2>/dev/null || true
  for _ in $(seq 1 40); do
    kill -0 "$LAUNCH_PID" 2>/dev/null || {
      wait "$LAUNCH_PID" 2>/dev/null || true
      LAUNCH_PID=""
      return 0
    }
    sleep 0.25
  done
  kill -TERM "$LAUNCH_PID" 2>/dev/null || true
  sleep 1
  kill -KILL "$LAUNCH_PID" 2>/dev/null || true
  wait "$LAUNCH_PID" 2>/dev/null || true
  LAUNCH_PID=""
}
cleanup() {
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
  # QoS volátil: publicar varias veces evita perder un marcador por descubrimiento DDS.
  ros2 topic pub --times 3 --rate 5 /nova/gait_command \
    std_msgs/msg/String "{data: $command}" >/dev/null
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
  ros2 launch nova_gait_controller mujoco_demo.launch.py headless:=true \
    sim_speed_factor:="$FACTOR" > "$SALIDA/mujoco_${NOMBRE}.log" 2>&1 &
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
    /world/empty/dynamic_pose/info > "$SALIDA/rosbag_${NOMBRE}.log" 2>&1 &
  BAG_PID=$!
  wait_for_log "$SALIDA/rosbag_${NOMBRE}.log" \
    "Subscribed to topic '/nova/gait_command'" "la suscripción del grabador a comandos"
  wait_for_log "$SALIDA/rosbag_${NOMBRE}.log" \
    "Subscribed to topic '/nova/gait_phase'" "la suscripción del grabador a fases"
  publish_marker stand
  sleep 1
  publish_marker "$MARCHA"
  sleep "$ESPERA"
  publish_marker stand
  sleep 1
  kill -INT "$BAG_PID"
  wait "$BAG_PID"
  BAG_PID=""
  python3 Experimentos/analizar_gateo_rosbag.py "$BAG" "$ANALISIS" \
    --start-command "$MARCHA" --samples-per-cycle "$MUESTRAS" --phase-duration "$FASE"
  python3 Experimentos/analizar_contactos_rosbag.py "$BAG" "$CONTACTOS"
  python3 Experimentos/analizar_mujoco_articulaciones.py "$BAG" "$ARTICULACIONES" \
    --samples-per-cycle "$MUESTRAS" --start-command "$MARCHA"

  stop_launch
done

python3 Experimentos/resumir_campana_mujoco.py "$SALIDA" --expected "$ULTIMA_REP" \
  --minimum-cycles "$CICLOS"
