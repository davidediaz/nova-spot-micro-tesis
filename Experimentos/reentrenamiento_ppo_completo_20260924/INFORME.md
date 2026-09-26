# Campaña PPO completa — 24 de septiembre de 2026

## Alcance

Se reentrenaron las dos caminatas del cuadrúpedo, `crawl` (gateo) y `step`
(paso), con las semillas `11, 23, 37, 53, 71` en MuJoCo y Gazebo. Todas las
corridas son exclusivamente de simulación; `hardware_transfer` permanece en
`false`.

La geometría usada en ambos entrenadores es la medida del prototipo:

| Parámetro | Valor |
| --- | ---: |
| Coxa | 0,0381 m |
| Fémur | 0,10795 m |
| Tibia | 0,13589 m |
| Separación de caderas X/Y | 0,180 / 0,120 m |
| Cuerpo L/W/H | 0,230 / 0,120 / 0,075 m |

El contrato RL es idéntico: 27 observaciones, 12 acciones, residual máximo de
`±0,08 rad` y cambio máximo de `±0,02 rad` por paso.

## Artefactos

- `mujoco/<marcha>_semilla_<n>/policy.zip`: 50.176 pasos efectivos por
  política (50.000 solicitados, completando el rollout de PPO de 1.024).
- `gazebo/<marcha>_semilla_<n>/policy.zip`: 1.024 pasos efectivos por
  política, sincronizados con Gazebo mediante ROS 2.
- `mujoco_evaluation.csv`: 5 episodios nominales y 5 PPO por política de
  MuJoCo, sin randomización durante la evaluación.
- `gazebo_evaluation.csv`: 1 episodio nominal y 1 PPO por política Gazebo;
  esta primera evaluación se usa como diagnóstico, no como aceptación
  estadística.
- `campaign_manifest.json`: semillas, pasos, geometría y bloqueo de hardware.

## Evaluación MuJoCo

Promedio sobre las cinco semillas:

| Marcha | Condición | Retorno | Avance (m) | Inclinación máxima (rad) |
| --- | --- | ---: | ---: | ---: |
| Gateo | nominal | 1091,31 | 0,4917 | 0,00993 |
| Gateo | PPO | 1086,42 | 0,4598 | 0,02390 |
| Paso | nominal | 1451,30 | 0,0155 | 0,01392 |
| Paso | PPO | 1447,13 | 0,1534 | 0,02406 |

La selección conservadora para continuar validación offline es `crawl` semilla
53 (avance 0,4799 m, inclinación 0,01178 rad) y `step` semilla 71 (avance
0,1553 m, inclinación 0,01424 rad). No son candidatas para hardware: la
recompensa PPO promedio baja frente a la nominal y el gateo no mejora el
avance promedio.

## Evaluación Gazebo y limitaciones

La matriz de 10 políticas terminó correctamente y dejó sus trazas en cada
directorio. El presupuesto de 1.024 pasos es una campaña de interacción y
robustez, no una convergencia final: los episodios de varias semillas
terminaron por inestabilidad antes de completar los cinco ciclos.

La evaluación emparejada de un episodio por condición promedió:

| Marcha | Condición | Retorno | Avance (m) | Inclinación máxima (rad) |
| --- | --- | ---: | ---: | ---: |
| Gateo | nominal | 108,54 | -0,0164 | 0,03881 |
| Gateo | PPO | 94,93 | -0,0942 | 0,04459 |
| Paso | nominal | 139,28 | -0,0662 | 0,01440 |
| Paso | PPO | 110,49 | -0,0638 | 0,01316 |

Los episodios Gazebo no activaron la bandera de terminación del entorno, pero
varias carreras duraron menos fases por la dinámica y el supervisor. La caída
de retorno PPO frente a nominal impide seleccionar una política Gazebo.

Durante la primera corrida se detectó y corrigió un defecto en el puente ROS:
la acción de `/nova/rl_action` era limitada, pero no se sumaba a la trayectoria
nominal. Esa primera corrida fue interrumpida y no se usa; todas las políticas
conservadas aquí se generaron después de corregir `ppo_residual_node.py`.

Por lo anterior, no se declara todavía una política Gazebo aceptada. El
siguiente entrenamiento debe aumentar el presupuesto de Gazebo y repetir la
evaluación con varios episodios por semilla antes de escoger un modelo.

## Verificación y seguridad

- Suite ROS/Python: `99 passed`.
- `check_env` de MuJoCo: aprobado.
- Paquetes ROS 2: compilación aprobada.
- No se ejecutaron PWM, SSH, Raspberry Pi ni servos.
- Ninguna política debe transferirse al hardware hasta cerrar calibración,
  alimentación, PCA9685, vigilancia y pruebas físicas controladas.

## Reentrenamiento largo de las candidatas seleccionadas

Después de la campaña inicial se hizo adaptación PPO desde MuJoCo hacia Gazebo
para las candidatas gateo semilla 53 y paso semilla 71. Cada una completó
20.480 pasos efectivos (20.000 solicitados, rollout de 1.024), con checkpoint
cada 2.048 pasos. Los parámetros finales están en:

- `reentrenamiento_ppo_largo_20260924/gazebo/crawl_semilla_53/policy.zip`
- `reentrenamiento_ppo_largo_20260924/gazebo/step_semilla_71/policy.zip`

La validación final de tres episodios por condición produjo:

| Marcha | Condición | Retorno | Avance (m) | Inclinación máxima (rad) |
| --- | --- | ---: | ---: | ---: |
| Gateo | nominal | 119,41 | 0,1143 | 0,06659 |
| Gateo | PPO largo | 115,56 | 0,1276 | 0,06421 |
| Paso | nominal | 159,75 | 0,0933 | 0,04462 |
| Paso | PPO largo | 154,04 | 0,0312 | 0,04639 |

El gateo largo mejora el avance y reduce ligeramente la inclinación, aunque
reduce el retorno; queda como candidato offline para una evaluación posterior.
El paso largo no se acepta aún porque pierde avance frente al nominal. Ninguna
política se envió al hardware.
