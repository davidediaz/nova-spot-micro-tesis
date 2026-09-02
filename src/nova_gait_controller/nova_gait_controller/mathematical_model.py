"""Computable mathematical model of the provisional Nova Spot Micro.

Frames follow REP-103: x forward, y left and z up.  The functions in this
module deliberately keep measured quantities separate from engineering
estimates; see :class:`ModelParameters`.
"""

from dataclasses import dataclass
from math import cos, pi, sin, tanh

import numpy as np

from .kinematics import COXA_LENGTH, FEMUR_LENGTH, TIBIA_LENGTH, forward_leg


@dataclass(frozen=True)
class ModelParameters:
    """SI parameters of the current, not-yet-characterized reference model."""

    hip_spacing_x: float = 0.180
    hip_spacing_y: float = 0.120
    coxa_length: float = COXA_LENGTH
    femur_length: float = FEMUR_LENGTH
    tibia_length: float = TIBIA_LENGTH
    body_mass: float = 1.20
    coxa_mass: float = 0.12
    femur_mass: float = 0.12
    tibia_mass: float = 0.11
    foot_mass: float = 0.03
    body_length: float = 0.230
    body_width: float = 0.120
    body_height: float = 0.075
    coxa_section_x: float = 0.035
    coxa_section_z: float = 0.035
    femur_section_x: float = 0.035
    femur_section_y: float = 0.030
    tibia_section_x: float = 0.030
    tibia_section_y: float = 0.025
    joint_damping: float = 0.08
    coulomb_friction: float = 0.03
    rotor_armature: float = 0.002
    ground_friction: float = 0.90
    contact_stiffness: float = 12000.0
    contact_damping: float = 80.0
    gravity: float = 9.80665

    @property
    def total_mass(self):
        return self.body_mass + 4.0 * (
            self.coxa_mass + self.femur_mass + self.tibia_mass + self.foot_mass)


DEFAULT_PARAMETERS = ModelParameters()


@dataclass(frozen=True)
class MG996RParameters:
    """TowerPro catalogue data at 6 V; not a continuous safe operating limit."""

    mass: float = 0.055
    stall_torque: float = 11.0 * 0.0980665  # kgf cm -> N m
    no_load_speed: float = (pi / 3.0) / 0.15  # 60 degrees in 0.15 s
    stall_current: float = 1.40
    no_load_current: float = 0.170
    idle_current: float = 0.010
    min_voltage: float = 4.8
    nominal_voltage: float = 6.0
    max_voltage: float = 6.6
    deadband_seconds: float = 1e-6


MG996R = MG996RParameters()


def leg_jacobian(q_coxa, q_femur, q_tibia, side):
    """Analytic J(q) such that foot velocity relative to hip is J q_dot."""
    lf, lt, lc = FEMUR_LENGTH, TIBIA_LENGTH, COXA_LENGTH
    q23 = q_femur + q_tibia
    a = side * q_coxa
    zp = -lf * cos(q_femur) - lt * cos(q23)
    dzp_2 = lf * sin(q_femur) + lt * sin(q23)
    dzp_3 = lt * sin(q23)
    dx_2 = -lf * cos(q_femur) - lt * cos(q23)
    dx_3 = -lt * cos(q23)
    lateral = side * lc
    # d/du of the lateral rotation, followed by du/dq_coxa = side.
    dy_1 = side * (-sin(a) * lateral - cos(a) * zp)
    dz_1 = side * (cos(a) * lateral - sin(a) * zp)
    return (
        (0.0, dx_2, dx_3),
        (dy_1, -sin(a) * dzp_2, -sin(a) * dzp_3),
        (dz_1, cos(a) * dzp_2, cos(a) * dzp_3),
    )


def mat_vec(matrix, vector):
    return tuple(sum(a * b for a, b in zip(row, vector)) for row in matrix)


def transpose_mat_vec(matrix, vector):
    return tuple(sum(matrix[row][column] * vector[row] for row in range(3))
                 for column in range(3))


def foot_force_to_joint_torque(q, force, side):
    """Map a Cartesian force at a foot to joint torque using tau = J^T f."""
    return transpose_mat_vec(leg_jacobian(*q, side), force)


def hip_position(leg, parameters=DEFAULT_PARAMETERS):
    """Hip pivot position in the body frame for fl, fr, rl or rr."""
    if leg not in ('fl', 'fr', 'rl', 'rr'):
        raise ValueError(f'Pata desconocida: {leg}')
    x = parameters.hip_spacing_x / 2.0 if leg[0] == 'f' else -parameters.hip_spacing_x / 2.0
    y = parameters.hip_spacing_y / 2.0 if leg[1] == 'l' else -parameters.hip_spacing_y / 2.0
    return x, y, 0.0


def foot_position_body(leg, q, parameters=DEFAULT_PARAMETERS):
    """Foot position in body coordinates, including the hip translation."""
    side = 1 if leg[1] == 'l' else -1
    hip = hip_position(leg, parameters)
    local = forward_leg(*q, side)
    return tuple(a + b for a, b in zip(hip, local))


def gravity_torque(q, side, parameters=DEFAULT_PARAMETERS):
    """Generalized gravity vector g(q) for one leg.

    Link centres are modeled at half-length. Coxa motion is about the horizontal
    x axis; femur and tibia move in the sagittal plane carried by that rotation.
    The result is the gradient of gravitational potential energy.
    """
    qc, qf, qt = q
    a = side * qc
    lc, lf, lt = parameters.coxa_length, parameters.femur_length, parameters.tibia_length
    masses = parameters

    def potential(angles):
        c, f, t = angles
        ar = side * c
        # z coordinates of the four lumped centres relative to the hip.
        zc = sin(ar) * side * lc / 2.0
        zf = sin(ar) * side * lc + cos(ar) * (-lf * cos(f) / 2.0)
        zt = (sin(ar) * side * lc
              + cos(ar) * (-lf * cos(f) - lt * cos(f + t) / 2.0))
        zfoot = forward_leg(c, f, t, side)[2]
        return parameters.gravity * (
            masses.coxa_mass * zc + masses.femur_mass * zf
            + masses.tibia_mass * zt + masses.foot_mass * zfoot)

    eps = 1e-6
    result = []
    for index in range(3):
        plus = [qc, qf, qt]
        minus = [qc, qf, qt]
        plus[index] += eps
        minus[index] -= eps
        result.append((potential(plus) - potential(minus)) / (2.0 * eps))
    return tuple(result)


def passive_joint_torque(q_dot, parameters=DEFAULT_PARAMETERS):
    """Viscous plus smoothed Coulomb resistance acting against motion."""
    return tuple(parameters.joint_damping * speed
                 + parameters.coulomb_friction * tanh(speed / 0.01)
                 for speed in q_dot)


def _rotation_x(angle):
    c, s = cos(angle), sin(angle)
    return np.array(((1.0, 0.0, 0.0), (0.0, c, -s), (0.0, s, c)))


def _rotation_y(angle):
    c, s = cos(angle), sin(angle)
    return np.array(((c, 0.0, s), (0.0, 1.0, 0.0), (-s, 0.0, c)))


def _box_inertia(mass, x, y, z):
    return np.diag((mass * (y*y + z*z) / 12.0,
                    mass * (x*x + z*z) / 12.0,
                    mass * (x*x + y*y) / 12.0))


def leg_link_com_positions(q, side, parameters=DEFAULT_PARAMETERS):
    """COM positions of coxa, femur, tibia and foot relative to the hip."""
    qc, qf, qt = q
    a = side * qc
    rx = _rotation_x(a)
    coxa_end = rx @ np.array((0.0, side * parameters.coxa_length, 0.0))
    coxa_com = rx @ np.array((0.0, side * parameters.coxa_length / 2.0, 0.0))
    femur_direction = rx @ _rotation_y(qf) @ np.array((0.0, 0.0, -1.0))
    tibia_direction = rx @ _rotation_y(qf + qt) @ np.array((0.0, 0.0, -1.0))
    femur_com = coxa_end + femur_direction * parameters.femur_length / 2.0
    knee = coxa_end + femur_direction * parameters.femur_length
    tibia_com = knee + tibia_direction * parameters.tibia_length / 2.0
    foot = knee + tibia_direction * parameters.tibia_length
    return tuple(tuple(float(value) for value in point)
                 for point in (coxa_com, femur_com, tibia_com, foot))


def _position_jacobian(function, q, step=1e-6):
    jacobian = np.zeros((3, 3))
    for column in range(3):
        plus, minus = np.array(q, dtype=float), np.array(q, dtype=float)
        plus[column] += step
        minus[column] -= step
        jacobian[:, column] = (
            np.asarray(function(plus)) - np.asarray(function(minus))) / (2.0 * step)
    return jacobian


def leg_mass_matrix(q, side, parameters=DEFAULT_PARAMETERS):
    """Rigid-link joint-space inertia M(q) for one 3-DOF leg.

    It includes translational and rotational link inertia, the foot point mass,
    and reflected actuator armature. All values use the nominal URDF geometry.
    """
    qc, qf, qt = q
    positions = leg_link_com_positions(q, side, parameters)
    masses = (parameters.coxa_mass, parameters.femur_mass,
              parameters.tibia_mass, parameters.foot_mass)
    matrix = np.eye(3) * parameters.rotor_armature
    for index, (position, mass) in enumerate(zip(positions, masses)):
        jacobian = _position_jacobian(
            lambda angles, i=index: leg_link_com_positions(angles, side, parameters)[i], q)
        matrix += mass * jacobian.T @ jacobian

    axis_1 = np.array((float(side), 0.0, 0.0))
    axis_2 = _rotation_x(side * qc) @ np.array((0.0, 1.0, 0.0))
    angular_jacobians = (
        np.column_stack((axis_1, np.zeros(3), np.zeros(3))),
        np.column_stack((axis_1, axis_2, np.zeros(3))),
        np.column_stack((axis_1, axis_2, axis_2)),
    )
    local_inertias = (
        _box_inertia(parameters.coxa_mass, parameters.coxa_section_x,
                     parameters.coxa_length, parameters.coxa_section_z),
        _box_inertia(parameters.femur_mass, parameters.femur_section_x,
                     parameters.femur_section_y, parameters.femur_length),
        _box_inertia(parameters.tibia_mass, parameters.tibia_section_x,
                     parameters.tibia_section_y, parameters.tibia_length),
    )
    rotations = (_rotation_x(side * qc),
                 _rotation_x(side * qc) @ _rotation_y(qf),
                 _rotation_x(side * qc) @ _rotation_y(qf + qt))
    for jacobian, inertia, rotation in zip(angular_jacobians, local_inertias, rotations):
        world_inertia = rotation @ inertia @ rotation.T
        matrix += jacobian.T @ world_inertia @ jacobian
    return matrix


def coriolis_torque(q, q_dot, side, parameters=DEFAULT_PARAMETERS, step=1e-5):
    """C(q,q_dot)q_dot computed from Christoffel symbols of M(q)."""
    q = np.asarray(q, dtype=float)
    velocity = np.asarray(q_dot, dtype=float)
    derivatives = []
    for coordinate in range(3):
        plus, minus = q.copy(), q.copy()
        plus[coordinate] += step
        minus[coordinate] -= step
        derivatives.append((leg_mass_matrix(plus, side, parameters)
                            - leg_mass_matrix(minus, side, parameters)) / (2.0 * step))
    result = np.zeros(3)
    for i in range(3):
        for j in range(3):
            for k in range(3):
                christoffel = 0.5 * (derivatives[k][i, j]
                                     + derivatives[j][i, k]
                                     - derivatives[i][j, k])
                result[i] += christoffel * velocity[j] * velocity[k]
    return tuple(float(value) for value in result)


def inverse_dynamics(q, q_dot, q_ddot, side, external_foot_force=(0.0, 0.0, 0.0),
                     parameters=DEFAULT_PARAMETERS):
    """Required actuator torque Mqdd+C+g+passive-J^T f for one leg."""
    inertial = leg_mass_matrix(q, side, parameters) @ np.asarray(q_ddot, dtype=float)
    coriolis = np.asarray(coriolis_torque(q, q_dot, side, parameters))
    gravity = np.asarray(gravity_torque(q, side, parameters))
    passive = np.asarray(passive_joint_torque(q_dot, parameters))
    contact = np.asarray(foot_force_to_joint_torque(q, external_foot_force, side))
    return tuple(float(value) for value in inertial + coriolis + gravity + passive - contact)


def actuator_torque_limit(speed, voltage=6.0, actuator=MG996R):
    """Symmetric speed-dependent torque envelope using a linear DC approximation."""
    if not actuator.min_voltage <= voltage <= actuator.max_voltage:
        raise ValueError('Voltaje fuera del rango de catálogo del MG996R')
    scale = voltage / actuator.nominal_voltage
    stall = actuator.stall_torque * scale
    no_load_speed = actuator.no_load_speed * scale
    return max(0.0, stall * (1.0 - abs(speed) / no_load_speed))


def actuator_current(torque, actuator=MG996R):
    """Catalogue-based current estimate; returns stall current when saturated."""
    ratio = min(1.0, abs(torque) / actuator.stall_torque)
    return actuator.no_load_current + ratio * (actuator.stall_current - actuator.no_load_current)


def saturated_actuator_torque(requested_torque, speed, voltage=6.0,
                              current_limit=1.40, actuator=MG996R):
    """Apply MG996R speed, voltage and per-servo current envelopes.

    This is a catalogue-based engineering bound, not an identified motor model.
    It returns ``(delivered_torque, estimated_current, saturated)``.
    """
    if current_limit <= 0.0:
        raise ValueError('El límite de corriente debe ser positivo')
    speed_limit = actuator_torque_limit(speed, voltage, actuator)
    usable_current = max(0.0, current_limit - actuator.no_load_current)
    current_torque = actuator.stall_torque * min(
        1.0, usable_current /
        (actuator.stall_current - actuator.no_load_current))
    limit = min(speed_limit, current_torque)
    delivered = max(-limit, min(limit, float(requested_torque)))
    return delivered, min(current_limit, actuator_current(delivered, actuator)), \
        abs(delivered - requested_torque) > 1e-12


def apply_backlash(command, previous_output, backlash_rad):
    """Dead-zone approximation shared by both simulator command paths."""
    if backlash_rad < 0.0:
        raise ValueError('La holgura no puede ser negativa')
    delta = float(command) - float(previous_output)
    if abs(delta) <= backlash_rad:
        return float(previous_output)
    return float(command) - (backlash_rad if delta > 0.0 else -backlash_rad)


def robot_center_of_mass(joint_positions, parameters=DEFAULT_PARAMETERS):
    """Whole-robot COM in the body frame for a dict keyed by fl/fr/rl/rr."""
    required = {'fl', 'fr', 'rl', 'rr'}
    if set(joint_positions) != required:
        raise ValueError('Se requieren exactamente las articulaciones fl, fr, rl y rr')
    weighted = np.zeros(3)  # body COM is the body-frame origin
    link_masses = (parameters.coxa_mass, parameters.femur_mass,
                   parameters.tibia_mass, parameters.foot_mass)
    for leg in ('fl', 'fr', 'rl', 'rr'):
        side = 1 if leg[1] == 'l' else -1
        hip = np.asarray(hip_position(leg, parameters))
        for local, mass in zip(leg_link_com_positions(joint_positions[leg], side, parameters),
                               link_masses):
            weighted += mass * (hip + np.asarray(local))
    return tuple(float(value) for value in weighted / parameters.total_mass)


def compliant_contact_force(position, velocity, parameters=DEFAULT_PARAMETERS):
    """Penalty contact against z=0 with damped normal and smooth Coulomb friction."""
    x_velocity, y_velocity, z_velocity = velocity
    penetration = max(0.0, -position[2])
    if penetration == 0.0:
        return 0.0, 0.0, 0.0
    normal = max(0.0, parameters.contact_stiffness * penetration
                 - parameters.contact_damping * z_velocity)
    tangential_speed = (x_velocity*x_velocity + y_velocity*y_velocity) ** 0.5
    if tangential_speed < 1e-12:
        return 0.0, 0.0, normal
    friction = parameters.ground_friction * normal * tanh(tangential_speed / 0.01)
    return (-friction * x_velocity / tangential_speed,
            -friction * y_velocity / tangential_speed, normal)


def convex_hull_xy(points):
    """Return the counter-clockwise convex hull of (x, y) contact points."""
    pts = sorted(set((float(x), float(y)) for x, y in points))
    if len(pts) <= 1:
        return pts

    def cross(o, a, b):
        return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

    lower = []
    for point in pts:
        while len(lower) >= 2 and cross(lower[-2], lower[-1], point) <= 0.0:
            lower.pop()
        lower.append(point)
    upper = []
    for point in reversed(pts):
        while len(upper) >= 2 and cross(upper[-2], upper[-1], point) <= 0.0:
            upper.pop()
        upper.append(point)
    return lower[:-1] + upper[:-1]


def static_stability_margin(com_xy, contacts_xy):
    """Signed shortest distance from projected COM to the support polygon.

    Positive means statically stable, zero is the boundary, and negative means
    the COM projection lies outside. At least three non-collinear contacts are
    required.
    """
    from math import hypot
    hull = convex_hull_xy(contacts_xy)
    if len(hull) < 3:
        raise ValueError('Se requieren al menos tres contactos no colineales')
    px, py = com_xy
    distances = []
    inside = True
    for start, end in zip(hull, hull[1:] + hull[:1]):
        dx, dy = end[0] - start[0], end[1] - start[1]
        signed = (dx * (py - start[1]) - dy * (px - start[0])) / hypot(dx, dy)
        distances.append(abs(signed))
        if signed < -1e-12:
            inside = False
    return min(distances) if inside else -min(distances)
