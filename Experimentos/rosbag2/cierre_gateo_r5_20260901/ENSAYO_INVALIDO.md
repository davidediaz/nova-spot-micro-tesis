# Ensayo inválido — cierre de gateo sin marcador `stand`

La bolsa registró fases y 217.643 mensajes, pero no contiene una orden
`stand` posterior al `gateo`. El analizador no puede delimitar el cierre de la
ventana y por ello esta ejecución no cuenta como repetición válida ni aporta
métricas a la línea base.

La próxima ejecución mantendrá el grabador activo al menos 10 s después de
publicar `stand` y verificará con `ros2 bag info` que el conteo de órdenes
incluya tanto `gateo` como `stand` antes de aceptar el ensayo.
