#!/usr/bin/env python3
"""Genera los resultados numéricos reproducibles usados en el modelo LaTeX."""

import json
import sys
from pathlib import Path

import numpy as np
from scipy.linalg import expm, solve_discrete_are

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'src' / 'nova_gait_controller'))

from nova_gait_controller.kinematics import (  # noqa: E402
    cartesian_crawl, forward_leg, inverse_leg,
)
from nova_gait_controller.mathematical_model import (  # noqa: E402
    DEFAULT_PARAMETERS, actuator_current, actuator_torque_limit,
    coriolis_torque, foot_force_to_joint_torque, gravity_torque,
    leg_jacobian, leg_mass_matrix, passive_joint_torque, robot_center_of_mass,
    static_stability_margin,
)


def rounded(value, digits=9):
    if isinstance(value, np.ndarray):
        return [rounded(item, digits) for item in value.tolist()]
    if isinstance(value, (list, tuple)):
        return [rounded(item, digits) for item in value]
    if np.iscomplexobj(value):
        return {'real': round(float(np.real(value)), digits),
                'imag': round(float(np.imag(value)), digits)}
    return round(float(value), digits)


q = np.array((0.10, 0.42, -0.84))
qd = np.array((0.10, -0.05, 0.08))
qdd = np.array((0.20, 0.10, -0.15))
force = np.array((1.0, 0.5, 5.0))
side = 1

foot = np.asarray(forward_leg(*q, side))
q_recovered = np.asarray(inverse_leg(*foot, side))
jacobian = np.asarray(leg_jacobian(*q, side))
singular_values = np.linalg.svd(jacobian, compute_uv=False)
joint_force_torque = np.asarray(foot_force_to_joint_torque(q, force, side))

mass = leg_mass_matrix(q, side)
inertial = mass @ qdd
coriolis = np.asarray(coriolis_torque(q, qd, side))
gravity = np.asarray(gravity_torque(q, side))
passive = np.asarray(passive_joint_torque(qd))
total = inertial + coriolis + gravity + passive - joint_force_torque

all_q = {leg: tuple(q) for leg in ('fl', 'fr', 'rl', 'rr')}
com = np.asarray(robot_center_of_mass(all_q))
contacts = []
for leg in ('fl', 'fr', 'rl', 'rr'):
    leg_side = 1 if leg[1] == 'l' else -1
    x_hip = DEFAULT_PARAMETERS.hip_spacing_x / 2 if leg[0] == 'f' else -DEFAULT_PARAMETERS.hip_spacing_x / 2
    y_hip = DEFAULT_PARAMETERS.hip_spacing_y / 2 if leg[1] == 'l' else -DEFAULT_PARAMETERS.hip_spacing_y / 2
    local = forward_leg(*q, leg_side)
    contacts.append((x_hip + local[0], y_hip + local[1]))
margin = static_stability_margin(com[:2], contacts)

poses = cartesian_crawl(tuple(q), samples=24, step_length=0.018, step_height=0.014)
fl_z = [forward_leg(*pose[:3], side=1)[2] for pose in poses]

# Modelo local del eje de fémur con compensación nominal de gravedad.
eps = 1e-6
q_plus, q_minus = q.copy(), q.copy()
q_plus[1] += eps
q_minus[1] -= eps
gravity_stiffness = (
    gravity_torque(q_plus, side)[1] - gravity_torque(q_minus, side)[1]
) / (2 * eps)
inertia = mass[1, 1]
damping = DEFAULT_PARAMETERS.joint_damping
A = np.array(((0.0, 1.0), (-gravity_stiffness / inertia, -damping / inertia)))
B = np.array(((0.0,), (1.0 / inertia,)))
Ts = 0.02
block = np.block([[A, B], [np.zeros((1, 3))]])
disc = expm(block * Ts)
Ad, Bd = disc[:2, :2], disc[:2, 2:]
controllability = np.column_stack((Bd, Ad @ Bd))
Q = np.diag((400.0, 4.0))
R = np.array(((0.5,),))
P = solve_discrete_are(Ad, Bd, Q, R)
K = np.linalg.solve(R + Bd.T @ P @ Bd, Bd.T @ P @ Ad)
closed = Ad - Bd @ K

x = np.array((np.deg2rad(10.0), 0.0))
history = []
for index in range(250):
    u = float(-(K @ x)[0])
    history.append((index * Ts, *x, u))
    x = Ad @ x + Bd[:, 0] * u
settling = next((t for t, angle, speed, _ in history
                 if abs(angle) <= np.deg2rad(0.2)
                 and all(abs(row[1]) <= np.deg2rad(0.2) for row in history[int(t/Ts):])), None)

output = {
    'cinematica': {
        'q_rad': rounded(q), 'pie_m': rounded(foot),
        'q_recuperada_rad': rounded(q_recovered),
        'error_maximo_rad': rounded(np.max(np.abs(q_recovered - q)), 12),
        'jacobiano_m_rad': rounded(jacobian),
        'valores_singulares': rounded(singular_values),
        'condicion': rounded(singular_values[0] / singular_values[-1], 6),
        'tau_por_fuerza_Nm': rounded(joint_force_torque),
    },
    'dinamica': {
        'M_kg_m2': rounded(mass), 'autovalores_M': rounded(np.linalg.eigvalsh(mass)),
        'inercial_Nm': rounded(inertial), 'coriolis_Nm': rounded(coriolis),
        'gravedad_Nm': rounded(gravity), 'pasiva_Nm': rounded(passive),
        'contacto_JT_f_Nm': rounded(joint_force_torque), 'tau_total_Nm': rounded(total),
        'limite_tau_6V_Nm': rounded([actuator_torque_limit(v) for v in qd]),
        'corriente_estimada_A': rounded([actuator_current(t) for t in total]),
    },
    'estabilidad': {
        'com_m': rounded(com), 'contactos_xy_m': rounded(contacts),
        'margen_m': rounded(margin),
    },
    'marcha': {
        'ciclo_s': 4.32, 'frecuencia_referencia_Hz': rounded(1 / 0.18, 6),
        'elevacion_fl_discreta_m': rounded(max(fl_z) - min(fl_z)),
        'muestras_elevadas_fl': sum(z > min(fl_z) + 1e-9 for z in fl_z),
    },
    'control_discreto_femur': {
        'inercia': rounded(inertia), 'amortiguamiento': rounded(damping),
        'rigidez_gravitacional': rounded(gravity_stiffness),
        'A': rounded(A), 'B': rounded(B), 'Ts_s': Ts,
        'Ad': rounded(Ad), 'Bd': rounded(Bd),
        'rango_controlabilidad': int(np.linalg.matrix_rank(controllability)),
        'K_lqr': rounded(K), 'polos_abiertos': rounded(np.linalg.eigvals(Ad)),
        'polos_cerrados': rounded(np.linalg.eigvals(closed)),
        'angulo_inicial_deg': 10.0,
        'par_maximo_Nm': rounded(max(abs(row[3]) for row in history), 6),
        'establecimiento_0_2deg_s': rounded(settling, 3),
    },
}

print(json.dumps(output, indent=2, ensure_ascii=False))
