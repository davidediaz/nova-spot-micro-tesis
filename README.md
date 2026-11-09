# Nova Spot Micro — locomoción de un robot cuadrúpedo con aprendizaje por refuerzo

Este es el repositorio de la tesis sobre el robot cuadrúpedo **Nova Spot Micro**. Contiene:

- el modelo del robot para los simuladores;
- un controlador de marchas en ROS 2, para Gazebo y MuJoCo;
- políticas PPO residuales: una red neuronal que corrige una marcha base;
- el firmware de la interfaz de E/S, el programa de control del robot físico y los datos de todos los ensayos;
- el documento de tesis.

## Estado al 9 de noviembre de 2026

Hay cinco marchas, cada una con su mejor política elegida. Todas se probaron en el robot físico **suspendido** de una
barra, con 60 s de caminata y 4 o 5 cámaras sincronizadas.

| Marcha | Política | Viabilidad en simulación | Parecido robot–simulación |
|---|---|---|---|
| Gateo | v27, semilla 7013 | 100 % | 90 % |
| Paso | v24, semilla 4109 | 100 % | 85 % |
| Carrera | v32, semilla 9301 | 95 % | 83 % |
| Galope | v32, semilla 9407 | 60 % | 82 % |
| Trote | v32, semilla 9209 | 60 % | 80 % |

Para el detalle, las limitaciones y cómo verificar los resultados, ver
[`Experimentos/entrenamiento_real_20261016/politicas_elegidas_20261105/README.md`](Experimentos/entrenamiento_real_20261016/politicas_elegidas_20261105/README.md).
La versión exacta de esas políticas está fijada con la etiqueta `politicas-elegidas-20261105`.

## Mapa de carpetas

| Carpeta | Qué contiene |
|---|---|
| [`Experimentos/`](Experimentos/README.md) | **Todo lo medido y entrenado.** Simulación (agosto–septiembre), entrenamiento PPO con el modelo del robot real y ensayos en el robot físico (octubre–noviembre). Cada subcarpeta tiene su informe. |
| ↳ [`Experimentos/entrenamiento_real_20261016/`](Experimentos/entrenamiento_real_20261016/README.md) | Programas de entrenamiento, evaluación y ejecución en el robot. Campañas v2 a v33, políticas elegidas (`ppo_v10_robot/`) y gráficas. |
| ↳ [`Experimentos/camaras/`](Experimentos/camaras/README.md) | Grabación sincronizada de cámaras y sensores, análisis de video y datos de cada caminata (`grabaciones/`). |
| [`Documento_TESIS/`](Documento_TESIS/README.md) | Documento de tesis en LaTeX (`Thesis.tex`, `Chapters/`), con sus figuras, tablas generadas y `compilar.sh`. |
| [`Documentacion/`](Documentacion/README.md) | Notas técnicas, protocolos, explicaciones matemáticas, presentaciones y gráficas para exponer. |
| [`src/`](src/README.md) | Paquetes ROS 2: `nova_sm3_description` (modelo URDF y MJCF, mundos, lanzadores de Gazebo y MuJoCo) y `nova_gait_controller` (máquina de marchas, métricas y supervisor). |
| [`Arduino/`](Arduino/README.md) | Firmware de la interfaz de E/S (PCA9685, multiplexores y sensores) y bocetos de prueba. El vigente es `movimiento_suspendido_11_servos/`. |
| [`Raspberry/`](Raspberry/README.md) | Preparación de la Raspberry Pi 4 (controlador previsto), pruebas de hardware y documentación de conexiones. |
| [`gif/`](gif/README.md) | Animaciones cortas: trote PPO en MuJoCo y gateo nominal en Gazebo. |
| [`Curso_y_seguimiento/`](Curso_y_seguimiento/README.md) | Material del curso Proyecto de Grado II, seguimiento con el profesor y página web de progreso. |
| `scripts/` | Utilidades: preparar y verificar la Raspberry Pi y ejemplos del modelo matemático. |
| `CONTINUIDAD.md` | **Bitácora diaria** del proyecto: qué se hizo, con qué datos y qué quedó pendiente. Es el mejor punto de partida para retomar. |

En la raíz quedan solo este README, `CONTINUIDAD.md`, `index.html` (abre la página de progreso) y
`visor_interactivo.html` (visor web del robot). Los informes de sesiones concretas están en
`Documentacion/informes/`.

Cada archivo está una sola vez. Las copias que había, como los datos repetidos dentro de cada cámara, la carpeta
«Caminata final» y el paquete «GRABACION_FINAL», existen solo en el PC del laboratorio; su contenido útil está en
la carpeta que indica la tabla.

## Empezar en otro PC

```bash
git clone https://github.com/davidediaz/nova-spot-micro-tesis.git
cd nova-spot-micro-tesis
python3.10 -m venv .venv-mujoco
.venv-mujoco/bin/pip install -r Experimentos/entrenamiento_real_20261016/politicas_elegidas_20261105/requirements.txt \
    --extra-index-url https://download.pytorch.org/whl/cpu
cd Experimentos/entrenamiento_real_20261016
# Ver una política caminando en MuJoCo (ventana; --video x.mp4 para guardarla; --suspendido para verla colgada)
../../.venv-mujoco/bin/python ver_politica_mujoco.py ppo_v10_robot/ppo_v32_trote_semilla_9209_650k
# Comprobar los archivos y repetir la viabilidad de las 5 políticas
PY=../../.venv-mujoco/bin/python politicas_elegidas_20261105/verificar.sh
```

- **Gazebo:** el controlador ROS 2 (gateo y paso nominales) se compila y lanza como se explica en
  [`src/README.md`](src/README.md). Las políticas PPO se entrenan y evalúan en MuJoCo; todavía no corren en Gazebo.
- **Robot físico:** ver la sección «Cómo reproducirlo» del README de las políticas elegidas.

## Qué no está en el repositorio

- **Videos de las cámaras e imágenes de las cámaras.** Son pesados y en algunos aparecen personas. Están en el PC del
  laboratorio y en un disco externo («Vidios tesis»). Los videos de evidencia del 5-nov se publicarán en YouTube.
- **Copias de un mismo archivo:** los datos repetidos dentro de cada cámara, la carpeta «Caminata final» (copia de
  `Experimentos/camaras/grabaciones`) y el paquete «GRABACION_FINAL» (PDF y gráficas que ya están en
  `Documento_TESIS/` y `Documentacion/`).
- **Copias intermedias de los entrenamientos** (`intermedias/`, cientos de MB). Sí están la política final, la
  configuración y los registros de cada semilla.
- **Entornos y compilaciones locales:** `.venv-mujoco/`, `build/`, `install/`, `log/` y los repositorios de
  referencia (`referencias/`).

## Ramas y etiquetas

| Nombre | Qué es |
|---|---|
| `main` | Versión principal y actualizada. |
| `entrenamiento/ppo-robot-real-20261016` | Rama de trabajo desde octubre; se integra en `main`. |
| `politicas-elegidas-20261105` | Etiqueta fija con las 5 políticas elegidas el 5-nov-2026. |
| `gh-pages` | Página web de seguimiento. |
| `resultados/mujoco-step-80-semillas-20260928` | Resultados de la campaña de 80 semillas de septiembre. |
