# Validación articular de marcha paso

- Bolsa: `Experimentos/campanas_mujoco/barrido_ganancias_paso_20260903/kp120_kv12/rosbag2/paso_r1`.
- Ciclos completos: 5.
- Duración media: 5.760625 s.
- Error RMS articular medio: 0.003950 rad.
- Error máximo absoluto: 0.010022 rad.

El error se evalúa cerca del final de `time_from_start` de cada referencia, comparando los doce objetivos con `/joint_states`. El ciclo 1 se conserva como transitorio; las medias usan los ciclos 2 en adelante.

La evaluación usa el mismo contrato de referencias y estados articulares en ambos simuladores.