# Guion sencillo para explicar las siete diapositivas

Versión vigente: `Primera_entrega_avances_7_diapositivas.pptx` y PDF. La diapositiva adicional fue solicitada por el usuario. La nueva diapositiva 3 detalla los objetivos; resultados pasa a la 4. Ensayar para mantener la exposición en 8–10 minutos. Porcentajes y fuentes en `GUIA_EXPOSICION.md`.

## Diapositiva 1

Nuestro propósito es que el robot camine de forma estable y comprobar si el aprendizaje ayuda a mejorar su movimiento. Ya tenemos el modelo en simulación y el prototipo que se ve en las fotografías. En las pruebas físicas respondieron los doce motores, pero apareció un exceso de corriente y detuvimos las pruebas. Todavía debemos resolver la causa antes de continuar. Las fotografías muestran la construcción; no demuestran por sí solas una marcha segura.

## Diapositiva 2

Cada fila corresponde a uno de los cinco objetivos. Para el primero tenemos un modelo matemático, pero falta contrastarlo con mediciones del robot. Para el segundo tenemos un programa que detecta fallos, pero falta comprobar la seguridad eléctrica. En el tercero ya creamos y probamos movimientos en simulación. En el cuarto entrenamos el algoritmo, aunque no logró la mejora buscada. El quinto está menos avanzado porque falta completar la comparación. Estos porcentajes son estimaciones: dividimos cada objetivo en cuatro etapas y cada etapa cerrada suma 25 %. La guía técnica explica cuáles son.

## Diapositiva 3

Esta diapositiva explica qué buscamos con cada objetivo y qué falta para cerrarlo. Todos tienen avances, pero ninguno está cumplido por completo. El tercero es el más avanzado porque ya implementamos y probamos los movimientos en simulación. El quinto tiene menor avance: faltan la comparación final y las pruebas del robot real. En el cuarto entrenar el algoritmo cuenta como trabajo realizado, pero todavía no demuestra la mejora buscada. Los porcentajes son estimaciones justificadas en la guía, no una calificación del profesor.

## Diapositiva 4

Gazebo y MuJoCo son programas que simulan el robot. En Gazebo hicimos cinco pruebas y el avance medio fue de unos 2,4 centímetros por cada secuencia completa de gateo. En MuJoCo ajustamos el movimiento y el avance pasó de 2,7 a 9,9 milímetros por ciclo. Aún falta mejorar cuándo despega y aterriza cada pata. El programa de seguridad detectó los nueve fallos que provocamos y envió la orden de detener la marcha; falta comprobar la parada eléctrica real. Entrenamos el algoritmo de aprendizaje cinco veces, pero sus correcciones no cumplieron los criterios de mejora. La captura de Gazebo ilustra el modelo actual: los números vienen de los informes de pruebas anteriores.

## Diapositiva 5

La tesis ya tiene un borrador de 73 páginas. Están escritos el modelo, los procedimientos, el funcionamiento del sistema y los resultados disponibles. Faltan las mediciones y pruebas del robot real, la comparación final y las conclusiones definitivas. También debemos añadir las nuevas pruebas y fotos. Hay frases antiguas que dicen que no hemos entrenado el algoritmo, aunque ya lo hicimos. Vamos a corregirlas para que el documento refleje el mismo estado en todas sus secciones. Tener los capítulos escritos no significa que la tesis esté terminada.

## Diapositiva 6

El orden de trabajo empieza por resolver el exceso de corriente y comprobar el apagado seguro. Después ajustaremos un motor y una pata antes de probar el robot completo. Registraremos sus movimientos y el consumo. Finalmente evaluaremos las correcciones aprendidas frente al movimiento básico, usando las mismas condiciones. La comparación debe mostrar tanto lo que mejora como lo que empeora. En paralelo actualizaremos la tesis. Las principales dificultades son la validación física pendiente y que aún no hemos demostrado la mejora mediante aprendizaje.

## Diapositiva 7

Para la próxima revisión proponemos entregar un informe de revisión eléctrica y una versión actualizada de la tesis. El informe debe decir qué revisamos, qué medimos, con qué instrumentos y qué falta. Si una prueba no puede hacerse con seguridad, lo registraremos como pendiente. No prometemos una caminata antes de resolver esos requisitos. Nuestro proyecto todavía no puede darse por terminado porque falta comprobar la marcha segura del robot real y evaluar las correcciones aprendidas. La evidencia de cierre serán pruebas comparables, mediciones y conclusiones que expliquen lo que funcionó y lo que no.
