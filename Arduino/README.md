# Firmware de la interfaz de E/S

El microcontrolador auxiliar hace de interfaz entre el programa de control y el hardware:

- el controlador PWM PCA9685 (0x40), con 12 servos MG996R;
- el multiplexor analógico CD74HC4067, que lee los potenciómetros;
- los multiplexores I²C TCA9548A (0x70 y 0x71), que conectan los encoders AS5600.

| Carpeta | Contenido |
|---|---|
| `movimiento_suspendido_11_servos/` | **Firmware vigente** (5-nov-2026). Modos: `@` transmisión continua, `+` con coxas, `$` y `^` revisión de sensores, `b` gateo en lazo abierto y `x` apagar. Aplica topes por canal y límite de 3° por línea. El `.hex` compilado está en `Experimentos/entrenamiento_real_20261016/politicas_elegidas_20261105/`. |
| `sketches_uno_20261019/` | Versiones intermedias de octubre. |
| `diagnostico_pca9685_uno/`, `escaner_i2c_mega/`, `prueba_*` | Bocetos de diagnóstico del bus I²C y del PCA9685. |
| `sketches_home_pi/` | Bocetos de las primeras pruebas por pata. |
| `AVANCES_PCA9685_2026-08-24.md` | Notas de las primeras pruebas. |

Para cargarlo, se compila con `arduino-cli compile --fqbn arduino:avr:uno --output-dir build .` y se sube con
`avrdude -p atmega328p -c arduino -P /dev/ttyACM0 -b 115200 -D -U flash:w:build/movimiento_suspendido_11_servos.ino.hex:i`.
