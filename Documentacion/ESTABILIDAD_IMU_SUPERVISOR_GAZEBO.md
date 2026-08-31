# Contactos robustos, IMU, margen de estabilidad y supervisor en Gazebo

Fecha: 31 de agosto de 2026, America/Bogota.

## Resultado implementado

### Contacto medido

`contact_monitor` conserva ahora dos estados por pata:

- `raw_contact`: observación derivada directamente del mensaje y su timeout;
- `contact`: estado estable después de debounce;
- `transition_pending`: indica que existe un cambio crudo aún no confirmado.

La pérdida debe persistir 0,12 s adicionales después de aparecer como estado
crudo y el recontacto debe persistir 0,03 s. Esto evita interpretar una pausa
del orden del timeout de 0,10 s como un vuelo completo. Los valores son
provisionales y deben medirse en una nueva bolsa; el filtro no se utiliza para
ocultar el contacto crudo.

### IMU simulada

Se añadió un sensor IMU de 100 Hz sobre `base_link` y el mundo propio
`worlds/nova_empty.sdf` carga el sistema IMU de Gazebo Fortress. El puente
publica `sensor_msgs/Imu` en `/nova/imu`.

Una muestra real entregó orientación casi horizontal, velocidad angular
cercana a cero y aceleración vertical aproximada de 9,8 m/s² en reposo. El
sensor no tiene todavía modelo explícito de ruido, sesgo o covarianza; por ello
no representa al BNO055 físico.

### Polígono de soporte y margen

El nodo `stability_monitor` combina:

- pose del cuerpo;
- estados articulares;
- FK nominal y posiciones provisionales de cadera;
- contactos filtrados.

Publica `/nova/stability` con puntos de pie, polígono convexo, proyección nominal
del centro de masa y margen estático firmado. Con menos de tres contactos no
colineales declara `available=false`. El campo `model=nominal_not_identified`
impide presentarlo como una medición física identificada.

### Supervisor ampliado

Además de altura y orientación, el supervisor puede observar:

- estructura, finitud y límites nominales de trayectorias articulares;
- vencimiento de pose, contactos y margen;
- discrepancias de contacto;
- margen estático negativo.

Las referencias inválidas están activas porque son un error determinista. Las
paradas por timeout, contacto y margen permanecen desactivadas por defecto
hasta cuantificar falsos positivos. El estado de una parada enclavada se publica
en `/nova/safety/status`; no se implementó todavía rearme, para evitar un rearme
automático inseguro.

## Verificación

- 47 pruebas automatizadas aprobadas.
- Fuentes Python compiladas y Xacro generado sin error.
- `nova_gait_controller` compiló e instaló `stability_monitor`.
- Gazebo publicó muestras reales en `/nova/imu`, `/nova/foot_contacts` y
  `/nova/stability`.
- Se ejecutaron aproximadamente tres ciclos cortos de gateo y se ordenó
  `stand`; no hubo publicaciones en `/nova/safety/triggered`.

## Limitaciones y siguiente ensayo

Esta validación demuestra integración, no caracteriza estadísticamente el
filtro ni aprueba los nuevos criterios de parada. El siguiente ensayo formal
debe grabar al menos diez ciclos con IMU, contacto crudo/filtrado, fase, margen,
referencias y supervisor. Debe comparar transiciones antes/después del filtro y
provocar por separado referencia no finita, pérdida de datos, contacto
inconsistente y margen negativo antes de habilitar cada parada.
