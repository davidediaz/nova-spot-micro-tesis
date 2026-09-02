# Diagnóstico de la referencia PPO y la escala cero

## Hallazgo

La referencia nominal de 0,027761 m/ciclo usada inicialmente estaba sesgada por
`campana_ppo_gazebo_20260902/nominal_03`. Esa bolsa produjo siete segmentos de
aproximadamente 2,88 s en una marcha paso cuyo ciclo configurado es 5,76 s, y
avances discontinuos de hasta ±0,318 m. Se reclasificó como inválida y se
conservó con `ENSAYO_INVALIDO.md`.

## Recalculo

Con `nominal_01`, `nominal_02`, `nominal_04` y `nominal_05`, la referencia es
0,021935 m/ciclo y 0,003808 m/s. La escala residual 0,00 obtuvo 0,021878
m/ciclo y 0,003798 m/s: diferencias de -0,258 % y -0,259 %. Roll y pitch
también permanecieron prácticamente iguales. Por tanto, el bypass reproduce la
marcha nominal dentro de la variación observada; no existe la discrepancia
grande sugerida por la referencia contaminada.

## Interpretación vigente

La escala cero es un control técnico, no una mejora PPO. Ninguna escala positiva
cumple el criterio conjunto. A 0,25 el avance y la velocidad disminuyen cerca de
18 %, y las escalas mayores degradan todavía más el movimiento y la postura.
No se autoriza transferencia de la política al robot físico.

## Prevención

`comparar_escala_ppo.py` filtra la referencia por duración observada de ciclo
(5,76 ± 0,10 s) y falla si una condición no contiene ciclos válidos. Las
comparaciones futuras deben exigir además instancia única de cada nodo y veinte
ciclos programados por ensayo según el protocolo definitivo.
