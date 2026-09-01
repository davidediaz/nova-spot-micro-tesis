# Pruebas provocadas del supervisor — contrato sin ROS 2

Se verificó de forma automática el contrato lógico de las entradas del
supervisor antes de activar todas las paradas en simulación integrada.

| Condición provocada | Respuesta exigida | Estado |
|---|---|---|
| Altura inferior y superior al intervalo | `altura_baja` / `altura_alta` | Aprobada |
| Roll o pitch superior al umbral | `roll` / `pitch` | Aprobada |
| Pose NaN o infinita | `pose_no_finita` | Aprobada |
| Referencia NaN o infinita | `referencia_no_finita` | Aprobada |
| Articulación fuera del límite | `limite_articular` | Aprobada |
| Fuente ausente, vencida o con tiempo NaN | identificación de la fuente | Aprobada |
| Contacto observado distinto del previsto | `contactos_no_coinciden` | Aprobada |
| Margen negativo o no finito | `margen_estabilidad` / `margen_no_finito` | Aprobada |

La suite completa alcanzó 73 pruebas aprobadas. Estas son pruebas unitarias de
la decisión y no demuestran todavía publicación de `stand`, enclavamiento y
registro durante una ejecución de Gazebo. Por esa razón las paradas de timeout,
contacto y margen permanecen desactivadas en `monitoring.yaml` hasta realizar
ensayos integrados y cuantificar falsos positivos.
