# Ruta completa de trabajo

Esta es la ruta operativa completa, no solo el siguiente experimento. Las fases
se ejecutan en orden porque las fases de hardware y aprendizaje dependen de la
seguridad y de una marcha nominal estable.

| Fase | Trabajo | Estado | Condición para cerrar |
|---:|---|---|---|
| 1 | Problema, objetivos, alcance, estado del arte, metodología y presupuesto | Completada / revisión | Objetivos y alcance aprobados por el profesor |
| 2 | Modelo nominal: geometría, FK, IK, Jacobiano, dinámica, actuadores, contacto, estabilidad y control discreto | Completada | Fuentes, pruebas y PDF reproducible |
| 3 | ROS 2 y simulación: URDF/MJCF, controlador, métricas, supervisor, fase y contactos | Completada | Pruebas automatizadas y simulaciones ejecutables |
| 4 | Gateo: corregir descenso, sincronizar contactos y congelar línea base | En curso | Nueva bolsa de contactos reproducida |
| 5 | Marcha paso: validación en Gazebo y MuJoCo | Completada | Dos ensayos Gazebo y validación articular MuJoCo |
| 6 | Protocolo experimental y criterios con el profesor | En curso | Métrica primaria, frecuencia, umbrales y éxito aprobados |
| 7 | Caracterización física sin energizar | Pendiente | Fotos, componentes, geometría, masas, holguras y diferencias |
| 8 | Seguridad eléctrica | En curso | Fuente, fusible, cableado, tierra, OE y parada física probados |
| 9 | Calibración de los 12 MG996R | Iniciada | Centros, sentidos, límites, corriente y temperatura registrados por articulación |
| 10 | Raspberry Pi, ROS 2, red, Mega, I2C y PCA9685 | En curso | Ubuntu 22.04, SSH, DDS, I2C y movimiento limitado verificados |
| 11 | Interfaz articulación–PWM y vigilancia de comunicaciones | Pendiente | Arranque deshabilitado y pérdida de datos lleva a estado seguro |
| 12 | Transferencia progresiva al robot | En curso controlado | Individual y multicanal → pata → suspendido → suelo; sin marchas antes de cerrar seguridad |
| 13 | Control por aprendizaje (PPO) | Ejecutada sin mejora aceptada | Revisar alcance con los directores y demostrar estabilidad/continuidad si se mantiene |
| 14 | Tres pruebas de evaluación | En curso | Completar margen de estabilidad estática, seguimiento articular y repetibilidad |
| 15 | Caracterización física y seguridad | Pendiente crítico | Medir dimensiones, masas y límites; resolver sobrecarga, calibración y parada segura |
| 16 | Validación progresiva en robot | Pendiente | Transferir cuando OE1 y la seguridad eléctrica estén cerrados |
| 17 | Redacción y revisión de tesis | En curso | Integrar matriz, resultados, limitaciones, trazabilidad y PDF final |
| 18 | Entrega y sustentación | Pendiente | Fuentes, anexos, hashes, presentación y demostración |

## Dependencias críticas

```text
Corrección de gateo
        ↓
Protocolo aprobado → caracterización física → seguridad eléctrica
                                      ↓
                               calibración MG996R
                                      ↓
          Raspberry/Mega/PCA9685 → calibración y parada segura → interfaz PWM
                                      ↓
                         transferencia progresiva al robot
                                      ↓
                     validación nominal física → revisión del alcance PPO
                                      ↓
                         tres pruebas de evaluación → tesis y sustentación
```

## Estado de la próxima semana

1. Medir dimensiones, masas, límites y correspondencia física entre canales y articulaciones.
2. Diagnosticar la sobrecarga, calibrar los MG996R y verificar la fuente bajo carga.
3. Implementar OE con pull-up y parada física antes de ejecutar posturas o marchas.
4. Completar las pruebas de margen estático, seguimiento articular y repetibilidad.
5. Revisar con los directores el alcance final de PPO si no mejora la línea base.
