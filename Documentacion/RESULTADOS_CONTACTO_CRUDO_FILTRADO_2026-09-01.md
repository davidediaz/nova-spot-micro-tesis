# Resultado para tesis: contacto crudo y vuelo sostenido

Fecha del ensayo: 1 de septiembre de 2026.

## Pregunta experimental

¿Las transiciones de contacto observadas en las patas traseras durante el
gateo nominal representan un despegue sostenido o interrupciones breves del
flujo de contacto de Gazebo?

## Método resumido

Se ejecutaron 24 ciclos completos de gateo nominal en Gazebo, sin modificar la
longitud de paso de 18 mm, la elevación de 14 mm ni la cadencia de 0,18 s por
referencia. El monitor declaró `raw_contact=false` después de 0,10 s sin una
muestra de colisión. Para confirmar pérdida de contacto, ese estado crudo debía
persistir 0,12 s adicionales; el recontacto se confirmó después de 0,03 s.

La bolsa registró fase, contacto crudo y filtrado, diagnóstico sincronizado,
trayectorias, estados articulares, pose, IMU, margen nominal y supervisor. La
unidad descriptiva de esta prueba es el ensayo; los 24 ciclos caracterizan la
persistencia temporal y no se presentan como 24 réplicas independientes.

## Resultados

| Pata | Coincidencia cruda | Coincidencia filtrada | Duración media sin contacto crudo | Máxima | Superan 0,12 s |
|---|---:|---:|---:|---:|---:|
| FL | 62,304 % | 60,747 % | 0,944766 s | 0,999304 s | 49/49 |
| FR | 62,731 % | 61,290 % | 0,935656 s | 0,994892 s | 48/49 |
| RL | 89,414 % | 87,717 % | 0,074645 s | 0,089805 s | 0/24 |
| RR | 89,088 % | 87,339 % | 0,073803 s | 0,089396 s | 0/25 |

La coincidencia simultánea fue 20,639 % con el estado crudo y 13,621 % con el
estado filtrado. Los despegues delanteros se confirmaron unos 0,259 s después
de lo previsto. En las patas traseras no existieron pares filtrados de
despegue/aterrizaje porque ninguna interrupción cruda alcanzó la persistencia
requerida.

Durante la misma ventana se completaron 24 ciclos sin activaciones del
supervisor. El ciclo medio duró 4,319990 s, el avance medio fue 0,023558 m por
ciclo y la velocidad media 0,005453 m/s.

## Interpretación defendible

El estado crudo por timeout sí genera transiciones aparentes en RL y RR, pero
su duración máxima fue inferior a 0,09 s. Por tanto, estos eventos no respaldan
la afirmación de que las patas traseras ejecutan una fase de vuelo sostenida.
El debounce evita contar esos eventos breves como vuelo, aunque introduce el
retardo esperado y reduce la coincidencia temporal con el plan discreto.

Este resultado corrige la interpretación anterior: la trayectoria nominal
puede producir avance estable y repetible mientras las patas traseras
permanecen esencialmente apoyadas y deslizan. No debe afirmarse que el patrón
físico observado coincide con la secuencia ideal FL--RR--FR--RL.

## Limitaciones

- Los contactos provienen del modelo de colisión de Gazebo, no de sensores
  físicos calibrados.
- Los umbrales de 0,10/0,12/0,03 s son provisionales; esta prueba caracteriza
  su efecto, pero no demuestra que sean óptimos.
- El filtro clasifica persistencia, no mide separación geométrica pie--suelo.
- Solo existe un ensayo formal bajo esta configuración; los ciclos no son
  réplicas estadísticas independientes.
- El margen de estabilidad publicado usa un modelo nominal no identificado.

## Evidencia trazable

- Bolsa local y registro: `Experimentos/rosbag2/contactos_debounce_nominal_valido_20260901_0828/`.
- Análisis de contacto: `Experimentos/analisis/contactos_debounce_nominal_valido_20260901_0828/`.
- Análisis de movimiento: `Experimentos/analisis_movimiento/contactos_debounce_nominal_valido_20260901_0828/`.
- Tentativa inválida conservada: `Experimentos/rosbag2/contactos_debounce_nominal_20260901_0823/ENSAYO_INVALIDO.md`.

Esta sección puede incorporarse después al capítulo de resultados, manteniendo
la separación entre observación, interpretación y limitaciones.
