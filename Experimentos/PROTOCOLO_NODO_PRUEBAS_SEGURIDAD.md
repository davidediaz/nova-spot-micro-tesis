# Nodo aislado de pruebas del supervisor

Se añadió `safety_test_node`, que publica estímulos exclusivamente en tópicos
de prueba y registra las respuestas en JSON. Los escenarios cubren margen,
pérdida de contacto, datos vencidos, altura baja y alta, roll, pitch, límite
articular y discontinuidad. El escenario `timeout` no publica telemetría.

Ejemplo de margen (en terminales separadas):

```bash
ros2 run nova_gait_controller safety_supervisor --ros-args \
  -p enable_stability_stop:=true -p stability_topic:=/nova/stability_test \
  -p startup_grace_period:=0.0
ros2 run nova_gait_controller safety_test_node --scenario margin \
  --output /tmp/prueba_margen.json
```

Para contacto se cambian los parámetros a
`enable_contact_stop:=true` y `contact_diagnostics_topic:=/nova/contact_diagnostics_test`.
Para vencimiento se usa `enable_data_timeout_stop:=true` y el escenario
`timeout`. El nodo termina a los cuatro segundos y conserva todos los eventos
recibidos; no modifica los tópicos nominales.

La campaña completa se ejecuta con:

```bash
colcon build --packages-select nova_sm3_description nova_gait_controller
Experimentos/ejecutar_pruebas_dinamicas_supervisor.sh \
  Experimentos/pruebas_dinamicas_supervisor_YYYYMMDD
```

El validador exige en cada escenario `triggered=true`, el motivo esperado y la
orden `stand`. GitHub Actions repite la campaña después de compilar y ejecutar
las pruebas unitarias.
