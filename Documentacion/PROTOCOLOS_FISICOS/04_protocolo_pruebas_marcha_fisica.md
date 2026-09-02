# Progresión de pruebas físicas

No ejecutar gateo ni paso hasta cerrar las etapas anteriores y disponer de un
observador de parada física.

| Nivel | Prueba | Duración máxima | Evidencia | Criterio de avance |
|---|---|---:|---|---|
| P0 | OE, fuente y PWM sin servos | 60 s | vídeo y multímetro | corte inmediato verificado |
| P1 | Un servo asegurado | 3 ciclos | corriente/temperatura | sin atasco ni sobrecorriente |
| P2 | Una pata suspendida | 3 ciclos | ángulos y holgura | límites y sentido correctos |
| P3 | Robot suspendido | 5 ciclos de postura | vídeo y log ROS | doce canales confirmados |
| P4 | Postura en suelo con soporte | 10 s | IMU, corriente y vídeo | inclinación dentro del umbral |
| P5 | Paso de 1 ciclo | 1 ciclo | rosbag2 completo | parada y contactos coherentes |
| P6 | Gateo progresivo | 3→5→20 ciclos | rosbag2 y métricas | revisión posterior de seguridad |

La primera marcha física usa velocidad reducida y sin PPO. La política residual
solo se considerará después de caracterizar el robot y repetir la línea base.
