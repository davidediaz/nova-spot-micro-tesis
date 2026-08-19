# Registro del ensayo de gateo nominal

## Identificación

- Fecha: 14 de agosto de 2026.
- Hora local: 09:25:40--09:28:34, America/Bogota.
- Simulador: Gazebo Sim con ROS 2 Humble.
- Bolsa: `linea_base_gateo_limpia_20260814_0925`.
- Formato: rosbag2, almacenamiento SQLite3.
- Tamaño: 96,4 MiB.
- Duración total de la bolsa: 174,227692248 s.
- Mensajes almacenados: 83.442.

## Configuración congelada

- Marcha: `gateo` / `crawl` cartesiano.
- Muestras por ciclo: 24.
- Duración por muestra: 0,18 s.
- Duración nominal del ciclo: 4,32 s.
- Longitud de paso: 0,018 m.
- Elevación del pie: 0,014 m.
- SHA-256 de `gaits.yaml`:
  `0772d57faab20f8da50176f4e94fc9d885e618211e230c34511c18256a71990a`.

No se modificaron el paso, la altura ni la velocidad durante el ensayo.

## Ventana válida de gateo

- Orden `gateo`: 1786717589,075082956 s (tiempo Unix del mensaje).
- Orden `stand`: 1786717688,053851987 s.
- Duración continua: 98,978769031 s.
- Ciclos ejecutados completos: 20, delimitados mediante grupos de 24
  referencias articulares.
- Duración observada media por ciclo: 4,797996 s.
- Muestras de métricas dentro de la ventana: 5.813.
- Activaciones del supervisor: 0.

Se supera el requisito de al menos diez ciclos continuos. Aunque la duración
configurada era 4,32 s, las referencias se publicaron aproximadamente cada
0,20 s y el ciclo observado fue de 4,797996 s. Por ello se cuentan grupos
completos de 24 referencias registradas.

## Resumen observado en la ventana válida

| Magnitud | Inicio | Final | Mínimo | Máximo |
|---|---:|---:|---:|---:|
| x (m) | -0,001811 | 0,493510 | -0,014817 | 0,493510 |
| y (m) | 0,000000 | 0,005190 | -0,009581 | 0,013473 |
| altura (m) | 0,222356 | 0,224245 | 0,222356 | 0,224272 |
| roll (grados) | 0,000000 | 0,020540 | -2,255451 | 2,255240 |
| pitch (grados) | 0,027241 | 0,015405 | -4,412489 | 0,391404 |

Estos valores son un control preliminar de integridad. El análisis por ciclo y
las gráficas deben generarse en el siguiente paso del protocolo.

## Tópicos registrados

- `/clock`
- `/joint_states`
- `/dynamic_joint_states`
- `/joint_trajectory_controller/controller_state`
- `/joint_trajectory_controller/joint_trajectory`
- `/nova/gait_command`
- `/nova/metrics/diagnostics`
- `/nova/metrics/json`
- `/nova/safety/triggered`
- `/tf`
- `/tf_static`
- `/world/empty/dynamic_pose/info`

El tópico `controller_state` no produjo mensajes y el tópico de seguridad tuvo
cero mensajes porque el supervisor no se activó. Las órdenes de inicio y cierre
sí quedaron almacenadas.

## Integridad y reproducción

SHA-256 de la base de datos:

`d4a7b5dd7780170591537ef560d106ad99a36629164bb091ce0d61573526b772`

Comando de inspección:

```bash
source /opt/ros/humble/setup.bash
ros2 bag info linea_base_gateo_limpia_20260814_0925
```

Comando de reproducción:

```bash
source /opt/ros/humble/setup.bash
ros2 bag play linea_base_gateo_limpia_20260814_0925 --clock
```

## Incidencia descartada

Antes de este ensayo se generó `linea_base_gateo_20260814_0918`, pero se
detectaron dos instancias simultáneas de los nodos de control, métricas,
supervisión y puente. Esa bolsa se conserva únicamente como evidencia de la
incidencia y no debe utilizarse como resultado experimental. La presente bolsa
se grabó después de confirmar exactamente una instancia de cada nodo.
