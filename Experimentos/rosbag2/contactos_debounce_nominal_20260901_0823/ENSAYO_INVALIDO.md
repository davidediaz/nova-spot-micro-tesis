# Ensayo inválido: ausencia de fases de gateo

Fecha: 1 de septiembre de 2026, America/Bogota.

Esta tentativa no debe utilizarse para resultados. Aunque la bolsa almacenó
tres mensajes `gateo` y cinco mensajes `stand`, el controlador no recibió la
orden inicial: `/nova/gait_phase` contiene cero mensajes y la trayectoria solo
contiene las cinco referencias `stand` finales.

La duración total de 292,656711 s, los 179.426 mensajes y el tamaño de 138,1
MiB no constituyen evidencia de ciclos ejecutados. La causa operativa fue que
el publicador temporal detectó como suscriptor al grabador, pero no se confirmó
previamente la recepción efectiva en `gait_controller`.

Corrección para la repetición: publicar `gateo`, observar un mensaje real de
`/nova/gait_phase` con `mode=crawl` y verificar el aumento de trayectorias antes
de abrir la ventana formal. La bolsa se conserva por trazabilidad.
