# Modelo matemático Nova Spot Micro en LaTeX

Esta carpeta contiene la versión LaTeX consolidada y explicada paso a paso del
modelado matemático.
Las ecuaciones fueron reconstruidas como matemáticas nativas y no dependen de
capturas del documento Word.

Además de cinemática, dinámica, contacto y estabilidad, incluye un capítulo
amplio de control discreto: muestreo y aliasing, ZOH, ecuaciones en diferencias,
transformada Z, mapeo de polos, discretización exacta/Euler/Tustin, estabilidad
de Schur/Jury/Lyapunov, error permanente, controlabilidad, observabilidad, PID
digital, anti-windup, realimentación de estados, integral, LQR, observadores,
Kalman, lugar de raíces, respuesta en frecuencia, robustez, retardos,
cuantización, sistemas multirrate, MPC y control híbrido de la marcha.

La edición vigente también incorpora trazabilidad académica en cuatro niveles
(teoría, adaptación Nova, código y evidencia), un diccionario razonado de
variables y un registro por ecuación que explica su procedencia, las variables
que entrega, su adaptación al robot y la decisión de tesis para la que se usa.
Los ejemplos siguen el esquema objetivo, fuente, datos, hipótesis, sustitución,
comprobación e interpretación; por ello separan resultados nominales,
resultados de simulación y mediciones físicas pendientes.

## Archivos

- `main.tex`: fuente completa y editable.
- `main.pdf`: documento compilado.
- `README.md`: instrucciones y alcance.
- `compilar.sh`: compilación reproducible con `latexmk`.
- `../../scripts/generar_ejemplos_modelo.py`: reproduce los valores usados en
  los ejemplos de FK/IK, Jacobiano, dinámica, estabilidad y control discreto.

## Compilar

Desde esta carpeta:

```bash
./compilar.sh
```

Equivalente manual:

```bash
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

Los archivos auxiliares se guardan en `build/`; el PDF final queda en la raíz
de esta carpeta.

Para recalcular los ejemplos desde el código del proyecto:

```bash
cd /home/pavilion/Documentos/Cuadrupedo
python3 scripts/generar_ejemplos_modelo.py
```

El script imprime JSON con datos de entrada, matrices, términos intermedios y
resultados. Los ejemplos del documento indican expresamente cuáles magnitudes
son nominales, cuáles proceden de simulación y cuáles todavía requieren
identificación física.

## Estado de validez

Es un modelo nominal computable y verificado internamente, no un gemelo digital
del ejemplar físico. Continúan pendientes la identificación física, las
gráficas de workspace y singularidad, la validación de `Jdot` y la comparación
cuantitativa con mediciones independientes.
