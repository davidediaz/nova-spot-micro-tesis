# Guía de exposición: cuatro objetivos originales

Versión vigente: `Primera_entrega_avances_objetivos_corregidos.pptx` y PDF.
Siete diapositivas autorizadas por el usuario. El objetivo general está literal
en la apertura y los cuatro específicos completos en la diapositiva 3. Se
conservan las cinco fotos y la captura real de Gazebo.

## Correspondencia vigente

OE1: hardware y software. OE2: modelado cinemático y dinámico. OE3: control
aprendido con estabilidad y continuidad en paso/gateo. OE4: Prueba de Margen de
Estabilidad Estática, Prueba de Seguimiento de Posición Articular y Prueba de
Repetibilidad del Patrón de Marcha.

Texto íntegro: `Documento_TESIS/Chapters/3 Objetivos.tex`, sincronizado con
`tesis_overleaf/Chapters/3 Objetivos.tex`. Matriz de respaldo:
`Documento_TESIS/MATRIZ_OBJETIVO_EVIDENCIA.md`. Estos cuatro objetivos sustituyen
la clasificación anterior. Marcha convencional y comparación con/sin PPO son
métodos de apoyo y no constituyen objetivos independientes adicionales.

## Porcentajes propuestos

Cuatro entregables por objetivo, de 25 % cada uno. Solo se puntúan entregables
cerrados dentro de su alcance indicado. Son estimaciones por productos, no
aprobación docente ni proporción de horas. No se trasladaron automáticamente
los porcentajes anteriores. Igual porcentaje no implica igual trabajo pendiente.

| OE | Acreditado: dos entregables de 25 % | Pendiente: dos entregables de 25 % | Avance |
|---|---|---|---|
| OE1 | Software integrado; respuesta inicial de motores documentada | Calibración/alimentación verificadas; ejecución física integral | 50 % |
| OE2 | Modelo cinemático verificado; modelo dinámico nominal verificado | Contraste de parámetros físicos; validación consolidada para diseño | 50 % |
| OE3 | Estrategia acotada implementada; entrenamiento y evaluación registrados | Estabilidad demostrada en paso/gateo; continuidad y coordinación aprendida validadas integralmente | 50 % |
| OE4 | Evidencia de seguimiento en simulación; evidencia de repetibilidad en simulación | Prueba de margen estático cerrada; evaluación integral de las tres pruebas y conclusiones bajo protocolo común | 50 % |

La evidencia en simulación solo acredita alcance computacional. Una parada ante
margen negativo verifica reacción del supervisor, no estabilidad de la marcha.
Entrenar PPO no demuestra la garantía que plantea OE3. Ningún objetivo está cerrado.

## Evidencia (rutas relativas al proyecto)

- OE1: `Raspberry/`, continuidad del 4 de septiembre y `Experimentos/pruebas_dinamicas_supervisor_20260902`.
- OE2: `Documentacion/MODELO_MATEMATICO_LATEX`, capítulo de modelo y `Documentacion/CONTRASTE_FUENTES_OFICIALES_NOVA_2026-09-07.md`.
- OE3: `Experimentos/DIAGNOSTICO_REFERENCIA_PPO_ESCALA_CERO_20260902.md` y capítulo de resultados.
- OE4: `Documentacion/EQUIVALENCIA_GAZEBO_MUJOCO_2026-09-02.md`, `Experimentos/comparacion_cadencia_corregida_20260814` y monitor de estabilidad.
- MuJoCo: `Documentacion/MUJOCO_CIERRE_2026-09-03.md`.
- Fotos y captura: `Github/evidencias/2026-09-07/README.md`.

El PDF de tesis recompilado tiene 72 páginas. Las cifras no se cambiaron:
23,955 mm/ciclo se presenta como unos 2,4 cm y 9,87 mm/ciclo como 9,9 mm.
La captura actual de Gazebo no corresponde a las campañas históricas citadas.
Actualizar objetivos no genera resultados nuevos ni cierra pruebas físicas.

## Exposición

El guion vigente está en `GUION_SENCILLO.md`. Ensayar para mantener 8–10 minutos.
Explicar por qué cada objetivo es parcial y qué evidencia falta; priorizar
estabilidad del control aprendido y las tres pruebas de OE4. Compromiso
propuesto: informe de revisión eléctrica y borrador de tesis actualizado.
