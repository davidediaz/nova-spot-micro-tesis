#!/usr/bin/env python3
"""Ejemplo numérico reproducible del modelo matemático Nova Spot Micro."""

import numpy as np

from nova_gait_controller.kinematics import forward_leg
from nova_gait_controller.mathematical_model import (
    MG996R, coriolis_torque, foot_force_to_joint_torque, foot_position_body,
    gravity_torque, inverse_dynamics, leg_jacobian, leg_mass_matrix,
    passive_joint_torque, robot_center_of_mass, static_stability_margin,
)


def vector(values):
    return np.asarray(values, dtype=float)


def show(name, values, precision=6):
    print(f'{name} = {np.array2string(np.asarray(values), precision=precision)}')


def main():
    q = vector((0.10, 0.42, -0.84))
    q_dot = vector((0.10, -0.05, 0.08))
    q_ddot = vector((0.20, 0.10, -0.15))
    force = vector((1.00, 0.50, 5.00))
    side = 1

    print('MODELO MATEMÁTICO NOVA SPOT MICRO — EJEMPLO NUMÉRICO')
    print('Ecuación: tau = M(q)q_ddot + C(q,q_dot)q_dot + g(q)')
    print('                + tau_pasiva(q_dot) - J(q)^T f\n')
    show('q [rad]', q)
    show('q_dot [rad/s]', q_dot)
    show('q_ddot [rad/s^2]', q_ddot)
    show('f_pie [N]', force)

    foot = forward_leg(*q, side)
    jacobian = np.asarray(leg_jacobian(*q, side))
    mass = leg_mass_matrix(q, side)
    term_inertia = mass @ q_ddot
    term_coriolis = vector(coriolis_torque(q, q_dot, side))
    term_gravity = vector(gravity_torque(q, side))
    term_passive = vector(passive_joint_torque(q_dot))
    term_contact = vector(foot_force_to_joint_torque(q, force, side))
    torque = vector(inverse_dynamics(q, q_dot, q_ddot, side, force))

    print('\n1. CINEMÁTICA DIRECTA: p = FK(q)')
    show('p_pie [m]', foot)
    print('\n2. JACOBIANO: p_dot = J(q)q_dot')
    show('J(q)', jacobian)
    show('p_dot [m/s]', jacobian @ q_dot)
    print('\n3. DINÁMICA: sustitución término por término')
    show('M(q) [kg m^2]', mass)
    show('M(q)q_ddot [N m]', term_inertia)
    show('C(q,q_dot)q_dot [N m]', term_coriolis)
    show('g(q) [N m]', term_gravity)
    show('tau_pasiva [N m]', term_passive)
    show('J(q)^T f [N m]', term_contact)
    show('tau_resultante [N m]', torque)
    reconstructed = term_inertia + term_coriolis + term_gravity + term_passive - term_contact
    print(f'Comprobación de la ecuación: {np.allclose(torque, reconstructed)}')
    print(f'Máximo uso del par de bloqueo MG996R: '
          f'{100.0 * np.max(np.abs(torque)) / MG996R.stall_torque:.2f} %')

    print('\n4. CENTRO DE MASA Y ESTABILIDAD')
    stance = {leg: tuple(q) for leg in ('fl', 'fr', 'rl', 'rr')}
    com = robot_center_of_mass(stance)
    contacts = [foot_position_body(leg, stance[leg])[:2] for leg in stance]
    margin = static_stability_margin(com[:2], contacts)
    show('COM corporal [m]', com)
    show('contactos xy [m]', contacts)
    print(f'margen_estatico = {margin:.6f} m ({margin*1000:.2f} mm)')
    print(f'Condición: {"estable cuasiestáticamente" if margin > 0 else "fuera del soporte"}')


if __name__ == '__main__':
    main()
