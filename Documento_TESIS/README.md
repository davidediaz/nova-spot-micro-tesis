# Documento final de tesis

Esta carpeta reúne, desde el 1 de septiembre de 2026, el material que se
convertirá en la entrega final de la tesis sobre el robot cuadrúpedo Nova Spot
Micro. Es distinta del anteproyecto ubicado en `tesis_overleaf`: aquel archivo
sirve como antecedente y fuente revisable, pero no debe confundirse con el
documento final.

## Criterio de redacción

El texto final describirá el trabajo ejecutado y la evidencia obtenida. Se
emplearán formulaciones como:

- «se diseñó», «se implementó» y «se verificó» para actividades terminadas;
- «se analizó» y «se obtuvo» para resultados respaldados por datos;
- «se encontró» o «los resultados indicaron» para interpretaciones;
- «permaneció pendiente» o «no se demostró» cuando una actividad no esté
  cerrada.

No se transformarán automáticamente expresiones del anteproyecto como «se
realizará» en afirmaciones de cumplimiento. Cada afirmación en pasado deberá
estar respaldada por código, configuración, protocolo, registro, tabla, figura,
prueba o medición identificable.

## Cadena obligatoria de trazabilidad

Cada resultado del documento debe poder recorrerse en ambos sentidos:

`problema → pregunta → objetivo → actividad → método → evidencia → resultado → conclusión`

Una conclusión sin resultado verificable se tratará como una interpretación no
demostrada. Una simulación incluirá modelo, supuestos, parámetros, condiciones,
configuración, resultados, contraste e identificación explícita de sus
limitaciones.

## Organización inicial

- `Presentacion_PartiendoCronograma.pdf`: orientación de Proyecto de Grado II
  sobre ejecución, evidencia, criterios de aceptación y productos documentales.
- `MATRIZ_OBJETIVO_EVIDENCIA.md`: mapa vivo entre objetivos, métodos, evidencia,
  resultados y secciones finales.
- `PLAN_DOCUMENTO_FINAL.md`: estructura y reglas para migrar contenido del
  anteproyecto sin afirmar resultados todavía inexistentes.

Los capítulos editables en LaTeX se incorporarán progresivamente cuando se
revise cada sección. Los datos pesados de rosbag2 permanecen en
`Experimentos/rosbag2`; dentro de esta carpeta se citarán sus registros, hashes,
tablas y gráficas reproducibles sin duplicar las bases de datos.

## Fuente recibida

La presentación fue copiada desde
`/home/pavilion/Descargas/Presentacion_PartiendoCronograma.pdf`. Ambas copias
tenían el SHA-256:

`200ed2f5ada680325b5bbbd9efd83e2e906b9bdb65c609715d209c7a88cdc160`
