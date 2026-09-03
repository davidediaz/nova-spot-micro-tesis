# Validación corta inválida

La consulta de introspección `ros2 topic info` usada como barrera de arranque
quedó bloqueada y no se alcanzó a publicar ninguna orden. La bolsa contiene
cero comandos, fases y referencias de marcha; no entra en resultados.

La barrera se sustituyó por la confirmación explícita en logs del controlador
listo y de las suscripciones del grabador.
