# Primera entrega de avances — 7 de septiembre de 2026

Presentación ampliada a siete diapositivas por solicitud explícita del usuario. Ensayar para conservar 8–10 minutos.
Los porcentajes y el compromiso son propuestas para revisión del grupo; no son
calificaciones ni decisiones ya aprobadas por los directores.

## Archivos

- `Primera_entrega_avances_7_diapositivas.pptx`: versión vigente editable, con las cinco fotografías y notas del orador.
- `Primera_entrega_avances_7_diapositivas.pdf`: versión vigente para proyectar. Los archivos anteriores se conservan.
- `generar_presentacion.py`: fuente reproducible con python-pptx.
- Guía del profesor: `/home/pavilion/Descargas/Primera entrega de avances - Proyecto de grado II.pdf`.

## Cómo se estimó el avance

Se proponen cuatro hitos de igual peso por objetivo (25 % cada uno). Solo se
puntúan hitos cerrados con evidencia; un hito parcial no suma. Esto mide avance
por entregables, no dificultad, horas invertidas ni probabilidad de éxito.
No se calcula un porcentaje global: los objetivos tienen dependencias y alcances diferentes.

| OE | Cuatro hitos propuestos | Cálculo |
|---|---|---|
| OE1 | Modelo cinemático implementado ✓; dinámica nominal y verificación computacional ✓; caracterización física completa pendiente; identificación/contraste físico pendiente | 2/4 = 50 % |
| OE2 | Arquitectura ROS 2 integrada ✓; reacción del supervisor en nueve escenarios ✓; electrónica y protecciones físicas parciales; calibración, rearme y validación integral pendientes | 2/4 = 50 % |
| OE3 | Generador cartesiano e IK ✓; máquina de estados de postura/paso/gateo ✓; ensayos repetibles en simulación ✓; validación física pendiente | 3/4 = 75 % |
| OE4 | Contrato residual acotado ✓; cinco semillas entrenadas ✓; política aceptada en validación pendiente; integración progresiva física pendiente | 2/4 = 50 % |
| OE5 | Diseño de cantidades y semillas documentado ✓; comparación exploratoria parcial, sin cierre de campaña; análisis final emparejado pendiente; comparación física pendiente | 1/4 = 25 % |

En OE3 el hito de simulación acredita ejecución y repetibilidad, no equivalencia
dinámica ni ajuste completo del patrón de contacto. En OE5 el primer hito solo
acredita el diseño de cantidades y semillas: métricas y umbrales finales siguen
pendientes de acuerdo. Entrenar una política en OE4 no significa demostrar mejora.

## Evidencias para abrir si el profesor las solicita

Rutas relativas a `/home/pavilion/Documentos/Cuadrupedo`:

| Afirmación | Evidencia |
|---|---|
| Objetivos completos y alcance | `Documento_TESIS/Chapters/3 Objetivos.tex` |
| Modelado nominal, OE1 | `Documentacion/MODELO_MATEMATICO_LATEX/main.pdf`; `Documento_TESIS/MATRIZ_OBJETIVO_EVIDENCIA.md` |
| Reacción de seguridad, OE2 | `Experimentos/pruebas_dinamicas_supervisor_20260902/`; `Documentacion/PRUEBAS_AUTOMATICAS_SEGURIDAD.md` |
| Gateo Gazebo: cinco ensayos y 23,955 mm/ciclo | `Documento_TESIS/Chapters/10 Resultados.tex`, tabla de síntesis; campaña `cierre_gateo_*_20260901` |
| Mejora de contacto trasero mediante precarga | `Experimentos/rosbag2/preload_gateo_200_r2_20260901/`; tabla de síntesis de resultados |
| Campañas MuJoCo del 3 de septiembre, OE3 | `Documentacion/MUJOCO_CIERRE_2026-09-03.md`; `Experimentos/campanas_mujoco/paso_ajustado_5x20_20260903/` |
| PPO entrenado, no aceptado, OE4/OE5 | `Experimentos/DIAGNOSTICO_REFERENCIA_PPO_ESCALA_CERO_20260902.md`; capítulo de resultados |
| Diseño de muestra, OE5 | `Documentacion/DECISION_TAMANO_MUESTRAL_Y_SEMILLAS_RL.md` |
| Movimiento inicial y sobrecarga física | `CONTINUIDAD.md`, entrada del 4 de septiembre; `Seguimiento/Seguimiento.md`, estado de hardware al 4 de septiembre |
| Ruta de cierre físico | `Raspberry/PLAN_VALIDACION_FISICA_DESPUES_SIMULACION_2026-09-02.md` |
| Documento final actual | `Documento_TESIS/Documento_TESIS_PRELIMINAR.pdf`, 73 páginas verificadas el 7 de septiembre |

Las cifras se transcribieron de informes existentes; esta preparación no ejecutó
nuevas campañas ni volvió a analizar las bolsas. Los experimentos locales sin
seguimiento Git se conservaron intactos.

## Respuestas a las ocho preguntas del profesor

1. **¿Qué evidencia demuestra cada objetivo?** OE1: modelo, código y pruebas; OE2: arquitectura y nueve registros de fallos provocados; OE3: bolsas, CSV y campañas de marcha; OE4: políticas entrenadas y evaluaciones; OE5: protocolo y comparación descriptiva. Todas demuestran alcance parcial; ninguna sustituye las mediciones físicas pendientes.
2. **¿Qué resultados concretos se obtuvieron y qué significan?** El gateo Gazebo produjo 23,955 mm/ciclo en su campaña nominal. El paso ajustado MuJoCo alcanzó 9,87 mm/ciclo y 36,58 % de coincidencia de contactos frente a 2,70 mm/ciclo y 0 % nominal. La simulación permite registrar y mejorar el comportamiento; no demuestra transferencia física. El supervisor respondió en nueve escenarios y PPO no cumplió el criterio conjunto de aceptación.
3. **¿Qué objetivo tiene menor cumplimiento?** OE5: la comparación final necesita una política revisada, métricas acordadas y un robot caracterizado y seguro; todavía no existe la comparación física ni la campaña final emparejada.
4. **¿Qué resultados están incorporados al documento?** Modelado, líneas base Gazebo, contacto crudo/filtrado, precarga, supervisor, entrenamiento y resultado negativo PPO, y comparación inicial de 11 ciclos Gazebo–MuJoCo. Las campañas MuJoCo del 3 de septiembre y la incidencia física del 4 requieren actualización documental.
5. **¿Qué falta para formular conclusiones?** Caracterización y calibración, mediciones de seguridad y locomoción física, criterios finales y comparación emparejada. Ya se pueden formular conclusiones limitadas de simulación y del resultado negativo PPO; no afirmar superioridad RL ni cierre físico.
6. **¿Qué debe actualizarse del anteproyecto?** Metodología en función de lo ejecutado, alcance del modelo digital configurable, resultados y límites reales de PPO, instrumentación realmente disponible, cronograma y presupuesto. Evitar convertir mecánicamente futuro en pasado.
7. **¿Cuál sería la principal debilidad si sustentáramos hoy?** La brecha de validación física, junto con la ausencia de evidencia de mejora de la capa aprendida. El movimiento de doce servos y una postura observada no satisfacen una campaña de locomoción segura.
8. **¿Qué debe ocurrir para declarar terminado el trabajo?** Cerrar los criterios físicos, completar la evaluación prevista con datos válidos y resultados reproducibles, vincular conclusiones con cada objetivo y entregar el documento coherente. Si el resultado RL sigue siendo negativo, debe reportarse y acordarse con los directores cómo afecta el alcance; no declarar integración o mejora que no ocurrió.

## Compromiso propuesto y aceptación

Para la siguiente revisión: informe de diagnóstico eléctrico y calibración
inicial, junto con la tesis sincronizada. Debe registrar fecha, montaje,
instrumentos, tensiones, consumos de canales/grupos efectivamente ensayados,
estado de CH1 y de la parada física, incidencias y decisión de continuar o
mantener el bloqueo. Una prueba que no pueda ejecutarse queda marcada como
pendiente con su motivo; no se prometen mediciones ni caminatas sin condiciones.
La tesis deberá incorporar las campañas nuevas y corregir las conclusiones sobre
PPO, recompilarse e inspeccionarse visualmente.

## Correcciones documentales detectadas, aún pendientes

- Conclusión 6: dice que falta entrenar las políticas, aunque el capítulo de resultados documenta entrenamiento y evaluación.
- Tabla inicial de resultados: limita MuJoCo a cadencia y articulaciones, aunque la sección posterior ya presenta pose/contactos.
- Conclusión sobre ausencia de vuelo trasero: precisar que corresponde al ensayo nominal; la precarga 2,0 tiene evidencia posterior distinta.
- Incorporar campañas del 3 de septiembre y avance/incidencia física del 4.
- Hay encabezados y próximas acciones históricos en continuidad/seguimiento: consultar las entradas posteriores antes de presentar un pendiente como vigente.

Estas observaciones se reportan en la diapositiva 4. No se modificó el documento
final durante la preparación de esta exposición.

## Guion por diapositiva

### Diapositiva 1

Tiempo: 1:10. Explicar que el aporte comprobado es una plataforma de generación, registro y evaluación. La hipótesis de mejora mediante RL todavía no está demostrada. La postura física observada no equivale a una marcha validada.

### Diapositiva 2

Tiempo: 2:00. Recorrer cada objetivo: actividad, resultado, evidencia y faltante. OE3 es el más avanzado por implementación y ensayos en simulación. OE5 es el menor: la comparación exploratoria no cumple el diseño final ni incluye hardware. Rúbrica propuesta para esta exposición, no aprobada por los directores.

### Diapositiva 3

Tiempo: 2:00. Avance por ciclo indica desplazamiento neto. La coincidencia de contactos es simultánea respecto al plan y no un porcentaje de estabilidad. Las campañas MuJoCo cambian trayectoria y ganancias: no aíslan una sola causa. 5×20 es el diseño; el ejecutor registró 21 ciclos y el análisis comparable usa 2–20. Nueve pruebas prueban reacción lógica, no corte eléctrico. El resultado negativo PPO impide afirmar mejora.

### Diapositiva 4

Tiempo: 1:10. No hay capítulos declarados definitivamente cerrados. La estructura, métodos y resultados disponibles ya están redactados. El capítulo de conclusiones aún dice que falta entrenar políticas, aunque resultados documenta el entrenamiento: hay que reconciliarlo. El resumen inicial de paso también limita MuJoCo a articulaciones aunque el propio capítulo ya describe pose y contactos. Las campañas del 3 de septiembre y la sobrecarga del 4 deben incorporarse con trazabilidad.

### Diapositiva 5

Tiempo: 1:10. Las semanas son una ruta condicionada, no una promesa de marcha. La prioridad es identificar la causa de sobrecarga, verificar alimentación y seguridad y medir antes de transferir. La siguiente campaña RL requiere una política revisada y criterios acordados. Una conclusión negativa rigurosa es válida como resultado, pero no permite dar por cumplida la integración física prevista.

### Diapositiva 6

Tiempo: 1:00. Presentar este compromiso como propuesta del grupo a ratificar. Criterio verificable: informe con condiciones, instrumentos, mediciones, incidencias y dictamen de continuar o mantener bloqueo; tesis compilada con los nuevos resultados y las conclusiones corregidas. Si una prueba con carga no puede ejecutarse con seguridad, registrar la causa y el requisito faltante, sin inventar mediciones. No prometer una caminata para la próxima revisión.

## Fotografías incorporadas

Las fotografías 1 y 5 aparecen en la diapositiva 1; las 2, 3 y 4 en la diapositiva 3. Se conservan completas y sin retoque. Describen ensamble y electrónica; la fecha de captura no está confirmada. Originales, descripciones y hashes en `Github/evidencias/2026-09-07/README.md`. Se mantiene la presentación en seis diapositivas y la rúbrica de avance sin cambios.

La diapositiva 3 incorpora además una captura nativa de Gazebo del 7 de septiembre, obtenida para ilustrar el entorno del proyecto. No corresponde a las campañas históricas cuyos resultados se citan. Las cinco fotos se mantienen en la presentación.

## Versión simplificada

Se simplificaron las seis diapositivas y sus notas del orador. `GUION_SENCILLO.md` contiene la explicación oral. Las cifras exactas y la rúbrica de esta guía se conservan como respaldo: 23,955 mm/ciclo se presenta como aproximadamente 2,4 cm y 9,87 mm/ciclo como 9,9 mm. No se modificaron los resultados, porcentajes ni criterios de cumplimiento.

## Ampliación autorizada a siete diapositivas

Se insertó una diapositiva de objetivos en la posición 3, después del resumen de avance. Expone los cinco objetivos resumidos, estado parcial, porcentaje y faltantes. Ninguno se declara cumplido al 100 %. Resultados pasa a la diapositiva 4; documento, ruta y compromiso a 5, 6 y 7. El guion vigente con la numeración correcta está en `GUION_SENCILLO.md`; la sección de guion anterior se conserva como antecedente.
