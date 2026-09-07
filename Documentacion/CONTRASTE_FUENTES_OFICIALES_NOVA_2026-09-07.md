# Dimensiones, masa y límites: contraste con las fuentes oficiales

Consulta: 7 de septiembre de 2026. Revisión documental de OE1; no es una
caracterización experimental. No se modificaron parámetros ni columnas de
mediciones físicas.

## Dimensiones de referencia

El enlace de código Teensy de la [página oficial de archivos](https://novaspotmicro.com/parts-list.html)
conduce a una carpeta v5.0, aunque la página anuncia v5.2b. Se identifica la
versión efectivamente consultada, sin asumir que ambas son iguales.

| Magnitud | Código oficial v5.0 | Modelo local | Diferencia documental |
|---|---:|---:|---:|
| Coxa / hombro | 90 mm | 90 mm | 0 mm |
| Fémur | 105 mm | 105 mm | 0 mm |
| Tibia | 132 mm | 132 mm | 0 mm |
| Separación longitudinal de pivotes | 180 mm | 180 mm | 0 mm |
| Separación transversal de pivotes | 120 mm | 120 mm | 0 mm |

Fuente: [NovaServos.h, bodyBone y servoBone](https://github.com/cguweb-com/Arduino-Projects/blob/main/Nova-SM3/Code/Nova-SM3_teensy-v5.0/NovaServos.h).
El archivo también indica 200 mm del suelo al pivote de coxa y marca estos
arreglos como previstos para cinemática futura. Esa altura depende de la
postura; no es el espesor de la carcasa.

Nuestro cuerpo de 230 × 120 × 75 mm es una caja simplificada del URDF. No se
localizó una cota exterior equivalente en las páginas consultadas. Tampoco se
confirmó documentalmente el diámetro de pie de 36 mm. Los archivos CAD/STL
están enlazados en [Bones & Body](https://novaspotmicro.com/the-bones-body.html),
pero no se extrajeron cotas del visor Autodesk, que no pudo consultarse con la
herramienta utilizada. Los ceros de la tabla indican coincidencia de referencias,
no error físico nulo.

## Masa

El autor declara aproximadamente seis libras para su montaje completo en
[The Muscles](https://novaspotmicro.com/the-muscles.html). Conversión:
6 × 0,45359237 = 2,72155422 kg, aproximadamente 2,72 kg. El modelo local suma
2,72 kg; la diferencia aritmética es −1,554 g, pero la fuente es aproximada y
no permite afirmar precisión a gramos.

Nuestro reparto (cuerpo/electrónica 1,20 kg y cuatro patas de 0,38 kg) es una
estimación de ingeniería. No se encontraron masas medidas por eslabón en las
páginas consultadas. El material, relleno, refuerzos, electrónica y motores
cambian la masa del ejemplar. Debemos pesarlo completo y por conjuntos.

## Límites de movimiento y diferencia de motores

El código [NovaServos.h](https://github.com/cguweb-com/Arduino-Projects/blob/main/Nova-SM3/Code/Nova-SM3_teensy-v5.0/NovaServos.h)
publica `servoHome` y `servoLimit` por motor; por ejemplo, para la pata delantera
derecha los pares son 314–434, 185–515 y 365–607. Son valores de control PWM,
no grados ni radianes. El [programa principal](https://github.com/cguweb-com/Arduino-Projects/blob/main/Nova-SM3/Code/Nova-SM3_teensy-v5.0/Nova-SM3_teensy-v5.0.ino)
configura 60 Hz. No se trasladan esos valores a nuestros motores.

La [lista oficial de componentes](https://novaspotmicro.com/parts-list.html)
especifica ocho DS3218 anunciados como 20KG/270° y cuatro servos de 35KG/7,4 V.
No corresponde a los MG996R documentados en nuestro prototipo. Los 270° del
producto no equivalen al recorrido mecánico seguro de una articulación montada.

| Articulación | Límites locales en radianes | Equivalente aproximado |
|---|---|---|
| Coxa | −0,60 a +0,60 | −34,4° a +34,4° |
| Fémur | −1,20 a +1,20 | −68,8° a +68,8° |
| Tibia | −2,20 a +0,10 | −126,1° a +5,7° |

Son límites provisionales del URDF, no límites físicos calibrados. La ficha
local `CARACTERISTICAS_MG996R_360_SUMINISTRADAS.md` documenta además ambigüedad
sobre el rango del MG996R-360 y ausencia de corriente declarada.

## Resultado y siguiente acción

Se corroboraron cinco dimensiones nominales y el orden de magnitud de masa.
Continúan pendientes las medidas reales, masas por conjunto, centros y límites
por motor, holguras y validación bajo carga. Mantener vacías las columnas m1,
m2 y m3 hasta medir. El contraste de fuentes no cierra OE1 ni aumenta por sí
solo su porcentaje.

Texto recomendado para el pendiente: «Dimensiones nominales contrastadas con la
fuente oficial; falta medir nuestro ejemplar y validar masas y límites de sus
actuadores».

Archivos locales cotejados: `src/nova_sm3_description/urdf/nova_sm3.urdf.xacro`,
`Documentacion/caracterizacion_fisica_geometria.csv`,
`Documentacion/caracterizacion_fisica_masas.csv` y ficha MG996R suministrada.
