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
OBS = 17; ACT = 12; STEPS = 96

class ResidualEnv:
    def __init__(self, seed): self.rng=np.random.default_rng(seed); self.reset()
    def reset(self):
        self.t=0; self.roll,self.pitch= self.rng.normal(0,.025,2); self.height=float(self.rng.normal(.22,.004)); self.q=np.zeros(ACT); self.prev=np.zeros(ACT); return self.obs()
    def obs(self): return np.r_[self.roll,self.pitch,self.height-.22,self.q,np.sin(2*np.pi*self.t/STEPS),np.cos(2*np.pi*self.t/STEPS)]
    def step(self, action):
        self.t += 1
        self.prev = bounded_residual_action(action,self.prev)
        disturbance=self.rng.normal(0,.004,2)
        self.roll += -.14*self.roll + .020*self.prev[0:4].mean() + disturbance[0]
        self.pitch += -.14*self.pitch + .020*self.prev[8:12].mean() + disturbance[1]
        self.height += -.10*(self.height-.22) + self.rng.normal(0,.0007)
        self.q = .92*self.q + .08*self.prev
        done, reason = residual_termination(self.height,self.roll,self.pitch,False)
        r=residual_reward(self.roll,self.pitch,self.height-.22,self.q,self.prev,done)
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
        obs=env.reset(); maxang=0.; total=0.; failed=False
        for _ in range(STEPS):
            action=pi.W@obs; obs,r,done,reason=env.step(action); total+=r; maxang=max(maxang,abs(env.roll),abs(env.pitch)); failed |= bool(reason)
            if done: break
        vals.append((total,maxang,failed))
    return np.asarray(vals,dtype=object)

def main():
    out=Path(__file__).resolve().parent/'ppo_residual_20260902'; out.mkdir(exist_ok=True)
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
                all_rows.append({'semilla':seed,'modo':mode,'ang_max_rad':np.mean(maxang),'fallos':int(np.sum(np.asarray(maxang)>.35))})
            else: all_rows.append({'semilla':seed,'modo':mode,'ang_max_rad':float(np.mean(ev[:,1].astype(float))),'fallos':int(np.sum(ev[:,2].astype(bool)))})
    with (out/'comparacion_nominal_ppo.csv').open('w',newline='',encoding='utf-8') as f:
        w=csv.DictWriter(f,fieldnames=list(all_rows[0]));w.writeheader();w.writerows(all_rows)
    np.savetxt(out/'curvas_aprendizaje.csv',np.asarray(curves),delimiter=',')
    fig,ax=plt.subplots(figsize=(9,4.8)); ax.plot(np.mean(curves,axis=0),label='PPO residual (media de 5 semillas)'); ax.axhline(0,color='k',ls='--',label='Referencia cero'); ax.set(xlabel='Episodio',ylabel='Recompensa media',title='Entrenamiento PPO residual en entorno reducido');ax.grid(alpha=.3);ax.legend();fig.tight_layout();fig.savefig(out/'curva_entrenamiento.png',dpi=200);plt.close(fig)
    lines=['# PPO residual: entrenamiento preparatorio','',f'- Semillas: {SEEDS}.','- Episodios por semilla: 180.','- Entorno: dinámica cinemática reducida, sin Gazebo y sin contacto resuelto.','- Acciones: 12 correcciones, limitadas a ±0,08 rad y 0,02 rad por paso.','', 'La comparación nominal/PPO se incluye como verificación del contrato y del flujo de entrenamiento. No constituye todavía una comparación de estabilidad en Gazebo; esa etapa requiere conectar la política a observaciones reales del simulador y repetir el protocolo de cinco ensayos.']
    (out/'INFORME_PPO.md').write_text('\n'.join(lines),encoding='utf-8')
    print('Entrenamiento completado; resultados en',out)
if __name__=='__main__': main()
