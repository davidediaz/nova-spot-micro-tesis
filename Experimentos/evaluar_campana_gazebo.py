#!/usr/bin/env python3
"""Run the paired nominal/PPO Gazebo evaluation for all campaign policies."""

from __future__ import annotations

import argparse
import csv
import os
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SEEDS = (11, 23, 37, 53, 71)
GAITS = ("crawl", "step")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--campaign", type=Path, default=ROOT /
                        "Experimentos/reentrenamiento_ppo_completo_20260924")
    parser.add_argument("--episodes", type=int, default=1)
    args = parser.parse_args()
    output = args.campaign / "gazebo_evaluation.csv"
    rows = []
    env = os.environ.copy()
    env["PYTHONPATH"] = "/tmp/nova_rl_deps:" + env.get("PYTHONPATH", "")
    for gait in GAITS:
        for seed in SEEDS:
            policy = args.campaign / "gazebo" / f"{gait}_semilla_{seed}" / "policy.zip"
            partial = args.campaign / "gazebo_evaluation_parts" / f"{gait}_{seed}.csv"
            command = [sys.executable, str(ROOT / "Experimentos" /
                       "evaluar_ppo_gazebo.py"), "--gait", gait,
                       "--seed", str(seed), "--policy", str(policy),
                       "--episodes", str(args.episodes), "--output", str(partial)]
            print("+", " ".join(command), flush=True)
            subprocess.run(command, cwd=ROOT, env=env, check=True)
            with partial.open(newline="", encoding="utf-8") as handle:
                for row in csv.DictReader(handle):
                    row["seed"] = seed
                    rows.append(row)
    with output.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=[
            "simulator", "gait", "condition", "episodes", "return",
            "advance_m", "max_tilt_rad", "steps", "terminated", "seed",
        ])
        writer.writeheader()
        for row in rows:
            writer.writerow(row)
    print(f"Evaluación Gazebo escrita: {len(rows)} filas")


if __name__ == "__main__":
    main()
