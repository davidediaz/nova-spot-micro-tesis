# Auditoría de perfiles emparejados Gazebo--MuJoCo

| Perfil | Masa Gazebo (kg) | Masa MuJoCo (kg) | Par efectivo (N m) | Velocidad sin carga (rad/s) | Auditoría |
|---|---:|---:|---:|---:|:---:|
| nominal | 2,720 | 2,720 | 1,078732 | 6,981317 | aprobada |
| realistic_provisional | 2,992 | 2,992 | 0,683808 | 6,368921 | aprobada |
| low_mass_low_friction | 2,448 | 2,448 | 0,903328 | 6,981317 | aprobada |

La auditoría también comprueba amortiguamiento, fricción articular, fricción de
suelo y esfuerzo de las doce articulaciones. El perfil realista provisional se
cargó realmente en Gazebo: se creó la entidad, se inicializaron las doce
articulaciones y se activaron `joint_state_broadcaster` y
`joint_trajectory_controller`. Su MJCF se cargó directamente con MuJoCo y
reportó 19 posiciones generalizadas, 18 velocidades, 12 actuadores y 7 sensores.

Esta es una comparación estructural bajo parámetros iguales. No es todavía una
comparación de locomoción: faltan los cinco ensayos de veinte ciclos por
simulador y publicar pose/contactos equivalentes desde la interfaz MuJoCo.
