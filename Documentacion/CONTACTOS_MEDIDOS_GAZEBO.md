# Contactos medidos de los pies en Gazebo

Versión: 14 de agosto de 2026.

## Implementación

El URDF incorpora un sensor de contacto de 100 Hz en la colisión esférica de
cada pie. Las uniones fijas de los pies se preservan al convertir URDF a SDF
para mantener juntos sensor y colisión. `ros_gz_bridge` transporta los cuatro
mensajes `gz.msgs.Contacts` a `ros_gz_interfaces/msg/Contacts`.

Entradas crudas:

- `/nova/contacts/front_left`;
- `/nova/contacts/front_right`;
- `/nova/contacts/rear_left`;
- `/nova/contacts/rear_right`.

El nodo `contact_monitor` publica dos mensajes JSON de tipo
`std_msgs/msg/String`:

- `/nova/foot_contacts`: estado observado por pie, validez, antigüedad de la
  muestra y fuerza aproximada;
- `/nova/contact_diagnostics`: fase, contactos previstos y observados,
  contactos faltantes, contactos inesperados y coincidencia.

La fuerza se calcula con las magnitudes disponibles en los `wrenches` de
Gazebo. En la versión instalada, el puente puede entregar una lista de contacto
válida sin transmitir fuerzas distintas de cero; por ello es una métrica
aproximada y el booleano de contacto es la señal primaria.

## Semántica de validez

Un sensor se considera inicializado cuando ha entregado su primera muestra.
Después, Gazebo puede dejar de publicar al desaparecer la colisión: una edad
superior a 0,10 s significa `contact=false`, no sensor averiado. La detección de
pérdida real del flujo completo requerirá un heartbeat independiente. El galope
continúa con plan no disponible. El monitor es exclusivamente informativo y no
ordena una parada automática.

Los flujos nativos pueden superar la tasa nominal en esta versión de Gazebo.
El monitor usa QoS `best effort`, profundidad 1 y limita la salida consolidada
a 100 Hz para conservar solamente la medición reciente y no retrasar la fase.

## Validación realizada

- El URDF fue convertido y revisado como SDF efectivo.
- Los cuatro flujos crudos entregaron contactos en Gazebo.
- En `stand`, el consolidado observó `fl`, `fr`, `rl` y `rr`, todos válidos.
- En gateo, fase 7 del ciclo 10, se esperaban `fl`, `fr` y `rl`; se observaron
  también los cuatro apoyos y el comparador informó `rr` como inesperado.
- En `step`, fase 27 del ciclo 1, se esperaban `fl`, `fr` y `rr`; se observaron
  los cuatro apoyos y el comparador informó `rl` como inesperado.
- Pasaron 32 pruebas automatizadas y ambos paquetes compilaron.

Las discrepancias observadas no son fallos del comparador: muestran que el
instante geométrico de elevación o descenso no coincide necesariamente con toda
la ventana discreta asignada a oscilación. Deben cuantificarse por transición y
por ciclo antes de fijar tolerancias o ampliar el supervisor.

## Ensayo cuantitativo posterior

La medición pendiente quedó completada con la bolsa válida
`Experimentos/rosbag2/contactos_gateo_validado_20260814_1410`. Contiene 76
ciclos completos, 329,856750 s entre marcadores, 176.657 mensajes y cero
activaciones del supervisor. El analizador reproducible es
`Experimentos/analizar_contactos_rosbag.py`.

La coincidencia simultánea ponderada por tiempo fue 32,550 %. FL y FR
despegaron aproximadamente 0,380 s tarde y aterrizaron aproximadamente 1,364 s
tarde. RL y RR no presentaron transición de despegue y permanecieron apoyadas,
deslizándose durante su oscilación prevista. Esto demuestra que avance visual y
ausencia de caída no bastan para afirmar que se ejecuta el patrón de contactos.

## Siguiente paso vigente

Corregir el generador de gateo para lograr despegue trasero y reducir los
retardos delanteros, sin convertir todavía estas discrepancias en paradas
automáticas. La trayectoria corregida será una nueva versión experimental y
deberá repetir el ensayo cuantitativo antes de calcular el polígono de soporte.
