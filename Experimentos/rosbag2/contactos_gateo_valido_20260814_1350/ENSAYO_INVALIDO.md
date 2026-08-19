# Ensayo no válido para retardos por omisión de fases en el monitor

La bolsa contiene 14 ciclos completos, los tópicos de salida bajaron a unos
100 Hz y `/nova/gait_phase` conserva correctamente FL--RR--FR--RL. Sin embargo,
el ejecutor de un solo hilo del monitor siguió priorizando callbacks de contacto
y el diagnóstico procesó solo las ventanas de FL y FR.

Se conserva como evidencia del segundo hallazgo. La corrección posterior separa
fase y contactos en grupos de callbacks distintos y usa un ejecutor de dos
hilos. Los porcentajes producidos para esta bolsa no son resultados válidos.
