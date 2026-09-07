# Matriz objetivo–método–evidencia del documento final

Actualizada el 7 de septiembre de 2026 con los cuatro objetivos suministrados por el usuario. Sustituye la clasificación anterior de cinco objetivos; no altera resultados históricos.

## Objetivo general

Desarrollar un sistema de control para la plataforma cuadrúpedo Spot Micro que integre aprendizaje por refuerzo para su ejecución y estabilización en los diferentes modos de locomoción tipo paso y gateo en condiciones de entorno controladas.

| Objetivo específico (texto suministrado) | Método ejecutado | Evidencia | Resultado actual | Criterio de cierre | Estado |
|---|---|---|---|---|---|
| OE1. Implementar el hardware y software necesario para la ejecución de movimiento de las extremidades de la plataforma spot micro con la que cuenta el laboratorio de robótica, siguiendo la documentación técnica del fabricante. | ROS 2, Raspberry/PCA9685 y movimiento inicial de doce servos; supervisor con nueve escenarios provocados | Raspberry/; Experimentos/pruebas_dinamicas_supervisor_20260902 | Integración inicial disponible; sobrecarga física pendiente de diagnóstico | Cerrar alimentación, protecciones, calibración y ejecución física documentada | Parcial |
| OE2. Modelar comportamiento cinemático y dinámico de la plataforma para simulación y posterior diseño a partir de la literatura y estudios previos sobre robots cuadrúpedos. | Cinemática, dinámica nominal, URDF/MJCF y verificaciones computacionales | Documentacion/MODELO_MATEMATICO_LATEX; capítulo 7; contraste de fuentes oficiales del 07/09 | Modelo nominal reproducible, no identificado físicamente | Contrastar parámetros del ejemplar y documentar validación y limitaciones del modelo | Parcial |
| OE3. Diseñar una estrategia de control basada en aprendizaje automático para la coordinación del movimiento del robot, garantizando estabilidad y continuidad durante los modos de locomoción tipo paso y gateo. | Marcha base y correcciones acotadas; cinco semillas PPO entrenadas y evaluadas | Experimentos/DIAGNOSTICO_REFERENCIA_PPO_ESCALA_CERO_20260902.md; capítulo de resultados | Entrenamiento ejecutado; no se demostró la estabilidad y continuidad requeridas para cerrar el objetivo | Validar la estrategia aprendida en paso y gateo con criterios de estabilidad y continuidad | Parcial |
| OE4. Evaluar el funcionamiento del modelo de caminata del robot cuadrúpedo mediante tres pruebas: la Prueba de Margen de Estabilidad Estática, la Prueba de Seguimiento de Posición Articular y la Prueba de Repetibilidad del Patrón de Marcha. | Margen nominal implementado; seguimiento articular y repetibilidad medidos en simulación | Documentacion/EQUIVALENCIA_GAZEBO_MUJOCO_2026-09-02.md; Experimentos/comparacion_cadencia_corregida_20260814; capítulo de resultados | Evidencia parcial de las tres líneas; reacción a margen negativo no equivale a validar estabilidad | Completar Prueba de Margen de Estabilidad Estática, Prueba de Seguimiento de Posición Articular y Prueba de Repetibilidad del Patrón de Marcha bajo protocolo común | Parcial |

## Lectura del avance

La marcha convencional es soporte de OE1/OE3 y fuente de ensayos para OE4; no constituye un quinto objetivo. La comparación con y sin PPO se mantiene como método de evaluación, no como un objetivo independiente adicional. Ningún resultado negativo se presenta como estabilidad garantizada.

La caracterización física aporta al modelo (OE2) y al funcionamiento de hardware (OE1). El cálculo de margen o una parada ante un valor negativo no cierra la Prueba de Margen de Estabilidad Estática. Seguimiento y repetibilidad tienen evidencia en simulación, con validación integral pendiente.
