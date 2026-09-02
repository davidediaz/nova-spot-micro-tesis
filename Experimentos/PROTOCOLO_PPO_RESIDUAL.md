# Protocolo de preparación PPO residual

La política futura recibirá el estado de fase, pose, orientación, velocidades,
contactos y margen de estabilidad, y producirá una corrección de 12
articulaciones. La corrección se limita a ±0,08 rad y a 0,02 rad por paso,
seguida de saturación en límites articulares. La terminación se activa por
altura insegura, inclinación, estado no finito o supervisor enclavado.

La línea base para comparar será la misma marcha, semilla, duración y ventana
de ciclos que el ensayo nominal. Se entrenó una política preparatoria en un
entorno cinemático reducido con las cinco semillas fijadas. Esta evidencia
verifica el flujo PPO y las restricciones, pero no sustituye la conexión a
Gazebo ni la comparación final de estabilidad; ambas permanecen pendientes.
