# Validación de la marcha paso

Fecha: 14 de agosto de 2026.

## Gazebo

Se ejecutaron dos ensayos independientes de 12 ciclos completos cada uno, con
los mismos parámetros y cero activaciones del supervisor.

En régimen permanente, ciclos 2--12, el primer ensayo obtuvo:

- ciclo: 5,759993 s;
- avance: 0,022031 m/ciclo;
- velocidad: 0,003825 m/s;
- excursión lateral: 0,005438 m;
- altura: 0,224125 m;
- roll máximo: 1,281777 grados;
- pitch máximo: 2,483731 grados;
- salto articular máximo: 0,008349 rad.

La repetición difirió 0,000 % en duración, -0,136 % en avance y velocidad,
-0,399 % en excursión lateral, 0,000 % en altura, 0,003 % en roll, 0,004 % en
pitch y 0,161 % en salto articular. Todas las diferencias de medias fueron
inferiores al 0,4 %.

Archivos:

- `Experimentos/rosbag2/paso_linea_base_20260814`;
- `Experimentos/rosbag2/paso_repeticion_20260814`;
- `Experimentos/comparacion_paso_20260814`.

## MuJoCo

Se ejecutaron 12 ciclos completos en modo headless:

- ciclo medio: 5,759999 s;
- error RMS articular medio: 0,026232 rad;
- error máximo absoluto: 0,054983 rad;
- 384 referencias analizadas;
- 7.929 estados articulares;
- 57.472 mensajes en la bolsa.

Archivos:

- `Experimentos/rosbag2/paso_mujoco_20260814`;
- `Experimentos/analisis/paso_mujoco_20260814`;
- `Experimentos/analizar_mujoco_articulaciones.py`.

## Integridad

- Gazebo base: `77661f37b9fa2f6b7cef0e4fb2da4d0f1f4468c86ce500ccecbd7a674cd26a20`.
- Gazebo repetición: `88b697e1fc7cb5167b2ef93f2e3cb088df3826546364d1ebbf9b07105c36bcd4`.
- MuJoCo: `e64611393e7cf589b784377ef1fc15f465f3430fc2ad13e9a16f319e4d379094`.

## Alcance de la conclusión

Gazebo valida pose corporal, seguridad y reproducibilidad. MuJoCo valida
cadencia y seguimiento articular. La configuración actual de MuJoCo no publica
una pose corporal equivalente a `/world/empty/dynamic_pose/info`; por ello no se
comparan todavía avance, altura, roll ni pitch entre simuladores. Esta limitación
debe conservarse en la tesis.
