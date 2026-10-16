# Entrenamiento PPO ajustado al robot real — 16 de octubre de 2026

## Datos reales usados
Las caminatas `b` del robot suspendido (sesiones 131, 135 y 136 de `~/CODIGO/datos_aprendizaje/datos_cuadrupedo.sqlite`) se registraron con los potenciómetros leídos por el MUX 16CH (selectores D8–D11, SIG A0). Con `identificar_actuadores_reales.py` se obtuvo lo siguiente (`actuadores_reales.json`):

| Articulación | Sensor | r | Retardo | Ganancia |
|---|---|---:|---:|---:|
| Fémur 2 (FL) | C5 | −0,81 | 100 ms | 0,88 |
| Fémur 4 (RL) | C6 | −0,84 | 100 ms | 0,92 |
| Tibia 2 (FL) | C9 | −0,88 | 100 ms | 0,98 |
| Tibia 4 (RL) | C10 | −0,01 | — | 0,04 (casi no se mueve en la caminata) |
| Tibia 3 (RR) | C11 | −0,10 | — | señal no fiable |

La tibia 1 (FR, CH8) tiene un servo dañado (tramo muerto en su potenciómetro) y queda sin PWM. Las coxas se mantienen fijas en su equilibrio: 150°, 45°, 55° y 150°.

## Simulación ajustada (`entrenar_ppo_real.py`)
- Marcha nominal: la caminata `b` real, gateo FL→RR→FR→RL, fémures ±15°, tibias 14°, 0,5 s + 0,15 s por fase (ciclo de 2,64 s).
- Actuador: retardo de 5 pasos (100 ms) y ganancia por articulación según la tabla; tibia FR sin rigidez.
- Observación (17): ángulos de fémur 2, fémur 4 y tibia 2 con ruido de 1°, más seno y coseno de la fase y el residual previo. Son señales que el Uno sí puede medir.
- Acción: residual ±0,08 rad con cambio máximo de 0,02 rad por paso, aplicado solo a fémures y tibias útiles (coxas y tibia FR en cero).
- Aleatorización de la fricción del suelo y del amortiguamiento. Sin cambios en el entrenador ni en el MJCF originales.

## Resultados (150 000 pasos por semilla; evaluación con escenarios de desarrollo 801–805, 6 ciclos)

| Semilla | Avance (m) | Deriva lateral (m) | Inclinación máx. (rad) | Caídas |
|---|---:|---:|---:|---:|
| Nominal | 0,173 | 0,111 | 0,128 | 0 |
| 11 | **0,299** | **0,046** | **0,097** | 0 |
| 23 | 0,214 | 0,126 | 0,140 | 0 |
| 37 | 0,245 | 0,070 | 0,108 | 0 |
| 53 | 0,249 | 0,080 | 0,153 | 0 |
| 71 | 0,237 | 0,064 | 0,112 | 0 |

Las cinco políticas avanzan más que la nominal. Las semillas 11, 37 y 71 mejoran a la vez el avance, la deriva y la inclinación. La semilla 11 es la mejor: +73 % de avance, −58 % de deriva y −24 % de inclinación.

## Límites
- La evaluación es en simulación, con escenarios de desarrollo; las semillas finales 101–505 no se usaron.
- Los signos de fémur y tibia del modelo se asumieron a partir de la marcha nominal del proyecto, sin calibración ángulo-servo.
- No se ha transferido ninguna política al robot (`hardware_transfer=false`). Para probarla falta un modo del firmware que reciba residuales desde el PC por el puerto serie y envíe C5, C6 y C9 como observación.
