# Propuesta de instrumentación física del Nova Spot Micro

Fecha de decisión preliminar: 31 de agosto de 2026.

## Estado y propósito

Esta arquitectura está **propuesta, no instalada ni validada**. Su finalidad es
medir el comportamiento real del cuadrúpedo, cerrar la diferencia entre la
referencia enviada y la respuesta física, validar el modelo de simulación y
definir observaciones útiles para una futura capa correctiva de aprendizaje por
refuerzo.

## Instrumentación priorizada

1. Doce sensores magnéticos AS5600, uno por articulación, con imanes
   diametrales y soportes rígidos. Entregarían ángulo real, error de seguimiento,
   velocidad estimada, histéresis, holgura y detección de articulaciones
   bloqueadas.
2. Dos multiplexores I2C TCA9548A, inicialmente previstos con direcciones
   distintas, para aislar los AS5600 que comparten la dirección fija `0x36`.
   Dos dispositivos de ocho canales ofrecen capacidad suficiente para doce
   encoders.
3. Una IMU BNO055 cerca del centro del cuerpo para orientación, velocidad
   angular, aceleración lineal y gravedad. Se reutilizará el componente ya
   contemplado antes de evaluar una sustitución.
4. Cuatro detectores de contacto, inicialmente FSR o microswitch, uno por pie.
   Las celdas de carga quedan como mejora posterior después de validar un solo
   pie instrumentado.
5. Un monitor INA228, correctamente dimensionado junto con su resistencia
   shunt para la corriente total, en la alimentación de los servos. Permitirá
   medir tensión, corriente, potencia y energía y detectar bloqueos o sobrecarga.
6. Sensores ToF VL53L4CD frontal y hacia el suelo solamente en una fase
   posterior de navegación. No son necesarios para cerrar primero el control
   postural y de marcha.
7. Termistores en servos como opción posterior si las pruebas muestran que la
   temperatura limita la duración de los ensayos.

## Restricciones de integración

- El AS5600 debe medir el eje real de salida de la articulación; montarlo en el
  lado incorrecto de la transmisión impediría observar la holgura relevante.
- Cada soporte requiere alineación coaxial, separación imán-sensor controlada y
  verificación de diagnóstico magnético antes de instalar los doce.
- La lógica I2C de la Raspberry Pi debe permanecer compatible con 3,3 V. Debe
  comprobarse el voltaje de las resistencias `pull-up` de todas las tarjetas.
- Se separarán los recorridos de señal y potencia, se mantendrá tierra común y
  se caracterizará el ruido con los servos apagados y encendidos.
- La adquisición es secuencial, no simultánea. Se medirán frecuencia efectiva,
  latencia, dispersión temporal y pérdidas del barrido completo.
- Cada muestra se publicará con marca temporal y estado de salud. Una interfaz
  prevista es `/nova/joint_states_measured`, sin confundirla con referencias ni
  con estados simulados.
- La incorporación de sensores no habilita todavía postura ni marcha física;
  continúan vigentes calibración individual, OE seguro, protección eléctrica y
  progresión de pruebas.

## Variables previstas para aprendizaje por refuerzo

La observación candidata incluye doce ángulos, doce velocidades filtradas,
doce errores respecto a la referencia, cuatro contactos o fuerzas, orientación,
velocidad angular, aceleración lineal, tensión, corriente, potencia, fase de
marcha y margen de estabilidad.

Las acciones seguirán siendo correcciones pequeñas, acotadas y supervisadas de
las referencias nominales; no se permitirá que una política genere PWM directo.
La recompensa podrá penalizar error articular, inclinación, oscilación,
deslizamiento, saturación, consumo e intervenciones, y premiar avance y margen
de estabilidad. Esta definición continúa pendiente de pruebas y aprobación del
protocolo.

## Validación progresiva acordada

1. Prototipar un AS5600 en una sola articulación y verificar cero, sentido,
   límites, linealidad, repetibilidad y diagnóstico del imán.
2. Repetir el barrido en ambos sentidos, sin carga y con carga, para cuantificar
   holgura e histéresis.
3. Instrumentar una pata mediante un multiplexor y medir ruido, frecuencia,
   latencia y pérdidas con potencia de servos apagada y encendida.
4. Añadir un contacto en un pie y comprobar su repetibilidad antes de instalar
   cuatro unidades.
5. Integrar y sincronizar IMU, contacto, ángulos y potencia en ROS 2.
6. Extender a las doce articulaciones únicamente si el prototipo conserva
   precisión y estabilidad del bus.
7. Comparar las mediciones reales con Gazebo y MuJoCo antes de usarlas para
   entrenamiento o transferencia de una política.

## Evidencia y referencias técnicas

- AS5600, ficha oficial de ams OSRAM:
  <https://look.ams-osram.com/m/7059eac7531a86fd/original/AS5600-DS000365.pdf>
- TCA9548A, información oficial de Texas Instruments:
  <https://www.ti.com/product/TCA9548A>
- BNO055, información oficial de Bosch Sensortec:
  <https://www.bosch-sensortec.com/media/boschsensortec/downloads/product_flyer/bst-bno055-fl000.pdf>
- INA228, información oficial de Texas Instruments:
  <https://www.ti.com/product/INA228>
- VL53L4CD, ficha oficial de STMicroelectronics:
  <https://www.st.com.cn/resource/en/datasheet/vl53l4cd.pdf>

## Decisiones todavía pendientes

- Confirmar modelos exactos y variantes de las tarjetas comerciales.
- Seleccionar FSR, microswitch o celda de carga según geometría del pie.
- Dimensionar el INA228, shunt, conectores, fusible y rango de corriente.
- Diseñar y validar el soporte mecánico de un AS5600.
- Aprobar frecuencia de adquisición, filtros, métricas y criterios de éxito.
- Actualizar presupuesto y diagrama eléctrico antes de comprar o conectar.
