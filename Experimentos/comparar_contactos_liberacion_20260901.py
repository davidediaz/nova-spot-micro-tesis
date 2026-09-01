#!/usr/bin/env python3
"""Compare contact timing for nominal and rear-liftoff candidates."""
import csv
from pathlib import Path

CASES = {
    'nominal_r7': Path('Experimentos/analisis/cierre_gateo_r7_20260901'),
    'ratio_0.75': Path('Experimentos/resultados_liberacion_gateo_075_20260901/contactos'),
    'ratio_0.80': Path('Experimentos/resultados_liberacion_gateo_080_20260901/contactos'),
}

rows = []
for name, folder in CASES.items():
    data = list(csv.DictReader((folder / 'resumen_por_pata.csv').open(encoding='utf-8')))
    for leg in ('fl', 'fr', 'rl', 'rr'):
        for transition in ('liftoff', 'landing'):
            found = next((r for r in data if r['leg'] == leg and r['transition'] == transition), None)
            if found:
                delay = found['mean_delay_s'] or 'NA'
                agreement = found['agreement_percent'] or 'NA'
                rows.append((name, leg, transition, delay, agreement))
out = Path('Experimentos/comparacion_contactos_liberacion_20260901.md')
lines = ['# Comparación de liberación trasera', '', '| Caso | Pata | Transición | Retardo medio (s) | Coincidencia (%) |', '|---|---|---|---:|---:|']
for row in rows:
    lines.append(f'| {row[0]} | {row[1]} | {row[2]} | {row[3]} | {row[4]} |')
lines += ['', 'La comparación usa la misma herramienta y ponderación temporal. Los candidatos 0,75 y 0,80 mejoran ligeramente la coincidencia global, pero no demuestran vuelo trasero sostenido; se conserva 0,80 como candidato de trabajo por su margen cinemático.']
out.write_text('\n'.join(lines) + '\n', encoding='utf-8')
print(out)
