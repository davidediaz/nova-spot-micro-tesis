# Plan inicial del documento final

## Diferencia frente al anteproyecto

El anteproyecto formuló lo que se esperaba realizar. El documento final deberá
explicar qué se realizó realmente, mediante qué procedimiento, qué datos se
obtuvieron, cómo se analizaron y qué puede concluirse sin exceder la evidencia.
El cambio no consiste únicamente en reemplazar tiempos verbales.

## Estructura propuesta

1. Preliminares: portada, firmas, resumen, abstract, palabras clave e índices.
2. Introducción y planteamiento del problema revisados según el alcance real.
3. Objetivos y alcance definitivo.
4. Marco teórico y estado del arte estrictamente utilizados en el desarrollo.
5. Caracterización de la plataforma y requisitos.
6. Modelado cinemático/dinámico y modelos URDF, Gazebo y MuJoCo.
7. Arquitectura de control, electrónica, instrumentación y seguridad.
8. Metodología ejecutada y protocolo experimental.
9. Implementación de la marcha nominal y de la capa correctiva RL.
10. Resultados: simulación, hardware y comparación nominal frente a nominal+RL.
11. Análisis y discusión.
12. Conclusiones por objetivo, limitaciones y trabajo futuro.
13. Referencias y apéndices técnicos.

La estructura podrá ajustarse a la plantilla institucional, pero deberá
mantener separados método, resultado, discusión y conclusión.

## Reglas de incorporación

- Conservar una sola fuente de verdad para cada tabla o figura.
- Identificar fecha, versión, configuración, unidad experimental y exclusiones.
- No mezclar bolsas generadas con versiones distintas de trayectoria o
  temporizador.
- Conservar y explicar ensayos inválidos relevantes para el control de calidad.
- Reportar el ciclo inicial como transitorio cuando corresponda.
- Tratar cada ensayo, no cada ciclo, como réplica independiente en la
  comparación estadística final.
- Denominar el modelo actual «modelo nominal computable» mientras no exista
  identificación física suficiente; no llamarlo gemelo digital.
- No afirmar seguimiento articular físico sin medición real de posición.
- Expresar resultados negativos: por ejemplo, el avance del robot no demuestra
  por sí solo que el patrón de contactos previsto se haya ejecutado.

## Material ya apto para migración controlada

- Modelo matemático y documentación técnica, sujetos a revisión editorial.
- Líneas base reproducibles de gateo y marcha paso en simulación.
- Diseño y validación de fase, contacto, IMU y margen nominal.
- Resultado del 1 de septiembre de 2026 que distinguió interrupciones crudas de
  vuelo trasero sostenido.
- Protocolo experimental y matriz de ensayos/semillas, con decisiones aún
  pendientes claramente señaladas.

## Material que todavía no puede redactarse como resultado final

- Caracterización definitiva del robot físico.
- Seguridad eléctrica y calibración de los doce servos.
- Validación física de postura, paso y gateo.
- Entrenamiento y selección final de políticas PPO.
- Comparación experimental nominal frente a nominal más RL.
- Conclusiones finales de cumplimiento de los objetivos cuarto y quinto.
