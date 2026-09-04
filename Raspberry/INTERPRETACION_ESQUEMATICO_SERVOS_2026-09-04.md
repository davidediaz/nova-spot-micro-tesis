# Interpretación del esquemático físico de servos — 2026-09-04

Se revisó `/home/pavilion/Descargas/Esquemático .pdf` (3 páginas). La primera
página establece la numeración eléctrica por grupos:

| Grupo | Canales | Número físico | Interpretación provisional |
|---|---:|---:|---|
| Morado | CH0–CH3 | 1–4 | Coxa / articulación proximal |
| Rojo | CH4–CH7 | 1–4 | Fémur / articulación intermedia |
| Azul | CH8–CH11 | 1–4 | Tibia / articulación distal |

Por tanto, la correspondencia provisional por pata es:

```text
Pata 1: CH0 (coxa), CH4 (fémur), CH8 (tibia)
Pata 2: CH1 (coxa), CH5 (fémur), CH9 (tibia)
Pata 3: CH2 (coxa), CH6 (fémur), CH10 (tibia)
Pata 4: CH3 (coxa), CH7 (fémur), CH11 (tibia)
```

La segunda página muestra esas etiquetas sobre el cuadrúpedo. El PDF no deja
inequívoco cuál de las patas 1–4 es `front_left`, `front_right`, `rear_left` o
`rear_right` porque no incluye una flecha de “frente” vista desde el robot.

## Confirmaciones pendientes

1. Mirando el robot desde su dirección de avance, ¿qué número (1–4) es la pata
   delantera izquierda?
2. ¿La numeración sigue alrededor del cuerpo en sentido horario o antihorario?
3. ¿Confirmas que morado/rojo/azul corresponden, respectivamente, a coxa,
   fémur y tibia?

No se modificó aún `Raspberry/configuracion/servos.yaml`; se espera confirmar
estas tres relaciones antes de asociar canales a nombres ROS 2 y ejecutar una
marcha.
