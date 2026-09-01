# Prueba provocada del supervisor: trayectoria inválida

Fecha: 1 de septiembre de 2026. Entorno: Gazebo/ROS 2 Humble.

Se inició `demo.launch.py` nominal y se publicaron tres mensajes
`JointTrajectory` con una articulación inexistente (`bad_joint`). El controlador
rechazó los mensajes con `Joints on incoming trajectory don't match the
controller joints.` El supervisor registró `PARADA PREVENTIVA -> stand:
nombres_articulares_invalidos,articulacion_desconocida` y `gait_controller`
confirmó el cambio a `stand`.

La parada por referencia inválida quedó demostrada en integración, con
transición a postura segura. Las paradas por vencimiento de datos, contacto
inconsistente y margen de estabilidad permanecen pendientes.
