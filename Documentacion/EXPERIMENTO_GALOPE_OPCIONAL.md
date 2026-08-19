# Galope como experimento opcional de simulación

Fecha de decisión: 14 de agosto de 2026.

## Decisión de alcance

El galope se conserva como demostración exploratoria de cinco estados, pero se
excluye formalmente de:

- la marcha nominal de la tesis;
- las líneas base y la comparación nominal frente a RL;
- los criterios principales de éxito;
- la transferencia al robot físico;
- las afirmaciones de estabilidad o contacto validadas.

No tiene un plan formal de contactos: `/nova/gait_phase` publica
`contact_plan_available=false`. Tampoco se ha validado dinámica centroidal,
impactos, estabilidad ni seguridad para esta marcha.

## Protección operativa

El parámetro `enable_experimental_gallop` vale `false` por defecto. En ese
estado, los comandos `galope` y `gallop` son rechazados y el modo actual se
conserva.

Solo para una sesión controlada en Gazebo o MuJoCo puede habilitarse:

```bash
ros2 param set /gait_controller enable_experimental_gallop true
ros2 topic pub --once /nova/gait_command std_msgs/msg/String "{data: galope}"
```

Al reiniciar el lanzamiento normal vuelve a quedar deshabilitado. No se debe
activar este parámetro en Raspberry Pi ni durante pruebas con servos energizados.

## Estado

Este punto de alcance queda cerrado. Una posible investigación futura podrá
crear un protocolo dinámico independiente, pero no es requisito para completar
la tesis actual.
