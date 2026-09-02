# Protocolo de puesta en marcha y seguridad

## Precondiciones

1. Robot sobre mesa firme, patas libres y soporte anti-caída instalado.
2. Fuente desconectada; verificar 0 V entre V+ y GND antes de cablear.
3. OE del PCA9685 con pull-up y parada física accesible; probar continuidad.
4. Fusible y límite de corriente documentados; Raspberry alimentada por USB-C.
5. No conectar los doce servos: iniciar con una sola unidad asegurada.

## Secuencia

| Etapa | Acción | Criterio de aceptación | Abortar si |
|---|---|---|---|
| E0 | Inspección y fotografías | Sin cables pellizcados ni piezas sueltas | daño, olor o calentamiento |
| E1 | Encender lógica sin V+ | I²C detecta PCA9685 y OE permanece deshabilitado | PWM inesperado |
| E2 | Medir fuente sin carga | V+ dentro de 5,0–6,0 V y polaridad correcta | sobretensión o rizado excesivo |
| E3 | Un servo asegurado | Movimiento limitado, sin atasco ni ruido anómalo | corriente/temperatura anormal |
| E4 | Una pata suspendida | Centro y extremos calibrados, parada corta PWM | vibración, golpe o pérdida de control |
| E5 | Robot suspendido | 12 canales responden individualmente | canal cruzado o servo invertido |
| E6 | Suelo con soporte | Solo postura estática, supervisor activo | inclinación, caída o corriente límite |

La orden ROS `stand` no sustituye el corte de potencia. Ante cualquier duda se
deshabilita OE y se desconecta la fuente antes de tocar el mecanismo.
