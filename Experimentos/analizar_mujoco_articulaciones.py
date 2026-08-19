#!/usr/bin/env python3
"""Valida ciclos y seguimiento articular de una bolsa MuJoCo."""

import argparse
import bisect
import csv
from pathlib import Path

import numpy as np
from rclpy.serialization import deserialize_message
from rosbag2_py import ConverterOptions, SequentialReader, StorageOptions
from rosidl_runtime_py.utilities import get_message


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("bag", type=Path)
    parser.add_argument("output", type=Path)
    parser.add_argument("--samples-per-cycle", type=int, default=32)
    args = parser.parse_args()
    args.output.mkdir(parents=True, exist_ok=True)

    reader = SequentialReader()
    reader.open(StorageOptions(uri=str(args.bag), storage_id="sqlite3"),
                ConverterOptions("cdr", "cdr"))
    types = {item.name: item.type for item in reader.get_all_topics_and_types()}
    commands, trajectories, states = [], [], []
    while reader.has_next():
        topic, raw, timestamp = reader.read_next()
        if topic not in {"/nova/gait_command", "/joint_trajectory_controller/joint_trajectory", "/joint_states"}:
            continue
        message = deserialize_message(raw, get_message(types[topic]))
        if topic == "/nova/gait_command":
            commands.append((timestamp, message.data))
        elif topic == "/joint_trajectory_controller/joint_trajectory" and message.points:
            trajectories.append((timestamp, message))
        else:
            states.append((timestamp, message))

    starts = [timestamp for timestamp, command in commands if command in ("paso", "step")]
    if not starts:
        raise RuntimeError("No se encontró la orden paso/step")
    start = max(starts)
    end = next(timestamp for timestamp, command in commands
               if timestamp > start and command in ("stand", "stop"))
    targets = [(timestamp, message) for timestamp, message in trajectories if start <= timestamp < end]
    complete_cycles = (len(targets) - 1) // args.samples_per_cycle
    usable_targets = targets[:complete_cycles * args.samples_per_cycle]

    state_times = [timestamp for timestamp, _ in states]
    errors = []
    rows = []
    for target_time, trajectory in usable_targets:
        point = trajectory.points[0]
        delay_ns = point.time_from_start.sec * 1_000_000_000 + point.time_from_start.nanosec
        wanted_time = target_time + delay_ns
        position = bisect.bisect_left(state_times, wanted_time)
        candidates = [index for index in (position - 1, position) if 0 <= index < len(states)]
        index = min(candidates, key=lambda item: abs(state_times[item] - wanted_time))
        _, state = states[index]
        measured = dict(zip(state.name, state.position))
        target = dict(zip(trajectory.joint_names, point.positions))
        sample_errors = [measured[name] - target[name] for name in target if name in measured]
        if len(sample_errors) != len(target):
            raise RuntimeError("Faltan articulaciones en /joint_states")
        errors.append(sample_errors)

    error_array = np.asarray(errors, dtype=float)
    target_times = [timestamp for timestamp, _ in targets]
    for cycle in range(complete_cycles):
        cycle_errors = error_array[
            cycle * args.samples_per_cycle:(cycle + 1) * args.samples_per_cycle]
        first = cycle * args.samples_per_cycle
        last = (cycle + 1) * args.samples_per_cycle
        duration = (target_times[last] - target_times[first]) / 1e9
        rows.append({
            "ciclo": cycle + 1,
            "duracion_s": duration,
            "error_rms_rad": float(np.sqrt(np.mean(cycle_errors ** 2))),
            "error_max_abs_rad": float(np.max(np.abs(cycle_errors))),
        })

    with (args.output / "metricas_mujoco_por_ciclo.csv").open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)

    steady = rows[1:] if len(rows) > 1 else rows
    lines = [
        "# Validación articular de marcha paso en MuJoCo",
        "",
        f"- Bolsa: `{args.bag}`.",
        f"- Ciclos completos: {complete_cycles}.",
        f"- Duración media: {np.mean([row['duracion_s'] for row in steady]):.6f} s.",
        f"- Error RMS articular medio: {np.mean([row['error_rms_rad'] for row in steady]):.6f} rad.",
        f"- Error máximo absoluto: {max(row['error_max_abs_rad'] for row in rows):.6f} rad.",
        "",
        "El error se evalúa cerca del final de `time_from_start` de cada referencia, comparando los doce objetivos con `/joint_states`. El ciclo 1 se conserva como transitorio; las medias usan los ciclos 2 en adelante.",
        "",
        "MuJoCo no publica todavía una pose corporal equivalente al puente de Gazebo; por ello esta validación demuestra ejecución temporal y seguimiento articular, no estabilidad corporal cuantitativa.",
    ]
    (args.output / "INFORME_MUJOCO.md").write_text("\n".join(lines), encoding="utf-8")
    print(f"MuJoCo: {complete_cycles} ciclos, {len(usable_targets)} referencias")


if __name__ == "__main__":
    main()
