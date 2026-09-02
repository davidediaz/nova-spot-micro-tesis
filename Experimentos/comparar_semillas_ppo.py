#!/usr/bin/env python3
import csv,sys
from pathlib import Path
import numpy as np
def main():
 root=Path(__file__).resolve().parents[1]; c=root/'Experimentos'/sys.argv[1]; fs=['avance_m','velocidad_media_m_s','roll_max_abs_deg','pitch_max_abs_deg','salto_articular_max_rad']; rows=[]
 for d in sorted(c.glob('semilla_*')):
  data=list(csv.DictReader((d/'analisis/metricas_por_ciclo.csv').open(encoding='utf-8')))[1:]
  rows.append({'semilla':d.name.replace('semilla_',''),**{f:float(np.mean([float(x[f]) for x in data])) for f in fs}})
 with (c/'comparacion_semillas.csv').open('w',newline='',encoding='utf-8') as h:
  w=csv.DictWriter(h,fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
 print('\n'.join(str(r) for r in rows))
if __name__=='__main__': main()
