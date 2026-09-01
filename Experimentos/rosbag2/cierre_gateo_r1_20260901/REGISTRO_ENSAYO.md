# Cierre de línea base de gateo — repetición 1

Fecha: 1 de septiembre de 2026. Ejecución independiente en Gazebo.

- Configuración: 24 muestras, 0,18 s por referencia, ciclo nominal 4,32 s.
- Ventana `gateo`--`stand`: 126,025836 s.
- Ciclos completos: 29; el primero se conserva como transitorio.
- Cadencia media observada: 4,319985 s.
- Avance medio: 0,023658 m/ciclo.
- Velocidad media: 0,005476 m/s.
- Roll/pitch máximos medios: 2,072463/4,096528 grados.
- Salto articular máximo medio: 0,019621 rad.
- Activaciones verdaderas del supervisor: cero.

La coincidencia simultánea cruda/filtrada fue 20,425/13,455 %. Las pérdidas
traseras crudas alcanzaron como máximo 0,080615 s en RL y 0,088292 s en RR;
ninguna superó 0,12 s. Se reprodujo así la limitación de contacto conocida y no
se demostró vuelo trasero sostenido.

Integridad:

- bolsa SQLite3: `fa18711477c53cdcb0fa3c2fabfde9658aaa52a0f4d479986472a50edbdbf0e9`;
- `gaits.yaml`: `ab00f5af5aa99680d0da2780dbce29746eccb2733df59fcb4881a78c01798c9a`;
- `monitoring.yaml`: `be89c1236f2c39e2fabe1d506b2a5a09d44fafecec261201697d00494a81736a`.

La bolsa contiene 101.370 mensajes y ocupa 81,0 MiB; permanece local por la
política de datos pesados. Los CSV, gráficas e informes derivados sí se
versionan. Esta ejecución cuenta como repetición 1 de 5 y no cierra por sí sola
la línea base final.
