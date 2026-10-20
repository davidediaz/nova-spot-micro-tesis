#!/usr/bin/env python3
"""Ventana del simulador MuJoCo con una marcha en tiempo real (en bucle).

Usa el mismo entorno que el entrenamiento (NovaRealEnv: actuador real, retardo, límite de
3°/línea) y la misma marcha que se envía al robot. Con --politica añade la corrección PPO.
Cerrar la ventana para terminar.

Uso: ver_marcha_sim.py --marcha trote [--politica ppo_trote/semilla_11/policy.zip] [--suspendido]
  --suspendido: fija el cuerpo en el aire, como el robot real colgado de la barra.
"""
import argparse
import json
import sys
import time
from pathlib import Path

import mujoco
import mujoco.viewer
import numpy as np

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import entrenar_ppo_real as E  # noqa: E402


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--marcha", choices=("gateo", "paso", "trote"), default="trote")
    ap.add_argument("--politica", type=Path)
    ap.add_argument("--suspendido", action="store_true")
    ap.add_argument("--ciclos", type=int, default=30)
    a = ap.parse_args()
    E.MARCHA = a.marcha
    E.PASO_CICLO_S, E.TROTE_CICLO_S = 2.0, 1.0
    E.FEMUR_AMP_DEG, E.TIBIA_AMP_DEG = (12.0, 12.0) if a.marcha == "trote" else (15.0, 10.0)
    E.SENSADAS, E.SIN_RESIDUAL = E.SENSADAS_COMPLETO, E.SIN_RESIDUAL_COMPLETO
    E.NovaRealEnv.pesos = dict(avance=10.0, actitud=30.0, lateral=20.0, giro=10.0)
    actuador = json.loads((HERE / "actuadores_reales_v5.json").read_text())
    modelo = None
    if a.politica:
        from stable_baselines3 import PPO
        modelo = PPO.load(a.politica, device="cpu")
    env = E.NovaRealEnv(actuador, seed=901, control_dt=0.03, episode_cycles=a.ciclos)
    obs, _ = env.reset(seed=901)
    if a.suspendido:
        env.model.body_gravcomp[:] = 1.0          # sin gravedad efectiva: patas al aire
        env.data.qpos[2] += 0.15
    with mujoco.viewer.launch_passive(env.model, env.data) as visor:
        visor.cam.distance, visor.cam.elevation, visor.cam.azimuth = 0.9, -15, 90
        while visor.is_running():
            t0 = time.time()
            act = np.zeros(12) if modelo is None else modelo.predict(obs, deterministic=True)[0]
            obs, r, term, trunc, info = env.step(act)
            visor.cam.lookat[:] = env.data.xpos[env.base_body]
            visor.sync()
            if term or trunc:
                obs, _ = env.reset(seed=901)
            espera = env.control_dt - (time.time() - t0)
            if espera > 0:
                time.sleep(espera)


if __name__ == "__main__":
    main()
