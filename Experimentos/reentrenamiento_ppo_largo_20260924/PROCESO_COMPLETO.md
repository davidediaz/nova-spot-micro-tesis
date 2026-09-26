# Proceso completo de entrenamiento PPO — Nova Spot Micro

Fecha de cierre: 24 de septiembre de 2026.

## 1. Auditoría y sincronización

- Se revisó el inventario completo del repositorio local, con 1.180 archivos
  versionados.
- Se revisaron README, ruta de trabajo, progreso semanal, protocolo PPO,
  campañas anteriores, resultados MuJoCo y documentación Gazebo.
- El remoto GitHub es `https://github.com/davidediaz/nova-spot-micro-tesis.git`.
- `origin/main` y el checkout local estaban en `9b12eea`; no había cambios
  nuevos que traer del remoto.
- Se conservaron todos los cambios locales existentes; no se hizo reset ni se
  sobrescribió trabajo previo.

## 2. Geometría conservada

| Elemento | Medida |
| --- | ---: |
| Coxa | 1,50 in = 0,03810 m |
| Fémur | 4,25 in = 0,10795 m |
| Tibia | 5,35 in = 0,13589 m |
| Separación de caderas X/Y | 0,180 / 0,120 m |
| Cuerpo largo/ancho/alto | 0,230 / 0,120 / 0,075 m |

Las medidas se centralizaron en `kinematics.py` y se reflejaron en el visor 3D,
URDF, MJCF y metadatos de entrenamiento.

## 3. Contrato de aprendizaje

- Algoritmo: PPO de Stable-Baselines3, CPU.
- Observación: 27 elementos.
- Acción: 12 correcciones articulares.
- Residual máximo: ±0,08 rad.
- Cambio máximo por paso: ±0,02 rad.
- Marchas: `crawl`/gateo y `step`/paso.
- Semillas de campaña: 11, 23, 37, 53 y 71.
- Transferencia a hardware: siempre `false`.

Dependencias aisladas usadas en `/tmp/nova_rl_deps`: Gymnasium, MuJoCo,
Stable-Baselines3, PyTorch CPU y dependencias auxiliares.

## 4. Corrección crítica de Gazebo

La primera prueba de Gazebo detectó que `/nova/rl_action` recibía y limitaba
la acción, pero no la sumaba a la trayectoria nominal. Esa corrida se detuvo y
no se utiliza.

Se corrigió `ppo_residual_node.py` para aplicar:

```text
trayectoria_corregida = trayectoria_nominal + residual_limitado
```

También se mejoró el cierre del executor ROS para tolerar interrupciones y se
regeneraron las políticas después de la corrección.

## 5. Campaña inicial completa

Se ejecutó `campana_ppo_completa.py` para las dos marchas, cinco semillas y
ambos simuladores:

- MuJoCo: 50.176 pasos efectivos por política.
- Gazebo: 1.024 pasos efectivos por política.
- Total: 20 políticas, cada una con `policy.zip`, metadatos y traza.
- Evaluación MuJoCo: cinco episodios nominales y cinco PPO por política.
- Evaluación Gazebo: un episodio nominal y uno PPO por política.

La evaluación inicial seleccionó como candidatas offline gateo semilla 53 y
paso semilla 71.

## 6. Reentrenamiento largo

Se hizo adaptación PPO desde las políticas MuJoCo seleccionadas hacia Gazebo:

| Marcha | Inicialización | Pasos solicitados | Pasos efectivos |
| --- | --- | ---: | ---: |
| Gateo | MuJoCo semilla 53 | 20.000 | 20.480 |
| Paso | MuJoCo semilla 71 | 20.000 | 20.480 |

Se guardaron checkpoints cada 2.048 pasos y se conservaron las trazas JSONL.

## 7. Validación final de tres episodios

| Marcha | Condición | Retorno | Avance (m) | Inclinación máxima (rad) |
| --- | --- | ---: | ---: | ---: |
| Gateo | nominal | 119,41 | 0,1143 | 0,06659 |
| Gateo | PPO largo | 115,56 | 0,1276 | 0,06421 |
| Paso | nominal | 159,75 | 0,0933 | 0,04462 |
| Paso | PPO largo | 154,04 | 0,0312 | 0,04639 |

Conclusión: gateo mejora el avance y reduce ligeramente la inclinación, por lo
que queda como candidato offline. Paso no se acepta todavía porque pierde
avance frente a la marcha nominal.

## 8. Archivos finales

- `gazebo/crawl_semilla_53/policy.zip`
- `gazebo/crawl_semilla_53/metadata.json`
- `gazebo/crawl_semilla_53/training_trace.jsonl`
- `gazebo/crawl_semilla_53/checkpoints/`
- `gazebo/step_semilla_71/policy.zip`
- `gazebo/step_semilla_71/metadata.json`
- `gazebo/step_semilla_71/training_trace.jsonl`
- `gazebo/step_semilla_71/checkpoints/`
- `crawl_evaluation.csv`
- `step_evaluation.csv`
- `INFORME.md`
- `campaign_manifest.json`

## 9. Verificación y seguridad

- Suite de pruebas: `99 passed`.
- `check_env` de MuJoCo: aprobado.
- Paquetes ROS 2: compilados correctamente.
- No quedaron procesos de Gazebo después de las validaciones.
- No se ejecutó PWM, SSH, Raspberry Pi ni servo físico.
- Ninguna política está autorizada para hardware hasta terminar calibración,
  alimentación, PCA9685, supervisión y pruebas físicas controladas.
