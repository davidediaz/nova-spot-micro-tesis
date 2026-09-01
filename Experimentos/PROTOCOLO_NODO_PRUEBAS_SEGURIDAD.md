# Nodo aislado de pruebas del supervisor

Se añadió `safety_test_node`, que publica diagnósticos exclusivamente en
`/nova/stability_test` o `/nova/contact_diagnostics_test` y registra las
respuestas en JSON. El escenario `timeout` no publica telemetría.

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
