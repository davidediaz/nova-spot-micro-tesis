# Entrenamiento PPO con el robot real (16 de octubre a noviembre de 2026)

Es la carpeta principal del trabajo con el robot físico. Contiene el entorno de simulación con el actuador medido,
las campañas de entrenamiento, la selección de políticas y el programa que las ejecuta en el robot.
`INFORME.md` cuenta la historia de las primeras campañas. `../../CONTINUIDAD.md` registra cada día de trabajo.

## Lo más importante

| Archivo o carpeta | Para qué |
|---|---|
| [`politicas_elegidas_20261105/`](politicas_elegidas_20261105/README.md) | **Las 5 mejores políticas a la fecha**, con evidencia, sumas SHA-256, `verificar.sh`, `requirements.txt`, firmware y cómo reproducirlas. |
| `ppo_v10_robot/` | Políticas copiadas para el robot. Cada una es una carpeta con `policy.zip` y `metadata.json` (marcha, pesos de la recompensa y modelo de servos). |
| `ver_politica_mujoco.py` | Ver una política en MuJoCo: ventana o video, en el piso o colgada. |
| `ejecutar_politica_robot.py` | Ejecutar una política (o la marcha nominal) en el robot por USB, con los sensores. |

## Programas

| Programa | Qué hace |
|---|---|
| `entrenar_ppo_real.py` | Entorno `NovaRealEnv` (MuJoCo con actuador medido) y entrenamiento PPO. Con `--registrar-perdidas` guarda `terminos.csv`, `progress.csv` y `monitor.monitor.csv`. |
| `evaluar_viabilidad.py` | Viabilidad: % de 20 episodios aleatorizados en que la política no cae, avanza ≥ 90 % de la nominal, se desvía poco e inclina < 15°. |
| `seleccionar_copias.py` | Selección anterior: caminatas largas simuladas con puntuación. |
| `comparar_sim_real.py` | Parecido robot–simulación de una caminata grabada: forma, amplitud y desfase por articulación. |
| `ajustar_ganancia_marcha.py` | Modelo de servos ajustado por marcha a partir de la amplitud medida en el robot (genera `actuadores_<marcha>_articulacion.json`). |
| `graficas_convergencia.py` | Gráficas de recompensa, castigo, épocas y pasos, con el punto de convergencia (±2 %). |
| `graficas_recompensa_perdida.py` | Recompensa por episodio y pérdidas de PPO por actualización. |
| `barrido_nominal.py` | Barrido de amplitudes de la marcha base (así se eligió el galope de 18°/7°). |
| `revisar_sensores.py`, `probar_tibia1.py`, `sostener_*.py` | Revisión de sensores y ajustes en vivo con el robot. |
| `identificar_*.py`, `actualizar_modelo_real.py` | Identificación del actuador con las caminatas del robot. |
| `cola_v*.sh`, `reanudar_*.sh`, `viabilidad_v32.sh` | Colas con las que se lanzó cada campaña: sirven de registro exacto de los argumentos. |

## Datos de configuración

- `actuadores_*.json`: modelos del actuador. `actuadores_ciclo2.json` es el de referencia;
  `*_articulacion.json` son los ajustados por marcha (v32 y v33).
- `calibracion_postura.json`: postura de trabajo, ganancia de cada tibia y de las coxas.
- `sensores_robot.json`: calibración de los sensores del robot.

## Campañas (`ppo_v<N>_<marcha>/semilla_<S>/`)

| Versiones | Fechas | Contenido |
|---|---|---|
| v2–v16, ciclo 1 y 2 | 16–22 oct | Gateo, paso y trote; ciclo de mejora en el robot. |
| v17–v28 | 26–28 oct | Carrera y galope, postura del 27-oct, ganancias de tibia, selección por viabilidad. |
| v29–v31 | 29 oct–3 nov | Registro de pérdidas y convergencia (solo para gráficas). |
| v32 | 5 nov | Reentrenamiento con el modelo de servos ajustado (trote, carrera y galope elegidas). |
| v33 | 5 nov | Desde cero con el modelo ajustado, en el PC 2 (convergencia). |

En el repositorio está de cada semilla la política final, `metadata.json`, `evaluacion.csv` y los registros
(`training_trace.csv`, y desde la v29 `terminos.csv`, `progress.csv` y `monitor.monitor.csv`). Las copias
intermedias (`intermedias/`) se quedan solo en el PC del laboratorio y, en v32 y v33, también en el PC 2.

## Resultados

- `viabilidad_*.txt` y `viabilidad_*.csv`: viabilidad de cada campaña.
- `graficas/`: gráficas de convergencia (`convergencia/` para la v31 y `convergencia_v33/`), recompensa y pérdidas.
