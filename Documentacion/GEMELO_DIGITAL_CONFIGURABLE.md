# Modelo digital configurable de Nova Spot Micro

## Alcance

Esta implementación aumenta el realismo y hace comparables Gazebo y MuJoCo,
pero continúa siendo un modelo provisional: no se denomina gemelo digital
identificado hasta sustituir las escalas por masas, inercias, holguras,
fricción, retardos y curvas eléctricas medidos en el ejemplar físico.

La fuente única es
`src/nova_sm3_description/config/digital_twin_profiles.yaml`. Cada perfil fija
masa, inercia, amortiguamiento, fricción articular y de suelo, holgura, retardos,
tensión y límite de corriente. `Experimentos/generar_perfiles_gemelo.py` produce
un URDF para Gazebo, un MJCF para MuJoCo, un mundo SDF y un manifiesto con hashes.
`Experimentos/auditar_modelos_gemelo.py` comprueba masa total, fricciones,
amortiguamiento y límite de esfuerzo antes de admitir una comparación.

## Actuador MG996R

El límite efectivo combina la envolvente lineal par--velocidad y tensión con un
límite de corriente por servo. El perfil `realistic_provisional` usa 5,5 V y
1,0 A, que reducen el par estático computable a 0,727925 N m y la velocidad sin
carga a 6,399541 rad/s. Son cotas de catálogo, no resultados físicos.

`actuator_model_node` aplica la misma zona muerta de holgura, retardo de comando
y límite de cambio en ambas rutas. El inyector existente aplica el retardo de
sensores en tópicos separados. Los controladores deben publicar primero en
`/nova/ideal_trajectory`; la salida filtrada alimenta el controlador articular.

Ejemplo para el perfil realista provisional:

```bash
ros2 launch nova_gait_controller actuator_model.launch.py \
  backlash_rad:=0.017453293 command_delay_ms:=20 \
  max_speed_rad_s:=6.399540591
ros2 launch nova_gait_controller demo.launch.py \
  trajectory_topic:=/nova/ideal_trajectory
```

Gazebo acepta los archivos generados mediante `profile_gazebo.launch.py` y
MuJoCo mediante el argumento `mujoco_model` de `mujoco_sim.launch.py`.

## Comparación pendiente

Para cada perfil deben ejecutarse cinco ensayos de 20 ciclos en cada simulador,
excluyendo solo el ciclo 1 del resumen. Se congelarán marcha, referencias,
perfil y semilla. Se compararán período, error RMS/máximo articular, avance,
roll, pitch, contactos, margen, saturaciones y corriente estimada. La pose
corporal y los contactos deben exponerse en MuJoCo antes de afirmar equivalencia
completa; mientras falten, la comparación se limita a cadencia y articulaciones.

No se mezclarán resultados de perfiles distintos ni se transferirá el perfil
realista al hardware sin caracterización y seguridad eléctrica.

La prueba de integración cargó el perfil realista provisional en Gazebo con
las doce articulaciones y los dos controladores activos. El mismo MJCF cargó en
MuJoCo con 12 actuadores y siete sensores. El resumen estructural está en
`Experimentos/modelos_gemelo_generados/INFORME_PERFILES_EMPAREJADOS.md`.
