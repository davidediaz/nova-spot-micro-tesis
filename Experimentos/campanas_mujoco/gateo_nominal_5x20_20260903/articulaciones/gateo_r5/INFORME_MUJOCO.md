# Validación articular de marcha paso

- Bolsa: `Experimentos/campanas_mujoco/gateo_nominal_5x20_20260903/rosbag2/gateo_r5`.
- Ciclos completos: 21.
- Duración media: 4.319998 s.
- Error RMS articular medio: 0.010893 rad.
- Error máximo absoluto: 0.046287 rad.

El error se evalúa cerca del final de `time_from_start` de cada referencia, comparando los doce objetivos con `/joint_states`. El ciclo 1 se conserva como transitorio; las medias usan los ciclos 2 en adelante.

La evaluación usa el mismo contrato de referencias y estados articulares en ambos simuladores.