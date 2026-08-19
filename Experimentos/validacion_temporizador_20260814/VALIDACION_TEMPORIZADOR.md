# Validación del temporizador corregido

Fecha: 14 de agosto de 2026.

## Problema

El controlador programaba cada fase como `ahora + 0,18 s`. El callback periódico
de 20 ms llegaba ligeramente después del vencimiento y ese retraso se acumulaba,
produciendo intervalos cercanos a 0,20 s y ciclos cercanos a 4,80 s.

## Corrección

La siguiente fecha se calcula desde la fecha planificada anterior, no desde el
instante tardío del callback. Así, el jitter individual no se acumula.

No se cambiaron las 24 muestras, el paso de 0,018 m, la elevación de 0,014 m ni
la duración configurada de 0,18 s.

## Pruebas

- 24 pruebas automatizadas aprobadas.
- Paquete `nova_gait_controller` recompilado correctamente.
- 152 referencias registradas en una prueba ROS 2 sin Gazebo.
- Seis ciclos completos medidos.

Resultados temporales:

| Magnitud | Resultado |
|---|---:|
| Intervalo medio | 0,180003383 s |
| Intervalo mediano | 0,179973536 s |
| Intervalo mínimo | 0,178788222 s |
| Intervalo máximo | 0,181061025 s |
| Ciclo medio de 24 referencias | 4,320106573 s |

Duraciones de los seis ciclos: 4,320490; 4,320822; 4,319224; 4,320223;
4,320701 y 4,319179 s.

## Integridad

- SHA-256 de `gait_controller.py` corregido:
  `a4306cbe59f75e6293675be08ccfee6a693120409a470dc5a6d1ce362aac7934`.
- SHA-256 de la bolsa ligera:
  `c58b3e45aa2a5aec14c270a18e6b60a32a9cdf05dbf8fa8da3c2e0dcdea560f6`.

La corrección crea una versión experimental nueva. Las bolsas anteriores siguen
siendo válidas para su versión, pero no deben combinarse con futuros ensayos de
la cadencia corregida.
