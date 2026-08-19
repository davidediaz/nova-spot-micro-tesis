# Diseño técnico de la marcha paso

Versión inicial: 14 de agosto de 2026.

## Objetivo

Implementar un patrón cartesiano conservador distinto del gateo base, con una
pata en oscilación, transferencia lateral explícita y retorno periódico sin
saltos grandes de referencia.

## Secuencia

- Orden: delantera izquierda, trasera derecha, delantera derecha, trasera
  izquierda.
- 32 referencias por ciclo.
- Ocho referencias por paso de una pata.
- Apoyo nominal: 75 % del ciclo.
- Oscilación nominal: 25 % del ciclo.
- Transferencia lateral sinusoidal, dirigida fuera de la pata en oscilación.

## Parámetros iniciales

| Parámetro | Valor |
|---|---:|
| Duración por referencia | 0,18 s |
| Duración nominal del ciclo | 5,76 s |
| Longitud de paso | 0,016 m |
| Elevación | 0,008 m |
| Transferencia lateral | 0,004 m |

La elevación se redujo de una primera propuesta de 0,012 m a 0,008 m porque las
pruebas detectaron un salto objetivo máximo superior a 0,10 rad. Con 0,008 m el
salto cíclico máximo quedó por debajo de 0,08 rad.

## Formulación

Durante apoyo, el pie se desplaza hacia atrás respecto al cuerpo. Durante
oscilación, avanza desde el extremo posterior al anterior con elevación
parabólica. Los extremos de la oscilación se incluyen explícitamente en el
muestreo discreto para evitar una discontinuidad al volver al apoyo.

La transferencia lateral se expresa como:

`y_shift = side * weight_shift * sin(pi * quarter_progress)`

donde el signo desplaza el tronco hacia el lado opuesto a la pata en
oscilación. Cada objetivo cartesiano se convierte mediante la IK propia y se
rechaza si viola alcance o límites articulares.

La referencia de Mike4192 se utilizó solo para contrastar los conceptos de
control de apoyo, siguiente punto de contacto y transferencia corporal. La
geometría, parámetros, convención de ejes y código son propios de NovaSM3.

## Pruebas

- 26 pruebas automatizadas aprobadas.
- 32 objetivos de 12 articulaciones, todos alcanzables.
- Continuidad verificada, incluido el cierre del ciclo.
- Transferencia lateral acotada a 0,004 m.
- Paquete ROS 2 recompilado correctamente.

## Ensayo exploratorio en Gazebo

Bolsa: `Experimentos/rosbag2/paso_exploratorio_20260814`.

- cuatro ciclos completos;
- ciclo observado medio: 5,759993 s;
- avance medio: 0,020730 m/ciclo, incluyendo el transitorio;
- velocidad media: 0,003599 m/s;
- excursión lateral media: 0,005490 m;
- roll máximo medio: 1,275295 grados;
- pitch máximo medio: 2,496521 grados;
- salto articular máximo medio: 0,008528 rad;
- cero activaciones del supervisor.

El resultado permite avanzar a una línea base de al menos diez ciclos en
Gazebo. La validación posterior en Gazebo y MuJoCo está documentada en
`MARCHA_PASO_VALIDACION.md`; el hardware continúa fuera de alcance hasta cerrar
caracterización, seguridad eléctrica y calibración.
