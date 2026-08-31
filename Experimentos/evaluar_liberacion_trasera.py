#!/usr/bin/env python3
"""Criba cartesiana de liberación temprana de las patas traseras.

Mantiene congelados paso, elevación máxima, cadencia y descenso 0,20/0,75.
Solo cambia la altura trasera normalizada al 25 % de la oscilación.
"""

import argparse
import csv
from pathlib import Path

from nova_gait_controller.kinematics import cartesian_crawl, forward_leg


STAND = (0.10, 0.42, -0.84)
LEGS = (("fl", 0, 1), ("fr", 3, -1), ("rl", 6, 1), ("rr", 9, -1))
NOMINAL = 2 ** -0.5
MAX_JOINT_JUMP_RAD = 0.20
CANDIDATES = (NOMINAL, 0.75, 0.80, 0.85, 0.90, 0.95, 1.00)


def evaluate(liftoff_ratio):
    poses = cartesian_crawl(
        STAND, samples=24, step_length=0.018, step_height=0.014,
        lateral_shift=0.004, fore_aft_shift=0.008,
        front_landing_height_ratio=0.20,
        rear_landing_height_ratio=0.75,
        rear_liftoff_height_ratio=liftoff_ratio)
    cyclic = poses + poses[:1]
    joint_jump = max(
        abs(cyclic[index][joint] - cyclic[index - 1][joint])
        for index in range(1, len(cyclic)) for joint in range(12))
    foot_jump = 0.0
    for _, offset, side in LEGS:
        points = [forward_leg(*pose[offset:offset + 3], side) for pose in cyclic]
        foot_jump = max(foot_jump, max(
            sum((points[index][axis] - points[index - 1][axis]) ** 2
                for axis in range(3)) ** 0.5
            for index in range(1, len(points))))

    neutral_z = forward_leg(*STAND, side=-1)[2]
    rr_liftoff_z = forward_leg(*poses[8][9:12], side=-1)[2] - neutral_z
    return {
        "rear_liftoff_height_ratio": liftoff_ratio,
        "rear_height_at_25_percent_m": rr_liftoff_z,
        "max_joint_jump_rad": joint_jump,
        "max_foot_jump_m": foot_jump,
        "reachable": True,
        "periodic": True,
        "passes_implemented_limit": joint_jump < MAX_JOINT_JUMP_RAD,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    args.output.mkdir(parents=True, exist_ok=True)

    rows = []
    for ratio in CANDIDATES:
        try:
            rows.append(evaluate(ratio))
        except ValueError:
            rows.append({
                "rear_liftoff_height_ratio": ratio,
                "rear_height_at_25_percent_m": "",
                "max_joint_jump_rad": "", "max_foot_jump_m": "",
                "reachable": False, "periodic": False,
                "passes_implemented_limit": False,
            })

    with (args.output / "matriz_liberacion_trasera.csv").open(
            "w", newline="", encoding="utf-8") as stream:
        writer = csv.DictWriter(stream, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)

    report = [
        "# Criba cartesiana de liberación trasera",
        "",
        "Fecha: 31 de agosto de 2026, America/Bogota.",
        "",
        "La evidencia de Gazebo mostró que RL y RR recuperaban contacto "
        "0,07--0,08 s después del despegue observado, todavía durante el "
        "ascenso. Por ello esta criba mantiene el descenso 0,20/0,75 y actúa "
        "solo sobre la altura trasera al 25 % de la oscilación.",
        "",
        "Se conservaron 24 muestras, paso de 0,018 m, elevación máxima de "
        "0,014 m, transferencia lateral de 0,004 m y longitudinal de 0,008 m.",
        "",
        "| Relación de ascenso trasero | Altura al 25 % (m) | "
        "Salto articular máximo (rad) | Salto cartesiano máximo (m) | Pasa |",
        "|---:|---:|---:|---:|:---:|",
    ]
    for row in rows:
        if row["reachable"]:
            report.append(
                f"| {row['rear_liftoff_height_ratio']:.9f} | "
                f"{row['rear_height_at_25_percent_m']:.6f} | "
                f"{row['max_joint_jump_rad']:.6f} | "
                f"{row['max_foot_jump_m']:.6f} | "
                f"{'sí' if row['passes_implemented_limit'] else 'no'} |")
        else:
            report.append(
                f"| {row['rear_liftoff_height_ratio']:.9f} | -- | -- | -- | no |")
    report.extend([
        "",
        "Esta criba no demuestra separación física. Los valores aceptados "
        "deben compararse en Gazebo contra el nominal y 0,20/0,75 desde "
        "estados iniciales equivalentes. El archivo `gaits.yaml` conserva el "
        "valor nominal; no se ha congelado una nueva línea base.",
    ])
    (args.output / "INFORME_CRIBA_LIBERACION_TRASERA.md").write_text(
        "\n".join(report) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
