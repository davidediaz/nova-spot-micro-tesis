#!/usr/bin/env python3
import csv
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

ROOT=Path(__file__).resolve().parents[1]; BASE=ROOT/'Experimentos/campana_ppo_gazebo_20260902'; OUT=BASE/'comparacion_final'
FIELDS=[('avance_m','Avance (m/ciclo)'),('velocidad_media_m_s','Velocidad (m/s)'),('roll_max_abs_deg','Roll máximo (°)'),('pitch_max_abs_deg','Pitch máximo (°)'),('salto_articular_max_rad','Salto articular (rad)')]
def rows(label):
 p=BASE/label/'analisis/metricas_por_ciclo.csv'; return list(csv.DictReader(p.open(encoding='utf-8')))[1:]
def main():
 OUT.mkdir(exist_ok=True); nominal=[rows(f'nominal_0{i}') for i in range(1,6)]; ppo=[rows(f'ppo_0{i}') for i in range(1,6)]
 result=[]
 for field,label in FIELDS:
  n=np.array([np.mean([float(r[field]) for r in x]) for x in nominal]); q=np.array([np.mean([float(r[field]) for r in x]) for x in ppo]); diff=q-n
  result.append({'metrica':label,'nominal_media':n.mean(),'ppo_media':q.mean(),'diferencia_media':diff.mean(),'diferencia_relativa_pct':100*diff.mean()/n.mean(),'rmse_pareado':float(np.sqrt(np.mean(diff**2)))})
 with (OUT/'comparacion_final.csv').open('w',newline='',encoding='utf-8') as f: w=csv.DictWriter(f,fieldnames=list(result[0]));w.writeheader();w.writerows(result)
 fig,ax=plt.subplots(1,2,figsize=(12,5),constrained_layout=True); x=np.arange(5)
 n=np.array([np.mean([float(r['pitch_max_abs_deg']) for r in z]) for z in nominal]); q=np.array([np.mean([float(r['pitch_max_abs_deg']) for r in z]) for z in ppo]); ax[0].plot(x+1,n,'o-',label='Nominal');ax[0].plot(x+1,q,'s--',label='PPO residual');ax[0].set(xlabel='Ensayo emparejado',ylabel='Pitch máximo (°)');ax[0].grid(alpha=.3);ax[0].legend()
 n=np.array([np.mean([float(r['avance_m']) for r in z]) for z in nominal]); q=np.array([np.mean([float(r['avance_m']) for r in z]) for z in ppo]); ax[1].plot(x+1,n,'o-',label='Nominal');ax[1].plot(x+1,q,'s--',label='PPO residual');ax[1].set(xlabel='Ensayo emparejado',ylabel='Avance (m/ciclo)');ax[1].grid(alpha=.3);ax[1].legend();fig.suptitle('Comparación final nominal–PPO en Gazebo');fig.savefig(OUT/'comparacion_final.png',dpi=220);plt.close(fig)
 lines=['# Comparación final nominal–PPO en Gazebo','', '- Cinco ensayos por condición; se analizaron al menos tres ciclos completos por ensayo.', '- El ciclo 1 se excluyó de los promedios por ser transitorio.', '', '| Métrica | Nominal | PPO residual | Diferencia relativa | RMSE pareado |','|---|---:|---:|---:|---:|']
 for r in result: lines.append(f"| {r['metrica']} | {r['nominal_media']:.6f} | {r['ppo_media']:.6f} | {r['diferencia_relativa_pct']:.3f} % | {r['rmse_pareado']:.6f} |")
 lines += ['', 'Las diferencias describen esta campaña corta en Gazebo y no prueban transferencia al robot físico. La política usada fue la semilla 11 en las cinco corridas PPO; las demás semillas quedan disponibles para una selección bloqueada posterior.']
 (OUT/'INFORME_COMPARACION_FINAL.md').write_text('\n'.join(lines),encoding='utf-8'); print('comparación final generada')
if __name__=='__main__': main()
