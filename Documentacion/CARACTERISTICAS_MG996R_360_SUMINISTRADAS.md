# Características suministradas de los doce servos

Fuente archivada: `Fuentes/MG996R-360_AG_Electronica.pdf` (3 páginas).
SHA-256: `9cbb94b33d2b84a52fad1c8379f98d6034231150f4b8f29b6a0fcd1054addd5d`.

| Magnitud | Valor declarado |
|---|---:|
| Tensión | 4,8--6,6 V |
| Par a 4,8 V | 9,4 kgf cm = 0,921825 N m |
| Par a 6,0 V | 11 kgf cm = 1,078732 N m |
| Velocidad a 4,8 V | 0,19 s/60° = 5,511566 rad/s |
| Velocidad a 6,0 V | 0,15 s/60° = 6,981317 rad/s |
| Masa | 55 g |
| Banda muerta | 1 microsegundo de pulso PWM |
| Temperatura | 0--55 °C |
| Engranajes/rodamiento | metal/doble rodamiento de bolas |
| Dimensiones A--F | 42,7; 40,9; 37; 20; 54; 26,8 mm |

## Ambigüedades y faltantes

La portada y la tabla denominan el producto `MG996R-360` y anuncian 360 grados,
pero la descripción dice «su giro es 60°», posiblemente confundiendo el
intervalo de medición de velocidad con el rango angular. La fotografía muestra
una etiqueta MG996R convencional. La ficha no define relación pulso--posición,
topes, control posicional en 360 grados ni rotación continua. Por ello no se
cambia el URDF hasta comprobar físicamente si el pulso ordena posición o
velocidad.

La ficha tampoco declara corriente en vacío, nominal o de bloqueo. Los valores
de 0,17/1,40 A y los límites de corriente de los perfiles continúan siendo
hipótesis; deben medirse con un servo asegurado y una fuente limitada.

## Comprobación física mínima

Con una unidad desacoplada, fuente limitada y OE accesible: registrar la
etiqueta, observar si 1500 microsegundos detiene o centra, aplicar pulsos
pequeños a ambos lados y determinar si se ordena posición o velocidad. No se
debe forzar ningún tope ni extrapolar una unidad a las doce sin verificar cada
canal.
