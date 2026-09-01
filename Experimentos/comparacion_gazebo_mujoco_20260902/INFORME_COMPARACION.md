# Comparación Gazebo–MuJoCo

- Ciclos comparados: 12.
- Duración media Gazebo: 5.760011 s.
- Duración media MuJoCo: 5.760003 s.
- Diferencia relativa de duración: -0.0001 %.

## Sensores equivalentes

MuJoCo incorpora en `mujoco/nova_sm3.xml` un acelerómetro y cuatro sensores táctiles, equivalentes conceptualmente a la IMU `/nova/imu` y a los cuatro tópicos `/nova/contacts/*` de Gazebo.
La bolsa MuJoCo histórica usada en esta comparación fue grabada antes de exponer esos sensores en ROS 2; por eso contiene `/joint_states` y `/tf`, pero no tópicos de IMU/contacto. La comparación cuantitativa de contactos e IMU queda marcada como siguiente adquisición, no se infiere a partir de datos ausentes.

La figura compara únicamente variables con registro común y no afirma equivalencia física entre motores.