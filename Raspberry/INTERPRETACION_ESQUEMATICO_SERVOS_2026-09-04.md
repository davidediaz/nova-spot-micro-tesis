# Interpretación del esquemático físico de servos — 2026-09-04

Se revisó `/home/pavilion/Descargas/Esquemático .pdf` (3 páginas). La primera
página establece la numeración eléctrica por grupos:

La codificación fue confirmada con la fotografía lateral guardada en
[`documentacion/cuadrupedo_vista_lateral_articulaciones_2026-09-04.png`](documentacion/cuadrupedo_vista_lateral_articulaciones_2026-09-04.png).

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

## Confirmación del usuario

- Patas 1 y 2: delanteras.
- Patas 3 y 4: traseras.
- Pata 1: delantera derecha.
- Pata 2: delantera izquierda.
- Pata 3: trasera derecha.
- Pata 4: trasera izquierda.

Con la orientación confirmada, la asociación ROS 2 queda (la numeración del PDF
empieza en CH0 para la pata 1):

```text
front_right: CH0 (coxa), CH4 (fémur), CH8 (tibia)
front_left:  CH1 (coxa), CH5 (fémur), CH9 (tibia)
rear_right:  CH2 (coxa), CH6 (fémur), CH10 (tibia)
rear_left:   CH3 (coxa), CH7 (fémur), CH11 (tibia)
```

## Confirmación final

La fotografía confirma que morado = coxa, rojo = fémur y azul = tibia. El mapa
de canales y patas anterior queda validado visualmente.

No se modificó aún `Raspberry/configuracion/servos.yaml`; se espera confirmar
estas tres relaciones antes de asociar canales a nombres ROS 2 y ejecutar una
marcha.
