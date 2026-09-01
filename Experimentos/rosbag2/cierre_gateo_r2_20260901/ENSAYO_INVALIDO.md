# Ensayo inválido — repetición 2 de gateo

La bolsa se conserva para trazabilidad, pero no cuenta como repetición válida.
El comando `gateo` se publicó antes de que el `gait_controller` y los
controladores de trayectoria terminaran de activarse. Como consecuencia, la
bolsa contiene cero mensajes de `/nova/gait_phase` y una sola trayectoria; el
analizador no puede formar un ciclo completo.

No se extraen métricas ni se presenta este ensayo como resultado. La causa
operativa queda corregida para la próxima ejecución: verificar con
`ros2 node list` la presencia de `/gait_controller`,
`/joint_trajectory_controller`, monitores y supervisor, esperar la confirmación
de suscriptores, iniciar la grabación y publicar el comando solo después.
