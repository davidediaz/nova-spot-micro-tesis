# Continuidad histórica de la tesis Nova Spot Micro

Última actualización: 19 de agosto de 2026, America/Bogota.

## Repositorio público de seguimiento

Desde el 19 de agosto de 2026 el proyecto tiene un repositorio público para
que el profesor pueda revisar el progreso semanal, la ruta de trabajo, la
bitácora, el código y las evidencias:

- Repositorio: <https://github.com/davidediaz/nova-spot-micro-tesis>
- Panel web: <https://davidediaz.github.io/nova-spot-micro-tesis/>
- Bitácora visual: `Github/BITACORA.html`
- Cronograma semanal: `Github/CRONOGRAMA_SEMANAL.md`
- Ruta completa: `Github/RUTA_TRABAJO.md`

Regla permanente de trazabilidad: cada cambio relevante del proyecto debe
quedar registrado en este archivo y en el repositorio público mediante un
commit descriptivo. La actualización debe indicar fecha, archivos modificados,
motivo, pruebas o evidencia, resultado y siguiente acción. No se deben
reescribir silenciosamente resultados históricos ni mezclar bolsas producidas
con configuraciones diferentes.

### Reinstalación de la memoria Raspberry Pi — 19 de agosto de 2026

Se borró y reinstaló la memoria USB/microSD de 32 GB identificada de forma
inequívoca como `/dev/sda`, modelo `Storage Device`, 28,9 GiB. El SSD interno
`/dev/nvme0n1` no fue utilizado como destino. Se empleó la imagen oficial
`ubuntu-22.04.5-preinstalled-desktop-arm64+raspi.img.xz`, cuyo SHA-256 fue
`74764944dd4a96bdddd30cf1ffc133ecbe5ebb1d1f2eaa34cd5f8fbb57211c86`.

La escritura terminó con 9.269.411.840 bytes y sincronización completada. La
tabla resultante muestra `system-boot` (512 MiB, FAT) y `writable` (8,1 GiB,
ext4). El script reproducible y protegido por comprobación de modelo, tamaño,
hash y confirmación explícita está en
`Raspberry/reinstalar_ubuntu22_desktop_pi.sh` y en el repositorio público.

Estado: imagen grabada y verificada en el computador. Falta arrancar la
Raspberry y confirmar Ubuntu 22.04, escritorio gráfico, red, SSH y expansión de
la partición `writable`. No conectar ni energizar todavía los servos.

Verificación offline posterior: la partición `writable` contiene
`Ubuntu 22.04.5 LTS (Jammy Jellyfish)`, paquetes `ubuntu-desktop`,
`ubuntu-desktop-minimal`, `ubuntu-standard` y `gnome-shell`, además de sesiones
gráficas Xorg y Wayland. La comprobación confirma la imagen y la interfaz
gráfica instaladas; aún falta el primer arranque físico de la Raspberry para
validar red, SSH y funcionamiento real del escritorio.

Este archivo es la memoria persistente para continuar el proyecto en sesiones
posteriores. Antes de realizar nuevas tareas se debe leer este documento y el
seguimiento operativo ubicado en `Seguimiento/Seguimiento.md`.

## Estado general confirmado

El proyecto se encuentra en:

`/home/pavilion/Documentos/Cuadrupedo`

Workspace ROS 2 principal:

- `src/nova_gait_controller`
- `src/nova_sm3_description`
- `build/`
- `install/`
- `log/`

El robot cuadrúpedo Nova Spot Micro ya camina mediante gateo cartesiano en
Gazebo Sim con ROS 2 Humble. También existen el modelo de MuJoCo, la cinemática
propia, el control articular, el nodo de métricas y el supervisor de seguridad.

La referencia externa de Mike4192 se conserva en:

`referencias/spotMicro_mike4192`

Repositorio de referencia:

`https://github.com/mike4192/spot_micro_kinematics_python`

Se usa como apoyo conceptual; la implementación del proyecto es propia y está
adaptada al modelo NovaSM3.

## Configuración nominal congelada del gateo

Archivo de configuración:

`src/nova_gait_controller/config/gaits.yaml`

Parámetros utilizados en el ensayo de línea base:

- marcha: `gateo` / `crawl`;
- muestras por ciclo: 24;
- longitud de paso: 0,018 m;
- elevación del pie: 0,014 m;
- duración por muestra: 0,18 s;
- duración nominal del ciclo: 4,32 s;
- tópico de órdenes: `/nova/gait_command`;
- tópico de trayectoria: `/joint_trajectory_controller/joint_trajectory`.

SHA-256 del archivo `gaits.yaml` empleado:

`0772d57faab20f8da50176f4e94fc9d885e618211e230c34511c18256a71990a`

## Registro rosbag2 realizado el 14 de agosto de 2026

Se completó el primer registro válido de la línea base en Gazebo:

`Experimentos/rosbag2/linea_base_gateo_limpia_20260814_0925`

Resultados de integridad:

- comienzo de la bolsa: 09:25:40;
- final de la bolsa: 09:28:34;
- duración total: 174,227692248 s;
- ventana continua entre `gateo` y `stand`: 98,978769031 s;
- ciclos ejecutados completos, delimitados cada 24 referencias: 20;
- duración configurada por ciclo: 4,32 s;
- duración observada media por ciclo: 4,797996 s;
- requisito mínimo solicitado: 10 ciclos / 43,2 s;
- mensajes almacenados: 83.442;
- tamaño aproximado: 96,4 MiB;
- muestras de métricas dentro de la ventana válida: 5.813;
- activaciones del supervisor: 0.

No se modificaron paso, elevación ni velocidad durante el ensayo. La diferencia
entre duración configurada y observada se debe a que el temporizador de control
de 20 ms publicó las referencias aproximadamente cada 0,20 s. Los ciclos se
segmentan mediante grupos de 24 referencias registradas y no dividiendo
únicamente el tiempo entre 4,32 s.

Resumen preliminar dentro de la ventana válida:

| Magnitud | Inicio | Final | Mínimo | Máximo |
|---|---:|---:|---:|---:|
| x (m) | -0,001811 | 0,493510 | -0,014817 | 0,493510 |
| y (m) | 0,000000 | 0,005190 | -0,009581 | 0,013473 |
| altura (m) | 0,222356 | 0,224245 | 0,222356 | 0,224272 |
| roll (grados) | 0,000000 | 0,020540 | -2,255451 | 2,255240 |
| pitch (grados) | 0,027241 | 0,015405 | -4,412489 | 0,391404 |

El registro detallado está en:

`Experimentos/rosbag2/linea_base_gateo_limpia_20260814_0925/REGISTRO_ENSAYO.md`

SHA-256 de la base SQLite3 válida:

`d4a7b5dd7780170591537ef560d106ad99a36629164bb091ce0d61573526b772`

### Tópicos registrados

- `/clock`
- `/joint_states`
- `/dynamic_joint_states`
- `/joint_trajectory_controller/controller_state`
- `/joint_trajectory_controller/joint_trajectory`
- `/nova/gait_command`
- `/nova/metrics/diagnostics`
- `/nova/metrics/json`
- `/nova/safety/triggered`
- `/tf`
- `/tf_static`
- `/world/empty/dynamic_pose/info`

`/joint_trajectory_controller/controller_state` no produjo mensajes. El tópico
`/nova/safety/triggered` tuvo cero mensajes porque no hubo activaciones. Las dos
órdenes, `gateo` y `stand`, quedaron almacenadas en la bolsa válida.

La verificación formal de este requisito quedó guardada en
`Experimentos/rosbag2/linea_base_gateo_limpia_20260814_0925/AUDITORIA_TOPICOS.md`.
Se confirmó: 10.232 mensajes de pose 3D, 17.372 estados articulares, 10.231
mensajes de métricas, dos órdenes de marcha y ninguna activación del
supervisor. El punto correspondiente quedó marcado como completado en
`Seguimiento/Seguimiento.md`.

## Incidencia encontrada y corregida

La primera grabación fue:

`Experimentos/rosbag2/linea_base_gateo_20260814_0918`

No debe utilizarse para resultados. Al inspeccionarla se descubrieron dos
instancias simultáneas de `gait_controller`, `nova_metrics`,
`nova_safety_supervisor`, `robot_state_publisher` y `ros_gz_bridge`. Esto
duplicaba mensajes de métricas y pose.

Se detuvo la instancia antigua iniciada a las 07:59, se vació el grafo ROS 2 y
se relanzó `demo.launch.py`. Antes de repetir se confirmó exactamente una
instancia de cada nodo. La primera bolsa se conservó únicamente como evidencia
y contiene `ENSAYO_INVALIDO.md`.

Regla para futuras pruebas: antes de grabar, ejecutar `ros2 node list | sort |
uniq -c` y comprobar que ninguna instancia aparezca duplicada.

## Documentación matemática en LaTeX

El modelado convertido y corregido se encuentra en:

`Documentacion/MODELO_MATEMATICO_LATEX`

Archivos principales:

- `main.tex`: fuente LaTeX editable;
- `main.pdf`: PDF compilado de 11 páginas;
- `README.md`: contenido e instrucciones;
- `compilar.sh`: compilación automatizada.

El documento incorpora ecuaciones nativas de LaTeX para cinemática directa e
inversa, transformaciones homogéneas, Jacobiano, singularidades, dinámica,
actuadores, contacto, estabilidad, trayectorias, marcha, identificación,
validación e incertidumbre.

## Seguimiento operativo

La lista completa de trabajo pendiente se mantiene en:

`Seguimiento/Seguimiento.md`

Los puntos de grabación, tópicos, análisis automático y repetición independiente
ya están completados. La primera fase de línea base en Gazebo queda cerrada.

## Análisis automático completado

El script reproducible es `Experimentos/analizar_gateo_rosbag.py`. Los
resultados están en
`Experimentos/analisis/linea_base_gateo_limpia_20260814_0925`: CSV por ciclo,
series temporales, resumen gráfico e informe. Se analizaron 20 ciclos completos.
El avance medio fue 0,022908 m/ciclo, la velocidad media 0,004775 m/s y el salto
articular máximo medio 0,018005 rad. El primer ciclo contiene el transitorio de
arranque y debe conservarse y señalarse, no eliminarse silenciosamente.

## Repetición y reproducibilidad completadas

La repetición ya fue completada. La bolsa válida es
`Experimentos/rosbag2/repeticion_gateo_limpia_20260814_0956`, con 36 ciclos
completos, duración observada media de 4,793341 s y cero eventos del supervisor.
La tentativa `repeticion_gateo_20260814_0948` quedó inválida por perder la orden
inicial `gateo`.

La comparación reproducible está en
`Experimentos/comparacion_reproducibilidad_20260814`. Sobre los primeros 20
ciclos equivalentes y usando ciclos 2--20 para las medias, las diferencias entre
ensayos fueron -0,102 % en avance, -0,036 % en velocidad, 0,193 % en excursión
lateral, -0,001 % en altura, -0,000 % en roll y -0,002 % en pitch. Esto respalda
una repetibilidad muy alta en simulación, sin declarar equivalencia estadística
formal con solo dos ejecuciones.

## Próxima acción exacta

Cerrar con los directores las definiciones experimentales de paso, ciclo, fallo,
intervención y métricas.

## Preparación reciente de la Raspberry Pi

El 18 de agosto de 2026 se verificó una Raspberry Pi con arquitectura `arm64`,
usuario `pavilion` y dos interfaces de red activas:

- Ethernet `eth0`: `192.168.0.132/24`;
- Wi-Fi `wlan0`: `192.168.0.134/24`.

El servicio SSH fue instalado, habilitado al arranque y verificado escuchando en
el puerto 22. El sistema encontrado fue Ubuntu 24.04.4 LTS (`noble`) y no tenía
ROS 2 instalado. Esta instalación se descartó para el proyecto porque el
computador de Gazebo, los paquetes existentes y los scripts preparatorios usan
ROS 2 Humble sobre Ubuntu 22.04.

Decisión operativa: reinstalar en la unidad de la Raspberry Ubuntu Desktop
22.04 LTS ARM64, con interfaz gráfica, habilitar SSH y después ejecutar
`scripts/preparar_raspberry_pi_ros2.sh`. Antes de grabar la imagen se debe
identificar inequívocamente la unidad extraíble conectada al computador y
confirmar el destino; no se debe sobrescribir ningún disco basándose solo en
una letra o nombre supuesto. No conectar ni energizar todavía los servos.

El 19 de agosto de 2026 se identificó la unidad extraíble como `/dev/sda`, USB
de 28,9 GiB con modelo `Storage Device` y serie `150101v01`; el sistema del
computador se confirmó separado en `/dev/nvme0n1`. Se descargó la imagen oficial
`ubuntu-22.04.5-preinstalled-desktop-arm64+raspi.img.xz`. Su SHA-256 calculado,
`74764944dd4a96bdddd30cf1ffc133ecbe5ebb1d1f2eaa34cd5f8fbb57211c86`,
coincidió con el listado de Canonical. La imagen Desktop se grabó en `/dev/sda`:
9.269.411.840 bytes, salida cero y sincronización completada. La tabla resultante
mostró `system-boot` (512 MiB, FAT) y `writable` (8,1 GiB, ext4). Falta arrancar
la Raspberry y confirmar Ubuntu 22.04, la interfaz gráfica, red y SSH; por ello
la instalación todavía no se considera validada.

## Temporizador corregido: nueva versión experimental

El 14 de agosto de 2026 se corrigió `gait_controller.py` para avanzar la fecha
de cada fase desde el vencimiento planificado anterior y no desde la ejecución
tardía del callback. Pasaron 24 pruebas. Una bolsa ligera con 152 referencias y
seis ciclos midió 0,180003383 s por fase y 4,320106573 s por ciclo. El registro
está en `Experimentos/validacion_temporizador_20260814/VALIDACION_TEMPORIZADOR.md`.

Esta modificación no cambia paso ni altura, pero sí corrige la velocidad
ejecutada y constituye una nueva versión. La próxima acción técnica es levantar
una línea base nueva en Gazebo con al menos diez ciclos, analizarla y repetirla;
no se deben mezclar sus resultados con las bolsas anteriores de ciclo cercano a
4,80 s.

### Nueva línea base en Gazebo completada

Se creó `Experimentos/rosbag2/linea_base_cadencia_corregida_20260814_1049` con
13 ciclos completos, 57,014709 s de gateo, 32.352 mensajes y cero activaciones
del supervisor. El ciclo medio observado fue 4,320013 s. En los ciclos 2--13,
el avance medio fue 0,023338 m/ciclo, la velocidad 0,005402 m/s, la excursión
lateral 0,015133 m, el roll máximo 2,233112 grados y el pitch máximo 4,365442
grados. El registro y los hashes están dentro de la bolsa.

La repetición indicada a continuación completó la reproducibilidad de esta nueva
línea base.

### Repetición de la cadencia corregida completada

La bolsa `Experimentos/rosbag2/repeticion_cadencia_corregida_20260814_1100`
contiene 13 ciclos completos, 32.395 mensajes y cero eventos del supervisor.
La comparación en `Experimentos/comparacion_cadencia_corregida_20260814` usa
los 13 ciclos equivalentes y los ciclos 2--13 para las medias. Las diferencias
relativas fueron -0,001 % en duración, 0,194 % en avance, 0,195 % en velocidad,
0,014 % en excursión lateral, -0,000 % en altura, 0,031 % en roll, 0,037 % en
pitch y 0,035 % en salto articular. La nueva versión corregida queda reproducida
con diferencias menores al 0,2 % en todas estas medias.

La fase de línea base corregida y su repetición queda cerrada. La próxima acción
es formalizar con los directores las definiciones experimentales de paso, ciclo,
fallo e intervención antes de diseñar la marcha `paso`.

## Protocolo experimental redactado

Se creó `Documentacion/PROTOCOLO_EXPERIMENTAL_BORRADOR.md`. El borrador define
paso como la oscilación completa de una pata y ciclo de gateo como 24 referencias
con una oscilación por pata, en orden FL--RR--FR--RL. También define ensayo,
ciclo válido, transitorio, fallo, intervención, caída, datos obligatorios,
métricas y criterios provisionales. Propone cinco ensayos de 20 ciclos por
condición y cinco semillas de RL para la comparación final, sujetos a revisión.

Este punto no está cerrado administrativamente: los directores deben aprobar
cantidades, semillas, métrica primaria, umbrales y la declaración de que el
modelo es nominal computable, no un gemelo digital identificado.

## Marcha paso: implementación inicial

Se añadió el comando `paso/step` con generador cartesiano propio. Usa 32
referencias, 0,18 s por referencia, longitud de 0,016 m, elevación de 0,008 m y
transferencia lateral sinusoidal de 0,004 m; el orden es FL--RR--FR--RL. Las 26
pruebas pasan y el paquete fue recompilado. El diseño está en
`Documentacion/MARCHA_PASO_DISENO.md`.

El ensayo `Experimentos/rosbag2/paso_exploratorio_20260814` completó cuatro
ciclos en Gazebo con cero eventos del supervisor, ciclo medio de 5,759993 s,
roll máximo medio de 1,275 grados y pitch máximo medio de 2,497 grados. La
próxima acción técnica es grabar al menos diez ciclos continuos de `paso`,
analizarlos, repetirlos y después validar el patrón en MuJoCo.

### Marcha paso validada

La acción anterior quedó completada. Gazebo ejecutó dos ensayos independientes
de 12 ciclos con cero eventos del supervisor; las diferencias de medias fueron
menores al 0,4 %. En ciclos 2--12, el avance fue 0,022031 m/ciclo, la velocidad
0,003825 m/s, el roll máximo 1,281777 grados y el pitch máximo 2,483731 grados.

MuJoCo headless completó 12 ciclos con duración media de 5,759999 s, error RMS
articular de 0,026232 rad y error máximo de 0,054983 rad. Su adaptador no publica
pose corporal equivalente a Gazebo, así que esta validación cubre cadencia y
articulaciones, no avance o estabilidad corporal. El informe consolidado está
en `Documentacion/MARCHA_PASO_VALIDACION.md`.

La próxima acción técnica recomendada es publicar fase de marcha y patas
previstas en contacto, requisito necesario para incorporar contactos y margen
de estabilidad en línea.

## Fase y contactos previstos publicados

La acción anterior quedó completada. `/nova/gait_phase` publica JSON sincronizado
con cada referencia: modo, muestra, total de muestras, ciclo, pata en oscilación,
contactos previstos y disponibilidad del plan. `crawl` y `step` siguen
FL--RR--FR--RL; `gallop` declara que todavía no dispone de plan formal. Pasaron
29 pruebas y se observó un mensaje ROS 2 real. El contrato está en
`Documentacion/FASE_Y_CONTACTOS_PREVISTOS.md`.

Las bolsas históricas anteriores no contienen este tópico porque preceden la
modificación. Toda bolsa nueva debe grabar `/nova/gait_phase`. La próxima acción
es añadir contactos medidos de los cuatro pies y comparar contacto previsto
frente a contacto observado.

## Contactos medidos de los cuatro pies en Gazebo

La acción anterior quedó completada para Gazebo. El URDF contiene cuatro
sensores de contacto de 100 Hz y conserva las uniones fijas de los pies durante
la conversión a SDF. El puente publica los flujos crudos en
`/nova/contacts/front_left`, `front_right`, `rear_left` y `rear_right`.

El nodo `contact_monitor` consolida las mediciones en `/nova/foot_contacts` y
el proceso independiente `contact_comparator` compara fase prevista frente a
contacto observado en `/nova/contact_diagnostics`. Tras recibir la primera
muestra de cada sensor, la ausencia de mensajes por más de 0,10 s significa
`contact=false`, porque Gazebo deja de publicar al desaparecer la colisión. El
comparador informa apoyos faltantes o inesperados y no activa paradas.

La validación real confirmó cuatro apoyos válidos en `stand`. En `crawl` se
detectó correctamente `rr` como contacto inesperado en una fase que esperaba
`fl`, `fr` y `rl`; en `step` se detectó `rl` como inesperado cuando se esperaban
`fl`, `fr` y `rr`. Esto revela una diferencia temporal entre la ventana discreta
de oscilación y el despegue físico que debe medirse, no ocultarse. Pasaron 32
pruebas y los paquetes compilaron. El diseño y las limitaciones están en
`Documentacion/CONTACTOS_MEDIDOS_GAZEBO.md`.

La próxima acción exacta es grabar al menos diez ciclos de gateo con
`/nova/gait_phase`, `/nova/foot_contacts` y `/nova/contact_diagnostics`, y
calcular retardos de despegue/aterrizaje y porcentaje de coincidencia por pata.
Después se añadirán contactos equivalentes en MuJoCo y el polígono de soporte.

## Ensayo cuantitativo de contactos completado

La acción anterior quedó completada con la bolsa válida
`Experimentos/rosbag2/contactos_gateo_validado_20260814_1410`: 76 ciclos
completos, 329,856750 s entre marcadores, 176.657 mensajes y cero activaciones
del supervisor. Se conservaron cuatro tentativas inválidas que permitieron
detectar y corregir saturación por contactos crudos, omisión de fases y pérdida
de marcadores efímeros.

El agregador y el comparador quedaron separados en dos procesos. La salida se
limita a 100 Hz, usa QoS de profundidad 1 para los contactos crudos y publica un
diagnóstico inmediatamente con cada fase. La prevalidación confirmó las cuatro
combinaciones FL--RR--FR--RL.

El resultado fue 32,550 % de coincidencia simultánea. FL y FR despegaron en
promedio 0,380297 s y 0,381066 s tarde, y aterrizaron 1,364317 s y 1,364194 s
tarde. RL y RR no mostraron transiciones de despegue: permanecieron apoyadas y
deslizaron. La marcha mantuvo ciclo medio de 4,320002 s, avance de 0,022970
m/ciclo y cero eventos del supervisor, pero no cumple el patrón de contactos
supuesto aunque visualmente camine.

Informes:
`Experimentos/analisis/contactos_gateo_validado_20260814_1410/INFORME_CONTACTOS.md`
y
`Experimentos/analisis_movimiento/contactos_gateo_validado_20260814_1410/INFORME_ANALISIS.md`.

La próxima acción técnica es corregir el generador de gateo para producir
despegue real de RL y RR y reducir los retardos delanteros, manteniendo por
ahora el supervisor solo informativo. La nueva trayectoria constituirá otra
versión experimental y deberá repetir el ensayo de contactos.

### Cierre de sesión y trazabilidad de las tentativas

Se conservaron deliberadamente las bolsas descartadas, cada una con su archivo
`ENSAYO_INVALIDO.md`:

- `contactos_gateo_20260814_1323`: saturación por más de 400.000 diagnósticos y
  acumulación de contactos crudos;
- `contactos_gateo_valido_20260814_1350`: el ejecutor atendía solo fases
  alternas;
- `contactos_gateo_final_20260814_1354`: no almacenó órdenes de marcha y aún
  omitía fases;
- `contactos_gateo_definitivo_20260814_1359`: almacenó 23 ciclos y marcadores,
  pero el diagnóstico publicado desde contactos podía omitir estados de fase.

Las correcciones resultantes fueron QoS `best effort` con profundidad 1,
limitación del agregado a 100 Hz, separación de agregador y comparador en dos
procesos, publicación inmediata al recibir fase y marcadores redundantes. La
bolsa aceptada es únicamente `contactos_gateo_validado_20260814_1410`.

El analizador reproducible es `Experimentos/analizar_contactos_rosbag.py`; crea
`transiciones_contacto.csv`, `resumen_por_pata.csv` e
`INFORME_CONTACTOS.md`. Los pares de transición usan una ventana de ±1,8 s para
capturar los aterrizajes delanteros tardíos y los porcentajes se ponderan por
tiempo, no por cantidad de mensajes.

Estado al cerrar: Gazebo y rosbag2 detenidos, robot devuelto a `stand`, 32
pruebas aprobadas, fuentes Python verificadas y ejecutables `contact_monitor` y
`contact_comparator` instalados. El registro detallado con hashes está en
`Experimentos/rosbag2/contactos_gateo_validado_20260814_1410/REGISTRO_ENSAYO.md`.

## Galope relegado a experimento opcional

Se cerró el punto pendiente de alcance: `gallop/galope` se conserva en el
código únicamente como experimento opcional de simulación. El parámetro
`enable_experimental_gallop` vale `false` por defecto; mientras esté desactivado,
el controlador rechaza el comando y conserva el modo actual.

El galope queda excluido de líneas base, comparación nominal frente a RL,
criterios principales de éxito y hardware. Solo puede habilitarse explícitamente
en Gazebo o MuJoCo. Continúa sin plan formal de contactos y publica
`contact_plan_available=false`. La decisión está en
`Documentacion/EXPERIMENTO_GALOPE_OPCIONAL.md` y cuenta con prueba automatizada
del bloqueo y la habilitación explícita.

## Cantidades experimentales y semillas RL fijadas

Se aprobó y adoptó la matriz para la comparación final. Para cada una de las
marchas `gateo` y `marcha paso` se ejecutarán cinco ensayos nominales y cinco
ensayos nominales más RL, con 20 ciclos programados por ensayo. Son 100 ciclos por condición, 200
por marcha y 400 ciclos finales en total.

El ciclo 1 se conserva como transitorio y los ciclos 2--20 describen régimen
permanente. La unidad independiente es el ensayo (`n=5` por condición); los
ciclos no se tratarán como réplicas independientes.

Las semillas de entrenamiento RL quedan congeladas en `11`, `23`, `37`, `53` y
`71`. Los escenarios/semillas de evaluación emparejada serán `101`, `202`,
`303`, `404` y `505`. Se reportarán las cinco políticas; la política final se
seleccionará con validación separada después de aprobar la métrica primaria y
se bloqueará antes de abrir los resultados finales.

Los fallos permanecen contabilizados aunque exista una repetición adicional.
La decisión completa y congelada está en
`Documentacion/DECISION_TAMANO_MUESTRAL_Y_SEMILLAS_RL.md`. Cualquier cambio
posterior deberá registrarse antes de iniciar los ensayos finales.

No se deben mezclar estas bolsas con ensayos producidos después de modificar el
temporizador, el paso, la altura o la velocidad.

## Actualización documental integral del 16 de agosto de 2026

Se sincronizaron con el estado experimental vigente el README principal, el
README del modelo, el protocolo, el seguimiento y la documentación de código,
ROS 2, cinemática, modelado matemático, marcha paso y contactos. Las fuentes
LaTeX dejan de presentar como futuros los nodos de métricas, supervisor, fase y
contactos que ya existen, e incorporan la cadencia corregida, la validación de
la marcha paso y el ensayo cuantitativo de 76 ciclos.

La actualización documental no modifica código de control, configuraciones ni
datos históricos. Tampoco declara resuelta la limitación de contacto: la
próxima acción técnica continúa siendo corregir el gateo y validar una nueva
versión experimental sin mezclarla con las bolsas anteriores.

Tras la actualización, la suite vigente ejecutó 33 pruebas aprobadas y los
cuatro PDF técnicos recompilaron correctamente: explicación del código (6
páginas), cinemática de marcha (5), estado ROS 2 (7) y modelo matemático (11).

### Ampliación del modelo con control discreto

El 16 de agosto de 2026 se amplió
`Documentacion/MODELO_MATEMATICO_LATEX/main.tex` con una explicación paso a
paso equivalente al temario de un curso de control discreto. Se incorporaron
muestreo, transformada Z, discretización, estabilidad, diseño PID y por estados,
observadores, frecuencia, robustez, efectos digitales, control híbrido y su
aplicación explícita a Nova. Se distingue en una tabla lo implementado de lo
propuesto para evitar presentar LQR, Kalman o MPC como funciones existentes.
El PDF resultante compila sin referencias indefinidas y tiene 25 páginas.

### Ejemplos desarrollados y presentación matemática

A petición del usuario, el 16 de agosto de 2026 se volvió a ampliar el modelo
para que no omita sustituciones ni pasos intermedios. Se añadieron cajas de
ejemplo con FK e IK, Jacobiano, condición y fuerza--par, dinámica inversa por
términos, envolvente del MG996R, COM y margen, oscilación discreta, cadencia,
linealización, discretización ZOH, LQR y análisis experimental de contactos y
reproducibilidad. Los valores se generan con
`scripts/generar_ejemplos_modelo.py` usando el código y parámetros del proyecto.
El PDF pasó de 25 a 31 páginas. Las formulaciones nominales continúan claramente
separadas de mediciones físicas todavía pendientes.

Verificación: 33 pruebas aprobadas. SHA-256 del PDF ampliado:
`bf1097e5d8511ea9ec9384c834ffa2a09474ced9ee521b2d6cdd950d209f0b68`.
SHA-256 del generador reproducible:
`d8d879df7d51e6639923908be3f89c3bf5e2778c4a1f5cd5cb17967126755f20`.

### Trazabilidad matemática y diccionario de variables

El 16 de agosto de 2026 se extendió nuevamente
`Documentacion/MODELO_MATEMATICO_LATEX/main.tex` para responder de forma
explícita qué significa cada variable, por qué se necesita, de dónde procede
cada familia matemática y qué resultado de tesis permite obtener. Se añadió
una cadena de trazabilidad teoría--adaptación Nova--código--evidencia, fuentes
base identificadas T01--T11, adaptaciones A01--A12, archivos C01--C12 y
evidencias E01--E09.

El documento contiene ahora tres diccionarios razonados (geometría y
cinemática; dinámica, actuador, contacto y estabilidad; marcha, control
discreto y experimento), cajas de trazabilidad junto a las derivaciones y un
registro final que enlaza todas las ecuaciones numeradas con su método,
variables entregadas, adaptación específica y uso verificable. También fija
un protocolo de siete pasos para cada ejemplo: objetivo, fuente, datos,
hipótesis, sustitución, comprobación e interpretación.

El PDF resultante tiene 39 páginas y compila sin errores, referencias
indefinidas ni desbordamientos. Los valores numéricos siguen siendo
reproducibles con `scripts/generar_ejemplos_modelo.py`; los parámetros de
catálogo y simulación permanecen separados de la identificación física aún
pendiente.

Verificación final: 33 pruebas aprobadas. SHA-256 de `main.tex`:
`a34780eff35a4b87931ac04355b890faa1b0a751be4bef23d697c10be3f05e12`.
SHA-256 de `main.pdf`:
`a146b360da969703f478e4692a037cfd179772a86da09fc74c967bc92a90389c`.
SHA-256 del generador:
`d8d879df7d51e6639923908be3f89c3bf5e2778c4a1f5cd5cb17967126755f20`.

### Punto exacto de reanudación

Este es el cierre vigente de la sesión. El modelo matemático ampliado se
considera documentalmente terminado en su versión nominal de 39 páginas. No se
debe volver a la versión anterior de 11, 25 o 31 páginas ni sobrescribir el PDF
sin recompilar y actualizar sus hashes.

Al reanudar, leer primero este archivo y después
`Seguimiento/Seguimiento.md`. La siguiente acción técnica del proyecto no es
añadir más teoría genérica: es corregir el generador de gateo para conseguir
despegue real de RL y RR y reducir los retardos de FL y FR; posteriormente se
debe grabar una bolsa nueva, analizar contactos y compararla sin mezclarla con
`contactos_gateo_validado_20260814_1410`.

En paralelo quedan pendientes la identificación física de geometría, masas,
inercias, fricción y MG996R; la validación de $\dot J$; las gráficas de workspace
y singularidad; contactos e IMU equivalentes en MuJoCo; y la aprobación con los
directores de métricas y umbrales experimentales. LQR, Kalman, MPC y la
corrección RL continúan documentados como diseño propuesto, no como funciones
ya implementadas o validadas en hardware.

### Iteración exploratoria de transferencia de peso (17 de agosto de 2026)

Se modificó el generador cartesiano de gateo para incorporar transferencia
común lateral y longitudinal, manteniendo sin cambios 24 referencias, paso de
0,018 m, elevación máxima de 0,014 m y 0,18 s por referencia. También se hizo
explícito el aterrizaje en la última muestra discreta de cada oscilación y se
añadieron pruebas de continuidad cíclica, altura y secuencia. Pasan 35 pruebas
y el paquete compila.

Tres ejecuciones exploratorias temporales en Gazebo compararon transferencia
longitudinal de 4, 8 y 12 mm. Las traseras pasaron de no despegar a presentar
transiciones medidas, y el despegue delantero mejoró de aproximadamente 0,38 s
a 0,34 s. El mejor porcentaje simultáneo fue 35,787 % con 8 mm (13 ciclos),
frente a 31,974 % con 4 mm y 34,879 % con 12 mm. Sin embargo, RL y RR aún
despegaron unos 1,17--1,19 s tarde: se descargan durante la oscilación delantera
del mismo lado, no en su ventana prevista. No se congela ni valida todavía una
nueva línea base.

El valor candidato queda en 8 mm. La próxima acción exacta es separar dentro de
cada cuarto de ciclo una etapa previa de transferencia de peso y otra de
oscilación, y hacer que `/nova/gait_phase` represente esas subfases. Después se
deben repetir pruebas unitarias y una comparación exploratoria antes de grabar
la bolsa formal de al menos diez ciclos. Las bolsas usadas en esta iteración
están en `/tmp` y no constituyen evidencia permanente.

### Gateo con subfases explícitas (17 de agosto de 2026)

Se completó la separación anterior conservando las 24 muestras y los parámetros
nominales. Cada cuarto usa `transfer_start`, `preload`, `liftoff`, `flight`,
`landing` y `touchdown`. `/nova/gait_phase` añade `planned_leg` y
`gait_subphase`; durante precarga y contacto final `swing_leg=null` y se esperan
cuatro apoyos. La trayectoria y el plan de contactos comparten la misma función
de perfil para evitar divergencias. Pasan 36 pruebas y el paquete compila.

Una ejecución exploratoria temporal de 15 ciclos en Gazebo confirmó todas las
subfases, avance de 0,376516 m, altura de 0,222356--0,224356 m, roll absoluto
máximo de 2,074764 grados, pitch absoluto máximo de 4,103346 grados y cero
eventos del supervisor. Los retardos medios de despegue fueron 0,135193 s (FL),
0,132697 s (FR), 0,137536 s (RL) y 0,140653 s (RR). Esto corrige el defecto de
las traseras, que antes no despegaban o lo hacían 1,17--1,19 s tarde.

El aterrizaje aún requiere ajuste diferenciado: FL y FR contactan unos 0,50 s
tarde, mientras RL y RR lo hacen unos 0,33 s antes de `touchdown`. La
coincidencia simultánea de 20,927 % no es directamente comparable con la
anterior porque el plan ahora exige cuatro apoyos en tres de cada seis muestras.
No se congela todavía la nueva línea base. La próxima acción exacta es ajustar
el descenso/aterrizaje por eje sin degradar los despegues ya corregidos y repetir
la exploración. La bolsa de esta prueba permanece en `/tmp` y no es evidencia
experimental permanente.

### Ajuste exploratorio de aterrizaje por eje (18 de agosto de 2026)

Se parametrizó la altura de la penúltima referencia (`landing`) por eje, sin
alterar paso, elevación máxima, 24 muestras ni cadencia. El contraste seguro
más amplio compatible con el límite de continuidad de 0,20 rad fue 0,20 de la
elevación máxima para FL/FR y 0,80 para RL/RR. En 22 ciclos completos los
despegues se conservaron entre 0,135 y 0,141 s tarde, pero los aterrizajes solo
cambiaron a 0,446 s y 0,455 s tarde delante, y -0,327 s y -0,323 s detrás. La
coincidencia simultánea fue 22,548 %.

El contraste se rechazó por mejora insuficiente y no constituye una nueva
línea base. Los parámetros quedaron disponibles, pero sus valores nominales se
restauraron a 0,70710678, equivalentes al perfil sinusoidal anterior. La bolsa
y el análisis permanecen en `/tmp`; falta el marcador `stand` en la bolsa, por
lo que se analizaron explícitamente como ventana exploratoria abierta. El
analizador admite ahora `--allow-open-window`, mientras su modo normal conserva
la exigencia estricta de ambos marcadores. Pasan 37 pruebas y el paquete
compila.

La próxima acción es rediseñar la forma temporal completa del descenso, no
solo su penúltima muestra, manteniendo continuidad y elevación máxima. Debe
compararse primero en pruebas cartesianas y luego en Gazebo antes de congelar
otra versión.

### Preparación de Thonny y comunicación con Raspberry (19 de agosto de 2026)

Se documentaron `Raspberry/INSTALACION_THONNY.md` y
`Raspberry/PROTOCOLO_COMUNICACION_RASPBERRY.md`. El canal principal será
Ethernet + SSH; ROS 2/DDS usará `ROS_DOMAIN_ID=42` y USB-serial de 3,3 V queda
como respaldo. La instalación de Thonny y la verificación de red, SSH, reloj,
I2C y arquitectura `aarch64` se realizarán después del primer arranque de la
Raspberry. No se conectan ni energizan servos en esta fase.
