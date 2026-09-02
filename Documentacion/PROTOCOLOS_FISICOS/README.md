# Paquete de preparación física

Este paquete reúne los formatos que se diligenciarán cuando el robot esté
disponible. Ningún formato autoriza energizarlo por sí solo. La secuencia
obligatoria es: inspección sin energía → pruebas eléctricas → un servo
asegurado → una pata suspendida → robot suspendido → suelo con soporte y
parada accesible.

## Archivos

- `01_protocolo_puesta_en_marcha.md`: lista de seguridad y criterios de aborto.
- `02_protocolo_calibracion_servos.md`: centro, sentido, límites PWM y prueba
  de velocidad/corriente por canal.
- `03_protocolo_identificacion_masas.md`: masas, centro de masa e inercia.
- `04_protocolo_pruebas_marcha_fisica.md`: progresión postura–pata–robot.
- `calibracion_servos_fisica.csv`: una fila por cada MG996R.
- `identificacion_masas_fisica.csv`: plantilla de mediciones repetidas.
- `pruebas_servos_fisica.csv`: registro de corriente, temperatura y fallos.

Las columnas vacías significan pendiente, nunca cero. Cada medición debe tener
fecha, instrumento, resolución, responsable y evidencia fotográfica o archivo
de registro.
