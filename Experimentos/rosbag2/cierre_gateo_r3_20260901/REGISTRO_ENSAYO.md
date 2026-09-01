# Cierre de línea base de gateo — repetición 2 válida

Fecha: 1 de septiembre de 2026. Gazebo, instancia única verificada.

- Configuración: 24 muestras, 0,18 s por referencia, ciclo nominal 4,32 s.
- Ventana `gateo`--`stand`: 220,731955 s.
- Ciclos completos: 50; el primer ciclo se conserva como transitorio.
- Cadencia media: 4,319977 s.
- Avance medio: 0,023899 m/ciclo.
- Velocidad media: 0,005532 m/s.
- Roll/pitch máximos medios: 2,072785/4,096269 grados.
- Salto articular máximo medio: 0,019630 rad.
- Activaciones del supervisor: cero.

La coincidencia simultánea cruda/filtrada fue 20,046/13,099 %. Las pérdidas
traseras filtradas no superaron 0,12 s (máximos crudos RL/RR: 0,096427/0,087604
s), de modo que no se demostró vuelo trasero sostenido.

La bolsa contiene 141.531 mensajes, cuatro órdenes capturadas (tres `gateo` y
una `stand`) y ocupa 74cb5892b975a0b8c9b11a08f97fbccb9fc142639bae6a7bbff2e857f9d65a23
como SHA-256 del SQLite3. Los análisis derivados están en
`Experimentos/analisis_movimiento/cierre_gateo_r3_20260901` y
`Experimentos/analisis/cierre_gateo_r3_20260901`.
