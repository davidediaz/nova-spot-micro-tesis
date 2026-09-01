"""Pure helpers shared by the metrics and safety-supervisor nodes."""

from math import asin, atan2, copysign, isfinite, pi


JOINT_LIMITS = {'coxa': (-0.60, 0.60), 'femur': (-1.20, 1.20),
                'tibia': (-2.20, 0.10)}


def quaternion_to_rpy(x, y, z, w):
    """Return intrinsic roll, pitch and yaw (radians) from a quaternion."""
    sin_roll = 2.0 * (w * x + y * z)
    cos_roll = 1.0 - 2.0 * (x * x + y * y)
    roll = atan2(sin_roll, cos_roll)

    sin_pitch = 2.0 * (w * y - z * x)
    pitch = copysign(pi / 2.0, sin_pitch) if abs(sin_pitch) >= 1.0 else asin(sin_pitch)

    sin_yaw = 2.0 * (w * z + x * y)
    cos_yaw = 1.0 - 2.0 * (y * y + z * z)
    return roll, pitch, atan2(sin_yaw, cos_yaw)


def unsafe_reasons(height, roll, pitch, min_height, max_height, max_tilt):
    """Describe every violated body-pose limit."""
    reasons = []
    if not all(isfinite(value) for value in (height, roll, pitch)):
        return ['pose_no_finita']
    if height < min_height:
        reasons.append('altura_baja')
    if height > max_height:
        reasons.append('altura_alta')
    if abs(roll) > max_tilt:
        reasons.append('roll')
    if abs(pitch) > max_tilt:
        reasons.append('pitch')
    return reasons


def stale_sources(last_received, now, timeout):
    """Return required telemetry sources that are absent or older than timeout."""
    if not isfinite(now) or not isfinite(timeout) or timeout <= 0.0:
        raise ValueError('tiempo o timeout invalido')
    return [name for name, stamp in last_received.items()
            if stamp is None or not isfinite(stamp) or now - stamp > timeout]


def diagnostic_reasons(contact, stability, min_stability_margin):
    """Validate parsed contact and stability diagnostics without ROS dependencies."""
    reasons = []
    if contact and contact.get('comparison_available') and contact.get('match') is False:
        reasons.append('contactos_no_coinciden')
    if stability and stability.get('available'):
        margin = stability.get('margin_m')
        if not isinstance(margin, (int, float)) or not isfinite(margin):
            reasons.append('margen_no_finito')
        elif margin < min_stability_margin:
            reasons.append('margen_estabilidad')
    return reasons


def invalid_trajectory_reasons(joint_names, points):
    """Return structural, finite-value and nominal-limit violations."""
    reasons = []
    if len(joint_names) != 12 or len(set(joint_names)) != len(joint_names):
        reasons.append('nombres_articulares_invalidos')
    if not points:
        reasons.append('trayectoria_sin_puntos')
        return reasons
    for point in points:
        if len(point.positions) != len(joint_names):
            reasons.append('dimension_articular_invalida')
            continue
        for name, value in zip(joint_names, point.positions):
            if not isfinite(value):
                reasons.append('referencia_no_finita')
                continue
            kind = next((key for key in JOINT_LIMITS if f'_{key}_joint' in name), None)
            if kind is None:
                reasons.append('articulacion_desconocida')
            elif not JOINT_LIMITS[kind][0] <= value <= JOINT_LIMITS[kind][1]:
                reasons.append('limite_articular')
    return list(dict.fromkeys(reasons))
