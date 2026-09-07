# Validación articular de marcha paso

- Bolsa: `Experimentos/campanas_mujoco/validacion_grupos_2x2_20260903/rosbag2/paso_r2`.
- Ciclos completos: 3.
- Duración media: 5.759994 s.
- Error RMS articular medio: 0.010530 rad.
- Error máximo absoluto: 0.028339 rad.

El error se evalúa cerca del final de `time_from_start` de cada referencia, comparando los doce objetivos con `/joint_states`. El ciclo 1 se conserva como transitorio; las medias usan los ciclos 2 en adelante.

La evaluación usa el mismo contrato de referencias y estados articulares en ambos simuladores.