# Índice de modelado matemático y marchas

Este índice permite al profesor llegar directamente a las fuentes principales
del proyecto. Las fuentes completas están versionadas en el repositorio.

## Modelado matemático

- [Modelo matemático LaTeX](../Documentacion/MODELO_MATEMATICO_LATEX/main.tex):
  derivaciones, ejemplos, diccionario de variables y trazabilidad teoría–código–evidencia.
- [Implementación matemática Python](../src/nova_gait_controller/nova_gait_controller/mathematical_model.py):
  Jacobianos, dinámica nominal, actuadores, contacto, centro de masa y estabilidad.
- [Generador reproducible de ejemplos](../scripts/generar_ejemplos_modelo.py).
- [Cinemática de las patas](../src/nova_gait_controller/nova_gait_controller/kinematics.py):
  FK, IK, Jacobiano auxiliar y trayectorias cartesianas.
- [Diseño matemático de la marcha paso](../Documentacion/MARCHA_PASO_DISENO.md).

## Código de marchas

- [Controlador de marcha ROS 2](../src/nova_gait_controller/nova_gait_controller/gait_controller.py):
  máquina de estados, publicación de referencias, fase y comandos `stand`,
  `gateo/crawl` y `paso/step`.
- [Generador de gateo](../src/nova_gait_controller/nova_gait_controller/kinematics.py):
  transferencia, precarga, despegue, vuelo, aterrizaje y contacto final.
- [Configuración de gateo y paso](../src/nova_gait_controller/config/gaits.yaml).
- [Pruebas de cinemática y continuidad](../src/nova_gait_controller/test/test_kinematics.py).
- [Pruebas de fase y temporización](../src/nova_gait_controller/test/test_gait_timing.py).
- [Validación de marcha paso](../Documentacion/MARCHA_PASO_VALIDACION.md).

## Evidencia experimental

- [Análisis reproducible de gateo](../Experimentos/analizar_gateo_rosbag.py).
- [Análisis reproducible de contactos](../Experimentos/analizar_contactos_rosbag.py).
- [Informe de contactos medidos](../Experimentos/analisis/contactos_gateo_validado_20260814_1410/INFORME_CONTACTOS.md).
- [Comparación de reproducibilidad](../Experimentos/comparacion_cadencia_corregida_20260814/INFORME_REPRODUCIBILIDAD.md).

Cada modificación de estas fuentes debe acompañarse de pruebas y de una
actualización en `CONTINUIDAD.md`, `Github/PROGRESO_SEMANAL.md` o la bitácora
correspondiente.
