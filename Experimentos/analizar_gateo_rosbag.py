#!/usr/bin/env python3
"""Analiza por ciclo la línea base de gateo almacenada con rosbag2."""

import argparse
import csv
import json
import math
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from rclpy.serialization import deserialize_message
from rosbag2_py import ConverterOptions, SequentialReader, StorageOptions
from rosidl_runtime_py.utilities import get_message


CYCLE_DURATION_S = 4.32


def read_bag(bag_path):
    reader = SequentialReader()
    reader.open(
        StorageOptions(uri=str(bag_path), storage_id="sqlite3"),
        ConverterOptions(input_serialization_format="cdr", output_serialization_format="cdr"),
    )
    topic_types = {item.name: item.type for item in reader.get_all_topics_and_types()}
    commands = []
    metrics = []
    safety = []
    trajectory_timestamps = []
    selected = {
        "/nova/gait_command", "/nova/metrics/json", "/nova/safety/triggered",
        "/joint_trajectory_controller/joint_trajectory",
    }

    while reader.has_next():
        topic, raw, timestamp_ns = reader.read_next()
        if topic not in selected:
            continue
        message = deserialize_message(raw, get_message(topic_types[topic]))
        if topic == "/nova/gait_command":
            commands.append((timestamp_ns, message.data))
        elif topic == "/nova/safety/triggered":
            safety.append((timestamp_ns, bool(message.data)))
        elif topic == "/joint_trajectory_controller/joint_trajectory":
            trajectory_timestamps.append(timestamp_ns)
        else:
            metrics.append((timestamp_ns, json.loads(message.data)))
    return commands, metrics, safety, trajectory_timestamps


def command_window(commands, start_commands):
    gateo_markers = [timestamp for timestamp, command in commands if command in start_commands]
    if not gateo_markers:
        raise RuntimeError("La bolsa no contiene una orden gateo/crawl")
    # Si el marcador se publicó de forma redundante, la última orden reinició
    # la fase cero y define el comienzo limpio de la ventana comparable.
    gateo = max(gateo_markers)
    stand = next(
        (timestamp for timestamp, command in commands if timestamp > gateo and command in ("stand", "stop")),
        None,
    )
    if stand is None:
        raise RuntimeError("La bolsa no contiene una orden stand/stop posterior al gateo")
    return gateo, stand


def rms(values):
    array = np.asarray(values, dtype=float)
    return float(np.sqrt(np.mean(array * array)))


def joint_continuity(samples):
    maximum_jump = 0.0
    maximum_speed = 0.0
    previous = None
    for sample in samples:
        names = sample["joint_names"]
        positions = dict(zip(names, sample["joint_positions_rad"]))
        velocities = [abs(float(value)) for value in sample.get("joint_velocities_rad_s", [])]
        if velocities:
            maximum_speed = max(maximum_speed, max(velocities))
        if previous is not None:
            common = positions.keys() & previous.keys()
            if common:
                maximum_jump = max(maximum_jump, max(abs(positions[name] - previous[name]) for name in common))
        previous = positions
    return maximum_jump, maximum_speed


def calculate_cycles(metrics, trajectory_timestamps, gateo_ns, stand_ns, samples_per_cycle):
    duration_s = (stand_ns - gateo_ns) / 1e9
    active_targets = [timestamp for timestamp in trajectory_timestamps if gateo_ns <= timestamp < stand_ns]
    complete_cycles = (len(active_targets) - 1) // samples_per_cycle
    if complete_cycles < 1:
        raise RuntimeError(
            f"No hay {samples_per_cycle} referencias articulares para formar un ciclo completo")
    boundaries = [
        active_targets[index * samples_per_cycle] for index in range(complete_cycles + 1)]
    rows = []
    traces = []

    for index in range(complete_cycles):
        start_ns = boundaries[index]
        end_ns = boundaries[index + 1]
        observed_duration_s = (end_ns - start_ns) / 1e9
        selected = [(timestamp, data) for timestamp, data in metrics if start_ns <= timestamp < end_ns]
        if len(selected) < 2:
            raise RuntimeError(f"El ciclo {index + 1} solo contiene {len(selected)} muestras")
        timestamps = np.asarray([(timestamp - gateo_ns) / 1e9 for timestamp, _ in selected])
        samples = [data for _, data in selected]
        x = np.asarray([sample["x_m"] for sample in samples], dtype=float)
        y = np.asarray([sample["y_m"] for sample in samples], dtype=float)
        height = np.asarray([sample["height_m"] for sample in samples], dtype=float)
        roll = np.asarray([sample["roll_deg"] for sample in samples], dtype=float)
        pitch = np.asarray([sample["pitch_deg"] for sample in samples], dtype=float)
        max_jump, max_speed = joint_continuity(samples)
        advance = float(x[-1] - x[0])
        row = {
            "ciclo": index + 1,
            "inicio_s": (start_ns - boundaries[0]) / 1e9,
            "fin_s": (end_ns - boundaries[0]) / 1e9,
            "duracion_observada_s": observed_duration_s,
            "muestras": len(samples),
            "avance_m": advance,
            "velocidad_media_m_s": advance / observed_duration_s,
            "deriva_lateral_m": float(y[-1] - y[0]),
            "excursion_lateral_m": float(np.max(np.abs(y - y[0]))),
            "altura_min_m": float(np.min(height)),
            "altura_max_m": float(np.max(height)),
            "altura_media_m": float(np.mean(height)),
            "roll_rms_deg": rms(roll),
            "roll_max_abs_deg": float(np.max(np.abs(roll))),
            "pitch_rms_deg": rms(pitch),
            "pitch_max_abs_deg": float(np.max(np.abs(pitch))),
            "salto_articular_max_rad": max_jump,
            "velocidad_articular_max_rad_s": max_speed,
        }
        rows.append(row)
        traces.append((timestamps, x, y, height, roll, pitch))
    return duration_s, rows, traces


def write_csv(rows, output_path):
    with output_path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def plot_time_series(traces, output_path, gait_label):
    time = np.concatenate([trace[0] for trace in traces])
    series = [np.concatenate([trace[column] for trace in traces]) for column in range(1, 6)]
    labels = ["Avance x (m)", "Posición y (m)", "Altura (m)", "Roll (°)", "Pitch (°)"]
    figure, axes = plt.subplots(5, 1, figsize=(12, 13), sharex=True, constrained_layout=True)
    for axis, values, label in zip(axes, series, labels):
        axis.plot(time, values, linewidth=0.9)
        axis.set_ylabel(label)
        axis.grid(True, alpha=0.3)
        for boundary in [trace[0][0] for trace in traces] + [traces[-1][0][-1]]:
            axis.axvline(boundary, color="0.75", linewidth=0.45)
    axes[-1].set_xlabel(f"Tiempo desde la orden {gait_label} (s)")
    figure.suptitle(f"{gait_label.capitalize()}: series temporales y límites de ciclo")
    figure.savefig(output_path, dpi=180)
    plt.close(figure)


def plot_cycle_summary(rows, output_path):
    cycle = [row["ciclo"] for row in rows]
    figure, axes = plt.subplots(3, 2, figsize=(13, 12), constrained_layout=True)
    plots = [
        ("avance_m", "Avance por ciclo (m)"),
        ("velocidad_media_m_s", "Velocidad media (m/s)"),
        ("excursion_lateral_m", "Excursión lateral (m)"),
        ("roll_max_abs_deg", "Roll máximo absoluto (°)"),
        ("pitch_max_abs_deg", "Pitch máximo absoluto (°)"),
        ("salto_articular_max_rad", "Salto articular máximo (rad)"),
    ]
    for axis, (field, label) in zip(axes.flat, plots):
        axis.bar(cycle, [row[field] for row in rows], color="#1f4e79")
        axis.set_xlabel("Ciclo")
        axis.set_ylabel(label)
        axis.set_xticks(cycle)
        axis.grid(True, axis="y", alpha=0.3)
    figure.suptitle("Resumen cuantitativo por ciclo")
    figure.savefig(output_path, dpi=180)
    plt.close(figure)


def describe(rows, field):
    values = np.asarray([row[field] for row in rows], dtype=float)
    return float(np.mean(values)), float(np.std(values, ddof=1)), float(np.min(values)), float(np.max(values))


def write_report(output_path, bag_path, duration_s, rows, safety, nominal_cycle_s,
                 gait_label):
    fields = [
        ("avance_m", "Avance por ciclo", "m"),
        ("velocidad_media_m_s", "Velocidad media", "m/s"),
        ("excursion_lateral_m", "Excursión lateral", "m"),
        ("altura_media_m", "Altura media", "m"),
        ("roll_max_abs_deg", "Roll máximo absoluto", "grados"),
        ("pitch_max_abs_deg", "Pitch máximo absoluto", "grados"),
        ("salto_articular_max_rad", "Salto articular máximo", "rad"),
    ]
    lines = [
        f"# Análisis automático de {gait_label}",
        "",
        f"- Bolsa: `{bag_path}`.",
        f"- Ventana {gait_label}--stand: {duration_s:.9f} s.",
        f"- Duración nominal configurada por ciclo: {nominal_cycle_s:.2f} s.",
        f"- Duración observada media por ciclo: {np.mean([row['duracion_observada_s'] for row in rows]):.6f} s.",
        f"- Ciclos completos analizados: {len(rows)}.",
        f"- Activaciones verdaderas del supervisor: {sum(value for _, value in safety)}.",
        "",
        "## Estadísticos entre ciclos",
        "",
        "| Métrica | Media | Desv. estándar | Mínimo | Máximo |",
        "|---|---:|---:|---:|---:|",
    ]
    for field, label, unit in fields:
        mean, std, minimum, maximum = describe(rows, field)
        lines.append(f"| {label} ({unit}) | {mean:.6f} | {std:.6f} | {minimum:.6f} | {maximum:.6f} |")
    total_advance = sum(row["avance_m"] for row in rows)
    lines.extend([
        "",
        "## Resultado",
        "",
        f"Los {len(rows)} ciclos completos acumularon {total_advance:.6f} m de avance medido entre la primera y última muestra de cada ciclo. ",
        "No se cambiaron paso, elevación ni duración de muestra durante la ventana.",
        "",
        "La continuidad articular se expresa como el mayor salto absoluto entre dos muestras consecutivas de una misma articulación. La velocidad articular máxima se obtiene del campo medido `joint_velocities_rad_s`.",
        "",
        "Archivos generados:",
        "",
        "- `metricas_por_ciclo.csv`",
        "- `series_temporales.png`",
        "- `resumen_por_ciclo.png`",
        "- `INFORME_ANALISIS.md`",
        "",
    ])
    output_path.write_text("\n".join(lines), encoding="utf-8")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("bag", type=Path)
    parser.add_argument("output", type=Path)
    parser.add_argument("--start-command", default="gateo")
    parser.add_argument("--samples-per-cycle", type=int, default=24)
    parser.add_argument("--phase-duration", type=float, default=0.18)
    arguments = parser.parse_args()
    arguments.output.mkdir(parents=True, exist_ok=True)
    commands, metrics, safety, trajectory_timestamps = read_bag(arguments.bag)
    aliases = {arguments.start_command}
    if arguments.start_command == "gateo":
        aliases.add("crawl")
    elif arguments.start_command == "paso":
        aliases.add("step")
    gateo_ns, stand_ns = command_window(commands, aliases)
    duration_s, rows, traces = calculate_cycles(
        metrics, trajectory_timestamps, gateo_ns, stand_ns,
        arguments.samples_per_cycle)
    write_csv(rows, arguments.output / "metricas_por_ciclo.csv")
    gait_label = "marcha paso" if arguments.start_command == "paso" else "gateo"
    plot_time_series(traces, arguments.output / "series_temporales.png", gait_label)
    plot_cycle_summary(rows, arguments.output / "resumen_por_ciclo.png")
    write_report(
        arguments.output / "INFORME_ANALISIS.md", arguments.bag, duration_s,
        rows, safety, arguments.samples_per_cycle * arguments.phase_duration,
        gait_label)
    print(json.dumps({"duration_s": duration_s, "complete_cycles": len(rows), "output": str(arguments.output)}, indent=2))


if __name__ == "__main__":
    main()
