# Experimentos

Aquí están todas las campañas, en orden cronológico. Cada subcarpeta guarda sus datos y, casi siempre, un
`INFORME*.md` con el resultado. Los programas `.py` y `.sh` sueltos de esta carpeta son los que generaron las
campañas de simulación de agosto y septiembre.

## 1. Simulación con el modelo nominal (agosto–septiembre de 2026)

| Carpeta | Qué se hizo |
|---|---|
| `validacion_temporizador_20260814`, `comparacion_*_20260814` | Corrección del temporizador de la marcha y reproducibilidad del gateo y del paso en Gazebo. |
| `curvas_descenso_cartesianas_20260824`, `exploracion_curvas_descenso_gazebo_20260827` | Forma de la trayectoria del pie al bajar. |
| `liberacion_trasera_cartesiana_202608*`, `resultados_liberacion_gateo_*`, `resultados_preload_gateo_*` | Despegue de las patas traseras y precarga en el gateo. |
| `resultados_gateo_*`, `resultados_paso_*`, `velocidades_nominales_20260901` | Gateo y paso a distintas velocidades. |
| `sensibilidad_nominal_20260901`, `perturbaciones_nominales_20260902` | Sensibilidad a masas, fricción y amortiguamiento. |
| `prueba_supervisor_*`, `pruebas_dinamicas_supervisor_20260902` | Pruebas provocadas del supervisor de seguridad. |
| `comparacion_gazebo_mujoco_20260902`, `comparacion_simuladores` | Mismo controlador en Gazebo y en MuJoCo. |
| `modelos_gemelo_generados` | Variantes del modelo (perfiles del gemelo digital). |
| `analisis*`, `rosbag2` | Análisis de contactos, movimiento y articulaciones a partir de las grabaciones ROS 2. |

## 2. PPO residual con el modelo nominal (septiembre de 2026)

| Carpeta | Qué se hizo |
|---|---|
| `ppo_residual_2026090*`, `campana_ppo_gazebo_*`, `campana_ppo_escala_*`, `campana_ppo_semillas_20260906` | Primera capa correctiva PPO en Gazebo: barrido de escala y 5 semillas. Resultado negativo: no supera a la marcha nominal. |
| `entrenamiento_ppo_*_20260924`, `reentrenamiento_ppo_*_2026092*` | Reentrenamientos en MuJoCo. |
| `campana_distribuida_step_s23_20260928` | Campaña de 80 semillas del paso. |
| `campana_step_estabilidad_*_202609*` | Variantes de la recompensa de estabilidad. |
| `campanas_mujoco` | Campañas de marcha en MuJoCo, con su README. |

## 3. Modelo del robot real y robot físico (desde el 16 de octubre de 2026)

| Carpeta | Qué se hizo |
|---|---|
| [`entrenamiento_real_20261016/`](entrenamiento_real_20261016/README.md) | Entorno de entrenamiento con el actuador medido en el robot, campañas v2 a v33, selección por viabilidad, ejecución en el robot y gráficas. **Es la carpeta principal del trabajo actual.** |
| [`camaras/`](camaras/README.md) | Grabación sincronizada de 5 cámaras y sensores, análisis de video y datos de cada caminata del robot. |
