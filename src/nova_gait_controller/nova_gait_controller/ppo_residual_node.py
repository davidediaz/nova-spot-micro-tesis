"""Aplica una política residual entrenada a referencias articulares nominales."""
import math
from pathlib import Path
import numpy as np
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Imu, JointState
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint
from .rl_correction import bounded_residual_action, apply_residual

JOINTS = ('front_left_coxa_joint','front_left_femur_joint','front_left_tibia_joint',
          'front_right_coxa_joint','front_right_femur_joint','front_right_tibia_joint',
          'rear_left_coxa_joint','rear_left_femur_joint','rear_left_tibia_joint',
          'rear_right_coxa_joint','rear_right_femur_joint','rear_right_tibia_joint')

class PPOResidualNode(Node):
    def __init__(self):
        super().__init__('ppo_residual_node')
        self.declare_parameter('policy_path','')
        self.declare_parameter('input_topic','/nova/nominal_trajectory')
        self.declare_parameter('output_topic','/joint_trajectory_controller/joint_trajectory')
        self.declare_parameter('enabled',True)
        self.W=None; self.prev=np.zeros(12); self.q=np.zeros(12); self.roll=0.; self.pitch=0.; self.phase=0.
        path=str(self.get_parameter('policy_path').value)
        if path:
            data=np.load(Path(path)); self.W=np.asarray(data['W'],dtype=float)
            if self.W.shape != (12,17): raise ValueError('W debe tener forma (12,17)')
        self.pub=self.create_publisher(JointTrajectory,self.get_parameter('output_topic').value,10)
        self.create_subscription(JointTrajectory,self.get_parameter('input_topic').value,self.cb,10)
        self.create_subscription(JointState,'/joint_states',self.joint_cb,10)
        self.create_subscription(Imu,'/nova/imu',self.imu_cb,10)
        self.get_logger().info('PPO residual %s' % ('activo' if self.W is not None and self.get_parameter('enabled').value else 'bypass'))
    def joint_cb(self,msg):
        vals=dict(zip(msg.name,msg.position)); self.q=np.asarray([vals.get(j,0.) for j in JOINTS])
    def imu_cb(self,msg):
        q=msg.orientation; sinr=2*(q.w*q.x+q.y*q.z); cosr=1-2*(q.x*q.x+q.y*q.y); self.roll=math.atan2(sinr,cosr)
        sinp=2*(q.w*q.y-q.z*q.x); self.pitch=math.copysign(math.pi/2,sinp) if abs(sinp)>=1 else math.asin(sinp)
    def cb(self,msg):
        if not msg.points: return
        point=msg.points[0]; target=np.asarray(point.positions,dtype=float)
        if target.shape != (12,): return
        residual=np.zeros(12)
        if self.W is not None and bool(self.get_parameter('enabled').value):
            obs=np.r_[self.roll,self.pitch,0.,self.q,math.sin(self.phase),math.cos(self.phase)]
            residual=bounded_residual_action(self.W@obs,self.prev); self.prev=residual; self.phase=(self.phase+1/96)%1
            target=apply_residual(target,residual)
        out=JointTrajectory(); out.joint_names=list(JOINTS); p=JointTrajectoryPoint(); p.positions=target.tolist(); p.time_from_start=point.time_from_start; out.points=[p]; self.pub.publish(out)

def main(args=None):
    rclpy.init(args=args); node=PPOResidualNode()
    try: rclpy.spin(node)
    except KeyboardInterrupt: pass
    finally: node.destroy_node(); rclpy.shutdown()
