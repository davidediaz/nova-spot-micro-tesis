#!/usr/bin/env python3
"""Protocolo de repetibilidad: varias repeticiones de cada condición, en orden alternado.

Cada condición (marcha + política) se camina --duracion-s segundos con las dos cámaras
(grabar_caminata.py) y se diagnostica (diagnostico_caminata.py). El orden se alterna por
rondas (ronda 1: A B C D, ronda 2: B C D A, ...) para que la fatiga, la temperatura de los
servos o la carga de la fuente no favorezcan a ninguna condición. Entre caminatas hay
--pausa-s segundos de descanso. Al final se actualiza el catálogo.
Las carpetas se llaman rep_<sesión>_<condición>_r<n>.

Uso: protocolo_repetibilidad.py --sesion 20261019 --repeticiones 3 \\
        --condicion gateo_base:gateo: --condicion gateo_ppo:gateo:ppo_v10_gateo/semilla_71/policy.zip ...
"""
import argparse
import json
import subprocess
import sys
import time
from pathlib import Path

AQUI = Path(__file__).resolve().parent


def salud(carpeta, duracion):
    diag = carpeta / "diagnostico.json"
    if not diag.exists():
        return "sin diagnóstico (caminata sin datos)"
    d = json.loads(diag.read_text())
    if d["duracion_s"] < 0.9 * duracion:
        return f"caminata cortada a los {d['duracion_s']:.0f} s"
    for n in ("femur1", "femur2", "femur3", "femur4"):
        a = d["articulaciones"].get(n, {})
        if a.get("caido") or a.get("r_medio", 0) < 0.9:
            return f"{n} no sigue la orden (r={a.get('r_medio')}): posible bus I2C bloqueado"
    return None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--sesion", required=True)
    ap.add_argument("--repeticiones", type=int, default=3)
    ap.add_argument("--duracion-s", type=float, default=180)
    ap.add_argument("--pausa-s", type=float, default=30)
    ap.add_argument("--condicion", action="append", required=True,
                    help="nombre:marcha:política (política vacía = base)")
    a = ap.parse_args()
    condiciones = [c.split(":", 2) for c in a.condicion]
    for ronda in range(a.repeticiones):
        orden = condiciones[ronda % len(condiciones):] + condiciones[:ronda % len(condiciones)]
        for nombre, marcha, politica in orden:
            carpeta = f"rep_{a.sesion}_{nombre}_r{ronda + 1}"
            if (AQUI / "grabaciones" / carpeta).exists():
                print("ya existe, se salta:", carpeta, flush=True)
                continue
            args = ["--duracion-s", str(a.duracion_s), "--dt", "0.03", "--tibia", "10", "--marcha", marcha]
            if marcha == "paso":
                args += ["--ciclo-paso", "2.0"]
            if politica:
                args += ["--politica", politica]
            print(time.strftime("%H:%M:%S"), "ronda", ronda + 1, carpeta, flush=True)
            r = subprocess.run([sys.executable, str(AQUI / "grabar_caminata.py"), "--nombre", carpeta, "--", *args],
                               capture_output=True, text=True)
            for l in r.stdout.splitlines():
                if any(k in l for k in ("AVISO", "estimados", "Grabación")):
                    print("  ", l, flush=True)
            if r.returncode != 0:
                print("  ERROR:", r.stderr.strip().splitlines()[-3:], flush=True)
                return 1
            subprocess.run([sys.executable, "-I", str(AQUI / "diagnostico_caminata.py"), str(AQUI / "grabaciones" / carpeta)],
                           capture_output=True)
            # 20-oct: comprobación de salud. Una caminata corta o con fémures que no siguen la orden
            # indica fallo del bus I2C o de la alimentación: se detiene el protocolo.
            problema = salud(AQUI / "grabaciones" / carpeta, a.duracion_s)
            if problema:
                print("  DETENIDO:", problema, flush=True)
                (AQUI / "grabaciones" / carpeta / "invalida.txt").write_text(problema + "\n")
                (AQUI / "grabaciones" / carpeta).rename(AQUI / "grabaciones" / f"{carpeta}_fallo")
                return 2
            time.sleep(a.pausa_s)
    subprocess.run([sys.executable, "-I", str(AQUI / "catalogo_caminatas.py")])
    return 0


if __name__ == "__main__":
    sys.exit(main())
