# Seguimiento

## Proyecto

Desarrollo y evaluación del control de locomoción del robot cuadrúpedo Nova
Spot Micro mediante una marcha nominal convencional y una política de
aprendizaje por refuerzo que aplique correcciones pequeñas, acotadas y
supervisadas.

Última actualización documental: 31 de agosto de 2026, America/Bogota.

## Punto de partida confirmado

No se parte de cero. Ya están implementados y comprobados:

- ROS 2 Humble con los paquetes `nova_gait_controller` y
  `nova_sm3_description`.
- Modelo provisional coherente en URDF/Gazebo y MJCF/MuJoCo.
- Cinemática directa e inversa propia para las cuatro patas.
- Jacobianos, masa, Coriolis, gravedad, dinámica inversa, centro de masa,
  margen estático, modelo MG996R y contacto penalizado.
- Control de postura, parada y gateo cartesiano mediante 12 articulaciones.
- Gateo estable en Gazebo durante más de diez ciclos: avance de 0,21887 m,
  altura entre 0,22287 y 0,22428 m y desviación lateral máxima de 0,00986 m.
- Parámetros base del gateo: 24 muestras, paso de 18 mm, elevación de 14 mm,
  0,18 s por muestra y ciclo de 4,32 s.
- Nodo de métricas de pose 3D y estados articulares.
- Supervisor provisional de simulación que ordena `stand` ante altura o
  inclinación insegura; su activación provocada ya fue verificada.
- Documentación matemática y técnica del código, ROS 2 y simulación.
- Word matemático consolidado el 14 de agosto de 2026 a partir de las fórmulas
  corregidas y la guía de complementos: 22 páginas, 37 ecuaciones/gráficos
  preservados y secciones detalladas sobre workspace, singularidades, J̇,
  contacto, estabilidad, identificación, validación y sensibilidad.
- Scripts preparatorios para Raspberry Pi 4 Model B con Ubuntu 22.04 y ROS 2
  Humble.

La referencia `mike4192/spot_micro_kinematics_python` se conserva como apoyo
conceptual para cinemática, transferencia de peso y marcha cuasiestática. La
implementación del proyecto es propia y está adaptada al URDF NovaSM3.

## Lo que falta, en orden de ejecución

### 1. Registrar y analizar la línea base en Gazebo

Estado: **completado el 14 de agosto de 2026**.

- [x] Grabar con `rosbag2` al menos diez ciclos continuos de gateo sin cambiar
  paso, altura ni velocidad.
- [x] Registrar pose 3D, estados articulares, métricas, órdenes de marcha y
  activaciones del supervisor.
- [x] Automatizar el cálculo de avance por ciclo, velocidad, desviación
  lateral, altura, roll, pitch y continuidad articular.
- [x] Guardar fecha, versión del código, configuración y duración de cada
  ensayo.
- [x] Repetir el ensayo para comprobar reproducibilidad y no depender de una
  sola ejecución favorable.

Criterio de cierre: bolsa reproducible, tabla de resultados y gráficas de al
menos diez ciclos con la configuración nominal congelada.

Avance del 14 de agosto de 2026: se creó la bolsa válida
`Experimentos/rosbag2/linea_base_gateo_limpia_20260814_0925`, con 98,978769 s
continuos entre las órdenes `gateo` y `stand` (20 ciclos ejecutados completos),
83.442 mensajes y cero activaciones del supervisor. Se guardó el registro del
ensayo, parámetros congelados, tópicos, resumen preliminar y SHA-256 dentro de
la bolsa. La primera tentativa `linea_base_gateo_20260814_0918` quedó marcada
como inválida porque había nodos ROS 2 duplicados. El análisis, el CSV y las
gráficas quedaron en `Experimentos/analisis/linea_base_gateo_limpia_20260814_0925`.
La duración configurada era 4,32 s por ciclo, pero las referencias articulares
muestran 4,797996 s de media: el temporizador publicó las fases aproximadamente
cada 0,20 s. Permanece pendiente la repetición de reproducibilidad.
La auditoría `AUDITORIA_TOPICOS.md` confirma 10.232 mensajes de pose 3D, 17.372
estados articulares, 10.231 mensajes de métricas, las órdenes `gateo` y
`stand`, y cero eventos de seguridad en el tópico del supervisor.

Repetición completada el 14 de agosto de 2026: la bolsa válida
`repeticion_gateo_limpia_20260814_0956` contiene 36 ciclos completos y cero
activaciones del supervisor. Se compararon los primeros 20 ciclos de cada
ensayo; en régimen permanente (ciclos 2--20) las diferencias relativas fueron
-0,102 % en avance, -0,036 % en velocidad, 0,193 % en excursión lateral,
-0,001 % en altura, -0,000 % en roll y -0,002 % en pitch. Los hashes del código,
configuración, analizador y bolsa están en `REGISTRO_REPETICION.md`. La tentativa
`repeticion_gateo_20260814_0948` se marcó inválida porque no almacenó la orden
inicial `gateo`.

Corrección posterior: el planificador temporal dejó de acumular el retraso del
callback de 20 ms. Las 24 pruebas pasaron y una validación ligera de seis ciclos
midió 0,180003383 s por fase y 4,320106573 s por ciclo. Esta es una nueva versión
experimental; requiere su propia línea base y repetición en Gazebo, separadas de
las dos bolsas anteriores.

Nueva línea base corregida: `linea_base_cadencia_corregida_20260814_1049`, con
13 ciclos, ciclo observado medio de 4,320013 s, 32.352 mensajes y cero eventos
del supervisor. Su análisis y gráficas están en
`Experimentos/analisis/linea_base_cadencia_corregida_20260814_1049`. Falta una
repetición equivalente de esta nueva versión.

Repetición corregida completada: `repeticion_cadencia_corregida_20260814_1100`,
con 13 ciclos, 32.395 mensajes y cero eventos del supervisor. La comparación de
los ciclos 2--13 arrojó diferencias menores al 0,2 % en duración, avance,
velocidad, excursión lateral, altura, roll, pitch y continuidad articular. La
línea base de la versión corregida queda cerrada y reproducida.

### 2. Cerrar las definiciones experimentales con los directores

Estado: **pendiente de acuerdo**.

- [x] Redactar formalmente qué significa `paso` en esta tesis: movimiento de una
  pata o secuencia completa de cuatro patas.
- [x] Documentar el orden de apoyo/oscilación del `gateo` y qué constituye un
  ciclo completo.
- [x] Definir en borrador ensayo, ciclo válido, fallo, intervención y caída.
- [x] Aprobar y adoptar número de ensayos, ciclos por condición y semillas de
  RL.
- [ ] Aprobar métricas principales, frecuencia de muestreo y criterios
  numéricos de éxito.
- [ ] Resolver la aparente contradicción de la tesis sobre el nivel de modelo
  dinámico que se entregará.

Criterio de cierre: protocolo escrito y aprobado antes de iniciar el
experimento comparativo.

Borrador técnico creado en
`Documentacion/PROTOCOLO_EXPERIMENTAL_BORRADOR.md`. Propone paso como oscilación
completa de una pata, ciclo como 24 referencias con las cuatro oscilaciones y
orden FL--RR--FR--RL. Define ensayo, transitorio, validez, fallo, intervención,
caída, datos, métricas, umbrales provisionales y alcance del modelo. Las
cantidades quedaron fijadas internamente en cinco ensayos de 20 ciclos por
condición y semillas RL `11`, `23`, `37`, `53`, `71`. La decisión está en
`Documentacion/DECISION_TAMANO_MUESTRAL_Y_SEMILLAS_RL.md`. La métrica primaria,
los umbrales y la redacción final permanecen pendientes.

### 3. Implementar la marcha `paso`

Estado: **implementada y validada en Gazebo y MuJoCo**.

- [x] Diseñar transferencia de peso, elevación, avance, colocación y
  recuperación estable.
- [x] Contrastar la secuencia con la referencia de Mike4192 sin copiar sus
  parámetros físicos.
- [x] Generar la trayectoria en espacio cartesiano y convertirla con la IK
  propia.
- [x] Validar alcanzabilidad, límites y continuidad.
- [x] Añadir pruebas unitarias y parámetros configurables.
- [x] Validar al menos diez ciclos en Gazebo y MuJoCo.
- [x] Relegar `galope` a experimento opcional de simulación.

Criterio de cierre: paso definido, documentado y repetible sin caída en ambos
simuladores.

Implementación inicial del 14 de agosto de 2026: comando `paso/step`, 32
referencias, ciclo nominal de 5,76 s, paso de 0,016 m, elevación de 0,008 m y
transferencia lateral de 0,004 m. Pasaron 26 pruebas. Un ensayo exploratorio de
cuatro ciclos en Gazebo tuvo cero eventos de seguridad, ciclo medio de 5,759993
s, avance de 0,020730 m/ciclo, roll máximo medio de 1,275 grados y pitch máximo
medio de 2,497 grados. Diseño en `Documentacion/MARCHA_PASO_DISENO.md`.

Validación extensa completada: dos ensayos Gazebo de 12 ciclos con cero eventos
del supervisor y diferencias de medias menores al 0,4 %. MuJoCo completó 12
ciclos con duración media de 5,759999 s, error RMS articular de 0,026232 rad y
error máximo de 0,054983 rad. La pose corporal de MuJoCo aún no está expuesta,
por lo que su validación se limita a cadencia y articulaciones. Informe en
`Documentacion/MARCHA_PASO_VALIDACION.md`.

El galope quedó formalmente fuera del alcance principal y deshabilitado por
defecto mediante `enable_experimental_gallop=false`. Solo puede habilitarse de
forma explícita en simulación; no entra en las líneas base, la comparación con
RL ni las pruebas de hardware. Decisión documentada en
`Documentacion/EXPERIMENTO_GALOPE_OPCIONAL.md`.

### 4. Incorporar estabilidad y sensores en simulación

Estado: **parcial**.

- [x] Publicar fase de marcha y patas previstas en contacto.
- [x] Añadir contactos de los cuatro pies en Gazebo.
- [x] Comparar en línea contacto previsto frente a observado, inicialmente sin
  actuación automática.
- [ ] Añadir contactos equivalentes en MuJoCo.
- [ ] Añadir o conectar una IMU simulada.
- [ ] Calcular en línea el polígono de soporte y el margen de estabilidad con
  contactos y centro de masa.
- [ ] Extender el supervisor con contacto inesperado, pérdida de comunicación,
  límites articulares y referencias inválidas.
- [ ] Definir mecanismo de rearme seguro del supervisor.
- [x] Ejecutar las pruebas unitarias nuevas con `python3 -m pytest`.

Criterio de cierre: métricas y supervisor reaccionan correctamente a pruebas
provocadas de altura, inclinación, contacto y pérdida de datos.

Avance del 14 de agosto de 2026: cuatro sensores de 100 Hz funcionan en Gazebo,
el nodo `contact_monitor` publica `/nova/foot_contacts` y
`/nova/contact_diagnostics`, y 32 pruebas pasan. Se confirmaron cuatro apoyos
válidos en `stand` y discrepancias detectadas correctamente durante `crawl` y
`step`. El monitor no detiene ni modifica la marcha. Detalles en
`Documentacion/CONTACTOS_MEDIDOS_GAZEBO.md`.

Ensayo cuantitativo completado: la bolsa
`contactos_gateo_validado_20260814_1410` contiene 76 ciclos y seis marcadores.
La coincidencia simultánea fue 32,550 %. Las patas delanteras despegaron unos
0,38 s tarde y aterrizaron unos 1,364 s tarde; las traseras no despegaron y
deslizaron. Cero eventos del supervisor. Antes de calcular un polígono de
soporte útil debe corregirse la trayectoria de gateo y repetir esta medición.

El controlador publica `/nova/gait_phase` como JSON sincronizado con cada
referencia. Incluye modo, muestra, ciclo, pata en oscilación y tres contactos
previstos para `crawl` y `step`; `gallop` declara el plan no disponible. Pasaron
29 pruebas y se verificó un mensaje ROS 2 real. Contrato documentado en
`Documentacion/FASE_Y_CONTACTOS_PREVISTOS.md`.

Iteración exploratoria del 17 de agosto de 2026: se añadió transferencia
lateral de 4 mm y longitudinal parametrizable al gateo, sin cambiar paso,
altura, muestras ni cadencia. Con 8 mm longitudinales se obtuvo el mejor valor
exploratorio (35,787 % de coincidencia simultánea, 13 ciclos), y por primera vez
hubo transiciones de las patas traseras. No obstante, sus despegues permanecen
1,17--1,19 s tarde. Pasan 35 pruebas y el paquete compila, pero el punto sigue
parcial: debe separarse la precarga de la oscilación y reflejar las subfases en
`/nova/gait_phase` antes de una nueva línea base formal.

Subfases implementadas y verificadas el 17 de agosto de 2026: cada cuarto de
gateo publica transferencia, precarga, despegue, vuelo, aterrizaje y contacto
final, con un plan de cuatro o tres apoyos coherente con la referencia. En 15
ciclos exploratorios, los cuatro despegues quedaron entre 0,133 y 0,141 s tarde;
RL y RR ya despegan en su ventana correcta. Hubo cero eventos del supervisor y
36 pruebas pasan. Falta ajustar aterrizajes: delanteras aproximadamente 0,50 s
tarde y traseras 0,33 s antes. No se ha congelado una línea base nueva.

Iteración del 18 de agosto de 2026: se hizo configurable la altura de `landing`
por eje y se ensayó el contraste continuo 0,20 delante / 0,80 detrás durante 22
ciclos completos. Los aterrizajes delanteros quedaron 0,446--0,455 s tarde y
los traseros 0,323--0,327 s antes; la mejora fue insuficiente. El contraste fue
descartado y los valores nominales volvieron al perfil sinusoidal 0,70710678.
Los despegues corregidos no se degradaron. Pasan 37 pruebas y el paquete
compila. La siguiente iteración debe modificar la curva completa de descenso,
no solamente la penúltima referencia.

Iteración del 20 de agosto de 2026: el mismo parámetro observable (altura
normalizada al 75 % de la oscilación) controla ahora una curva continua de
potencia desde el ápice hasta `touchdown`, diferenciable por eje. El ascenso
permanece inalterado. Con 24 muestras y el valor nominal, las referencias son
numéricamente iguales a las anteriores, por lo que aún no se reclama una
mejora física ni una nueva línea base. Pasan 39 pruebas y el paquete compila.
Falta comparar candidatos cartesianos y ensayarlos en Gazebo.

Criba cartesiana del 24 de agosto de 2026: se compararon nueve contrastes y el
control nominal con `Experimentos/evaluar_curvas_descenso.py`. Seis contrastes
con relación delantera 0,20--0,50 y trasera 0,75--0,80 cumplen alcanzabilidad,
periodicidad y salto articular menor de 0,20 rad; 0,85 detrás se descartó por
alcanzar 0,203263 rad. Pasan 39 pruebas. El informe está en
`Experimentos/curvas_descenso_cartesianas_20260824/INFORME_CRIBA_CARTESIANA.md`.
La siguiente exploración Gazebo usará nominal, 0,20/0,75, 0,20/0,80 y
0,50/0,75. El protocolo conserva un umbral provisional de 0,05 rad que no
cumple ni el nominal (0,170014 rad), por lo que requiere acuerdo formal.

Exploración Gazebo del 27 de agosto de 2026: se compararon esas cuatro curvas
en ventanas estrictas de 10--13 ciclos, con cero eventos del supervisor. La
coincidencia simultánea fue 20,949 % nominal, 23,855 % para 0,20/0,75,
23,721 % para 0,20/0,80 y 21,728 % para 0,50/0,75. Los despegues se mantuvieron
entre 0,132 y 0,143 s tarde. `0,20/0,75` redujo los aterrizajes delanteros a
0,436/0,460 s tarde, pero los traseros continuaron unos 0,32 s antes. Es el
candidato provisional, no una nueva línea base. Informe en
`Experimentos/exploracion_curvas_descenso_gazebo_20260827/INFORME_COMPARACION.md`.

Exploración del 31 de agosto de 2026: las transiciones mostraron que RL y RR
recuperaban contacto 0,07--0,08 s después del despegue observado, todavía en
ascenso. Se añadió una relación independiente de altura trasera al 25 % de la
oscilación. La criba aceptó como máximo 0,80 (salto 0,189604 rad); desde 0,85
se supera 0,20 rad. En Gazebo, 0,20/0,75 con ascenso 0,80 completó 15 ciclos,
pero solo desplazó los aterrizajes traseros a -0,305/-0,309 s y obtuvo 23,644 %
de coincidencia. El candidato fue rechazado y `gaits.yaml` conserva el nominal.
La próxima iteración debe revisar liberación física y semántica/debounce del
contacto; no seguir aumentando la altura temprana.

### 5. Caracterizar físicamente el robot sin energizar

Estado: **bloqueado temporalmente por ensamble incompleto**.

Actualización del 31 de agosto de 2026: falta imprimir y montar la pieza
`SM3_Cover_LeftFemur.stl` de la pata izquierda. Hasta completar esa pieza no se
consideran definitivas la inspección, las fotografías ni las mediciones de la
geometría física. Fuente indicada para impresión:
`https://github.com/cguweb-com/Arduino-Projects/blob/main/Nova-SM3/STL%20Files/SM3%20Files/SM3_Cover_LeftFemur.stl`.
La ficha de caracterización está preparada, pero no debe llenarse con valores
parciales presentados como robot terminado.

- [ ] Fotografiar estructura, patas, articulaciones, electrónica y cableado.
- [ ] Confirmar que las doce unidades sean MG996R y registrar fabricante o
  diferencias visibles.
- [x] Confirmar Raspberry Pi 4 Model B, PCA9685, BNO055 y demás componentes
  disponibles.
- [ ] Medir tres veces separaciones de cadera, longitudes de coxa/fémur/tibia y
  dimensiones del cuerpo.
- [ ] Medir masa total, cuerpo/electrónica y patas cuando sea posible.
- [ ] Inspeccionar holguras, topes, tornillos, rodamientos, pies y colisiones.
- [ ] Registrar toda diferencia frente al modelo provisional.

Criterio de cierre: inventario con evidencia fotográfica y mediciones
trazables. Esta fase no autoriza energizar los doce servos.

### 6. Diseñar y verificar la seguridad eléctrica

Estado: **pendiente**.

- [ ] Medir primero la corriente de un MG996R asegurado, sin carga y con límite
  de corriente.
- [ ] Seleccionar fuente de servos a partir de mediciones reales, no del
  consumo promedio ni únicamente de una hoja de datos.
- [ ] Dimensionar distribución, calibre de cable, conectores y fusible.
- [ ] Mantener alimentación lógica y potencia de servos separadas con tierra
  común controlada.
- [ ] Implementar parada física que corte o deshabilite potencia de actuadores
  sin depender de ROS 2.
- [ ] Definir el comportamiento seguro del pin `OE` del PCA9685.
- [ ] Seleccionar medición de tensión/corriente y confirmar la necesidad real
  de sensores de temperatura.

Criterio de cierre: esquema revisado, protecciones instaladas y protocolo de
emergencia probado antes de conectar simultáneamente los servos.

### 7. Calibrar los doce MG996R

Estado: **bloqueado hasta completar la seguridad eléctrica**.

- [ ] Calibrar un servo a la vez con el robot asegurado.
- [ ] Registrar canal, centro PWM, sentido, pulsos mínimo/máximo y límites
  mecánicos seguros.
- [ ] Medir corriente sin carga, bajo carga controlada y temperatura.
- [ ] Crear un archivo YAML de calibración por articulación.
- [ ] Probar una pata suspendida antes de habilitar las cuatro.
- [ ] Sustituir en URDF/MJCF los límites y parámetros provisionales que puedan
  identificarse.

Criterio de cierre: doce calibraciones trazables, sin colisiones ni topes
mecánicos, revisadas antes de apoyar el robot.

### 8. Preparar Raspberry Pi 4 e interfaz PCA9685

Estado: **scripts listos; hardware y microSD pendientes**.

- [ ] Conectar e identificar explícitamente una microSD.
- [ ] Instalar Ubuntu Server 22.04 ARM64 con SSH habilitado.
- [ ] Ejecutar y verificar los scripts de preparación de ROS 2 Humble.
- [ ] Confirmar Wi-Fi/SSH, `ROS_DOMAIN_ID`, DDS, reloj e I2C.
- [ ] Probar PCA9685 sin servos y comprobar PWM con instrumento.
- [ ] Desarrollar la interfaz física `ros2_control` usando las calibraciones
  medidas.
- [ ] Integrar BNO055, corriente/tensión, contactos y estado de parada.
- [ ] Añadir vigilancia por pérdida de comunicación y arranque con salidas
  deshabilitadas.

Avance del 18 de agosto de 2026: se detectó la Raspberry como `arm64`, con
Ethernet `192.168.0.132`, Wi-Fi `192.168.0.134` y SSH activo, habilitado y
escuchando en el puerto 22. Tenía Ubuntu 24.04.4 LTS y no tenía ROS 2. Se decidió
descartar esa instalación y reinstalar Ubuntu Server 22.04 LTS ARM64 para usar
la misma distribución ROS 2 Humble del computador de Gazebo. La unidad aún no
se ha conectado al computador ni se ha sobrescrito. La próxima comprobación
obligatoria es identificar de forma inequívoca el dispositivo de almacenamiento
antes de grabar la imagen.

Avance del 19 de agosto de 2026: se identificó `/dev/sda` como la unidad USB
extraíble de 28,9 GiB de la Raspberry, separada del NVMe interno. Se verificó el
SHA-256 oficial y se grabó correctamente Ubuntu 22.04.5 Desktop ARM64 con
interfaz gráfica (9.269.411.840 bytes, salida cero y `sync` completado). Las
particiones resultantes fueron `system-boot` y `writable`. Permanecen pendientes
el primer arranque y la comprobación en la Raspberry de versión, escritorio,
red, SSH y expansión del sistema de archivos; no marcar todavía como completada
la instalación de Ubuntu.

Avance del 20 de agosto de 2026: el primer arranque confirmó una Raspberry Pi
4 Model B con Ubuntu 22.04.5 LTS Desktop ARM64 (`aarch64`). Se conectó por
Wi-Fi en `192.168.0.101`; se instaló y habilitó `openssh-server`, y el acceso
desde el computador principal fue verificado. La actualización propuesta a
Ubuntu 24.04 fue cancelada para conservar compatibilidad con ROS 2 Humble.
La comunicación ROS 2 por Wi-Fi aún no se marca como validada: falta instalar
`ros-humble-demo-nodes-cpp` donde sea necesario y demostrar `talker/listener`
con dominio 42. No se conectaron ni energizaron servos.

Validación completada el 20 de agosto de 2026: con el `talker` en la Raspberry
Pi 4 y el `listener` en el computador principal se recibieron por Wi-Fi los
mensajes `Hello World: 378`--`385` durante aproximadamente 8 s, usando
`ROS_DOMAIN_ID=42` y `ROS_LOCALHOST_ONLY=0`. DDS queda validado para esta red.
La siguiente tarea es clonar y compilar el workspace en la Raspberry; los
actuadores permanecen desconectados.

La primera compilación del workspace en la Raspberry reveló que
`nova_sm3_description/CMakeLists.txt` intentaba instalar una carpeta `worlds`
vacía que no se conserva en Git. Se corrigió el instalador para usar solo
`config`, `launch`, `mujoco`, `rviz` y `urdf`; la corrección está pendiente de
actualizarse en la Raspberry y verificarse allí. No se ejecutaron nodos ni
hardware.

Verificación completada: la Raspberry actualizó al commit `d1e3525`, compiló
los dos paquetes y reconoció `nova_gait_controller` y
`nova_sm3_description`. No se ejecutó ningún launch, controlador, trayectoria
ni componente del PCA9685.

La validación del overlay también quedó completada: existe
`/home/pavilion/nova-spot-micro-tesis/install/setup.bash` y, tras cargarlo,
ambos paquetes aparecen con código de salida 0. No hay nodos, procesos físicos,
adaptadores I2C ni PWM activos. La siguiente fase será preparar I2C/PCA9685
con seguridad eléctrica cerrada.

Prueba I²C completada el 20 de agosto de 2026: con servos y `V+` desconectados,
la Raspberry detectó `0x40` y `0x70` en `i2c-1` mediante `i2cdetect`. El enlace
lógico con el PCA9685 queda validado; la potencia, OE, PWM y actuadores siguen
pendientes y no se ejecutó ningún controlador.

Estado al cierre de sesión: el LM2596 recibe 8 V y entrega aproximadamente 5 V
al rail `V+` del PCA9685; no hay servos conectados ni PWM habilitado. La próxima
sesión comenzará con las mediciones de `VCC`, `V+`, `OE`, tierra común y
protecciones, seguida de una prueba individual con un MG996R en `CH0`, sin
carga mecánica. La marcha del robot y la conexión de los doce servos siguen
bloqueadas.

Criterio de cierre: referencias articulares convertidas de forma limitada a
PWM, inicialmente sin actuadores y después con un solo servo.

### 9. Transferir progresivamente la marcha nominal

Estado: **prohibido iniciar antes de cerrar caracterización, calibración y
seguridad**.

- [ ] Ejecutar software con PCA9685 deshabilitado.
- [ ] Probar un servo y luego una pata suspendida.
- [ ] Probar cuatro patas con el robot suspendido.
- [ ] Mantener postura sobre el suelo con soporte y parada accesible.
- [ ] Ejecutar transferencia de peso y un paso.
- [ ] Ejecutar un ciclo de gateo y después ciclos continuos.
- [ ] Registrar orientación, corriente, tensión, temperatura, intervención y
  desplazamiento externo.
- [ ] Validar la marcha nominal física antes de cualquier corrección aprendida.

Criterio de cierre: postura, paso y gateo nominales repetibles bajo el protocolo
aprobado y sin eventos de seguridad.

### 10. Desarrollar la capa correctiva de aprendizaje por refuerzo

Estado: **no iniciar todavía**.

- [ ] Definir observaciones disponibles tanto en simulación como en hardware.
- [ ] Definir acciones como correcciones pequeñas de referencias nominales,
  nunca PWM directo.
- [ ] Fijar saturaciones, tasa máxima de cambio y autoridad del supervisor.
- [ ] Formular recompensa, terminaciones y currículo.
- [ ] Entrenar inicialmente PPO en MuJoCo con varias semillas.
- [ ] Aleatorizar masas, fricción, centro de masa, ganancias, retardos y ruido.
- [ ] Validar la política en Gazebo antes de cualquier transferencia.
- [ ] Conservar configuraciones, semillas, curvas, modelos y versiones.

Criterio de cierre: mejora repetible de métricas físicas frente a la misma
marcha nominal, sin aumentar caídas, saturaciones ni intervenciones.

### 11. Ejecutar la comparación experimental final

Estado: **fase final**.

Comparaciones obligatorias:

1. marcha nominal sin aprendizaje;
2. la misma marcha nominal con corrección aprendida.

Para `paso` y `gateo` se deberán registrar como mínimo los ciclos y ensayos
aprobados, con condiciones iniciales equivalentes. El análisis incluirá:

- inclinación RMS y máxima;
- avance y velocidad por ciclo;
- desviación lateral;
- variabilidad entre ciclos;
- margen de estabilidad;
- ciclos completados, fallos, caídas e intervenciones;
- corriente, tensión, temperatura y energía si la instrumentación lo permite;
- seguimiento articular solamente si existe medición física real de posición.

Criterio de cierre: conjunto de datos, análisis estadístico, comparación
nominal frente a nominal más RL y trazabilidad completa de cada ensayo.

### 12. Completar y corregir la tesis

Estado: **parcial**.

- [ ] Actualizar la introducción para explicar claramente la comparación con la
  capa correctiva RL.
- [ ] Incorporar los resultados técnicos ya comprobados sin presentar el
  modelo provisional como gemelo digital.
- [ ] Definir el nivel de modelado dinámico entregado y eliminar contradicciones
  de alcance.
- [ ] Corregir el presupuesto: suma directa de 1.591.800 COP frente al resumen
  de 2.029.270 COP y aclarar el precio de los 12 DS18B20.
- [ ] Eliminar o reemplazar el texto de plantilla de `AppendixA.tex` antes de
  incluir apéndices.
- [ ] Mantener una sola bibliografía mediante `\printbibliography`; no usar la
  lista manual de `Chapters/11 Referencias.tex`.
- [ ] Actualizar metodología, cronograma y trazabilidad según el protocolo
  definitivo.
- [ ] Incorporar tablas, gráficas, limitaciones y resultados de la comparación.

Criterio de cierre: PDF final compilado, objetivos trazables a resultados y
afirmaciones respaldadas por evidencia experimental.

## Próxima acción concreta

Sin modificar la longitud de paso de 18 mm, la elevación máxima de 14 mm ni la
cadencia de 0,18 s por referencia:

1. revisar la correspondencia entre ausencia de mensajes, despegue real,
   recontacto breve y `touchdown`; el falso vuelo dura aproximadamente el mismo
   orden que el timeout de 0,10 s;
2. diseñar una corrección de liberación trasera que no aumente la altura
   temprana por encima de 0,80 ni exceda 0,20 rad;
3. completar la caracterización física con
   `Documentacion/FICHA_CARACTERIZACION_FISICA.md`;
4. obtener las decisiones del profesor mediante
   `Documentacion/FICHA_APROBACION_PROTOCOLO.md`;
5. repetir en Gazebo frente a nominal y 0,20/0,75 solo después de definir una
   hipótesis nueva y verificable.

El supervisor de contactos seguirá informativo durante esta corrección. No se
debe comenzar PPO ni mover el hardware hasta superar las etapas que lo bloquean.

## Regla de actualización

Al finalizar cada sesión, marcar únicamente tareas demostradas con evidencia,
registrar el archivo o prueba correspondiente y cambiar la próxima acción
concreta. No marcar como terminado algo que solo se haya propuesto o visto
funcionar una vez.

Cada cambio realizado por cualquiera de los integrantes debe quedar notificado
en GitHub: se debe crear un commit descriptivo y subirlo al repositorio público
`https://github.com/davidediaz/nova-spot-micro-tesis`. La notificación debe
resumir fecha, archivos modificados, motivo, pruebas o evidencia, resultado y
siguiente acción. Para cambios de código o documentación se recomienda trabajar
en una rama y abrir un Pull Request hacia `main`; no se deben dejar cambios
locales sin sincronizar ni reescribir silenciosamente el historial experimental.

## Actualización de hardware del 24 de agosto de 2026

Se verificó en la Raspberry Pi 4 el Arduino Mega 2560 R3 por `/dev/ttyACM0` y
la detección del PCA9685 en `0x40`, tras corregir SDA y SCL invertidos. Con
alimentación externa para los MG996R se avanzó desde pruebas individuales hasta
un barrido simultáneo de `CH5`--`CH10` a 60 Hz entre 1300 y 1700 microsegundos.
Los canales restantes permanecen en `FULL_OFF`.

Este resultado sustituye el estado anterior de «servos todavía no conectados»,
pero no cierra la caracterización ni habilita una marcha. Permanecen pendientes
la correspondencia canal-articulación, calibración independiente, ensayo de la
fuente bajo carga y parada física segura mediante OE con pull-up. Evidencia:
`Raspberry/AVANCES_PCA9685_2026-08-24.md`.
