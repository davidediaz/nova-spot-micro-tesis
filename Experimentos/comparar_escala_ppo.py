#!/usr/bin/env python3
import csv,sys
from pathlib import Path
import numpy as np
EXPECTED_CYCLE_S=5.76
TOLERANCE_S=0.10
def valid_rows(path):
 rows=list(csv.DictReader(path.open(encoding='utf-8')))[1:]
 return [r for r in rows if abs(float(r['duracion_observada_s'])-EXPECTED_CYCLE_S)<=TOLERANCE_S]
def main():
 root=Path(__file__).resolve().parents[1]; camp=root/'Experimentos'/sys.argv[1]; fields=['avance_m','velocidad_media_m_s','roll_max_abs_deg','pitch_max_abs_deg','salto_articular_max_rad']; out=[]
 for d in sorted(camp.glob('escala_*')):
  rows=valid_rows(d/'analisis/metricas_por_ciclo.csv')
  if not rows: raise ValueError(f'{d.name}: ningún ciclo válido cercano a {EXPECTED_CYCLE_S} s')
  rec={'escala':d.name.replace('escala_','').replace('p','.')}
  for f in fields: rec[f]=float(np.mean([float(r[f]) for r in rows]))
  out.append(rec)
 with (camp/'comparacion_escalas.csv').open('w',newline='',encoding='utf-8') as h:
  w=csv.DictWriter(h,fieldnames=list(out[0]),lineterminator='\n');w.writeheader();w.writerows(out)
 nominal=[]
 for d in sorted((root/'Experimentos/campana_ppo_gazebo_20260902').glob('nominal_*/analisis/metricas_por_ciclo.csv')):
  data=valid_rows(d)
  if data: nominal.append({f:float(np.mean([float(x[f]) for x in data])) for f in fields})
 base={f:float(np.mean([x[f] for x in nominal])) for f in fields}
 for x in out:
  x['avance_rel_pct']=100*(x['avance_m']-base['avance_m'])/base['avance_m']; x['velocidad_rel_pct']=100*(x['velocidad_media_m_s']-base['velocidad_media_m_s'])/base['velocidad_media_m_s']; x['aceptada']=bool(x['avance_m']>=base['avance_m'] and x['velocidad_media_m_s']>=base['velocidad_media_m_s'] and x['roll_max_abs_deg']<=base['roll_max_abs_deg'] and x['pitch_max_abs_deg']<=base['pitch_max_abs_deg'])
 with (camp/'criterio_aceptacion.md').open('w',encoding='utf-8') as h:
  h.write('# Criterio de aceptación del barrido PPO\n\n')
  h.write('Línea base nominal recalculada con cuatro ensayos válidos: avance %.6f m/ciclo, velocidad %.6f m/s, roll %.6f°, pitch %.6f°. `nominal_03` se excluyó porque sus ciclos observados duran 2,88 s en vez de 5,76 s.\n\n' % tuple(base[f] for f in fields[:1]+fields[1:4]))
  h.write('| Escala | Avance | Velocidad | Roll | Pitch | Aceptada |\n|---:|---:|---:|---:|---:|:---:|\n')
  for x in out: h.write('| %s | %.6f | %.6f | %.3f | %.3f | %s |\n' % (x['escala'],x['avance_m'],x['velocidad_media_m_s'],x['roll_max_abs_deg'],x['pitch_max_abs_deg'],'sí' if x['aceptada'] else 'no'))
 print('\n'.join(str(x) for x in out))
if __name__=='__main__': main()
