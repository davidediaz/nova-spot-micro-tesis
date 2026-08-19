# Fase de marcha y contactos previstos

Versión: 17 de agosto de 2026.

## Tópico

El controlador publica `/nova/gait_phase` con tipo `std_msgs/msg/String` y
contenido JSON sincronizado con cada referencia articular.

Ejemplo:

```json
{
  "mode": "crawl",
  "sample_index": 2,
  "samples_per_cycle": 24,
  "cycle_index": 0,
  "planned_leg": "fl",
  "swing_leg": "fl",
  "gait_subphase": "liftoff",
  "expected_contacts": ["fr", "rl", "rr"],
  "contact_plan_available": true
}
```

## Campos

- `mode`: `crawl`, `step` o el modo activo.
- `sample_index`: índice cero basado de la referencia dentro del ciclo.
- `samples_per_cycle`: 24 para gateo y 32 para marcha paso.
- `cycle_index`: número de ciclo desde la última orden de cambio de modo.
- `planned_leg`: pata a la que pertenece el cuarto de ciclo actual.
- `swing_leg`: pata prevista en el aire; vale `null` durante transferencia,
  precarga y contacto final.
- `gait_subphase`: subfase discreta de la referencia actual.
- `expected_contacts`: patas previstas en apoyo.
- `contact_plan_available`: indica si existe un plan de contactos formal.

Abreviaturas: `fl` delantera izquierda, `fr` delantera derecha, `rl` trasera
izquierda y `rr` trasera derecha.

## Secuencia

Para `crawl` y `step`, el orden de oscilación es FL--RR--FR--RL. En el gateo,
cada cuarto de seis muestras declara, en orden, `transfer_start`, `preload`,
`liftoff`, `flight`, `landing` y `touchdown`. Las dos primeras y la última
esperan cuatro contactos; las tres muestras aéreas esperan tres. Así se separa
la descarga del apoyo de la elevación y el plan coincide con la trayectoria
cartesiana publicada. El índice de ciclo aumenta al volver la muestra a cero.

La marcha `step` conserva una pata en oscilación y tres contactos durante todo
su cuarto de ciclo; por compatibilidad publica `gait_subphase="swing"`.

Para `gallop`, el mensaje declara `contact_plan_available=false` hasta definir y
validar formalmente su patrón; no se inventan contactos.

## Validación

- 36 pruebas automatizadas aprobadas.
- Secuencia completa verificada para 24 y 32 muestras.
- Precarga, vuelo y contacto final verificados para las seis referencias de
  cada pata del gateo.
- Reinicio de fase y ciclo al cambiar de modo.
- Las seis subfases se observaron en una ejecución ROS 2 real de 15 ciclos.

## Contactos medidos añadidos

Desde el 14 de agosto de 2026, Gazebo dispone además de sensores medidos en los
cuatro pies. `/nova/foot_contacts` consolida contacto, validez, antigüedad y
fuerza aproximada por pie. `/nova/contact_diagnostics` compara el conjunto
previsto con el observado e informa contactos faltantes o inesperados.

La comparación es informativa: no ordena `stand` ni modifica la marcha. MuJoCo
todavía no publica contactos equivalentes. Toda bolsa nueva de locomoción debe
incluir `/nova/gait_phase`, `/nova/foot_contacts` y
`/nova/contact_diagnostics`.
