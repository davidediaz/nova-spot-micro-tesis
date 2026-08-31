# Ficha de caracterización física sin energizar

Fecha de ejecución: ____ / ____ / 2026  Responsable: ____________________

Esta ficha cierra la actividad vencida únicamente cuando todos los campos
tienen medición o evidencia. El robot debe permanecer desenergizado, sin PWM y
sin ejecutar posturas o marchas.

## Evidencia fotográfica obligatoria

| ID | Vista | Archivo | Verificada |
|---|---|---|:---:|
| F01 | Robot completo: frente | | [ ] |
| F02 | Robot completo: lateral izquierda | | [ ] |
| F03 | Robot completo: lateral derecha | | [ ] |
| F04 | Robot completo: superior | | [ ] |
| F05 | Electrónica y cableado | | [ ] |
| F06 | Fuente, LM2596, fusible y parada/OE | | [ ] |
| F07–F18 | Etiqueta de cada uno de los 12 servos | | [ ] |
| F19–F22 | Detalle de cada pata y sus articulaciones | | [ ] |

No fotografiar claves, redes ni datos personales. Conservar los originales sin
edición y registrar SHA-256 al incorporarlos al repositorio.

## Inventario

| Componente | Cantidad | Marca/modelo visible | Identificador | Estado/diferencia |
|---|---:|---|---|---|
| Raspberry Pi 4 Model B | 1 | | | |
| Arduino Mega 2560 R3 | 1 | | | |
| PCA9685 | 1 | V1.2.4.6 | 0x40 | |
| BNO055 | 1 | | | |
| MG996R | 12 | | | |
| Fuente | 1 | | | |
| LM2596 | 1 | | | |
| Fusible/limitación | | | | |
| Parada física/OE | | | | |

## Geometría — tres repeticiones independientes

Usar milímetros y registrar la resolución del instrumento: ______ mm.

| Magnitud | M1 | M2 | M3 | Media | Diferencia frente al modelo |
|---|---:|---:|---:|---:|---:|
| Largo del cuerpo | | | | | |
| Ancho del cuerpo | | | | | |
| Separación longitudinal de caderas | | | | | |
| Separación transversal de caderas | | | | | |
| Coxa FL / FR / RL / RR | | | | | |
| Fémur FL / FR / RL / RR | | | | | |
| Tibia FL / FR / RL / RR | | | | | |
| Diámetro/dimensión efectiva del pie | | | | | |

## Masas

Registrar resolución de balanza: ______ g. No desmontar elementos si hacerlo
puede dañar cableado o perder calibración.

| Conjunto | M1 (g) | M2 (g) | M3 (g) | Media (g) |
|---|---:|---:|---:|---:|
| Robot completo | | | | |
| Cuerpo y electrónica | | | | |
| Pata FL / FR / RL / RR, si es seguro | | | | |

## Inspección mecánica

| Elemento | FL | FR | RL | RR | Evidencia/observación |
|---|:---:|:---:|:---:|:---:|---|
| Holgura perceptible | | | | | |
| Tornillos flojos | | | | | |
| Tope o colisión mecánica | | | | | |
| Pie deteriorado o desigual | | | | | |
| Cable rozando o tensionado | | | | | |
| Diferencia de montaje | | | | | |

## Criterio de cierre

- [ ] Fotografías completas y hashes registrados.
- [ ] Doce servos confirmados o diferencias anotadas.
- [ ] Tres mediciones por dimensión y masa disponible.
- [ ] Inspección mecánica completa.
- [ ] Tabla nominal–medido preparada para actualizar URDF/MJCF.
- [ ] Cambios y limitaciones registrados en continuidad y GitHub.
