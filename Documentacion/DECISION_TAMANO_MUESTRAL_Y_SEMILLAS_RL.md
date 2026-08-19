# Decisión sobre ensayos, ciclos y semillas RL

Fecha: 14 de agosto de 2026.

Estado: aprobado y adoptado como diseño experimental del proyecto.

## Matriz aprobada

| Marcha | Condición | Ensayos independientes | Ciclos programados por ensayo | Total |
|---|---|---:|---:|---:|
| Gateo | Nominal | 5 | 20 | 100 |
| Gateo | Nominal + RL | 5 | 20 | 100 |
| Marcha paso | Nominal | 5 | 20 | 100 |
| Marcha paso | Nominal + RL | 5 | 20 | 100 |

Total final programado: 20 ensayos y 400 ciclos. El ciclo 1 se conserva y se
informa como transitorio; los ciclos 2--20 forman el resumen de régimen
permanente.

## Semillas

- Entrenamiento RL: `11`, `23`, `37`, `53`, `71`.
- Evaluación/escenarios emparejados: `101`, `202`, `303`, `404`, `505`.

Las semillas de evaluación solo producirán diferencias cuando exista
aleatorización declarada. Si la evaluación permanece determinista, funcionan
como identificadores preasignados de cinco reinicios independientes y no se
afirmará que generan variabilidad por sí solas.

## Selección y bloqueo de política

Se entrenarán y reportarán cinco políticas. La métrica primaria y la regla de
selección deben aprobarse antes de elegir una. La selección usará validación
separada, nunca los ensayos finales. Después se bloquearán pesos,
normalizadores, observaciones, saturaciones y configuración.

La política bloqueada se comparará con el nominal en los mismos cinco
escenarios. Los ciclos de un ensayo son mediciones repetidas; la réplica
independiente es el ensayo (`n=5` por condición).

## Fallos y repeticiones

Un fallo no desaparece al repetir. Se cuenta en la tasa de fallos y cualquier
repetición se identifica como adicional. Los ensayos exploratorios y de ajuste
no pueden incorporarse retrospectivamente al conjunto final.

## Justificación

Cinco ensayos permiten una comparación inicial entre ejecuciones sin tratar los
ciclos como réplicas independientes. Veinte ciclos por ensayo proporcionan un
transitorio conservado y 19 ciclos de régimen permanente. Esta cantidad es una
decisión práctica de tesis, no el resultado de un cálculo formal de potencia.
Si la variabilidad piloto exige más precisión, el aumento deberá decidirse y
aplicarse simétricamente antes de examinar el resultado comparativo final.
