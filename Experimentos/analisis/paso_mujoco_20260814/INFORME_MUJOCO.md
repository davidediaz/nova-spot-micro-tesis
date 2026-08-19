# Validación articular de marcha paso en MuJoCo

- Bolsa: `/home/pavilion/Documentos/Cuadrupedo/Experimentos/rosbag2/paso_mujoco_20260814`.
- Ciclos completos: 12.
- Duración media: 5.759999 s.
- Error RMS articular medio: 0.026232 rad.
- Error máximo absoluto: 0.054983 rad.

El error se evalúa cerca del final de `time_from_start` de cada referencia, comparando los doce objetivos con `/joint_states`. El ciclo 1 se conserva como transitorio; las medias usan los ciclos 2 en adelante.

MuJoCo no publica todavía una pose corporal equivalente al puente de Gazebo; por ello esta validación demuestra ejecución temporal y seguimiento articular, no estabilidad corporal cuantitativa.