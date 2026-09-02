# Validación articular de marcha paso en MuJoCo

- Bolsa: `Experimentos/rosbag2/cierre_paso_r1_20260901`.
- Ciclos completos: 21.
- Duración media: 5.760000 s.
- Error RMS articular medio: 0.008468 rad.
- Error máximo absoluto: 0.043400 rad.

El error se evalúa cerca del final de `time_from_start` de cada referencia, comparando los doce objetivos con `/joint_states`. El ciclo 1 se conserva como transitorio; las medias usan los ciclos 2 en adelante.

MuJoCo no publica todavía una pose corporal equivalente al puente de Gazebo; por ello esta validación demuestra ejecución temporal y seguimiento articular, no estabilidad corporal cuantitativa.