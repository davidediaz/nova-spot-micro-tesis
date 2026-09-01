# Línea base de marcha paso — repetición 1 válida

Fecha: 1 de septiembre de 2026. Instancia única y suscriptores verificados.

- Ventana `paso`--`stand`: 122,092760 s.
- Ciclos completos: 21; cadencia media 5,760859 s.
- Avance medio: 0,021663 m/ciclo; velocidad 0,003760 m/s.
- Roll/pitch máximos medios: 1,280799/2,485997 grados.
- Salto articular máximo medio: 0,008427 rad.
- Activaciones del supervisor: cero.
- Tres órdenes `paso` y dos órdenes `stand` capturadas.

La bolsa contiene 101.648 mensajes. SHA-256 del SQLite3:
`78c6d7f535415fccc6b1e0bf08b26695f141963d57a07409fc058c28de01a39c`.
El análisis de movimiento quedó en `Experimentos/analisis_movimiento`.
El análisis de contactos quedó en `Experimentos/analisis/cierre_paso_r1_20260901`:
21 ciclos, coincidencia simultánea cruda 39,067 % y filtrada 34,787 %. La
adaptación del analizador reconoce ahora `paso/step` y conserva compatibilidad
con `gateo/crawl`.
