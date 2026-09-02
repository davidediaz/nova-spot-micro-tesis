# Criterio de aceptación del barrido PPO

Línea base nominal recalculada con cuatro ensayos válidos: avance 0.021935 m/ciclo, velocidad 0.003808 m/s, roll 1.279726°, pitch 2.506391°. `nominal_03` se excluyó porque sus ciclos observados duran 2,88 s en vez de 5,76 s.

| Escala | Avance | Velocidad | Roll | Pitch | Aceptada |
|---:|---:|---:|---:|---:|:---:|
| 0.00 | 0.021878 | 0.003798 | 1.280 | 2.502 | no |
| 0.25 | 0.017988 | 0.003123 | 2.202 | 2.524 | no |
| 0.50 | 0.001340 | 0.000233 | 3.278 | 3.118 | no |
| 0.75 | 0.005592 | 0.000971 | 3.844 | 3.647 | no |
| 1.00 | 0.003775 | 0.000655 | 4.436 | 3.715 | no |
