# Validación articular de marcha paso en MuJoCo

- Bolsa: `Experimentos/rosbag2/equivalencia_paso_mujoco_r2_20260902`.
- Ciclos completos: 11.
- Duración media: 5.760016 s.
- Error RMS articular medio: 0.014768 rad.
- Error máximo absoluto: 0.047970 rad.

El error se evalúa cerca del final de `time_from_start` de cada referencia, comparando los doce objetivos con `/joint_states`. El ciclo 1 se conserva como transitorio; las medias usan los ciclos 2 en adelante.

MuJoCo no publica todavía una pose corporal equivalente al puente de Gazebo; por ello esta validación demuestra ejecución temporal y seguimiento articular, no estabilidad corporal cuantitativa.