# Torque y velocidad de los MG996R

El MG996R es un servo posicional convencional. La señal PWM solicita una
posición; no incluye una orden independiente de torque o velocidad y tampoco
devuelve esas mediciones.

Para este proyecto:

- la velocidad máxima por articulación se medirá con un servo asegurado y se
  limitará interpolando las referencias de posición;
- el torque se estimará con el modelo dinámico y corriente medida, o se medirá
  con instrumentación externa;
- `torque_limit_nm` será un umbral del supervisor, no una orden enviada al
  MG996R;
- no se habilitarán los doce canales mientras existan celdas vacías en
  `configuracion/calibracion_servos.csv` o valores `null` en `servos.yaml`.

La identificación debe hacerse primero sin carga, luego con carga controlada y
un único servo mecánicamente asegurado. No deben copiarse valores de catálogo
como si fueran mediciones del ejemplar físico.

