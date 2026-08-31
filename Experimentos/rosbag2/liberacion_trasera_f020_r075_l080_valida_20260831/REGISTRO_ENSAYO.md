# Registro de ensayo exploratorio de liberación trasera

Fecha: 31 de agosto de 2026, America/Bogota.

## Configuración

- 24 muestras, 0,18 s por referencia y ciclo nominal de 4,32 s.
- Paso: 0,018 m; elevación máxima: 0,014 m.
- Transferencia lateral/longitudinal: 0,004/0,008 m.
- Descenso delantero/trasero: 0,20/0,75.
- Altura trasera al 25 % de la oscilación: 0,80.
- `gaits.yaml` permaneció nominal; los parámetros se aplicaron en línea solo
  para esta exploración.

## Integridad y resultado

- Ventana `gateo`--`stand`: 65,633846 s.
- Ciclos completos: 15; ciclo medio: 4,320000 s.
- Mensajes totales: 48.043; fase: 365; trayectorias: 370.
- Eventos verdaderos del supervisor: 0.
- Coincidencia simultánea: 23,643955 %.
- Aterrizaje RL/RR: -0,305102/-0,309170 s.
- Despegue RL/RR: 0,138183/0,134114 s.
- Avance medio: 0,023090 m/ciclo; velocidad: 0,005345 m/s.
- SHA-256 SQLite3:
  `88d30c9dff93b7fea07c5d0f1ecd8485994dd1a3d906ca6fab494c83574e241e`.

## Decisión

El candidato se rechaza. Frente a 0,20/0,75, el adelanto trasero mejoró solo
unos 0,016 s y la coincidencia global bajó de 23,855 % a 23,644 %. Aumentar la
relación a 0,85 o más supera el límite cartesiano implementado de 0,20 rad.
No se congela una nueva línea base.

La tentativa anterior `liberacion_trasera_f020_r075_l080_20260831` es inválida
por contener cero fases y queda marcada por separado.
