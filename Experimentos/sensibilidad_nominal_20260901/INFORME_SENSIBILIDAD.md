# Criba de sensibilidad dinámica nominal

Fecha: 1 de septiembre de 2026. Análisis determinista sin Gazebo ni MuJoCo.

Se evaluaron 14 combinaciones de marcha y escenario. La mayor variación
del par máximo frente al caso nominal fue -8.997415 % en
`paso/masa_menos_10`. Los pares proceden de dinámica
inversa sobre referencias discretas; la corriente usa la envolvente de catálogo
del MG996R y no constituye una predicción eléctrica validada.

Este análisis prioriza masas y resistencias articulares. Geometría, fricción de
suelo, contacto y retardos deben estudiarse en simuladores porque esta criba no
integra movimiento del cuerpo ni solución temporal del contacto.
