#!/usr/bin/env python3
"""Evalúa todas las copias intermedias de un entrenamiento en caminatas largas y elige la mejor.

Cada copia (intermedias/policy_*_steps.zip y policy.zip final) se evalúa en el robot
simulado (actuador v5, tibia 1 con PWM) con episodios de --ciclos ciclos (60 ≈ 3 min) y
--semillas semillas. Puntuación: se descartan las que avanzan menos que la base o se
desvían más de --deriva-max; entre las demás gana la de menor
desvío/0,1 m + roll RMS + pitch RMS (grados) − avance/avance_base.
Escribe seleccion_<marcha>.csv y copia la ganadora con su metadata a ppo_v10_robot/.

Uso: seleccionar_copias.py --marcha paso --carpeta ppo_v10_paso [--ciclos 60 --semillas 2 --procesos 11]
"""
import argparse
import csv
import json
import os
import shutil
import sys
from multiprocessing import Pool
from pathlib import Path

os.environ.setdefault("OMP_NUM_THREADS", "1")
import numpy as np  # noqa: E402

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))


def evaluar(trabajo):
    import torch
    torch.set_num_threads(1)
    from stable_baselines3 import PPO
    import entrenar_ppo_real as E
    from evaluar_v4_v6 import episodio
    ruta, marcha, ciclos, semillas = trabajo
    E.MARCHA, E.PASO_CICLO_S = marcha, 2.0
    E.FEMUR_AMP_DEG, E.TIBIA_AMP_DEG, E.FASE_MOV_S = 15.0, 10.0, 0.5
    E.NovaRealEnv.pesos = dict(avance=10.0, actitud=30.0, lateral=20.0, giro=10.0)
    E.SENSADAS, E.SIN_RESIDUAL = E.SENSADAS_COMPLETO, E.SIN_RESIDUAL_COMPLETO
    actuador = json.loads((HERE / "actuadores_reales_v5.json").read_text())
    modelo = PPO.load(ruta, device="cpu") if ruta != "base" else None
    res = [episodio(E.NovaRealEnv(actuador, seed=s, control_dt=0.03, episode_cycles=ciclos), modelo, s)
           for s in range(901, 901 + semillas)]
    return ruta, {k: float(np.mean([r[k] for r in res])) for k in res[0] if k != "caida"} | \
        {"caidas": sum(r["caida"] for r in res)}


def pasos(ruta):
    p = Path(ruta)
    if p.name == "policy.zip":
        return json.loads((p.parent / "metadata.json").read_text())["timesteps"]
    return int(p.stem.split("_")[1])


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--marcha", choices=("gateo", "paso"), required=True)
    ap.add_argument("--carpeta", type=Path, required=True)
    ap.add_argument("--ciclos", type=int, default=60)
    ap.add_argument("--semillas", type=int, default=2)
    ap.add_argument("--procesos", type=int, default=11)
    ap.add_argument("--deriva-max", type=float, default=0.5)
    a = ap.parse_args()
    rutas = sorted(str(p) for p in a.carpeta.glob("semilla_*/intermedias/policy_*_steps.zip"))
    rutas += sorted(str(p) for p in a.carpeta.glob("semilla_*/policy.zip"))
    trabajos = [("base", a.marcha, a.ciclos, a.semillas)] + [(r, a.marcha, a.ciclos, a.semillas) for r in rutas]
    with Pool(a.procesos) as pool:
        resultados = dict(pool.imap_unordered(evaluar, trabajos))
    base = resultados.pop("base")
    filas = []
    for ruta, m in resultados.items():
        valida = m["avance_m"] > base["avance_m"] and m["deriva_m"] <= a.deriva_max and m["caidas"] == 0
        punt = m["deriva_m"] / 0.1 + m["roll_rms_deg"] + m["pitch_rms_deg"] - m["avance_m"] / base["avance_m"]
        filas.append(dict(copia=ruta, semilla=Path(ruta).parts[-3] if "intermedias" in ruta else Path(ruta).parts[-2],
                          pasos=pasos(ruta), valida=valida, puntuacion=round(punt, 3), **{k: round(v, 4) for k, v in m.items()}))
    filas.sort(key=lambda f: (not f["valida"], f["puntuacion"]))
    with (HERE / f"seleccion_{a.marcha}.csv").open("w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(filas[0])); w.writeheader(); w.writerows(filas)
    print(f"base: avance {base['avance_m']:.3f} m, deriva {base['deriva_m']:.3f} m, roll {base['roll_rms_deg']:.2f}°, "
          f"pitch {base['pitch_rms_deg']:.2f}°")
    for f in filas[:8]:
        print(f"{'OK ' if f['valida'] else '-- '}{f['semilla']:10s} {f['pasos']:>8d} pasos  avance {f['avance_m']:.3f}  "
              f"deriva {f['deriva_m']:.3f}  roll {f['roll_rms_deg']:.2f}  pitch {f['pitch_rms_deg']:.2f}  "
              f"incl.máx {f['inclinacion_max_deg']:.2f}  punt {f['puntuacion']:.2f}")
    mejor = filas[0]
    if mejor["valida"]:
        destino = HERE / "ppo_v10_robot" / f"{a.marcha}_{mejor['semilla']}_{mejor['pasos'] // 1000}k"
        destino.mkdir(parents=True, exist_ok=True)
        shutil.copy(mejor["copia"], destino / "policy.zip")
        md = json.loads((HERE / "ppo_v6/semilla_11/metadata.json").read_text())
        md.pop("actuador", None)
        md.update(seed=mejor["semilla"], timesteps=mejor["pasos"], origen=mejor["copia"],
                  evaluacion_3min={k: mejor[k] for k in ("avance_m", "deriva_m", "roll_rms_deg", "pitch_rms_deg",
                                                          "inclinacion_max_deg")},
                  marcha=dict(tipo=a.marcha, femur_deg=15.0, tibia_deg=10.0, fase_s=0.5, ciclo_paso_s=2.0))
        (destino / "metadata.json").write_text(json.dumps(md, indent=2, ensure_ascii=False))
        print("Elegida:", destino)


if __name__ == "__main__":
    main()
