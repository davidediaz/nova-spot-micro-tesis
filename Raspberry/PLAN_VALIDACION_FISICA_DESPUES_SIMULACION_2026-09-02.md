# Plan de validación física posterior a las pruebas simuladas

Estado: inventario de requisitos; no autoriza energizar ni ejecutar marchas.

## Estado confirmado

- Raspberry Pi 4 con Ubuntu 22.04.5, ROS 2 Humble, SSH y DDS por Wi-Fi.
- PCA9685 detectado en `0x40`; hubo movimiento limitado previo de CH5--CH10.
- Dos servos fueron sustituidos y los acoples reforzados después de esa prueba.
- No existe calibración válida de la configuración mecánica actual.
- Faltan trazabilidad CH0--CH11, parada por OE con pull-up, medición de fuente
  bajo carga e identificación completa del ejemplar.

## Puertas obligatorias, en orden

### F0 — Ensamble e inspección sin energía

- Montar e inspeccionar la tapa izquierda de fémur.
- Identificar los dos servos sustituidos y los acoples reforzados.
- Revisar topes, rozamientos, tornillos, holgura, cableado y rango manual.
- Trazar CH0--CH11 y completar fotografías F01--F22 con hashes.
- Medir tres veces geometría y masa según el protocolo existente.

Salida: ficha y CSV completos; decisión trazable sobre URDF/MJCF.

### F1 — Seguridad eléctrica sin servos

- Verificar esquema, polaridad y tierra común.
- Medir VCC, V+ y salida del LM2596; registrar instrumento y resolución.
- Instalar fusible o limitación dimensionada y parada física accesible.
- Mantener OE alto mediante pull-up durante arranque, reinicio y pérdida del
  controlador; comprobarlo con instrumento.
- Comprobar PWM con carga desconectada; los canales deben iniciar `FULL_OFF`.

Salida: lista de seguridad firmada, fotografías y mediciones. Sin esto no se
conecta un servo.

### F2 — Calibración individual

- Probar un servo sin carga y después un canal montado con pata suspendida.
- Para CH0--CH11 medir centro, sentido, mínimos y máximos seguros, zona muerta,
  velocidad, repetibilidad y corriente.
- Calibrar desde cero los dos reemplazos.
- Fijar límites conservadores antes de escribir la configuración de control.

Salida: `Raspberry/configuracion/calibracion_servos.csv` completo y revisado.

### F3 — Integración progresiva

- Probar una pata suspendida y luego cuatro patas con el robot suspendido.
- Verificar pérdida de comunicación y parada por OE antes de apoyar el robot.
- Probar postura con soporte, transferencia, un paso, un ciclo y solo después
  ciclos continuos.
- Registrar tensión, corriente, orientación, temperatura disponible,
  intervención y desplazamiento externo.

Salida: marcha nominal física repetible bajo el protocolo aprobado.

### F4 — Instrumentación y contraste del modelo

- Integrar primero BNO055 y monitor de potencia dimensionado.
- Seleccionar y validar un contacto por pie.
- Prototipar un AS5600 en una articulación y tres mediante TCA9548A en una pata
  antes de considerar doce sensores.
- Actualizar URDF, MJCF y parámetros solo con mediciones aceptadas.

## Bloqueos actuales

No se puede iniciar F2 mientras F0 y F1 estén incompletas. Tampoco se autoriza
PPO, marcha de doce servos ni prueba sobre el suelo antes de cerrar calibración,
rearme/parada segura y validación nominal progresiva.
