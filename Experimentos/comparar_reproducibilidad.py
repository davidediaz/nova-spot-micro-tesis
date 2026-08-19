#!/usr/bin/env python3
"""Compara dos CSV de métricas por ciclo usando igual número de ciclos."""

import argparse
import csv
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


FIELDS = [
    ("duracion_observada_s", "Duración observada", "s"),
    ("avance_m", "Avance", "m/ciclo"),
    ("velocidad_media_m_s", "Velocidad media", "m/s"),
    ("excursion_lateral_m", "Excursión lateral", "m"),
    ("altura_media_m", "Altura media", "m"),
    ("roll_max_abs_deg", "Roll máximo absoluto", "grados"),
    ("pitch_max_abs_deg", "Pitch máximo absoluto", "grados"),
    ("salto_articular_max_rad", "Salto articular máximo", "rad"),
]


def read_csv(path):
    with path.open(encoding="utf-8", newline="") as handle:
        return [{key: float(value) for key, value in row.items()} for row in csv.DictReader(handle)]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("ensayo_1", type=Path)
    parser.add_argument("ensayo_2", type=Path)
    parser.add_argument("output", type=Path)
    parser.add_argument("--label", default="gateo")
    args = parser.parse_args()
    args.output.mkdir(parents=True, exist_ok=True)
    first = read_csv(args.ensayo_1)
    second = read_csv(args.ensayo_2)
    common = min(len(first), len(second))
    first = first[:common]
    second = second[:common]
    # Se reportan todos los ciclos y también el régimen permanente sin el
    # primer ciclo transitorio; nunca se elimina silenciosamente del CSV.
    rows = []
    for field, label, unit in FIELDS:
        a = np.asarray([row[field] for row in first])
        b = np.asarray([row[field] for row in second])
        a_steady, b_steady = a[1:], b[1:]
        mean_a, mean_b = float(np.mean(a_steady)), float(np.mean(b_steady))
        relative = 100.0 * (mean_b - mean_a) / mean_a if mean_a else float("nan")
        rows.append({
            "metrica": label,
            "unidad": unit,
            "media_ensayo_1": mean_a,
            "media_ensayo_2": mean_b,
            "diferencia_absoluta": mean_b - mean_a,
            "diferencia_relativa_pct": relative,
            "rmse_ciclo_a_ciclo": float(np.sqrt(np.mean((b_steady - a_steady) ** 2))),
        })

    csv_path = args.output / "comparacion_reproducibilidad.csv"
    with csv_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)

    cycles = np.arange(1, common + 1)
    figure, axes = plt.subplots(2, 2, figsize=(13, 9), constrained_layout=True)
    graph_fields = [
        ("avance_m", "Avance (m/ciclo)"),
        ("velocidad_media_m_s", "Velocidad media (m/s)"),
        ("excursion_lateral_m", "Excursión lateral (m)"),
        ("pitch_max_abs_deg", "Pitch máximo absoluto (°)"),
    ]
    for axis, (field, label) in zip(axes.flat, graph_fields):
        axis.plot(cycles, [row[field] for row in first], "o-", label="Ensayo 1", linewidth=1.1)
        axis.plot(cycles, [row[field] for row in second], "s--", label="Ensayo 2", linewidth=1.1)
        axis.set_xlabel("Ciclo")
        axis.set_ylabel(label)
        axis.grid(True, alpha=0.3)
        axis.legend()
    figure.suptitle(
        f"Reproducibilidad de {args.label} sobre {common} ciclos equivalentes")
    figure.savefig(args.output / "comparacion_reproducibilidad.png", dpi=180)
    plt.close(figure)

    lines = [
        f"# Comparación de reproducibilidad de {args.label}",
        "",
        f"Se comparan los primeros {common} ciclos completos de cada ensayo.",
        "El ciclo 1 se conserva en los archivos y gráficas como transitorio de arranque;",
        f"los promedios comparativos siguientes usan los ciclos 2 al {common}.",
        "",
        "| Métrica | Ensayo 1 | Ensayo 2 | Diferencia relativa | RMSE ciclo a ciclo |",
        "|---|---:|---:|---:|---:|",
    ]
    for row in rows:
        lines.append(
            f"| {row['metrica']} ({row['unidad']}) | {row['media_ensayo_1']:.6f} | "
            f"{row['media_ensayo_2']:.6f} | {row['diferencia_relativa_pct']:.3f} % | "
            f"{row['rmse_ciclo_a_ciclo']:.6f} |"
        )
    lines.extend([
        "",
        "## Interpretación",
        "",
        "La reproducibilidad se evalúa con la diferencia relativa entre medias y el RMSE ciclo a ciclo. "
        "No se declara equivalencia estadística formal con solo dos ensayos; estos resultados cuantifican repetibilidad en simulación bajo la misma configuración.",
        "",
    ])
    (args.output / "INFORME_REPRODUCIBILIDAD.md").write_text("\n".join(lines), encoding="utf-8")
    print(f"Comparados {common} ciclos; resultados en {args.output}")


if __name__ == "__main__":
    main()
