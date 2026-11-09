# Taller 2 — Corte 1 — 31 de agosto de 2026

Contenido:

- `Taller2_OPG_Documento.pdf`: guía original entregada por la asignatura.
- `main.tex`: fuente editable de la matriz resuelta.
- `INFORME_TALLER_2_31_08_2026.pdf`: producto final compilado.

El informe consolida la transición entre el anteproyecto y el documento final
con corte al 31 de agosto de 2026. Distingue resultados demostrados, avances
parciales y tareas aún no demostrables. No declara terminados el ensamble
físico, la caracterización, el aprendizaje por refuerzo ni la comparación
experimental final.

Compilación:

```bash
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
cp main.pdf INFORME_TALLER_2_31_08_2026.pdf
```
