# Protocolo de perturbaciones en simulación

## Ejecutado

`perturbaciones_nominales_20260902/sensibilidad_dinamica.csv` contiene 14
escenarios de dinámica inversa para gateo y paso. Se variaron masas globales
±10 %, amortiguamiento ±50 % y fricción articular ±50 %. La mayor variación
del par máximo fue -8,997 % (paso con masa -10 %). Este resultado no incluye
contacto ni movimiento del cuerpo.

## Pendiente de integración Gazebo

- Fricción suelo: variar el coeficiente del plano en ±25 % y ±50 %.
- Empuje: aplicar impulsos horizontales de 1, 2 y 3 N durante 0,10 s en fases
  de apoyo y oscilación.
- Ruido: inyectar ruido gaussiano reproducible en IMU y contactos, con semilla
  registrada.
- Retardo: añadir 20, 50 y 100 ms a pose, IMU y contactos.

Cada condición debe ejecutarse con la configuración de precarga 2,0, registrar
18 ciclos y medir recuperación, roll/pitch, margen, contactos y activaciones.
Hasta disponer de estos inyectores, no se declara estabilidad ante
perturbaciones.
