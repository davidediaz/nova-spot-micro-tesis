#!/usr/bin/env python3
"""Criba cartesiana reproducible de curvas de descenso del gateo.

No ejecuta ROS 2 ni Gazebo. Mantiene congelados paso, elevacion, muestras y
transferencia, y compara solamente las relaciones de aterrizaje por eje.
"""

import argparse
import csv
from itertools import product
from pathlib import Path

from nova_gait_controller.kinematics import cartesian_crawl, forward_leg


STAND = (0.10, 0.42, -0.84)
LEGS = (("fl", 0, 1), ("fr", 3, -1), ("rl", 6, 1), ("rr", 9, -1))
NOMINAL = 2 ** -0.5
MAX_JOINT_JUMP_RAD = 0.20


def evaluate(front_ratio, rear_ratio):
    poses = cartesian_crawl(
        STAND, samples=24, step_length=0.018, step_height=0.014,
        lateral_shift=0.004, fore_aft_shift=0.008,
        front_landing_height_ratio=front_ratio,
        rear_landing_height_ratio=rear_ratio)
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
    return {
        "front_ratio": front_ratio,
        "rear_ratio": rear_ratio,
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

    # Delante se busca adelantar el contacto; detras, retrasarlo. El nominal se
    # conserva como control y la matriz rodea el contraste explorado 0.20/0.80.
    pairs = [(NOMINAL, NOMINAL), *product((0.20, 0.35, 0.50),
                                          (0.75, 0.80, 0.85))]
    rows = []
    for front, rear in pairs:
        try:
            rows.append(evaluate(front, rear))
        except ValueError:
            rows.append({
                "front_ratio": front, "rear_ratio": rear,
                "max_joint_jump_rad": "", "max_foot_jump_m": "",
                "reachable": False, "periodic": False,
                "passes_implemented_limit": False,
            })

    csv_path = args.output / "matriz_curvas_descenso.csv"
    with csv_path.open("w", newline="", encoding="utf-8") as stream:
        writer = csv.DictWriter(stream, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)

    accepted = [row for row in rows if row["passes_implemented_limit"]]
    report = [
        "# Criba cartesiana de curvas de descenso",
        "",
        "Se mantuvieron 24 muestras, paso de 0,018 m, elevación de 0,014 m, "
        "transferencia lateral de 0,004 m y longitudinal de 0,008 m.",
        "",
        f"Criterio implementado: salto articular cíclico menor que "
        f"{MAX_JOINT_JUMP_RAD:.2f} rad. Este es el límite de la prueba unitaria "
        "vigente; el umbral provisional de 0,05 rad del protocolo debe ser "
        "revisado porque tampoco lo cumple la trayectoria nominal.",
        "",
        "## Candidatos que pasan la criba",
        "",
        "| Relación delantera | Relación trasera | Salto máximo (rad) | "
        "Salto cartesiano máximo (m) |",
        "|---:|---:|---:|---:|",
    ]
    for row in accepted:
        report.append(
            f"| {row['front_ratio']:.9f} | {row['rear_ratio']:.9f} | "
            f"{row['max_joint_jump_rad']:.6f} | "
            f"{row['max_foot_jump_m']:.6f} |")
    report.extend([
        "",
        "La criba solo demuestra alcanzabilidad y continuidad de referencias. "
        "No permite inferir el instante de contacto; los candidatos deben "
        "medirse de forma exploratoria en Gazebo antes de congelar parámetros.",
    ])
    (args.output / "INFORME_CRIBA_CARTESIANA.md").write_text(
        "\n".join(report) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
