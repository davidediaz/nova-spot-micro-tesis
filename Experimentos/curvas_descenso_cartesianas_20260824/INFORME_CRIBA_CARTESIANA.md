# Criba cartesiana de curvas de descenso

Se mantuvieron 24 muestras, paso de 0,018 m, elevación de 0,014 m, transferencia lateral de 0,004 m y longitudinal de 0,008 m.

Criterio implementado: salto articular cíclico menor que 0.20 rad. Este es el límite de la prueba unitaria vigente; el umbral provisional de 0,05 rad del protocolo debe ser revisado porque tampoco lo cumple la trayectoria nominal.

## Candidatos que pasan la criba

| Relación delantera | Relación trasera | Salto máximo (rad) | Salto cartesiano máximo (m) |
|---:|---:|---:|---:|
| 0.707106781 | 0.707106781 | 0.170014 | 0.013903 |
| 0.200000000 | 0.750000000 | 0.184401 | 0.014337 |
| 0.200000000 | 0.800000000 | 0.191745 | 0.014858 |
| 0.350000000 | 0.750000000 | 0.180103 | 0.014337 |
| 0.350000000 | 0.800000000 | 0.191745 | 0.014858 |
| 0.500000000 | 0.750000000 | 0.180103 | 0.014337 |
| 0.500000000 | 0.800000000 | 0.191745 | 0.014858 |

La criba solo demuestra alcanzabilidad y continuidad de referencias. No permite inferir el instante de contacto; los candidatos deben medirse de forma exploratoria en Gazebo antes de congelar parámetros.
