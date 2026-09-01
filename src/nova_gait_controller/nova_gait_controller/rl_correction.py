"""Safety contract for a residual RL correction layered over a nominal gait."""

from dataclasses import dataclass
from math import isfinite

import numpy as np

from .safety import JOINT_LIMITS


@dataclass(frozen=True)
class ResidualLimits:
    max_action_rad: float = 0.08
    max_action_step_rad: float = 0.02
    max_roll_pitch_rad: float = 0.35
    min_height_m: float = 0.16
    max_height_m: float = 0.32


def bounded_residual_action(action, previous_action, limits=ResidualLimits()):
    """Clip amplitude and slew rate of twelve residual joint corrections."""
    action = np.asarray(action, dtype=float)
    previous = np.asarray(previous_action, dtype=float)
    if action.shape != (12,) or previous.shape != (12,):
        raise ValueError('la accion residual debe tener doce componentes')
    if not np.isfinite(action).all() or not np.isfinite(previous).all():
        raise ValueError('accion residual no finita')
    target = np.clip(action, -limits.max_action_rad, limits.max_action_rad)
    delta = np.clip(target - previous,
                    -limits.max_action_step_rad, limits.max_action_step_rad)
    return previous + delta


def apply_residual(nominal, residual):
    """Apply a bounded residual while preserving the nominal joint limits."""
    nominal = np.asarray(nominal, dtype=float)
    residual = np.asarray(residual, dtype=float)
    if nominal.shape != (12,) or residual.shape != (12,):
        raise ValueError('se requieren doce referencias nominales y residuales')
    corrected = nominal + residual
    kinds = ('coxa', 'femur', 'tibia') * 4
    lower = np.asarray([JOINT_LIMITS[kind][0] for kind in kinds])
    upper = np.asarray([JOINT_LIMITS[kind][1] for kind in kinds])
    return np.clip(corrected, lower, upper)


def residual_reward(roll, pitch, height_error, joint_error, action,
                    safety_triggered=False):
    """Transparent reward: stabilize the body with small smooth corrections."""
    values = np.asarray([roll, pitch, height_error, *joint_error, *action], dtype=float)
    if not np.isfinite(values).all():
        return -1000.0
    cost = (8.0 * roll**2 + 8.0 * pitch**2 + 20.0 * height_error**2
            + 0.5 * float(np.dot(joint_error, joint_error))
            + 0.05 * float(np.dot(action, action)))
    return 1.0 - cost - (100.0 if safety_triggered else 0.0)


def residual_termination(height, roll, pitch, supervisor_triggered,
                         limits=ResidualLimits()):
    """Terminate on the same conservative body envelope as the supervisor."""
    if supervisor_triggered:
        return True, 'supervisor'
    if not all(isfinite(value) for value in (height, roll, pitch)):
        return True, 'estado_no_finito'
    if not limits.min_height_m <= height <= limits.max_height_m:
        return True, 'altura'
    if abs(roll) > limits.max_roll_pitch_rad or abs(pitch) > limits.max_roll_pitch_rad:
        return True, 'inclinacion'
    return False, ''
