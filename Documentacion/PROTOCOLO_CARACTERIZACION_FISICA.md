# Protocolo de caracterización física de Nova Spot Micro

Estado: preparado, no ejecutado. Este protocolo no autoriza energizar el robot.

## Propósito y productos

El procedimiento contrasta el ejemplar construido con los valores nominales
del modelo. Debe producir fotografías originales, dos CSV diligenciados, el
mapa físico de los doce servos, la ficha de inspección y una decisión explícita
sobre la actualización de URDF, MJCF y parámetros cinemáticos.

Archivos de captura:

- `caracterizacion_fisica_geometria.csv`;
- `caracterizacion_fisica_masas.csv`;
- `FICHA_CARACTERIZACION_FISICA.md`;
- `Raspberry/configuracion/calibracion_servos.csv`.

Los valores de la columna `modelo_nominal` son referencias del software, no
mediciones del robot. Una celda vacía nunca se interpreta como cero.

## Condiciones previas

1. Completar y revisar el ensamble, incluida la tapa izquierda de fémur.
2. Apagar Raspberry, Arduino, PCA9685 y fuente de servos; comprobar ausencia de
   PWM y desconectar la batería o fuente.
3. Colocar el robot sobre una mesa estable y usar soporte cuando una pata deba
   quedar libre.
4. Registrar instrumento, resolución, fecha y responsable. No estimar datos.
5. No desmontar un subconjunto si existe riesgo de dañar cableado o perder una
   referencia mecánica; marcarlo como `no_medible` y explicar la razón.

## Secuencia de medición

### 1. Identificación y fotografías

Asignar F01--F22 según la ficha. Fotografiar una regla o escala cuando ayude a
interpretar la geometría. Conservar originales y registrar sus hashes SHA-256.
Identificar los dos servos sustituidos y los acoples reforzados.

### 2. Geometría

Medir entre ejes de rotación, no entre extremos visuales de las piezas. Para
cada magnitud realizar tres lecturas independientes, retirando y recolocando el
instrumento. Registrar milímetros con la precisión real del instrumento.

Calcular:

`media = (m1 + m2 + m3) / 3`

`diferencia_modelo = media - modelo_nominal`

Repetir coxa, fémur y tibia para las cuatro patas; no asumir simetría. Si la
dispersión máxima entre repeticiones supera dos veces la resolución del
instrumento, repetir la medición y dejar constancia.

### 3. Masas

Tarar la balanza antes de cada conjunto y repetir tres veces. La masa total es
obligatoria. Las masas de patas o subconjuntos solo se obtienen si el desmontaje
es seguro. Los valores nominales actuales provienen del modelo simplificado y
deben reemplazarse o justificarse tras la medición.

### 4. Mapa físico y calibración posterior

Con el robot todavía desenergizado, seguir cada cable desde CH0--CH11 hasta la
articulación y escribir el resultado en la ficha. El mapa propuesto es FL
CH0--2, FR CH3--5, RL CH6--8 y RR CH9--11; debe confirmarse físicamente.

La identificación del cableado no equivale a calibración. Centro PWM, límites,
sentido y velocidad se medirán después, canal por canal, únicamente cuando la
parada por OE, la alimentación y el soporte mecánico hayan sido aprobados.

## Criterios de aceptación

- Cada dimensión obligatoria contiene tres mediciones, media, diferencia,
  instrumento, resolución, fecha y evidencia.
- La masa total contiene tres repeticiones; los subconjuntos no medibles están
  justificados.
- Los doce canales tienen articulación confirmada y fotografía o anotación de
  trazado físico.
- Se registraron sustituciones, holguras, topes, cables tensionados y asimetrías.
- Ningún valor pendiente se copió a `servos.yaml` ni habilitó
  `hardware_ready`.
- Se emitió una tabla nominal--medido y una decisión versionada sobre qué
  parámetros actualizar.

Hasta cumplirlos, OE1 permanece parcial y no se ejecutan posturas o marchas
físicas.
