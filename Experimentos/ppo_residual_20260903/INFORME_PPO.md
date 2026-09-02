# PPO residual: reentrenamiento con observaciones físicas

- Semillas: (11, 23, 37, 53, 71).
- Episodios por semilla: 180.
- Observación: roll/pitch, altura, acelerómetro, giróscopo, cuatro contactos, 12 articulaciones y fase.
- Recompensa: estabilidad, altura, continuidad, avance y penalización de acción.
- Acciones: 12 correcciones, limitadas a ±0,08 rad y 0,02 rad por paso.

El entrenamiento sigue siendo un banco reducido sin contacto resuelto de Gazebo; sirve para seleccionar políticas antes de la validación dinámica.