# Prueba inicial de coxas — 15 de septiembre de 2026

Se probó el movimiento manual de las cuatro coxas con el robot elevado y el
PCA9685 alimentado desde la fuente externa de servos.

## Resultado

- `CH0` — Pata 1, delantera derecha: se movió hacia afuera mientras las otras
  coxas se movían hacia adentro. Se registró inversión de sentido (`direction:
  -1`) para `front_right_coxa_joint`.
- `CH1` — Pata 2, delantera izquierda: respuesta correcta.
- `CH2` — Pata 3, trasera derecha: respuesta correcta.
- `CH3` — Pata 4, trasera izquierda: respuesta correcta.

Las cuatro articulaciones permanecen sin calibrar. Todavía deben medirse centro,
sentido, límites PWM, velocidad, corriente y torque antes de habilitar una
marcha ROS 2.

## Siguiente prueba

Probar los fémures `CH4`–`CH7`, uno por uno, con recorrido reducido.

## Resultado de fémures

- `CH4` — Pata 1, delantera derecha: se movió hacia adelante mientras las
  otras patas se movían hacia atrás. Se registró inversión de sentido
  (`direction: -1`) para `front_right_femur_joint`.
- `CH5` — Pata 2: respuesta hacia atrás.
- `CH6` — Pata 3: respuesta hacia atrás.
- `CH7` — Pata 4: respuesta hacia atrás.

Los cuatro fémures siguen sin calibración de límites.

## Siguiente prueba

Probar las tibias `CH8`–`CH11`, una por una, con recorrido reducido.

## Resultado de tibias

- `CH8` — Pata 1, delantera derecha: se movió hacia adelante. Se registró
  inversión de sentido (`direction: -1`) para `front_right_tibia_joint`.
- `CH9` — Pata 2: se movió hacia atrás.
- `CH10` — Pata 3: se movió y regresó al punto inicial; la prueba termina
  centrando cada servo, por lo que el resultado es correcto.
- `CH11` — Pata 4: se movió hacia atrás.

Las doce articulaciones ya respondieron a la prueba manual. Todas siguen sin
calibración completa de centro, límites, velocidad, corriente y torque.
