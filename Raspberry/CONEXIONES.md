# Conexiones Raspberry Pi 4, PCA9685 y MG996R

## Raspberry Pi 4 hacia PCA9685

| Raspberry (pin físico) | Señal BCM | PCA9685 | Función |
|---:|---|---|---|
| 1 | 3V3 | VCC | Alimentación lógica de 3,3 V |
| 3 | GPIO2 / SDA1 | SDA | Datos I2C |
| 5 | GPIO3 / SCL1 | SCL | Reloj I2C |
| 6 | GND | GND | Tierra lógica común |
| 11 | GPIO17 | OE | HIGH apaga; LOW habilita PWM |

Se recomienda una resistencia pull-up externa de 10 kΩ entre `OE` y 3,3 V para
que las salidas permanezcan deshabilitadas durante el arranque.

## Alimentación de servos

- Fuente externa regulada de 5--6 V: positivo a `V+` del PCA9685.
- Negativo de la fuente: `GND` del PCA9685 y tierra común con Raspberry.
- No conectar `V+` al pin de 5 V de la Raspberry.
- No alimentar los servos desde `VCC`; `VCC` es solo lógica.
- Añadir fusible, parada física y cableado dimensionado después de medir
  corriente real de un MG996R asegurado.

## Conector de cada servo

- Marrón o negro: GND.
- Rojo: V+ externo de 5--6 V.
- Naranja, amarillo o blanco: señal PWM del canal.

Confirma los colores del fabricante antes de energizar.

## Canales propuestos

Estos son puertos del **PCA9685**, no pines físicos de la Raspberry. La
Raspberry envía por I2C las órdenes calculadas por el mismo generador de marcha
empleado en Gazebo; el PCA9685 produce las doce señales PWM.

| Canal | Articulación | Canal | Articulación |
|---:|---|---:|---|
| 0 | FL coxa | 6 | RL coxa |
| 1 | FL fémur | 7 | RL fémur |
| 2 | FL tibia | 8 | RL tibia |
| 3 | FR coxa | 9 | RR coxa |
| 4 | FR fémur | 10 | RR fémur |
| 5 | FR tibia | 11 | RR tibia |

FL: delantera izquierda; FR: delantera derecha; RL: trasera izquierda; RR:
trasera derecha. Los canales 12--15 quedan libres.
