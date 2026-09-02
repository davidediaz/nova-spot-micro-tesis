# Identificación de masas, centro de masa e inercia

## Masa y centro de masa

Tarar la balanza antes de cada conjunto y realizar tres lecturas. Medir robot
completo, cuerpo con electrónica y cada pata únicamente si el desmontaje es
seguro. Para el centro de masa, apoyar el robot en tres orientaciones conocidas
o usar una plataforma de reacción; registrar la geometría de apoyo y no
redondear antes de calcular.

## Inercia

Usar péndulo torsional o péndulo compuesto calibrado, nunca estimar la inercia
desde la apariencia. Registrar periodo, masa, distancia al eje, constante del
dispositivo, amplitud y al menos cinco repeticiones. Reportar incertidumbre y
la convención de ejes. Si no se dispone del montaje, dejar la fila como
`pendiente` y conservar los parámetros nominales solo como hipótesis.

La actualización de URDF/MJCF requiere comparar masa, centro e inercia medidos
contra el modelo y aprobar explícitamente cada cambio.
