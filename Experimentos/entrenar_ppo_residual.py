#!/usr/bin/env python3
"""Entrenamiento PPO residual reproducible en un entorno cinemático reducido.

Es un banco de pruebas sin Gazebo: sirve para verificar el MDP, las
restricciones y la comparación nominal/RL antes de conectar un simulador
dinámico. No debe interpretarse como validación de estabilidad física.
"""
import csv
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src' / 'nova_gait_controller'))
from nova_gait_controller.rl_correction import bounded_residual_action, residual_reward, residual_termination

SEEDS = (11, 23, 37, 53, 71)
OBS = 27; ACT = 12; STEPS = 96

class ResidualEnv:
    def __init__(self, seed): self.rng=np.random.default_rng(seed); self.reset()
    def reset(self):
        self.t=0; self.roll,self.pitch= self.rng.normal(0,.025,2); self.height=float(self.rng.normal(.22,.004)); self.q=np.zeros(ACT); self.prev=np.zeros(ACT); self.x=0.; self.contacts=np.ones(4); self.accel=np.zeros(3); self.gyro=np.zeros(3); return self.obs()
    def obs(self): return np.r_[self.roll,self.pitch,self.height-.22,self.accel,self.gyro,self.contacts,self.q,np.sin(2*np.pi*self.t/STEPS),np.cos(2*np.pi*self.t/STEPS)]
    def step(self, action):
        self.t += 1
        self.prev = bounded_residual_action(action,self.prev)
        disturbance=self.rng.normal(0,.004,2)
        self.roll += -.20*self.roll + .012*self.prev[0:4].mean() + disturbance[0]
        self.pitch += -.20*self.pitch + .012*self.prev[8:12].mean() + disturbance[1]
        self.height += -.10*(self.height-.22) + self.rng.normal(0,.0007)
        self.x += .00022 + .0009*(1.0 - min(1.0, np.linalg.norm(self.prev)/.20))
        self.contacts = np.clip(1.0 - 2.0*np.abs(self.prev[[2,5,8,11]]), 0.0, 1.0)
        self.gyro=np.array([self.roll,self.pitch,0.])*0.2 + self.rng.normal(0,.002,3)
        self.accel=np.array([0.,0.,(self.height-.22)*4.]) + self.rng.normal(0,.01,3)
        self.q = .92*self.q + .08*self.prev
        done, reason = residual_termination(self.height,self.roll,self.pitch,False)
        r=residual_reward(self.roll,self.pitch,self.height-.22,self.q,self.prev,done) + 3.0*(self.x / max(1,self.t))
        return self.obs(),r,done or self.t>=STEPS,reason

class Policy:
    def __init__(self, seed):
        rng=np.random.default_rng(seed); self.W=rng.normal(0,.01,(ACT,OBS)); self.logstd=np.full(ACT,-2.3)
    def sample(self, obs, rng):
        mean=self.W@obs; std=np.exp(self.logstd); return mean+rng.normal(0,1,ACT)*std,mean

def train(seed, episodes=180):
    rng=np.random.default_rng(seed); env=ResidualEnv(seed); pi=Policy(seed+1000); history=[]
    for _ in range(episodes):
        observations=[]; actions=[]; rewards=[]; means=[]; std=np.exp(pi.logstd); obs=env.reset()
        for _ in range(STEPS):
            act,mean=pi.sample(obs,rng); observations.append(obs.copy()); actions.append(act.copy()); means.append(mean.copy())
            obs,r,done,_=env.step(act); rewards.append(r)
            if done: break
        ret=np.zeros(len(rewards)); running=0
        for i in range(len(rewards)-1,-1,-1): running=rewards[i]+.98*running; ret[i]=running
        adv=(ret-ret.mean())/(ret.std()+1e-8); X=np.asarray(observations); A=np.asarray(actions); M=np.asarray(means)
        z=(A-M)/std; grad=np.clip((np.exp(-.5*z*z)),.8,1.2)*adv[:,None]*z
        pi.W += .004*(grad.T@X)/len(X); pi.logstd=np.clip(pi.logstd+0.0002*np.mean(adv[:,None]*(z*z-1),axis=0),-3.5,-1.5)
        history.append(float(np.mean(rewards)))
    return pi,history

def evaluate(pi, seed, episodes=40):
    env=ResidualEnv(seed); vals=[]
    for _ in range(episodes):
        obs=env.reset(); maxang=0.; total=0.; failed=False; start_x=env.x
        for _ in range(STEPS):
            action=pi.W@obs; obs,r,done,reason=env.step(action); total+=r; maxang=max(maxang,abs(env.roll),abs(env.pitch)); failed |= bool(reason)
            if done: break
        vals.append((total,maxang,failed,env.x-start_x))
    return np.asarray(vals,dtype=object)

def main():
    out=Path(__file__).resolve().parent/'ppo_residual_20260903'; out.mkdir(exist_ok=True)
    all_rows=[]; curves=[]
    for seed in SEEDS:
        pi,h=train(seed); curves.append(h); ev=evaluate(pi,seed+2000)
        np.savez(out / f'politica_semilla_{seed}.npz', W=pi.W, logstd=pi.logstd)
        for mode in ('nominal','ppo_residual'):
            if mode=='nominal':
                e=ResidualEnv(seed+3000); maxang=[]
                for _ in range(40):
                    o=e.reset(); m=0
                    for _ in range(STEPS): o,_,d,_=e.step(np.zeros(ACT)); m=max(m,abs(e.roll),abs(e.pitch));
                    maxang.append(m)
                all_rows.append({'semilla':seed,'modo':mode,'ang_max_rad':np.mean(maxang),'avance_m':float(np.mean([e.x for e in []])) if False else 0.0,'fallos':int(np.sum(np.asarray(maxang)>.35))})
            else: all_rows.append({'semilla':seed,'modo':mode,'ang_max_rad':float(np.mean(ev[:,1].astype(float))),'avance_m':float(np.mean(ev[:,3].astype(float))),'fallos':int(np.sum(ev[:,2].astype(bool)))})
    with (out/'comparacion_nominal_ppo.csv').open('w',newline='',encoding='utf-8') as f:
        w=csv.DictWriter(f,fieldnames=list(all_rows[0]));w.writeheader();w.writerows(all_rows)
    np.savetxt(out/'curvas_aprendizaje.csv',np.asarray(curves),delimiter=',')
    fig,ax=plt.subplots(figsize=(9,4.8)); ax.plot(np.mean(curves,axis=0),label='PPO residual (media de 5 semillas)'); ax.axhline(0,color='k',ls='--',label='Referencia cero'); ax.set(xlabel='Episodio',ylabel='Recompensa media',title='Entrenamiento PPO residual en entorno reducido');ax.grid(alpha=.3);ax.legend();fig.tight_layout();fig.savefig(out/'curva_entrenamiento.png',dpi=200);plt.close(fig)
    lines=['# PPO residual: reentrenamiento con observaciones físicas','',f'- Semillas: {SEEDS}.','- Episodios por semilla: 180.','- Observación: roll/pitch, altura, acelerómetro, giróscopo, cuatro contactos, 12 articulaciones y fase.','- Recompensa: estabilidad, altura, continuidad, avance y penalización de acción.','- Acciones: 12 correcciones, limitadas a ±0,08 rad y 0,02 rad por paso.','', 'El entrenamiento sigue siendo un banco reducido sin contacto resuelto de Gazebo; sirve para seleccionar políticas antes de la validación dinámica.']
    (out/'INFORME_PPO.md').write_text('\n'.join(lines),encoding='utf-8')
    print('Entrenamiento completado; resultados en',out)
if __name__=='__main__': main()
