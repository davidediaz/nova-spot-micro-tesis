# Protocolo experimental de locomoción Nova Spot Micro

Estado: cantidades aprobadas y adoptadas para el proyecto.

Versión: 1.1, 14 de agosto de 2026.

## 1. Objeto

Este protocolo fija el vocabulario, las unidades experimentales, los criterios
de validez y las métricas para comparar:

1. marcha nominal sin aprendizaje;
2. la misma marcha nominal con correcciones acotadas de aprendizaje por
   refuerzo.

Las condiciones deben usar la misma geometría, configuración nominal,
trayectoria base, duración, estado inicial y criterios de seguridad. La política
aprendida no puede comandar PWM directo ni anular el supervisor.

## 2. Definiciones obligatorias

### 2.1 Paso

Un **paso** es el evento completo de una sola pata desde el inicio de su fase de
oscilación, pasando por elevación y avance, hasta recuperar contacto o alcanzar
la posición prevista de apoyo. No significa una secuencia de las cuatro patas.

Cuando se hable del patrón implementado denominado “marcha paso”, se
escribirá siempre **marcha paso** para distinguir el nombre del modo de marcha
del evento elemental anterior.

### 2.2 Zancada o ciclo de gateo

Un **ciclo completo de gateo** es una secuencia de 24 referencias articulares en
la que cada pata ejecuta exactamente una oscilación y el estado de fase vuelve
al índice inicial. Con la versión corregida:

- 24 muestras por ciclo;
- 0,18 s configurados por muestra;
- 4,32 s nominales por ciclo.

La segmentación se realizará por las referencias registradas en
`/joint_trajectory_controller/joint_trajectory`, no solamente dividiendo el
tiempo total por 4,32 s. Esto conserva validez ante jitter del planificador.

### 2.3 Orden de oscilación

El orden implementado y confirmado en `cartesian_crawl` es:

1. delantera izquierda (`fl`);
2. trasera derecha (`rr`);
3. delantera derecha (`fr`);
4. trasera izquierda (`rl`).

Cada pata permanece nominalmente el 75 % del ciclo en apoyo y el 25 % en
oscilación. Con 24 referencias, cada oscilación ocupa seis referencias.

### 2.4 Ensayo

Un **ensayo** es una ejecución independiente desde una simulación o encendido
nuevo, con:

- identificación única y fecha;
- versión y hashes del código/configuración;
- condición experimental declarada;
- pose inicial nominal;
- orden `gateo`, ventana continua y orden `stand`;
- rosbag2 y análisis asociados;
- registro de cualquier intervención o incidencia.

Reproducir varias veces una bolsa no constituye varios ensayos.

### 2.5 Ciclo válido

Un ciclo es válido si:

- contiene las 24 referencias en el orden previsto;
- tiene pose y estados articulares suficientes para calcular las métricas;
- ocurre completamente entre las órdenes de inicio y cierre;
- no contiene pausa de grabación, reinicio de fase ni cambio de parámetros;
- no pertenece a una bolsa con nodos duplicados;
- no cruza una intervención manual o automática.

El primer ciclo se conserva y se etiqueta como **transitorio de arranque**. Las
tablas deben informar resultados con todos los ciclos y, de forma separada, el
régimen permanente desde el ciclo 2. No se elimina silenciosamente.

### 2.6 Fallo

Un **fallo** es cualquier evento que impide completar el número de ciclos
previsto o invalida la ejecución, incluyendo:

- caída;
- activación del supervisor;
- pérdida del controlador, simulador, rosbag2 o datos esenciales;
- referencia inalcanzable o fuera de límites;
- colisión no prevista;
- cambio de parámetros durante la ventana;
- nodos ROS 2 duplicados;
- ausencia de los marcadores necesarios para delimitar la marcha.

Todo fallo cuenta en la tasa de fallos aunque después se repita el ensayo.

### 2.7 Intervención

Una **intervención** es una acción humana o automática no prevista por la marcha
nominal que modifica o termina el ensayo: publicar `stand/stop`, pausar el
simulador, sujetar el robot, cambiar parámetros o activar el supervisor. La
orden `stand` programada al final de la ventana no es una intervención.

### 2.8 Caída

En simulación se declara **caída** cuando ocurre cualquiera de estos eventos:

- altura del cuerpo fuera de 0,16--0,32 m durante al menos tres muestras
  consecutivas;
- valor absoluto de roll o pitch mayor de 20 grados durante al menos tres
  muestras consecutivas;
- contacto persistente del cuerpo con el suelo, cuando los sensores de contacto
  estén disponibles;
- imposibilidad de recuperar `stand` sin reiniciar la simulación.

Los umbrales son provisionales y exclusivos de simulación. No se transfieren al
hardware sin validación física.

## 3. Diseño experimental propuesto

### 3.1 Unidad de análisis

- Unidad primaria: ensayo independiente.
- Unidad secundaria: ciclo completo dentro del ensayo.
- Los ciclos de un mismo ensayo no se tratarán como réplicas independientes al
  realizar inferencia estadística.

### 3.2 Cantidad aprobada internamente

Para cada marcha y condición:

- desarrollo técnico: mínimo dos ensayos de al menos 10 ciclos;
- comparación final: cinco ensayos independientes de 20 ciclos programados por
  condición;
- aprendizaje por refuerzo: cinco semillas de entrenamiento fijadas antes de
  entrenar: `11`, `23`, `37`, `53` y `71`;
- evaluación final: escenarios/semillas `101`, `202`, `303`, `404` y `505`, en
  el mismo orden para nominal y nominal más RL si se introduce aleatorización.

Esta decisión se aplica por separado a `gateo` y `marcha paso`. Por cada marcha
se programan 100 ciclos nominales y 100 ciclos nominales más RL: 200 ciclos por
marcha y 400 ciclos para las dos marchas. El primer ciclo de cada ensayo se
conserva como transitorio; el régimen permanente usa los ciclos 2--20.

La unidad inferencial continúa siendo el ensayo (`n=5` por condición); los 20
ciclos son mediciones repetidas y no elevan artificialmente el tamaño muestral.
Los ensayos técnicos, exploratorios o usados para ajustar parámetros no forman
parte de esos cinco ensayos finales.

Las cinco políticas RL se entrenarán y reportarán. La regla de selección de una
política final se fijará después de aprobar la métrica primaria, usando solo un
conjunto de validación separado. Después se congelarán pesos, normalización y
configuración; la selección no podrá usar los cinco ensayos comparativos
finales. La política bloqueada se evaluará en cinco ensayos de 20 ciclos frente
al nominal bajo escenarios emparejados.

Si un ensayo falla, permanece contabilizado en la tasa de fallos. Puede hacerse
una repetición identificada para completar datos, pero no sustituye ni borra el
fallo. Si el piloto revela que cinco ensayos no bastan para la precisión
deseada, cualquier aumento se decidirá antes de abrir los resultados finales y
se aplicará simétricamente a ambas condiciones.

## 4. Datos obligatorios

Cada bolsa debe incluir como mínimo:

- pose 3D y transformaciones;
- `/joint_states` y `/dynamic_joint_states`;
- referencias articulares;
- `/nova/metrics/json` y diagnósticos;
- `/nova/gait_command`;
- `/nova/safety/triggered`;
- reloj de simulación.

Para la transferencia al cuadrúpedo físico se conservará la misma lógica de
retroalimentación, adaptada a los sensores realmente instalados: posición o
estado de servos, IMU, contactos de pie y telemetría de alimentación cuando
esté disponible. No se considerará cerrado el control físico si solo se envían
referencias sin observar la respuesta del robot.

Antes de grabar se comprobará `ros2 node list | sort | uniq -c`; cada nodo debe
aparecer una sola vez. Se propone para aprobación una frecuencia común de
registro de **100 Hz** para contactos, pose, IMU y métricas; se acepta una
frecuencia efectiva mínima de **50 Hz** para señales que no puedan publicarse a
100 Hz. Se informará cualquier hueco superior a **0,10 s** y no se supondrá
muestreo uniforme.
El análisis usará marcas temporales reales y reportará huecos superiores a 0,10
s; no supondrá muestreo perfectamente uniforme.

## 5. Métricas

### 5.1 Primarias

- ciclos válidos completados;
- fallos, caídas e intervenciones por ensayo;
- avance por ciclo (m);
- velocidad media por ciclo (m/s);
- roll y pitch RMS y máximos absolutos (grados);
- excursión y deriva lateral por ciclo (m).

### 5.2 Secundarias

- altura mínima, media y máxima (m);
- duración observada del ciclo (s);
- salto articular máximo entre muestras consecutivas (rad);
- velocidad articular máxima (rad/s);
- margen de estabilidad, contactos, corriente, energía y temperatura cuando
  esas señales estén realmente disponibles.

No se afirmará seguimiento articular físico mientras no exista medición real de
posición en el hardware.

## 6. Criterios de evidencia alineados con los objetivos

La revisión de los directores debe centrarse en que cada prueba produzca
evidencia suficiente para los cuatro objetivos. Los valores numéricos siguientes
son umbrales iniciales de operación y análisis; podrán ajustarse antes de la
campaña final si los datos o el director lo justifican, dejando registro del
cambio. Un ensayo útil para la tesis debe:

- completa todos los ciclos previstos;
- no presenta caída, fallo ni intervención;
- el supervisor no se activa;
- mantiene la pose dentro de los límites de seguridad provisionales;
- no pierde referencias ni datos esenciales;
- registrar las señales de retroalimentación disponibles y su configuración;
- permitir evaluar estabilidad, seguimiento articular y repetibilidad;
- conservar fallos, caídas, intervenciones y datos incompletos;
- documentar la configuración, versión del código y condiciones iniciales.

Como guía inicial se conservarán cadencia, continuidad articular, error de
seguimiento, roll/pitch, altura, margen, contactos y variabilidad entre ensayos.
Estos valores apoyan OE1--OE4; no constituyen objetivos adicionales.

La tesis podrá reportar una estrategia como válida cuando exista evidencia
reproducible de coordinación, estabilidad y continuidad en paso y gateo, junto
con las tres pruebas de OE4. Si PPO no mejora, se reporta el resultado negativo
y se acuerda con los directores el alcance final; no se fuerza una mejora
numérica artificial.

## 7. Nivel de modelo que declarará la tesis

Se propone resolver la contradicción de alcance con esta redacción:

> El proyecto entrega un modelo nominal computable y coherente entre código,
> URDF/Gazebo y MJCF/MuJoCo. Incluye cinemática, Jacobianos, masa, términos
> dinámicos nominales, actuadores y contacto simplificado. No se presenta como
> gemelo digital identificado: masas, fricción, centro de masa, servos y contacto
> permanecen provisionales hasta su identificación y validación física.

Por tanto, la tesis puede evaluar control y repetibilidad en simulación, pero no
debe afirmar fidelidad cuantitativa del hardware antes de las mediciones físicas.

## 8. Decisiones adoptadas y asuntos pendientes

- aceptar “paso” como evento de una pata y “ciclo” como las cuatro oscilaciones;
- **Decisión cerrada:** cinco ensayos de 20 ciclos por
  condición y cinco semillas RL (`11`, `23`, `37`, `53`, `71`).
- confirmar las señales de retroalimentación, las pruebas y la evidencia mínima
  que demostrará cada objetivo;
- aprobar el nivel de modelo nominal y la limitación de no llamarlo gemelo
  digital identificado.

Las cantidades quedan congeladas para planificación, desarrollo y ejecución
experimental del proyecto. Cualquier cambio posterior deberá documentarse
antes de iniciar los ensayos finales y aplicarse simétricamente.

## 9. Estado técnico incorporado al protocolo

Desde la primera redacción se completaron la línea base de cadencia corregida,
su repetición, la validación de marcha paso en Gazebo y MuJoCo, y la publicación
de fase y contactos medidos. El ensayo cuantitativo de gateo mostró 32,550 % de
coincidencia simultánea con el plan y ausencia de despegue trasero. Estos datos
caracterizan la versión existente, pero no habilitan los ensayos comparativos
finales. La trayectoria corregida deberá congelarse y validarse antes de
ejecutar la matriz de 400 ciclos.
