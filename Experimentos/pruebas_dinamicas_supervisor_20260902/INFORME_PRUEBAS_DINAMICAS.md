# Pruebas dinámicas provocadas del supervisor — 2 de septiembre de 2026

## Objetivo y criterio

Se ejecutaron nueve procesos aislados ROS 2, uno por escenario, sin Gazebo ni
hardware. Cada ejecución usó un supervisor nuevo y tópicos de prueba separados.
El criterio exigió `triggered=true`, el motivo exacto en el estado y la orden
`stand`.

## Resultados

| Escenario | Estímulo | Motivo observado | Resultado |
|---|---|---|---|
| Margen | -0,20 m | `margen_estabilidad` | Aprobado |
| Contacto | falta RL | `perdida_contacto` | Aprobado |
| Timeout | sin pose, contacto ni estabilidad | `datos_vencidos:pose,contacts,stability` | Aprobado |
| Altura baja | 0,10 m | `altura_baja` | Aprobado |
| Altura alta | 0,36 m | `altura_alta` | Aprobado |
| Roll | 30 grados | `roll` | Aprobado |
| Pitch | 30 grados | `pitch` | Aprobado |
| Límite articular | coxa a 0,70 rad | `limite_articular` | Aprobado |
| Discontinuidad | salto de coxa de 0,40 rad | `discontinuidad_articular` | Aprobado |

El validador terminó con `9 escenarios dinámicos aprobados`. La suite
determinista, ejecutada después de recompilar, terminó con `79 passed`.

## Incidencia y corrección

La primera ejecución reveló que `safety_test_node` intentaba cerrar ROS 2 desde
su callback de temporizador y podía quedar bloqueado. Se cambió a una bandera
atendida por el bucle principal. El primer timeout, con gracia cero, se activó
antes de que el nodo de evidencia descubriera los tópicos; se repitió con 2 s
de gracia y quedó aprobado. Esos intentos iniciales no son resultados finales.

## Reproducibilidad y alcance

La campaña se reproduce con `ejecutar_pruebas_dinamicas_supervisor.sh`; el
validador comprueba los tres criterios y GitHub Actions la ejecuta después de
la suite unitaria. Los JSON y logs de esta carpeta son la evidencia.

Esto valida la integración ROS 2 y la salida enclavada a `stand` ante estímulos
controlados. No demuestra detección durante una caída física, eficacia mecánica
de `stand`, corte eléctrico por OE ni ausencia de falsos positivos en campañas
largas. El rearme seguro sigue pendiente y contacto, margen y timeout
permanecen deshabilitados por defecto.
