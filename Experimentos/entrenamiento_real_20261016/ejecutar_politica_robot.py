#!/usr/bin/env python3
"""Ejecuta la caminata `b` en el robot real desde el PC, opcionalmente con la
corrección PPO entrenada en entrenar_ppo_real.py.

Requiere el firmware movimiento_suspendido_11_servos con el modo `@`. Cada 20 ms
el PC envía los 12 ángulos de servo; el Uno aplica límites (fémur ±20°,
tibia ±18°, 3° por línea), mantiene las coxas en equilibrio, deja la tibia 1
sin PWM y responde con C5, C6, C9 (F2, F4, T2) y C1, C3, C2 (coxas).
Abrir el puerto reinicia el Uno, que arranca con todo en OFF.

Uso:  python ejecutar_politica_robot.py --ciclos 6 [--politica ppo/semilla_11/policy.zip]
"""
from __future__ import annotations

import argparse
import csv
import os
import sys
import termios
import time
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import entrenar_ppo_real as E  # noqa: E402
from entrenar_ppo_real import STAND, marcha_b, JOINTS  # noqa: E402

# Índices del firmware: 0-3 coxas (patas 1..4), 4-7 fémures, 8-11 tibias.
# Patas: 1=FR, 2=FL, 3=RR, 4=RL. Base y signos de la caminata `b` del firmware.
BASE = [159, 45, 54, 74, 110, 100, 100, 100, 100, 80, 100, 70]  # 19-oct: equilibrio nuevo de coxas
SIGNO_FEMUR = {1: -1, 2: 1, 3: -1, 4: 1}
SIGNO_TIBIA = {1: -1, 2: -1, 3: -1, 4: -1}
PATA = {1: "front_right", 2: "front_left", 3: "rear_right", 4: "rear_left"}
CUENTAS_POR_GRADO = 2.45
DT = 0.02  # se reemplaza por control_dt del metadata.json de la política


def a_grados_servo(q):
    """Ángulos del modelo (rad, orden JOINTS) -> 12 grados de servo del firmware."""
    out = list(BASE)
    for pata in (1, 2, 3, 4):
        jf = JOINTS.index(f"{PATA[pata]}_femur_joint")
        jt = JOINTS.index(f"{PATA[pata]}_tibia_joint")
        o = -(q[jf] - STAND[1])          # fémur adelante (rad)
        lift = -(q[jt] - STAND[2])       # elevación de tibia (rad)
        out[3 + pata] = round(BASE[3 + pata] + SIGNO_FEMUR[pata] * np.rad2deg(o))
        out[7 + pata] = round(BASE[7 + pata] + SIGNO_TIBIA[pata] * np.rad2deg(lift))
    return out


def abrir(puerto):
    fd = os.open(puerto, os.O_RDWR | os.O_NOCTTY)
    a = termios.tcgetattr(fd)
    a[4] = a[5] = termios.B115200
    a[0] = a[1] = a[3] = 0
    a[2] |= termios.CLOCAL | termios.CREAD
    a[6][termios.VMIN] = 0
    a[6][termios.VTIME] = 1
    termios.tcsetattr(fd, termios.TCSANOW, a)
    return fd


class Lector:
    def __init__(self, fd):
        self.fd, self.buf = fd, b""

    def linea(self, timeout=1.0):
        fin = time.time() + timeout
        while time.time() < fin:
            if b"\n" in self.buf:
                l, self.buf = self.buf.split(b"\n", 1)
                return l.decode(errors="replace").strip()
            self.buf += os.read(self.fd, 256)
        return None


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--puerto", default="/dev/ttyACM0")
    p.add_argument("--ciclos", type=int, default=6)
    p.add_argument("--politica", type=Path)
    p.add_argument("--salida", type=Path)
    p.add_argument("--dt", type=float)
    p.add_argument("--femur", type=float)
    p.add_argument("--tibia", type=float)
    p.add_argument("--fase", type=float)
    a = p.parse_args()
    global DT
    modelo = None
    if a.politica:
        from stable_baselines3 import PPO
        modelo = PPO.load(a.politica, device="cpu")
        meta = a.politica.with_name("metadata.json")
        if meta.exists():
            import json
            md = json.loads(meta.read_text())
            DT = float(md.get("control_dt", DT))
            m = md.get("marcha", {})
            E.FEMUR_AMP_DEG = m.get("femur_deg", E.FEMUR_AMP_DEG)
            E.TIBIA_AMP_DEG = m.get("tibia_deg", E.TIBIA_AMP_DEG)
            E.FASE_MOV_S = m.get("fase_s", E.FASE_MOV_S)
    if a.dt:
        DT = a.dt
    if a.femur: E.FEMUR_AMP_DEG = a.femur
    if a.tibia: E.TIBIA_AMP_DEG = a.tibia
    if a.fase: E.FASE_MOV_S = a.fase
    print(f"Periodo de control: {DT*1000:.0f} ms | marcha fémur {E.FEMUR_AMP_DEG}° tibia {E.TIBIA_AMP_DEG}° fase {E.FASE_MOV_S} s")
    nominal = marcha_b(DT)
    stand = np.tile(STAND, 4).astype(float)
    sin_residual = {"front_left_coxa_joint", "front_right_coxa_joint", "rear_left_coxa_joint",
                    "rear_right_coxa_joint", "front_right_tibia_joint"}
    mascara = np.array([0.0 if j in sin_residual else 1.0 for j in JOINTS])
    sensadas = ("front_left_femur_joint", "rear_left_femur_joint", "front_left_tibia_joint")
    idx_s = [JOINTS.index(j) for j in sensadas]

    fd = abrir(a.puerto)
    lec = Lector(fd)
    time.sleep(2.0)                      # reinicio del Uno al abrir el puerto
    os.read(fd, 4096)
    os.write(fd, b"@")
    while True:
        l = lec.linea(timeout=8.0)
        if l is None:
            sys.exit("El Uno no respondió STREAM_LISTO")
        if l.startswith("STREAM_LISTO"):
            break
    # Referencias ADC en la postura base (servo en BASE).
    os.write(fd, ("S," + ",".join(map(str, BASE)) + "\n").encode())
    r = lec.linea().split(",")
    ref = {"C5": int(r[2]), "C6": int(r[3]), "C9": int(r[4]),
           # 19-oct: la tibia 2 se lee por su AS5600 (TCA 0x70/3), campo 10 de la respuesta.
           "ENC_T2": int(r[10]) if len(r) > 10 else -1}
    if ref["ENC_T2"] < 0:
        sys.exit("El encoder de la tibia 2 (0x70/3) no responde: revisar antes de usar la PPO.")

    salida = a.salida or HERE / f"robot_{'ppo' if modelo else 'nominal'}_{time.strftime('%Y%m%d_%H%M%S')}.csv"
    f = salida.open("w", newline="")
    w = csv.writer(f)
    w.writerow(["t", "paso", "fase", *[f"orden_{i}" for i in range(12)], *[f"nominal_{i}" for i in range(12)],
                "C5", "C6", "C9", "C1", "C3", "C2", "ENC_T2", *[f"residual_{j}" for j in JOINTS]])
    residual_prev = np.zeros(12)
    rampa = round(1.0 / DT)
    total = rampa + a.ciclos * len(nominal)
    obs_q = np.zeros(3)
    t0 = time.time()
    # 19-oct: hora real de inicio, para sincronizar con el video de las cámaras.
    salida.with_suffix('.inicio.txt').write_text(f"{t0:.6f}\n")
    try:
        for k in range(total):
            if k < rampa:
                q_nom = stand + (k + 1) / rampa * (nominal[0] - stand)
                fase = 0.0
            else:
                i = (k - rampa) % len(nominal)
                q_nom, fase = nominal[i], i / len(nominal)
            residual = np.zeros(12)
            if modelo is not None and k >= rampa:
                obs = np.r_[obs_q, np.sin(2 * np.pi * fase), np.cos(2 * np.pi * fase),
                            residual_prev / 0.08].astype(np.float32)
                accion = modelo.predict(obs, deterministic=True)[0] * mascara
                objetivo = np.clip(accion, -1, 1) * 0.08
                residual = (residual_prev + np.clip(objetivo - residual_prev, -0.02, 0.02)) * mascara
            residual_prev = residual
            grados = a_grados_servo(q_nom + residual)
            grados_nom = a_grados_servo(q_nom)
            os.write(fd, ("S," + ",".join(map(str, grados)) + "\n").encode())
            resp = lec.linea(timeout=0.3)
            if not resp or not resp.startswith("R,"):
                print("Respuesta perdida en el paso", k, resp)
                break
            campos = resp.split(",")
            v = [int(x) for x in campos[2:8]]  # C5,C6,C9,C1,C3,C2
            enc = int(campos[10]) if len(campos) > 10 else -1  # AS5600 tibia 2 (crudo 0-4095)
            v.append(enc)
            # ADC -> grados de servo (pendiente negativa) -> ángulo del modelo.
            # Escalas medidas en el barrido de rango del 16-oct (cuentas/grado).
            d5 = -(v[0] - ref["C5"]) / 2.52   # F2 (pata 2, signo +1)
            d6 = -(v[1] - ref["C6"]) / 2.51   # F4 (pata 4, signo +1)
            # T2: 20° de servo dan ≈ −13,2° de encoder (barrido del 19-oct) → −0,66 °enc/°servo.
            if enc >= 0:
                d_enc = ((enc - ref["ENC_T2"]) * 360.0 / 4096.0 + 180.0) % 360.0 - 180.0
                d9 = d_enc / -0.66
            else:
                d9 = 0.0                       # lectura perdida: se toma la base
            obs_q = np.deg2rad([-d5, -d6, d9])
            w.writerow([round(time.time() - t0, 3), k, round(fase, 4), *grados, *grados_nom, *v,
                        *np.round(residual, 4)])
            espera = t0 + (k + 1) * DT - time.time()
            if espera > 0:
                time.sleep(espera)
    finally:
        os.write(fd, b"X\n")
        time.sleep(0.2)
        f.close()
        os.close(fd)
    print("Registro:", salida, "| pasos:", k + 1, "| duración:", round(time.time() - t0, 1), "s")


if __name__ == "__main__":
    main()
