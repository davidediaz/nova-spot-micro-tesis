# Ensayo no válido

La bolsa confirma que el monitor concurrente redujo el caudal, pero el proceso
que deserializaba los contactos crudos siguió impidiendo que el diagnóstico
consumiera todas las fases. Además, los publicadores efímeros llegaron al
controlador pero rosbag2 no almacenó `/nova/gait_command`.

Este hallazgo motivó separar el agregador de sensores y el comparador de fase en
dos procesos ROS 2 independientes. La bolsa se conserva como trazabilidad y no
se usa para resultados cuantitativos.
