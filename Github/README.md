# Nova Spot Micro — progreso de tesis

Abre [`index.html`](index.html) para ver el panel visual del proyecto. Puede
publicarse directamente con GitHub Pages.

Este directorio concentra el seguimiento semanal del proyecto de tesis del
cuadrúpedo Nova Spot Micro. Está pensado para que los directores puedan revisar
qué se hizo, qué evidencia se obtuvo y cuál es el siguiente paso.

## Proyecto

El proyecto desarrolla y evalúa el control de locomoción del robot NovaSM3
mediante:

- una marcha nominal cartesiana (`gateo` y `paso`);
- métricas de movimiento, contactos y seguridad en simulación;
- una futura capa correctiva de aprendizaje por refuerzo, acotada y supervisada.

El modelo actual es nominal y computable. Todavía no debe presentarse como un
gemelo digital identificado ni como un sistema validado en hardware.

## Progreso semanal

Consulta [`PROGRESO_SEMANAL.md`](PROGRESO_SEMANAL.md) para el resumen por semana.
Cada actualización debe incluir fecha, trabajo realizado, evidencia, problemas,
decisiones y siguiente objetivo.

## Estado actual

- ROS 2 Humble, Gazebo y MuJoCo preparados.
- Gateo y marcha paso implementados y probados en simulación.
- Línea base de cadencia corregida reproducida con diferencias menores al 0,2 %.
- Contactos de cuatro patas medidos en Gazebo.
- La trayectoria de gateo sigue en ajuste: los despegues mejoraron, pero los
  aterrizajes todavía no coinciden suficientemente con el plan previsto.
- Raspberry Pi 4 con Ubuntu 22.04.5, SSH y ROS 2/DDS por Wi-Fi verificados.
- Arduino Mega 2560 y PCA9685 verificados en `0x40`; se comprobó movimiento
  progresivo de MG996R y el sketch actual controla `CH5`--`CH10` dentro del
  rango conservador de 1300--1700 microsegundos.
- Las posturas y marchas físicas siguen bloqueadas hasta completar calibración,
  prueba de la fuente bajo carga y parada segura mediante OE.

## Código y modelo

El [índice de código](INDICE_CODIGO.md) enlaza el modelado matemático en LaTeX,
su implementación Python, la cinemática, el controlador de marcha, las
configuraciones, las pruebas y los informes experimentales. El código de
`gateo/crawl` y `paso/step` está en `src/nova_gait_controller`; no se presenta
el RL como implementado hasta que su fase correspondiente sea ejecutada y
validada.

La preparación de la Raspberry está documentada en
[`Raspberry/INSTALACION_THONNY.md`](../Raspberry/INSTALACION_THONNY.md) y el
protocolo de Ethernet, SSH, ROS 2/DDS y USB-serial en
[`Raspberry/PROTOCOLO_COMUNICACION_RASPBERRY.md`](../Raspberry/PROTOCOLO_COMUNICACION_RASPBERRY.md).
El avance comprobado del Mega y el PCA9685 está en
[`Raspberry/AVANCES_PCA9685_2026-08-24.md`](../Raspberry/AVANCES_PCA9685_2026-08-24.md).

Para el estado técnico completo, consultar:

- [`CONTINUIDAD.md`](../CONTINUIDAD.md)
- [`Seguimiento/Seguimiento.md`](../Seguimiento/Seguimiento.md)
- [`Documentacion/PROTOCOLO_EXPERIMENTAL_BORRADOR.md`](../Documentacion/PROTOCOLO_EXPERIMENTAL_BORRADOR.md)

## Regla de actualización

No se marca una tarea como terminada sin un archivo, prueba, registro o informe
que permita comprobarla. Las bolsas rosbag2 y los directorios de compilación se
conservan localmente, pero no forman parte del repositorio público por su tamaño.
