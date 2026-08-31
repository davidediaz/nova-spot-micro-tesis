"""Pure helpers for nominal online support-polygon estimation."""

from .kinematics import forward_leg
from .mathematical_model import convex_hull_xy, static_stability_margin


HIP_XY = {
    'fl': (0.090, 0.060), 'fr': (0.090, -0.060),
    'rl': (-0.090, 0.060), 'rr': (-0.090, -0.060),
}
PREFIX = {
    'fl': 'front_left', 'fr': 'front_right',
    'rl': 'rear_left', 'rr': 'rear_right',
}
SIDES = {'fl': 1, 'fr': -1, 'rl': 1, 'rr': -1}


def rotate_vector_by_quaternion(vector, quaternion):
    """Rotate an xyz vector by an xyzw unit quaternion."""
    vx, vy, vz = vector
    qx, qy, qz, qw = quaternion
    # v' = v + 2*q_vec x (q_vec x v + qw*v)
    tx = 2.0 * (qy * vz - qz * vy)
    ty = 2.0 * (qz * vx - qx * vz)
    tz = 2.0 * (qx * vy - qy * vx)
    return (
        vx + qw * tx + qy * tz - qz * ty,
        vy + qw * ty + qz * tx - qx * tz,
        vz + qw * tz + qx * ty - qy * tx,
    )


def nominal_foot_points(joint_names, positions, body_xyz, body_quaternion):
    """Return nominal world-frame foot points from measured joint positions."""
    values = dict(zip(joint_names, positions))
    points = {}
    for leg in HIP_XY:
        prefix = PREFIX[leg]
        q = tuple(values[f'{prefix}_{joint}_joint']
                  for joint in ('coxa', 'femur', 'tibia'))
        local = forward_leg(*q, side=SIDES[leg])
        hip = HIP_XY[leg]
        body_point = (hip[0] + local[0], hip[1] + local[1], local[2])
        rotated = rotate_vector_by_quaternion(body_point, body_quaternion)
        points[leg] = tuple(body_xyz[index] + rotated[index]
                            for index in range(3))
    return points


def support_result(com_xy, foot_points, contacts):
    """Build hull and signed margin, or declare it unavailable."""
    selected = [(foot_points[leg][0], foot_points[leg][1])
                for leg in contacts if leg in foot_points]
    hull = convex_hull_xy(selected)
    if len(hull) < 3:
        return {'available': False, 'margin_m': None, 'polygon_xy': hull}
    try:
        margin = static_stability_margin(com_xy, selected)
    except ValueError:
        return {'available': False, 'margin_m': None, 'polygon_xy': hull}
    return {'available': True, 'margin_m': margin, 'polygon_xy': hull}
