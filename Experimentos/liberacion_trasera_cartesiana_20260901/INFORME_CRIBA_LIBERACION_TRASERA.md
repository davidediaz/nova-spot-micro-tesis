# Criba cartesiana de liberación trasera

Fecha: 31 de agosto de 2026, America/Bogota.

La evidencia de Gazebo mostró que RL y RR recuperaban contacto 0,07--0,08 s después del despegue observado, todavía durante el ascenso. Por ello esta criba mantiene el descenso 0,20/0,75 y actúa solo sobre la altura trasera al 25 % de la oscilación.

Se conservaron 24 muestras, paso de 0,018 m, elevación máxima de 0,014 m, transferencia lateral de 0,004 m y longitudinal de 0,008 m.

| Relación de ascenso trasero | Altura al 25 % (m) | Salto articular máximo (rad) | Salto cartesiano máximo (m) | Pasa |
|---:|---:|---:|---:|:---:|
| 0.707106781 | 0.009899 | 0.184401 | 0.014337 | sí |
| 0.750000000 | 0.010500 | 0.184401 | 0.014337 | sí |
| 0.800000000 | 0.011200 | 0.189604 | 0.014337 | sí |
| 0.850000000 | 0.011900 | 0.201195 | 0.014337 | no |
| 0.900000000 | 0.012600 | 0.212661 | 0.014337 | no |
| 0.950000000 | 0.013300 | 0.224009 | 0.014337 | no |
| 1.000000000 | 0.014000 | 0.235241 | 0.014337 | no |

Esta criba no demuestra separación física. Los valores aceptados deben compararse en Gazebo contra el nominal y 0,20/0,75 desde estados iniciales equivalentes. El archivo `gaits.yaml` conserva el valor nominal; no se ha congelado una nueva línea base.
