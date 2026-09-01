# Matriz objetivo–método–evidencia del documento final

Estado inicial: 1 de septiembre de 2026. Esta matriz se actualizará únicamente
cuando exista evidencia verificable.

| Objetivo específico | Método o procedimiento ejecutado | Evidencia principal disponible | Resultado demostrable actual | Criterio de cierre | Sección final | Estado |
|---|---|---|---|---|---|---|
| OE1. Caracterizar la plataforma y desarrollar los modelos cinemático y dinámico | Se implementaron cinemática directa e inversa, jacobiano, dinámica nominal, contacto, margen estático y modelos URDF/MJCF; se verificaron mediante pruebas numéricas y simuladores | Capítulo 7 del documento final, `Documentacion/MODELO_MATEMATICO_LATEX`, paquetes ROS 2 y pruebas automatizadas | Existe un modelo nominal computable y reproducible; 50 pruebas verifican propiedades internas, pero la identificación física sigue incompleta | Geometría, masas, límites y diferencias físicas medidos y contrastados | Modelo matemático implementado | Parcial avanzado |
| OE2. Diseñar e implementar la arquitectura electrónica y de software segura | Se integraron ROS 2, supervisor, IMU, contactos y margen; se preparó Raspberry/PCA9685 de forma progresiva | `Documentacion/ESTABILIDAD_IMU_SUPERVISOR_GAZEBO.md`, `Raspberry/`, código y pruebas | La arquitectura de simulación funciona; la seguridad eléctrica y la calibración física no están cerradas | Protecciones, OE, parada física, calibraciones y pruebas provocadas aprobadas | Arquitectura y seguridad | Parcial |
| OE3. Implementar locomoción convencional para postura, paso y gateo | Se diseñaron trayectorias cartesianas, IK, máquina de estados, fase y líneas base repetidas en Gazebo/MuJoCo | `Documentacion/MARCHA_PASO_VALIDACION.md`, bolsas, CSV e informes de análisis | Postura, paso y gateo nominales son repetibles en simulación; el contacto trasero del gateo no coincide con el plan | Marchas nominales verificadas también en hardware bajo protocolo | Marcha nominal | Parcial avanzado |
| OE4. Entrenar e integrar una política RL correctiva y acotada | Se delimitaron acciones, semillas y restricciones; el entrenamiento permanece bloqueado | Protocolo experimental y decisión de semillas | No existe todavía una política entrenada que pueda presentarse como resultado | Cinco semillas entrenadas, selección bloqueada, validación separada y transferencia segura | Aprendizaje por refuerzo | No iniciado experimentalmente |
| OE5. Comparar la marcha nominal con y sin corrección aprendida | Se congeló la matriz de comparación y se produjeron líneas base nominales | `Documentacion/DECISION_TAMANO_MUESTRAL_Y_SEMILLAS_RL.md` y análisis nominales | Existe la referencia nominal, pero no la condición RL ni la comparación final | Cinco ensayos emparejados por condición y marcha, análisis estadístico y discusión | Resultados comparativos | Pendiente |

## Primera evidencia destinada al capítulo de resultados

El ensayo `contactos_debounce_nominal_valido_20260901_0828` analizó 24 ciclos
nominales. Se encontró que las interrupciones crudas de RL y RR duraron en
promedio 0,074645 s y 0,073803 s, respectivamente, y ninguna superó 0,12 s. Por
ello no se demostró un vuelo trasero sostenido, aunque el robot avanzó en
simulación. La redacción controlada está en
`Documentacion/RESULTADOS_CONTACTO_CRUDO_FILTRADO_2026-09-01.md`.
