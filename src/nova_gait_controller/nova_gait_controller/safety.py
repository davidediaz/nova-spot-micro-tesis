"""Pure helpers shared by the metrics and safety-supervisor nodes."""

from math import asin, atan2, copysign, pi


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
    if height < min_height:
        reasons.append('altura_baja')
    if height > max_height:
        reasons.append('altura_alta')
    if abs(roll) > max_tilt:
        reasons.append('roll')
    if abs(pitch) > max_tilt:
        reasons.append('pitch')
    return reasons
