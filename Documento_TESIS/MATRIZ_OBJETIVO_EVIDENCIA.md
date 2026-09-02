# Matriz objetivo–método–evidencia del documento final

Estado inicial: 1 de septiembre de 2026. Última actualización: 2 de septiembre
de 2026. Esta matriz se actualiza únicamente cuando existe evidencia
verificable.

| Objetivo específico | Método o procedimiento ejecutado | Evidencia principal disponible | Resultado demostrable actual | Criterio de cierre | Sección final | Estado |
|---|---|---|---|---|---|---|
| OE1. Caracterizar la plataforma y desarrollar los modelos cinemático y dinámico | Se implementaron y verificaron los modelos; además se prepararon el protocolo, la ficha y los CSV nominal--medido para caracterización física | Capítulos 7 y 9, `Documentacion/MODELO_MATEMATICO_LATEX`, `Documentacion/PROTOCOLO_CARACTERIZACION_FISICA.md`, paquetes ROS 2 y pruebas | Existe un modelo nominal reproducible y un procedimiento de medición trazable; todavía no existen mediciones físicas completas | Geometría, masas, límites y diferencias físicas medidos y contrastados | Modelo matemático y protocolo de caracterización | Parcial avanzado |
| OE2. Diseñar e implementar la arquitectura electrónica y de software segura | Se integraron ROS 2, supervisor, IMU, contactos y margen; se ejecutaron nueve escenarios provocados y se preparó Raspberry/PCA9685 | `Experimentos/pruebas_dinamicas_supervisor_20260902`, `Documentacion/ESTABILIDAD_IMU_SUPERVISOR_GAZEBO.md`, `Raspberry/` | La arquitectura y reacción del supervisor funcionan en simulación; faltan rearme, falsos positivos, seguridad eléctrica y calibración | Protecciones, OE, parada física, calibraciones, rearme y pruebas físicas aprobadas | Arquitectura y seguridad | Parcial avanzado |
| OE3. Implementar locomoción convencional para postura, paso y gateo | Se diseñaron trayectorias cartesianas, IK, máquina de estados y una campaña de 11 ciclos con pose, IMU y contactos comunes en Gazebo/MuJoCo | `Documentacion/EQUIVALENCIA_GAZEBO_MUJOCO_2026-09-02.md`, bolsas, CSV e informes | Las marchas son repetibles; la equivalencia instrumental está cerrada y evidencia diferencias dinámicas de avance y contacto | Marchas nominales verificadas también en hardware bajo protocolo | Marcha nominal | Parcial avanzado |
| OE4. Entrenar e integrar una política RL correctiva y acotada | Se entrenaron cinco semillas PPO, se conectaron observaciones ampliadas y se evaluaron escalas residuales en Gazebo | Modelos, curvas, bolsas y `Experimentos/DIAGNOSTICO_REFERENCIA_PPO_ESCALA_CERO_20260902.md` | El flujo fue ejecutado, pero ninguna escala positiva mejoró conjuntamente avance y postura; transferencia rechazada | Política reentrenada y seleccionada mediante validación separada que cumpla el criterio conjunto | Aprendizaje por refuerzo | Ejecutado, no aceptado |
| OE5. Comparar la marcha nominal con y sin corrección aprendida | Se ejecutó una comparación descriptiva no emparejada y se corrigió una referencia contaminada | Figuras PPO, bolsas, CSV y diagnóstico de escala cero | El resultado negativo bloquea transferencia, pero no satisface la campaña final de cinco pares por marcha | Cinco ensayos emparejados por condición y marcha, análisis estadístico y discusión | Resultados comparativos | Parcial, no concluyente |

## Primera evidencia destinada al capítulo de resultados

El ensayo `contactos_debounce_nominal_valido_20260901_0828` analizó 24 ciclos
nominales. Se encontró que las interrupciones crudas de RL y RR duraron en
promedio 0,074645 s y 0,073803 s, respectivamente, y ninguna superó 0,12 s. Por
ello no se demostró un vuelo trasero sostenido, aunque el robot avanzó en
simulación. La redacción controlada está en
`Documentacion/RESULTADOS_CONTACTO_CRUDO_FILTRADO_2026-09-01.md`.
