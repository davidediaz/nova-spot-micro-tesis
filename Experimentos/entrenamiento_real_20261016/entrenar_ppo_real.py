#!/usr/bin/env python3
"""PPO residual en MuJoCo ajustado al robot real del 16 de octubre de 2026.

Diferencias respecto a Experimentos/entrenar_ppo_mujoco.py (que no se modifica):
- Marcha nominal = la caminata `b` que funciona en el robot (firmware
  movimiento_suspendido_11_servos): gateo FL -> RR -> FR -> RL, fémures +/-15°,
  tibias 14° de elevación en la oscilación, 0,5 s de movimiento + 0,15 s de
  pausa por fase. Coxas fijas en su punto de equilibrio.
- Actuador identificado con los sensores del MUX (actuadores_reales.json):
  retardo y ganancia por articulación; tibia 1 (FR) sin PWM (sin fuerza).
- Observación limitada a lo que el Uno puede medir: ángulos de fémur 2, fémur 4
  y tibia 2 (con ruido de 1°), fase de la marcha y residual previo.
- El residual solo actúa sobre fémures y tibias con servo útil; coxas y tibia 1
  quedan con residual cero. La recompensa usa el estado del cuerpo simulado.
Solo simulación: no abre el puerto serie ni mueve el robot.
"""

from __future__ import annotations

import argparse
import csv
import json
import sys
from collections import deque
from pathlib import Path

import mujoco
import numpy as np
from gymnasium import spaces
from stable_baselines3 import PPO

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
sys.path.insert(0, str(ROOT / "Experimentos"))
from entrenar_ppo_mujoco import (  # noqa: E402
    JOINTS, STAND, MetricsCallback, NovaMujocoResidualEnv, _quat_roll_pitch,
)

MODEL = ROOT / "src/nova_sm3_description/mujoco/nova_sm3.xml"
LEG_JOINT_BASE = {"FL": 0, "FR": 3, "RL": 6, "RR": 9}
ORDEN_PATAS = ("FL", "RR", "FR", "RL")
FEMUR_AMP_DEG = 15.0
TIBIA_AMP_DEG = 14.0
FASE_MOV_S, FASE_PAUSA_S = 0.5, 0.15
SENSADAS = ("front_left_femur_joint", "rear_left_femur_joint", "front_left_tibia_joint")
SIN_RESIDUAL = {"front_left_coxa_joint", "front_right_coxa_joint", "rear_left_coxa_joint",
                "rear_right_coxa_joint", "front_right_tibia_joint"}


def marcha_b(control_dt):
    """Muestras articulares (rad) de la caminata `b`, una por paso de control."""
    a = np.deg2rad(FEMUR_AMP_DEG)
    pasos_mov = round(FASE_MOV_S / control_dt)
    pasos_pausa = round(FASE_PAUSA_S / control_dt)
    offset = {pata: -a + k * (2 * a / 3) for k, pata in enumerate(ORDEN_PATAS)}
    muestras = []
    for vuela in ORDEN_PATAS:
        inicio = dict(offset)
        for s in range(1, pasos_mov + pasos_pausa + 1):
            t = min(1.0, s / pasos_mov)
            q = np.tile(STAND, 4).astype(float)
            for pata in ORDEN_PATAS:
                if pata == vuela:
                    o = inicio[pata] + 2 * a * t
                    lift = np.deg2rad(TIBIA_AMP_DEG) * np.sin(np.pi * t)
                else:
                    o, lift = inicio[pata] - (2 * a / 3) * t, 0.0
                offset[pata] = o
                b = LEG_JOINT_BASE[pata]
                q[b + 1] = STAND[1] - o        # fémur adelante = q menor
                q[b + 2] = STAND[2] - lift     # tibia flexiona al levantar
            muestras.append(q)
    return np.asarray(muestras)


class NovaRealEnv(NovaMujocoResidualEnv):
    def __init__(self, actuador, seed=11, episode_cycles=6, domain_randomization=True,
                 sensor_noise_deg=1.0, control_dt=0.02):
        super().__init__(MODEL, gait="crawl", episode_cycles=episode_cycles,
                         control_dt=control_dt, seed=seed,
                         domain_randomization=domain_randomization)
        self.nominal = marcha_b(self.control_dt)
        self.samples = len(self.nominal)
        self.steps_per_sample = 1
        self.cycle_steps = self.samples
        self.max_steps = self.ramp_steps + self.episode_cycles * self.cycle_steps
        self.sensor_noise = np.deg2rad(sensor_noise_deg)
        self.retardo_pasos = max(0, round(actuador["retardo_s"] / self.control_dt))
        g = actuador["ganancia"]
        self.ganancia = np.full(12, g)
        for nombre, datos in actuador["articulaciones"].items():
            # Se usa la ganancia medida también cuando la correlación es baja
            # pero el sensor es bueno (tibia 4 casi no se mueve en la caminata).
            if datos["fiable"] or nombre == "rear_left_tibia_joint":
                self.ganancia[JOINTS.index(nombre)] = datos["ganancia"]
        self.mascara = np.array([0.0 if j in SIN_RESIDUAL else 1.0 for j in JOINTS])
        self.zona_muerta = np.deg2rad(float(actuador.get("zona_muerta_grados", 0.0)))
        self.idx_sensadas = [JOINTS.index(j) for j in SENSADAS]
        # Tibia 1 (FR) sin PWM: actuador sin rigidez, solo amortiguamiento.
        act = mujoco.mj_name2id(self.model, mujoco.mjtObj.mjOBJ_ACTUATOR, "front_right_tibia_act")
        self.model.actuator_gainprm[act, 0] = 0.0
        self.model.actuator_biasprm[act, 1] = 0.0
        obs_dim = len(SENSADAS) + 2 + 12
        self.observation_space = spaces.Box(-np.inf, np.inf, (obs_dim,), np.float32)
        self.cola = deque()

    def _observation(self):
        q = self.data.qpos[self.qpos_ids][self.idx_sensadas]
        q = q + self.rng.normal(0.0, self.sensor_noise, size=q.shape)
        fase = (max(0, self.step_count - self.ramp_steps) % self.cycle_steps) / self.cycle_steps
        return np.asarray(np.r_[q - np.asarray(STAND * 4)[self.idx_sensadas],
                                np.sin(2 * np.pi * fase), np.cos(2 * np.pi * fase),
                                self.previous_residual / 0.08], dtype=np.float32)

    def _cuerpo(self):
        roll, pitch = _quat_roll_pitch(self.data.xquat[self.base_body])
        return roll, pitch, float(self.data.xpos[self.base_body, 2])

    def _reward(self, residual, before_x):
        roll, pitch, h = self._cuerpo()
        dx = float(self.data.xpos[self.base_body, 0] - before_x)
        q_err = (self.data.qpos[self.qpos_ids] - self.current_nominal) * self.mascara
        w = getattr(self, "pesos", {})
        rec = (1.0 + w.get("avance", 18.0) * dx - w.get("actitud", 8.0) * (roll ** 2 + pitch ** 2)
               - 25.0 * (h - 0.235) ** 2 - 0.25 * q_err @ q_err - 0.04 * residual @ residual)
        if w.get("lateral") or w.get("giro"):
            from entrenar_ppo_mujoco import _quat_yaw
            lat = float(self.data.xpos[self.base_body, 1] - self.initial_y)
            yaw = float(np.arctan2(np.sin(_quat_yaw(self.data.xquat[self.base_body]) - self.initial_yaw),
                                   np.cos(_quat_yaw(self.data.xquat[self.base_body]) - self.initial_yaw)))
            rec -= w.get("lateral", 0.0) * lat ** 2 + w.get("giro", 0.0) * yaw ** 2
        return float(rec)

    def reset(self, *, seed=None, options=None):
        obs, info = super().reset(seed=seed, options=options)
        self.cola = deque([self.data.ctrl.copy()] * self.retardo_pasos)
        self.ultimo_efectivo = None
        return self._observation(), info

    def step(self, action):
        action = np.asarray(action, dtype=float) * self.mascara
        target = np.clip(action, -1.0, 1.0) * 0.08
        delta = np.clip(target - self.previous_residual, -0.02, 0.02)
        residual = (self.previous_residual + delta) * self.mascara
        self.previous_residual = residual
        ramp = self.step_count < self.ramp_steps
        if ramp:
            f = (self.step_count + 1) / self.ramp_steps
            nominal = self.initial_ctrl + f * (self.nominal[0] - self.initial_ctrl)
        else:
            nominal = self.nominal[(self.step_count - self.ramp_steps) % self.cycle_steps]
        self.current_nominal = nominal
        orden = nominal + residual
        stand = np.tile(STAND, 4)
        efectivo = stand + self.ganancia * (orden - stand)
        if self.zona_muerta > 0:
            # Zona muerta del servo: no se mueve si el cambio pedido es menor.
            previo = getattr(self, "ultimo_efectivo", None)
            if previo is not None:
                efectivo = np.where(np.abs(efectivo - previo) < self.zona_muerta, previo, efectivo)
            self.ultimo_efectivo = efectivo.copy()
        self.cola.append(efectivo)
        aplicado = self.cola.popleft() if len(self.cola) > self.retardo_pasos else efectivo
        before_x = float(self.data.xpos[self.base_body, 0])
        self.data.ctrl[:] = np.clip(aplicado, self.model.actuator_ctrlrange[:, 0],
                                    self.model.actuator_ctrlrange[:, 1])
        for _ in range(self.sim_substeps):
            mujoco.mj_step(self.model, self.data)
        reward = self._reward(residual, before_x)
        self.step_count += 1
        roll, pitch, h = self._cuerpo()
        obs = self._observation()
        terminated = bool(not np.isfinite(obs).all() or h < 0.12 or h > 0.40
                          or abs(roll) > 0.60 or abs(pitch) > 0.60)
        truncated = self.step_count >= self.max_steps
        return obs, reward, terminated, truncated, {
            "roll": roll, "pitch": pitch, "height": h,
            "x": float(self.data.xpos[self.base_body, 0]),
            "y": float(self.data.xpos[self.base_body, 1]),
            "residual_norm": float(np.linalg.norm(residual)), "ramp_active": ramp}


def evaluar(model, actuador, semillas, deterministic=True, control_dt=0.02):
    filas = []
    for cond in ("nominal", "ppo"):
        for s in semillas:
            env = NovaRealEnv(actuador, seed=s, control_dt=control_dt)
            obs, _ = env.reset(seed=s)
            x0, y0, ret, maxinc, caida = None, None, 0.0, 0.0, False
            while True:
                act = np.zeros(12) if cond == "nominal" else model.predict(obs, deterministic=deterministic)[0]
                obs, r, term, trunc, info = env.step(act)
                if x0 is None and not info["ramp_active"]:
                    x0, y0 = info["x"], info["y"]
                ret += r
                maxinc = max(maxinc, abs(info["roll"]), abs(info["pitch"]))
                if term:
                    caida = True
                if term or trunc:
                    break
            filas.append(dict(condicion=cond, semilla_eval=s, retorno=round(ret, 2),
                              avance_m=round(info["x"] - (x0 or 0), 4),
                              deriva_lateral_m=round(abs(info["y"] - (y0 or 0)), 4),
                              inclinacion_max_rad=round(maxinc, 4), caida=caida))
    return filas


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--seed", type=int, default=11)
    p.add_argument("--timesteps", type=int, default=150_000)
    p.add_argument("--eval-seeds", type=int, nargs="+", default=[801, 802, 803, 804, 805])
    p.add_argument("--output", type=Path, default=HERE / "ppo")
    p.add_argument("--actuador", type=Path, default=HERE / "actuadores_reales.json")
    p.add_argument("--dt", type=float, default=0.02, help="periodo de control (s)")
    p.add_argument("--femur", type=float, default=15.0)
    p.add_argument("--tibia", type=float, default=14.0)
    p.add_argument("--fase", type=float, default=0.5)
    p.add_argument("--w-avance", type=float, default=18.0)
    p.add_argument("--w-actitud", type=float, default=8.0)
    p.add_argument("--w-lateral", type=float, default=0.0)
    p.add_argument("--w-giro", type=float, default=0.0)
    a = p.parse_args()
    actuador = json.loads(a.actuador.read_text())
    global FEMUR_AMP_DEG, TIBIA_AMP_DEG, FASE_MOV_S
    FEMUR_AMP_DEG, TIBIA_AMP_DEG, FASE_MOV_S = a.femur, a.tibia, a.fase
    NovaRealEnv.pesos = dict(avance=a.w_avance, actitud=a.w_actitud, lateral=a.w_lateral, giro=a.w_giro)
    out = a.output / f"semilla_{a.seed}"
    out.mkdir(parents=True, exist_ok=True)
    env = NovaRealEnv(actuador, seed=a.seed, control_dt=a.dt)
    model = PPO("MlpPolicy", env, seed=a.seed, verbose=0, n_steps=1024, batch_size=256)
    model.learn(total_timesteps=a.timesteps, callback=MetricsCallback(out / "training_trace.csv"))
    model.save(out / "policy.zip")
    filas = evaluar(model, actuador, a.eval_seeds, control_dt=a.dt)
    with (out / "evaluacion.csv").open("w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(filas[0]))
        w.writeheader(); w.writerows(filas)
    (out / "metadata.json").write_text(json.dumps(dict(
        seed=a.seed, timesteps=int(model.num_timesteps), eval_seeds=a.eval_seeds, control_dt=a.dt,
        marcha=dict(femur_deg=a.femur, tibia_deg=a.tibia, fase_s=a.fase), pesos=NovaRealEnv.pesos,
        actuador=actuador, hardware_transfer=False,
        observacion=list(SENSADAS) + ["sin_fase", "cos_fase", "residual_previo x12"],
        nota="Simulación ajustada al robot real del 16-oct; no transferida al robot."),
        indent=2, ensure_ascii=False))
    for cond in ("nominal", "ppo"):
        sub = [f for f in filas if f["condicion"] == cond]
        print(cond, {k: round(float(np.mean([f[k] for f in sub])), 4)
                     for k in ("retorno", "avance_m", "deriva_lateral_m", "inclinacion_max_rad")},
              "caidas", sum(f["caida"] for f in sub))


if __name__ == "__main__":
    main()
