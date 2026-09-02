#!/usr/bin/env python3
import csv
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / 'Experimentos/campana_ppo_gazebo_20260902'
PPO = ROOT / 'Experimentos/campana_ppo_gazebo_20260903'
OUT = PPO / 'comparacion_final'
FIELDS = [('avance_m','Avance (m/ciclo)'),('velocidad_media_m_s','Velocidad (m/s)'),
          ('roll_max_abs_deg','Roll máximo (°)'),('pitch_max_abs_deg','Pitch máximo (°)'),
          ('salto_articular_max_rad','Salto articular (rad)')]
def rows(path):
    return list(csv.DictReader((path/'analisis/metricas_por_ciclo.csv').open(encoding='utf-8')))
def main():
    OUT.mkdir(exist_ok=True)
    nominal=[rows(BASE/f'nominal_0{i}') for i in range(1,6)]
    ppo=[rows(PPO/f'ppo_gazebo_0{i}') for i in range(1,6)]
    result=[]
    for field,label in FIELDS:
        n=np.array([np.mean([float(r[field]) for r in x[1:]]) for x in nominal])
        q=np.array([np.mean([float(r[field]) for r in x[1:]]) for x in ppo])
        d=q-n
        result.append({'metrica':label,'nominal_media':n.mean(),'ppo_reentrenada_media':q.mean(),
                       'diferencia_media':d.mean(),'diferencia_relativa_pct':100*d.mean()/n.mean(),
                       'rmse_pareado':float(np.sqrt(np.mean(d*d)))})
    with (OUT/'comparacion_reentrenada.csv').open('w',newline='',encoding='utf-8') as f:
        w=csv.DictWriter(f,fieldnames=list(result[0])); w.writeheader(); w.writerows(result)
    fig,ax=plt.subplots(1,2,figsize=(12,5),constrained_layout=True); x=np.arange(5)
    for axis,field,label in [(ax[0],'pitch_max_abs_deg','Pitch máximo (°)'),(ax[1],'avance_m','Avance (m/ciclo)')]:
        n=[np.mean([float(r[field]) for r in z[1:]]) for z in nominal]
        q=[np.mean([float(r[field]) for r in z[1:]]) for z in ppo]
        axis.plot(x+1,n,'o-',label='Nominal'); axis.plot(x+1,q,'s--',label='PPO reentrenada')
        axis.set(xlabel='Ensayo emparejado',ylabel=label); axis.grid(alpha=.3); axis.legend()
    fig.suptitle('Revalidación dinámica nominal–PPO en Gazebo'); fig.savefig(OUT/'comparacion_reentrenada.png',dpi=220); plt.close(fig)
    lines=['# Revalidación dinámica nominal–PPO en Gazebo','','- Cinco ensayos válidos por condición; se excluyó el ciclo 1 transitorio y se promediaron los ciclos restantes.','- PPO: política reentrenada con contactos, IMU y altura corporal; semilla 11.','- La comparación usa la campaña nominal independiente anterior como referencia.','', '| Métrica | Nominal | PPO reentrenada | Diferencia relativa | RMSE pareado |','|---|---:|---:|---:|---:|']
    for r in result: lines.append(f"| {r['metrica']} | {r['nominal_media']:.6f} | {r['ppo_reentrenada_media']:.6f} | {r['diferencia_relativa_pct']:.3f} % | {r['rmse_pareado']:.6f} |")
    lines += ['', 'Estos resultados son evidencia de simulación dinámica en Gazebo y no implican transferencia al robot físico. La mejora locomotora solo se afirmará si avance y velocidad aumentan sin degradar estabilidad.']
    (OUT/'INFORME_REVALIDACION.md').write_text('\n'.join(lines),encoding='utf-8')
if __name__=='__main__': main()
