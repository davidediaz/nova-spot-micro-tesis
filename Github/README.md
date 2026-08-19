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
- El hardware no se ha energizado.

Para el estado técnico completo, consultar:

- [`CONTINUIDAD.md`](../CONTINUIDAD.md)
- [`Seguimiento/Seguimiento.md`](../Seguimiento/Seguimiento.md)
- [`Documentacion/PROTOCOLO_EXPERIMENTAL_BORRADOR.md`](../Documentacion/PROTOCOLO_EXPERIMENTAL_BORRADOR.md)

## Regla de actualización

No se marca una tarea como terminada sin un archivo, prueba, registro o informe
que permita comprobarla. Las bolsas rosbag2 y los directorios de compilación se
conservan localmente, pero no forman parte del repositorio público por su tamaño.
