# Línea base con cadencia corregida

Fecha: 14 de agosto de 2026, 10:49--10:50, America/Bogota.

- Bolsa: `linea_base_cadencia_corregida_20260814_1049`.
- Duración total: 67,871973998 s.
- Ventana entre último `gateo` y primer `stand`: 57,014709063 s.
- Ciclos completos: 13.
- Mensajes: 32.352.
- Tamaño: 37,3 MiB.
- Activaciones del supervisor: 0.
- Paso: 0,018 m.
- Elevación: 0,014 m.
- Muestras por ciclo: 24.
- Fase configurada: 0,18 s.
- Ciclo observado medio: 4,320013 s.

Antes de grabar se confirmó exactamente una instancia de cada nodo. Se
almacenaron tres marcadores redundantes `gateo` y tres `stand`; el último
`gateo` define la fase cero limpia y el primer `stand` cierra la ventana.

## Régimen permanente, ciclos 2--13

| Métrica | Media |
|---|---:|
| Duración observada | 4,320013 s |
| Avance | 0,023338 m/ciclo |
| Velocidad | 0,005402 m/s |
| Excursión lateral | 0,015133 m |
| Altura | 0,223836 m |
| Roll máximo absoluto | 2,233112 grados |
| Pitch máximo absoluto | 4,365442 grados |
| Salto articular máximo | 0,018336 rad |

El ciclo 1 se conserva como transitorio y no se oculta. Los resultados
completos están en
`../../analisis/linea_base_cadencia_corregida_20260814_1049`.

## Integridad

- SHA-256 de la bolsa:
  `5d2f73daddef870f32269d5c18b930839b2839370be8a50fa3cfb84dae704ce4`.
- SHA-256 de `gait_controller.py`:
  `a4306cbe59f75e6293675be08ccfee6a693120409a470dc5a6d1ce362aac7934`.

Esta bolsa pertenece únicamente a la versión de cadencia corregida y no debe
combinarse con los ensayos anteriores de ciclo cercano a 4,80 s.
