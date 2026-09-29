# Resumen de caracterización AS5600 — 28 de septiembre de 2026

## Alcance

Se conectó a la Raspberry Pi 4 por SSH con la identidad previamente verificada de `cuadrupedo-pi.local`. Durante la sesión la IP cambió de `192.168.0.101` a `172.18.81.198`; se comparó la clave SSH de la nueva IP con la conocida antes de reconectar. El repositorio Git de la Raspberry presentaba un objeto local corrupto, por lo que el lector y el YAML se copiaron directamente por SSH.

El escaneo de I2C-1 mostró PCA9685 `0x40` y TCA9548A `0x70`/`0x71`. El usuario aclaró que `0x70` canales 6--7 y `0x71` canal 2 están vacíos. Con el mapa corregido respondieron las doce rutas ocupadas. El operador movió manualmente las articulaciones con la alimentación de servos desconectada. Para cada condición se obtuvieron veinte muestras I2C. No se ordenó PWM ni marcha.

## Mapa físico confirmado

| Pata | Articulación | Variable ROS | TCA/canal |
|---:|---|---|---|
| 1 delantera derecha | Tibia | `front_right_tibia_joint` | `0x71`/0 |
| 1 | Fémur | `front_right_femur_joint` | `0x71`/1 |
| 1 | Coxa | `front_right_coxa_joint` | `0x71`/3 |
| 2 delantera izquierda | Tibia | `front_left_tibia_joint` | `0x71`/4 |
| 2 | Fémur | `front_left_femur_joint` | `0x71`/5 |
| 2 | Coxa | `front_left_coxa_joint` | `0x71`/6 |
| 3 trasera derecha | Tibia | `rear_right_tibia_joint` | `0x70`/3 |
| 3 | Fémur | `rear_right_femur_joint` | `0x70`/4 |
| 3 | Coxa | `rear_right_coxa_joint` | `0x70`/5 |
| 4 trasera izquierda | Tibia | `rear_left_tibia_joint` | `0x70`/0 |
| 4 | Fémur | `rear_left_femur_joint` | `0x70`/1 |
| 4 | Coxa | `rear_left_coxa_joint` | `0x70`/2 |

Los TCA y PCA9685 comparten I2C-1: SDA GPIO2/pin físico 3 y SCL GPIO3/pin físico 5, con tierra común.

## Resultados

Ángulos absolutos del imán, en grados de 0 a 360. La columna de rango es el máximo menos el mínimo en veinte muestras. Los nombres horario y antihorario indican el extremo manual seguro señalado por el operador.

| Articulación | TCA/canal | Referencia inicial | Horario: media (rango) | Antihorario: media (rango) |
|---|---|---:|---:|---:|
| Coxa 1 | `0x71`/3 | 266,623° (31,201°) | 309,782° (0,791°) | 112,373° (1,142°) |
| Fémur 1 | `0x71`/1 | 185,061° (0,088°) | 232,831° (0,176°) | 132,460° (0,176°) |
| Tibia 1 | `0x71`/0 | 139,570° (0,000°) | 83,672° (0,000°) | 203,379° (0,000°) |
| Coxa 2 | `0x71`/6 | 128,635° (14,326°) | 115,604° (18,633°) | 146,162° (9,580°) |
| Fémur 2 | `0x71`/5 | 255,586° (0,000°) | 299,795° (0,000°) | 288,809° (0,000°) |
| Tibia 2 | `0x71`/4 | 60,000° (0,000°) | 83,232° (0,000°) | 249,811° (0,088°) |
| Coxa 3 | `0x70`/5 | 142,866° (5,801°) | 36,290° (16,435°) | 183,863° (0,615°) |
| Fémur 3 | `0x70`/4 | 195,827° (0,088°) | 47,039° (0,088°) | 98,126° (0,176°) |
| Tibia 3 | `0x70`/3 | 330,959° (4,483°) | 300,968° (8,877°) | 37,446° (5,713°) |
| Coxa 4 | `0x70`/2 | 210,586° (0,000°) | 216,562° (0,000°) | 192,484° (0,088°) |
| Fémur 4 | `0x70`/1 | 312,979° (0,000°) | 291,797° (0,000°) | 66,006° (0,000°) |
| Tibia 4 | `0x70`/0 | 338,994° (0,000°) | 75,472° (0,088°) | 303,047° (0,000°) |

La coxa 1 tuvo otra ventana inicial de referencia con rango 25,401°; ambas lecturas iniciales muestran que esa referencia visual no es repetible todavía.

## Calidad y limitaciones

Las doce direcciones responden I2C con el mapa corregido. Las capturas de coxa 2 presentan dispersión grande en los tres estados. Coxa 3 presenta alta dispersión en referencia y extremo horario, aunque la captura antihoraria fue más estable. Tibia 3 presentó dispersión apreciable en los tres estados. Coxa 1 tuvo una referencia inicial inestable y extremos manuales comparativamente más concentrados. Las demás lecturas se mantuvieron concentradas en estas ventanas.

La variación observada puede proceder de juego o movimiento mecánico, fijación del imán/encoder, alimentación/tierra o ruido. Esta sesión no identifica la causa. Los grados son absolutos del imán y aún no expresan los ángulos articulares del modelo. El YAML `Raspberry/configuracion/as5600_caracterizacion_provisional.yaml` conserva las medias, mínimos, máximos, rangos y marcas de estabilidad por condición; el informe cronológico detallado está en `Raspberry/LECTURA_AS5600_TCA_2026-09-28.md`.

## Siguiente trabajo

Falta medir sentido y cero de cada articulación respecto al modelo, considerar el cruce circular 0°/360°, comprobar repetibilidad durante movimiento, fijar márgenes antes de topes mecánicos y resolver las señales variables antes de usarlas para realimentación. Esta caracterización no habilita control de postura, marcha ni PPO físico.
