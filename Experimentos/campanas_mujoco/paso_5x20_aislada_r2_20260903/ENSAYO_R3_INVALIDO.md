# Ensayo `paso_r3` inválido

Las repeticiones `paso_r1` y `paso_r2` son válidas, con 21 ciclos completos y
672 referencias cada una. `paso_r3` registró la marcha, pero perdió el marcador
final `stand` y no puede delimitarse de forma trazable.

La auditoría encontró procesos hijos de campañas anteriores que sobrevivieron
al cierre del proceso padre `ros2 launch`. Estas instancias produjeron nodos
duplicados y retrocesos de reloj. Los grupos huérfanos fueron identificados y
detenidos; el ejecutor se corrigió para crear una sesión independiente y
señalizar todo su grupo de procesos al cerrar.
