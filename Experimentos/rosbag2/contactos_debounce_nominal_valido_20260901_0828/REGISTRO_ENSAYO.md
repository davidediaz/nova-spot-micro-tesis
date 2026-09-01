# Registro del ensayo nominal de contacto crudo y filtrado

Fecha: 1 de septiembre de 2026, America/Bogota.

## Objetivo

Distinguir un despegue físico sostenido de una interrupción breve producida
por el timeout del sensor de contacto de Gazebo. El ensayo compara el estado
crudo con el estado confirmado por debounce; el filtro permanece informativo y
no modifica la trayectoria ni activa una parada.

## Configuración congelada

- Marcha: `gateo/crawl`, 24 muestras por ciclo.
- Paso: 0,018 m; elevación: 0,014 m.
- Duración: 0,18 s por referencia; 4,32 s por ciclo.
- Transferencia lateral/longitudinal: 0,004/0,008 m.
- Curvas de descenso y ascenso: nominales, `0,7071067811865476`.
- Timeout de contacto: 0,10 s.
- Debounce de pérdida/recontacto: 0,12/0,03 s.
- Commit durante la ejecución: `5a67ea18cc61e7bbca496a370e32b8292c62c291`.

Antes de grabar se confirmó una sola instancia de cada nodo y cuatro contactos
en `stand`. También se observó que el diagnóstico publicaba explícitamente
`raw_observed_contacts` y `filtered_observed_contacts`.

## Integridad

- Bolsa: `contactos_debounce_nominal_valido_20260901_0828`.
- Ventana `gateo`--`stand`: 105,522328 s.
- Ciclos completos: 24.
- Duración media observada: 4,319990 s/ciclo.
- Mensajes totales: 79.790; fases: 587; trayectorias: 589.
- Marcadores: un `gateo` y tres `stand`.
- Eventos verdaderos del supervisor: 0.
- Tamaño SQLite3: aproximadamente 60,7 MiB.

SHA-256:

- SQLite3: `80cf336121eaa630c4e27b94c74e056d085e1ebd0c5169b79bbdd7e161864f82`.
- `gaits.yaml`: `ab00f5af5aa99680d0da2780dbce29746eccb2733df59fcb4881a78c01798c9a`.
- `monitoring.yaml`: `be89c1236f2c39e2fabe1d506b2a5a09d44fafecec261201697d00494a81736a`.
- analizador de contactos: `b9bd63b4cbaf3b79e19a8fd15a65798cc5dabc861e34f080335bafde02a8aaef`.
- analizador de movimiento: `049bcaadf9dd3fe8eb8427001205a54c7a27cc6b0192bbbad7171082b4b9cb2d`.

La base SQLite3 y `metadata.yaml` permanecen locales por la política de datos
pesados de `.gitignore`; el registro, CSV e informes sí se conservan en Git.

## Resultado

- Coincidencia simultánea cruda: 20,638810 %.
- Coincidencia simultánea filtrada: 13,621271 %.
- FL/FR: los episodios sin contacto duran aproximadamente 0,94 s y sí superan
  el umbral de persistencia.
- RL: 24 episodios crudos, media 0,074645 s, máximo 0,089805 s y cero episodios
  por encima de 0,12 s.
- RR: 25 episodios crudos, media 0,073803 s, máximo 0,089396 s y cero episodios
  por encima de 0,12 s.
- Avance: 0,023558 m/ciclo; velocidad: 0,005453 m/s.
- Roll/pitch máximos medios: 2,074511/4,102216 grados.

Conclusión: las transiciones traseras del estado crudo son interrupciones
breves y no demuestran vuelo sostenido. El menor porcentaje filtrado no indica
un empeoramiento mecánico causado por el filtro: refleja una clasificación más
conservadora y el retardo deliberado de confirmación. La trayectoria nominal
sigue sin producir despegue trasero confirmado.

Informes asociados:

- `../../analisis/contactos_debounce_nominal_valido_20260901_0828/INFORME_CONTACTOS.md`.
- `../../analisis_movimiento/contactos_debounce_nominal_valido_20260901_0828/INFORME_ANALISIS.md`.

La tentativa `contactos_debounce_nominal_20260901_0823` es inválida porque no
almacenó fases de gateo y se conserva con su explicación separada.
