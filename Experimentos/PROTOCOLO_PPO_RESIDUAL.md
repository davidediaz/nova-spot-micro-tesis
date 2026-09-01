# Protocolo de preparación PPO residual

La política futura recibirá el estado de fase, pose, orientación, velocidades,
contactos y margen de estabilidad, y producirá una corrección de 12
articulaciones. La corrección se limita a ±0,08 rad y a 0,02 rad por paso,
seguida de saturación en límites articulares. La terminación se activa por
altura insegura, inclinación, estado no finito o supervisor enclavado.

La línea base para comparar será la misma marcha, semilla, duración y ventana
de ciclos que el ensayo nominal. Todavía no existe una política entrenada ni
una comparación nominal--PPO; este archivo fija el protocolo para no presentar
el diseño como resultado experimental.
