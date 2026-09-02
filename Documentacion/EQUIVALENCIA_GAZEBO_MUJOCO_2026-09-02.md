# Equivalencia dinámica Gazebo–MuJoCo

## Contrato y campaña común

El complemento `nova_mujoco_observations` publica a 100 Hz la pose corporal en
`/world/empty/dynamic_pose/info`, la IMU en `/nova/imu` y los cuatro apoyos en
`/nova/foot_contacts`. Nombres, tipos, marcos y semántica coinciden con los
consumidores usados en Gazebo. Métricas, comparador de contacto, margen y
supervisor son los mismos nodos ROS 2.

Se compararon `cierre_paso_r1_20260901` (Gazebo) y
`equivalencia_paso_mujoco_r2_20260902` (MuJoCo): paso de 32 muestras, 0,18
s/muestra, longitud 16 mm, elevación 8 mm y transferencia 4 mm. La ventana común
es de 11 ciclos completos; el ciclo 1 se conserva como transitorio. No hubo
activaciones verdaderas del supervisor.

| Simulador | Avance/ciclo | Roll máximo | Pitch máximo | Altura | Error RMS | Coincidencia contactos | Margen medio |
|---|---:|---:|---:|---:|---:|---:|---:|
| Gazebo | 0,022025 m | 1,281788° | 2,483606° | 0,224125 m | 0,008412 rad | 36,183 % | 0,017957 m |
| MuJoCo | 0,001157 m | 0,624950° | 1,738599° | 0,220887 m | 0,014768 rad | 0,000 % | 0,074766 m |

MuJoCo mostró los cuatro pies apoyados casi permanentemente mientras el plan
esperaba una pata en oscilación. Por ello aún no reproduce el patrón de despegue,
aunque sí mantiene postura, cadencia, continuidad y seguimiento.

## Reproducción y alcance

MuJoCo debe reiniciarse en el keyframe `stand` antes de publicar la orden de
marcha. `Experimentos/comparar_simuladores_equivalentes.py` genera el CSV,
informe y figura. La primera tentativa se conserva con `ENSAYO_INVALIDO.md`
porque el reinicio posterior a `stand` borró las referencias y permitió caer.

Se completó la equivalencia del contrato y del procedimiento, no una calibración
de los motores físicos. Hasta contrastar fricción, contacto y actuación con
mediciones, el artefacto se denomina **modelo digital configurable**.
