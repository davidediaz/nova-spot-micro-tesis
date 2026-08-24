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
| 13 | RL correctivo acotado | No iniciar todavía | Marcha nominal física validada y protocolo congelado |
| 14 | Entrenamiento PPO y validación separada | Pendiente | Cinco semillas, política seleccionada y saturaciones probadas |
| 15 | Comparación nominal frente a nominal+RL | Pendiente | 400 ciclos programados y fallos contabilizados |
| 16 | Análisis estadístico y estabilidad | Pendiente | Dataset, IC, margen, métricas y comparación emparejada |
| 17 | Redacción y revisión de tesis | En curso | Resultados, limitaciones, trazabilidad y PDF final |
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
                     validación nominal física → RL correctivo
                                      ↓
                         comparación final → tesis y sustentación
```

## Estado de la próxima semana

1. Ajustar la curva completa de descenso del gateo.
2. Completar la ficha de aprobación del protocolo con el profesor.
3. Identificar la correspondencia física entre canales y articulaciones.
4. Calibrar cada MG996R dentro de límites conservadores y registrar resultados.
5. Verificar la fuente bajo carga e implementar OE con pull-up y parada física
   antes de ejecutar posturas o marchas.
