# Intervención mecánica y sustitución de servos — 31 de agosto de 2026

## Cambios informados

- Se sustituyeron dos servomotores debido a limitaciones físicas observadas en
  los componentes anteriores.
- Se reforzaron los acoples mecánicos del cuadrúpedo para reducir holguras o
  juego en las patas y aumentar la rigidez antes de las pruebas posteriores.
- Continúa en impresión la pieza `SM3_Cover_LeftFemur.stl`; el ensamble físico
  todavía no se considera completo.

## Alcance de esta evidencia

Este registro confirma que se realizaron las intervenciones, pero no demuestra
todavía su desempeño. No se dispone en este corte de fotografías, identificación
de las dos articulaciones/canales, marca o lote de los servos retirados y
reemplazos, mediciones de holgura antes/después, par, corriente, temperatura ni
pruebas repetidas bajo carga.

Por esa razón:

- no se actualizan aún límites articulares, centros PWM ni parámetros del
  URDF/MJCF;
- las calibraciones previas no deben transferirse automáticamente a los dos
  servos nuevos;
- no se autorizan postura, paso o gateo físicos;
- los refuerzos deben inspeccionarse para descartar topes, rozamiento,
  desalineación y pérdida de rango útil.

## Datos obligatorios para cerrar la intervención

| Dato | Servo reemplazado 1 | Servo reemplazado 2 |
|---|---|---|
| Pata y articulación | Pendiente | Pendiente |
| Canal PCA9685 | Pendiente | Pendiente |
| Marca/modelo anterior | Pendiente | Pendiente |
| Marca/modelo nuevo | Pendiente | Pendiente |
| Motivo físico concreto | Pendiente | Pendiente |
| Centro PWM seguro | Pendiente | Pendiente |
| Mínimo/máximo seguro | Pendiente | Pendiente |
| Sentido de giro | Pendiente | Pendiente |
| Corriente y temperatura | Pendiente | Pendiente |
| Fotografías antes/después | Pendiente | Pendiente |

Para los acoples se deben registrar fotografías, ubicación de cada refuerzo,
material o elemento añadido, rango libre de movimiento y una comparación de
holgura antes/después cuando sea posible.

## Próxima verificación segura

1. Terminar, inspeccionar y montar la tapa izquierda de fémur.
2. Identificar físicamente los dos servos sustituidos y los acoples reforzados.
3. Con el sistema desenergizado, comprobar alineación, topes, rozamientos,
   cableado y rango manual sin forzar transmisiones.
4. Cerrar OE con pull-up, parada física y límites de corriente.
5. Calibrar individualmente cada servo nuevo; después revisar los otros diez.
6. Probar una sola pata suspendida antes de cualquier integración multípata.

