# Contrato preparado para aprendizaje por refuerzo residual

Se implementó el contrato independiente de simulador para una política que
solo corrige la marcha nominal. La acción tiene doce correcciones articulares,
limitadas a ±0,08 rad y a variaciones de 0,02 rad por paso. Después se aplican
los límites articulares del supervisor; la política nunca produce PWM.

La recompensa penaliza inclinación, error de altura, error articular y magnitud
de la corrección. Una activación del supervisor añade una penalización de 100.
El episodio termina por supervisor, altura fuera de 0,16--0,32 m, roll/pitch
superior a 0,35 rad o estado no finito.

Las pruebas verifican límites de amplitud y velocidad, rechazo de NaN,
preservación de límites articulares, preferencia de recompensa y todas las
terminaciones. Esto prepara la interfaz segura, pero todavía no constituye un
entorno dinámico conectado a Gazebo/MuJoCo ni una política entrenada. OE4 sigue
sin resultado experimental hasta implementar observaciones sincronizadas,
dinámica de paso, aleatorización, entrenamiento con semillas 11, 23, 37, 53 y
71, y evaluación separada.
