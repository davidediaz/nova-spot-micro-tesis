# Ensayo inválido — repetición 2b de gateo

La instancia de Gazebo y los controladores estaban activos y se observaron
fases, trayectorias y métricas. Sin embargo, la bolsa registró cero mensajes de
`/nova/gait_command`; por ello no contiene los marcadores `gateo` y `stand`
necesarios para delimitar la ventana de análisis. No se extraen métricas ni
cuenta como repetición válida.

La causa probable es que `ros2 topic pub --once` esperó al suscriptor del
controlador, pero el grabador aún no había completado la suscripción al tópico.
La próxima ejecución verificará el número de suscriptores de
`/nova/gait_command` con `ros2 topic info -v` después de iniciar la bolsa y
publicará el comando más de una vez dentro de una ventana controlada, sin
reiniciar la marcha.
