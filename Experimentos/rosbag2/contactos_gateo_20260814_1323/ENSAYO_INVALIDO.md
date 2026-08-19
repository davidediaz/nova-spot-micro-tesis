# Ensayo no válido para cuantificar retardos

La bolsa conserva 21 ciclos completos y demuestra que los sensores crudos
funcionan, pero no debe usarse para estimar coincidencia ni retardos.

Gazebo entregó más de 400.000 actualizaciones consolidadas en la ventana. La
cola fiable del monitor acumuló datos antiguos y retrasó la recepción de
`/nova/gait_phase`: el diagnóstico solo alternó dos de las cuatro patas aunque
el tópico de fase contenía la secuencia completa. El análisis reveló el defecto
y motivó QoS `best effort` con profundidad 1 y limitación de salida a 100 Hz.

La bolsa se conserva como trazabilidad del diagnóstico. El ensayo válido debe
ser una repetición posterior a esa corrección y no necesita guardar los cuatro
flujos crudos de alta frecuencia.
