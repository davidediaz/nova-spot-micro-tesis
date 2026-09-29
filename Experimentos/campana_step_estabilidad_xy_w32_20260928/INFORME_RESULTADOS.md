# Resultados de desarrollo: step con estabilidad lateral y rumbo

Fecha: 28 de septiembre de 2026 (America/Bogota). Campaña de simulación MuJoCo; no se
transfirieron políticas a ROS, Raspberry Pi, PWM ni servos.

## Diseño

Cinco políticas PPO independientes, semillas de entrenamiento 11, 23, 37, 53
y 71, con 200.000 pasos solicitados cada una. Se usó la observación ampliada
(30 dimensiones: posición lateral y rumbo incluidos), pesos 32 para roll/pitch
y 8 para lateral/rumbo. La acción es residual, acotada a ±0,08 rad, con cambio
máximo 0,02 rad por control. Cada evaluación de desarrollo emplea las semillas
701–705; cada episodio cubre 20 ciclos de 5,76 s más una rampa transitoria de
1 s. Se reservaron las semillas de evaluación final 101, 202, 303, 404 y 505.

La corrección temporal hace avanzar cada muestra nominal durante nueve pasos
de control de 20 ms, con interpolación lineal. Por eso cada ciclo tiene 288
pasos y una evaluación completa tiene 5.810 pasos (50 de rampa + 20 × 288).
El entorno se comprobó aparte: inicia con control igual a la pose medida de
pie, sin salto de arranque, y termina exactamente en 1.490 pasos para cinco
ciclos de humo. Sin embargo, esa rampa/cadencia difiere de las campañas
anteriores: sus resultados no son comparables y estas cinco semillas siguen
siendo solo evidencia de desarrollo.

## Resultado

Las cinco políticas completaron 200.000 pasos y las evaluaciones concluyeron
sin terminaciones tempranas. En la evaluación PPO, promediando las cinco
políticas, roll RMS fue 0,00662 rad (0,38°), pitch RMS 0,01344 rad (0,77°),
inclinación máxima 0,03530 rad (2,02°) y altura mínima/máxima 0,23387/0,23832
m. Esos indicadores cumplen los objetivos numéricos provisionales de
estabilidad/altura de la ficha, aunque dicha ficha no está firmada.

No obstante, la caminata no se acepta ni se escoge política:

- El avance PPO medio fue 0,1877 m frente a 0,0805 m nominales, pero la
  dispersión entre políticas es grande (−0,0548 a 0,5483 m): solo 2/5 políticas
  superan el avance nominal y tres quedan por debajo.
- La excursión lateral máxima media fue 0,0826 m (rango 0,0490–0,1069 m), frente
  a 0,0040 m nominales; deriva lateral final media 0,0360 m. La penalización
  lateral/rumbo no resolvió la desviación de trayectoria.
- El error articular máximo medio fue 0,0738 rad y todas las cinco políticas
  superan el umbral provisional 0,05 rad. El máximo salto articular medio fue
  0,0115 rad, por debajo del umbral provisional 0,05 rad.
- Contacto medio 0,8355 frente a 0,8485 nominal; ninguna evaluación terminó
  temprano, pero el contacto no alcanza 0,90.

La variabilidad por semilla y la pérdida de seguimiento/deriva pesan más que
la mejora de la inclinación. No hay candidata justificada para gastar las
semillas bloqueadas de evaluación final; quedan intactas. Resultado técnico:
campaña completada, políticas no seleccionadas, marcha PPO no aprobada.

## Reproducibilidad y siguiente paso

El manifiesto, código ejecutor, logs por semilla, cinco `policy.zip`, trazas,
evaluación CSV y `SHA256SUMS` están junto a este informe. Para comprobar la
integridad, desde la raíz del repositorio:

```sh
cd Experimentos/campana_step_estabilidad_xy_w32_20260928
sha256sum -c SHA256SUMS
```

Próximo paso: ajustar y validar la referencia/control nominal para limitar
excursión lateral y error articular antes de volver a PPO. Mantener sin cambios
la ficha formal hasta revisión/firma del director; luego ejecutar evaluación
final emparejada solo si una política pasa los criterios de desarrollo y
comparación predefinidos. No hacer pruebas físicas todavía.
