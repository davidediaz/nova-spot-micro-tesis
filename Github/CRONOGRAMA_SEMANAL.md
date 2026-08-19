# Cronograma semanal de la tesis

Esta tabla traduce el cronograma formal de 32 semanas a una vista de trabajo
para el seguimiento con el profesor. Una actividad solo pasa a **completada**
cuando existe evidencia en el repositorio.

| Semanas | Actividades previstas | Producto verificable | Estado |
|---|---|---|---|
| 1–2 | Definición del problema | Planteamiento y pregunta de investigación | Completada |
| 2–3 | Objetivos y alcance | Objetivos aprobables y límites del proyecto | Completada / revisión |
| 3–5 | Estado del arte y bibliografía | Marco de referencias y antecedentes | Completada |
| 4–5 | Marco teórico y alcance | Capítulos de marco y delimitación | Completada / revisión |
| 5–6 | Metodología y presupuesto | Protocolo, matriz de actividades y presupuesto | En revisión |
| 7–15 | Modelado cinemático y matemático | FK, IK, Jacobiano, dinámica nominal, contacto, estabilidad y control discreto | Completada |
| 16–17 | Validación de modelos | Pruebas de coherencia, Gazebo y MuJoCo | Completada |
| 16–18 | Arquitectura electrónica | Diagrama de bloques, interfaces y requisitos eléctricos | En curso |
| 17–20 | Implementación electrónica | Fuente, distribución, fusible, tierra común, OE y parada física | Pendiente |
| 19–23 | Sistema embebido | Raspberry Pi, ROS 2, red, reloj, I2C y PCA9685 sin servos | Pendiente |
| 21–25 | Pruebas individuales de articulaciones | Calibración de 12 MG996R, límites, corriente y temperatura | Pendiente |
| 23–29 | Algoritmos de locomoción | Gateo, paso, contactos y futura corrección RL acotada | En curso |
| 26–31 | Evaluación de estabilidad | IMU, polígono de soporte, margen y supervisor ampliado | Parcial |
| 27–31 | Validación experimental | Ensayos nominales y nominales+RL con bolsas trazables | Pendiente |
| 28–31 | Redacción del documento final | Resultados, limitaciones, tablas y gráficas | En curso |
| 28–31 | Revisión del asesor | Observaciones registradas y cambios trazables | Pendiente |
| 31–32 | Entrega del trabajo de grado | PDF, código, datos y anexos finales | Pendiente |
| 31–32 | Sustentación | Presentación y demostración final | Pendiente |

## Actividades verificables del cronograma actualizado

| N.° | Actividad | Inicio–fin | Estado actual | Evidencia o siguiente producto |
|---:|---|---|---|---|
| 1 | Modelo matemático nominal | 01/02–16/08 | Completada | `Documentacion/MODELO_MATEMATICO_LATEX/main.tex` |
| 2 | Coherencia URDF/MJCF y simuladores | 01/03–14/08 | Completada | `src/` y pruebas de consistencia |
| 3 | Caracterización física sin energizar | 19/08–28/08 | Pendiente | Inventario, fotos y tres mediciones por dimensión |
| 4 | Actualización de URDF/MJCF medido | 31/08–04/09 | Pendiente | Tabla nominal–medido y regresión |
| 5 | Arquitectura ROS 2, métricas y supervisor | 01/04–18/08 | Completada | 37 pruebas y nodos ROS 2 |
| 6 | Seguridad eléctrica | 24/08–04/09 | Pendiente | Esquema, cálculos y parada física |
| 7 | Medición y calibración de 12 servos | 07/09–18/09 | Pendiente | YAML, curvas PWM–ángulo y límites |
| 8 | Raspberry Pi, ROS 2, red e I2C | 14/09–25/09 | Pendiente | Registro de instalación y prueba PCA9685 |
| 9 | Interfaz limitada articulación–PWM | 21/09–02/10 | Pendiente | Paquete, vigilancia y arranque seguro |
| 10 | Postura, gateo y paso cartesianos | 01/05–14/08 | Completada | Código, configuración y validaciones |
| 11 | Curva de descenso y contactos | 17/08–28/08 | En ejecución | Nueva exploración y CSV de transiciones |
| 12 | Líneas base finales | 31/08–11/09 | Pendiente | Dos ensayos por marcha y hashes |
| 13 | Transferencia gradual al robot | 05/10–23/10 | Pendiente | Listas de chequeo y registros |
| 14 | Especificación de RL acotado | 07/09–18/09 | Pendiente | Observaciones, acciones y recompensa congeladas |
| 15 | PPO con cinco semillas | 21/09–16/10 | Pendiente | Semillas 11, 23, 37, 53 y 71 |
| 16 | Selección e integración de política | 19/10–30/10 | Pendiente | Validación separada y supervisor |
| 17 | Protocolo y métricas aprobadas | 18/08–28/08 | En ejecución | Aval del profesor y matriz congelada |
| 18 | Comparación final nominal/RL | 02/11–13/11 | Pendiente | 400 ciclos programados |
| 19 | Análisis estadístico | 09/11–20/11 | Pendiente | Dataset, IC y tablas |
| 20 | Integración en la tesis | 16/11–27/11 | Pendiente | PDF completo para revisión |
| 21 | Versión final reproducible | 30/11–04/12 | Pendiente | PDF, anexos, datos, hashes y cambios |

## Regla de actualización semanal

Al terminar cada semana se añade una entrada en
[`PROGRESO_SEMANAL.md`](PROGRESO_SEMANAL.md) con actividades ejecutadas,
evidencias, desviaciones, decisiones del profesor y objetivo siguiente.
