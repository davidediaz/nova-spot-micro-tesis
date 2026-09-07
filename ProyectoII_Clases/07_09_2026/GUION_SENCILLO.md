# Guion: siete diapositivas y cuatro objetivos

Versión vigente: `Primera_entrega_avances_objetivos_corregidos`. Fuentes y porcentajes en `GUIA_EXPOSICION.md`.

## Diapositiva 1

Objetivo general: Desarrollar un sistema de control para la plataforma cuadrúpedo Spot Micro que integre aprendizaje por refuerzo para su ejecución y estabilización en los diferentes modos de locomoción tipo paso y gateo en condiciones de entorno controladas.

## Diapositiva 2

Los cuatro objetivos tienen un avance estimado del 50 %, por motivos diferentes. OE1: software y movimiento inicial, con integración física pendiente. OE2: modelo y pruebas computacionales, con contraste pendiente. OE3: estrategia y entrenamiento, sin estabilidad y continuidad demostradas. OE4: seguimiento y repetibilidad en simulación, con margen estático y evaluación integral pendientes. La rúbrica de la guía explica los cuatro hitos de cada objetivo.

## Diapositiva 3

Estos son los cuatro objetivos originales. El primero reúne hardware y software; el segundo es modelado; el tercero es control aprendido; el cuarto exige tres pruebas concretas. Todos están parciales. Los porcentajes se recalcularon con una rúbrica por entregables y no significan una calificación. El entrenamiento no demuestra por sí solo estabilidad ni continuidad.

## Diapositiva 4

Gazebo y MuJoCo son programas que simulan el robot. En Gazebo hicimos cinco pruebas y el avance medio fue de unos 2,4 centímetros por cada secuencia completa de gateo. En MuJoCo ajustamos el movimiento y el avance pasó de 2,7 a 9,9 milímetros por ciclo. Aún falta mejorar cuándo despega y aterriza cada pata. El programa de seguridad detectó los nueve fallos que provocamos y envió la orden de detener la marcha; falta comprobar la parada eléctrica real. Entrenamos el algoritmo de aprendizaje cinco veces, pero sus correcciones no cumplieron los criterios de mejora. La captura de Gazebo ilustra el modelo actual: los números vienen de los informes de pruebas anteriores.

## Diapositiva 5

La tesis ya tiene un borrador de 72 páginas. Están escritos el modelo, los procedimientos, el funcionamiento del sistema y los resultados disponibles. Faltan las mediciones y pruebas del robot real, la comparación final y las conclusiones definitivas. También debemos añadir las nuevas pruebas y fotos. Hay frases antiguas que dicen que no hemos entrenado el algoritmo, aunque ya lo hicimos. Vamos a corregirlas para que el documento refleje el mismo estado en todas sus secciones. Tener los capítulos escritos no significa que la tesis esté terminada.

## Diapositiva 6

El orden de trabajo empieza por resolver el exceso de corriente y comprobar el apagado seguro. Después ajustaremos un motor y una pata antes de probar el robot completo. Registraremos sus movimientos y el consumo. Finalmente evaluaremos las correcciones aprendidas frente al movimiento básico, usando las mismas condiciones. La comparación debe mostrar tanto lo que mejora como lo que empeora. En paralelo actualizaremos la tesis. Las principales dificultades son la validación física pendiente y que aún no hemos demostrado la mejora mediante aprendizaje.

## Diapositiva 7

Para la próxima revisión proponemos entregar un informe de revisión eléctrica y una versión actualizada de la tesis. El informe debe decir qué revisamos, qué medimos, con qué instrumentos y qué falta. Si una prueba no puede hacerse con seguridad, lo registraremos como pendiente. No prometemos una caminata antes de resolver esos requisitos. Nuestro proyecto todavía no puede darse por terminado porque falta comprobar la marcha segura del robot real y evaluar las correcciones aprendidas. La evidencia de cierre serán pruebas comparables, mediciones y conclusiones que expliquen lo que funcionó y lo que no.
