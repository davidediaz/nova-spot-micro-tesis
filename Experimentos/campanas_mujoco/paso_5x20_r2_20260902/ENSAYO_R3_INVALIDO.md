# Ensayo `paso_r3` inválido

La bolsa contiene 683 fases y 691.518 mensajes, pero no registró ninguna orden
en `/nova/gait_command`. Sin los marcadores `paso` y `stand` no es posible
delimitar de forma trazable la ventana válida. Se conserva únicamente como
evidencia del fallo de automatización y no entra en el resumen de campaña.

El mismo proceso MuJoCo se reinició entre ensayos y produjo retrocesos de
`/clock`. El ejecutor se corrigió para iniciar una instancia aislada por ensayo,
comprobar suscriptores y publicar marcadores redundantes antes de continuar.
