# Reentrenamiento PPO extendido — 25 de septiembre de 2026

## Alcance

Se reentrenaron las dos marchas residuales en MuJoCo con una campaña nueva,
separada de las ejecuciones del 24 de septiembre:

| Marcha | Semilla | Pasos solicitados | Pasos efectivos |
| --- | ---: | ---: | ---: |
| `crawl` / gateo | 53 | 200.000 | 200.704 |
| `step` / paso | 71 | 200.000 | 200.704 |

La observación tiene 27 componentes y la acción 12 correcciones articulares.
Cada corrección está limitada a `±0,08 rad` y el cambio por paso a `0,02 rad`.
La aleatorización de dominio de fricción y amortiguamiento estuvo activa durante
el entrenamiento y desactivada durante la evaluación.

## Resultado emparejado

La evaluación usa cinco episodios nominales y cinco PPO por marcha, con cinco
ciclos y sin aleatorización durante la evaluación.

| Marcha | Condición | Retorno medio | Avance medio (m) | Inclinación máxima (rad) |
| --- | --- | ---: | ---: | ---: |
| Gateo | nominal | 1091,31 | 0,4917 | 0,00993 |
| Gateo | PPO | 1095,71 | 1,2860 | 0,03505 |
| Paso | nominal | 1451,30 | 0,0155 | 0,01392 |
| Paso | PPO | 1497,67 | 3,5561 | 0,04289 |

PPO aumenta el avance en esta evaluación, pero también la inclinación máxima.
Por ello las políticas quedan como candidatas de simulación y no como políticas
aceptadas para transferencia.

## Gazebo y seguridad

Se intentó continuar gateo en Gazebo durante 50.000 pasos desde la política
MuJoCo extendida. La corrida llegó a 500 pasos y fue detenida porque la
sincronización por fase opera aproximadamente en tiempo real; el presupuesto
completo requería varias horas. No se generó una política final de Gazebo ni se
inició la adaptación de paso. La traza parcial se conserva para distinguir el
intento inconcluso de una campaña válida.

No se ejecutó PWM, SSH, Raspberry Pi ni servos. `hardware_transfer` permanece en
`false`. Ningún resultado de esta campaña autoriza mover el prototipo.

## Artefactos

- `mujoco/crawl_semilla_53/policy.zip`
- `mujoco/step_semilla_71/policy.zip`
- `mujoco/*/metadata.json`
- `mujoco/*/training_trace.jsonl`
- `mujoco_evaluation.csv`
- `campaign_manifest.json`
- `gazebo/crawl_semilla_53/training_trace.jsonl` (intento parcial, no válido como política)
