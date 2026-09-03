# Validación corta inválida

La prueba capturó nueve marcadores, pero el controlador de marcha todavía no
estaba suscrito cuando se publicó `paso`. La bolsa contiene cero fases y solo
cuatro referencias de `stand`, por lo que no entra en resultados.

La automatización se corrigió para exigir dos suscriptores en
`/nova/gait_command` (grabador y controlador) antes de iniciar el ensayo.
