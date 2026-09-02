# Pruebas automáticas de seguridad y continuidad

Fecha de implementación: 2 de septiembre de 2026.

## Alcance

La suite impide aceptar automáticamente cambios que rompan estas propiedades:

- las 12 articulaciones existen y sus límites coinciden entre el URDF, MuJoCo
  y el supervisor (`coxa`: -0,60 a 0,60 rad; `femur`: -1,20 a 1,20 rad;
  `tibia`: -2,20 a 0,10 rad);
- toda referencia es finita, tiene dimensión correcta y permanece dentro de
  sus límites;
- los tiempos de una trayectoria son finitos, positivos y estrictamente
  crecientes, y ningún salto dentro de una trayectoria o entre dos mensajes
  consecutivos supera 0,35 rad;
- una pata esperada pero ausente se clasifica como `perdida_contacto`, distinta
  de un contacto adicional inesperado;
- altura, `roll` y `pitch` activan sus motivos de seguridad al cruzar 0,16 m,
  0,32 m o 0,35 rad, respectivamente;
- las marchas nominales continúan siendo alcanzables, periódicas y suaves, y
  el supervisor conserva sus validaciones de telemetría vencida, margen de
  soporte y valores no finitos.

El umbral de salto de 0,35 rad es una barrera de integridad de referencias, no
un límite físico identificado del MG996R. Los umbrales de pose son los mismos
del supervisor provisional y deberán revisarse tras caracterizar el robot.

## Ejecución local

Desde la raíz del workspace y con ROS 2 Humble cargado:

```bash
colcon build --packages-select nova_sm3_description nova_gait_controller
source install/setup.bash
python3 -m pytest -q src/nova_gait_controller/test
```

## Integración continua

`.github/workflows/pruebas-automaticas.yml` ejecuta compilación y pruebas en un
contenedor ROS 2 Humble para cada `push` y cada `pull_request`. Un resultado
fallido hace fallar el trabajo de GitHub Actions; para impedir formalmente una
integración a `main`, el repositorio deberá marcar este trabajo como requerido
en las reglas de protección de rama de GitHub.

Estas son pruebas deterministas de software y modelos. No sustituyen ensayos
dinámicos de caída o pérdida de contacto en Gazebo/MuJoCo ni pruebas físicas;
esas campañas continúan pendientes y deberán guardar sus bolsas y criterios de
aceptación por separado.
