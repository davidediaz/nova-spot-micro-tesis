# PPO residual: entrenamiento preparatorio

- Semillas: (11, 23, 37, 53, 71).
- Episodios por semilla: 180.
- Entorno: dinámica cinemática reducida, sin Gazebo y sin contacto resuelto.
- Acciones: 12 correcciones, limitadas a ±0,08 rad y 0,02 rad por paso.

La comparación nominal/PPO se incluye como verificación del contrato y del flujo de entrenamiento. No constituye todavía una comparación de estabilidad en Gazebo; esa etapa requiere conectar la política a observaciones reales del simulador y repetir el protocolo de cinco ensayos.