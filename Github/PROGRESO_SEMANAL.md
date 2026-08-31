# Progreso semanal

## Semana del 11 al 17 de agosto de 2026

### Realizado

- Se corrigió el temporizador del controlador para mantener la cadencia
  planificada de 0,18 s por referencia.
- Se creó y reprodujo una nueva línea base de gateo: 24 referencias, ciclo de
  4,32 s y diferencias inferiores al 0,2 % entre ensayos.
- Se implementó y validó la marcha `paso` en Gazebo y MuJoCo.
- Se publicaron la fase de marcha y los contactos previstos.
- Se añadieron sensores de contacto para las cuatro patas en Gazebo.
- Se separaron el agregador de contactos y el comparador de diagnósticos.
- Se ejecutó un ensayo cuantitativo de 76 ciclos y se identificó que el gateo
  avanzaba, pero no respetaba todavía el patrón ideal de apoyos.
- Se incorporaron transferencia lateral y longitudinal y después subfases
  explícitas: transferencia, precarga, despegue, vuelo, aterrizaje y contacto.

### Evidencia

- `Experimentos/validacion_temporizador_20260814/`
- `Experimentos/rosbag2/linea_base_cadencia_corregida_20260814_1049/`
- `Experimentos/rosbag2/repeticion_cadencia_corregida_20260814_1100/`
- `Documentacion/MARCHA_PASO_VALIDACION.md`
- `Documentacion/CONTACTOS_MEDIDOS_GAZEBO.md`
- `Experimentos/analisis/contactos_gateo_validado_20260814_1410/INFORME_CONTACTOS.md`

### Problemas identificados

Los despegues de las cuatro patas quedaron aproximadamente entre 0,133 y
0,141 s tarde. Sin embargo, las patas delanteras aterrizan aproximadamente
0,50 s tarde y las traseras 0,33 s antes. Todavía no se congela una nueva línea
base de contactos.

### Siguiente objetivo

Comparar la nueva curva temporal continua de descenso por eje, validar continuidad y
subfases en pruebas cartesianas y después verificarla exploratoriamente en
Gazebo, sin cambiar longitud de paso, altura máxima ni cadencia.

## Semana del 18 al 24 de agosto de 2026

### Realizado hasta ahora

- Se probó un ajuste de altura de aterrizaje por eje (0,20 delante / 0,80
  detrás), pero la mejora fue insuficiente y se descartó.
- Se restauraron los parámetros nominales anteriores para no contaminar la
  evidencia histórica.
- Se confirmó una Raspberry Pi 4 Model B con Ubuntu 22.04.5 Desktop ARM64,
  Wi-Fi `192.168.0.101` y SSH remoto funcionando desde el PC principal.
- Falta demostrar el descubrimiento DDS mediante `talker/listener` y validar
  reloj e I2C; no se conectaron ni energizaron servos.
- El workspace de la Raspberry se actualizó al commit `d1e3525`, compiló los
  paquetes `nova_sm3_description` y `nova_gait_controller`, y los reconoció
  con ROS 2; no se ejecutó hardware.
- Se instaló Arduino IDE 1.8.19 ARM64 y se verificó el Arduino Mega 2560 por
  `/dev/ttyACM0`, con permisos mediante `dialout`.
- El Mega detectó el PCA9685 en `0x40` después de corregir la inversión de SDA
  y SCL. Se probaron servos MG996R de forma progresiva y el sketch actual mueve
  simultáneamente `CH5`--`CH10` entre 1300 y 1700 microsegundos; los demás
  canales permanecen en `FULL_OFF`.
- Se ampliaron y cerraron documentalmente el modelo matemático y sus ejemplos.

### Pendiente

- Ajustar y validar la nueva curva de descenso del gateo.
- Grabar y repetir una bolsa formal de contactos con la nueva versión.
- Integrar de forma controlada el enlace ROS 2 con el Mega/PCA9685 después de
  cerrar la calibración y las protecciones eléctricas.
- Identificar la articulación física de cada canal y calibrar centro, mínimo,
  máximo y sentido de cada MG996R.
- Verificar la fuente bajo carga e implementar parada física por OE con
  resistencia pull-up antes de ejecutar posturas o marchas.
- Mantener bloqueadas las marchas completas y el entrenamiento PPO hasta
  completar seguridad, caracterización y calibración.

## Plantilla para la próxima semana

Copiar esta estructura al final del archivo:

```markdown
## Semana del AAAA-MM-DD al AAAA-MM-DD

### Realizado

-

### Evidencia

-

### Problemas o decisiones

-

### Siguiente objetivo

-
```

## Semana del 25 al 31 de agosto de 2026

### Realizado

- Se compararon cuatro curvas de descenso en Gazebo; 0,20/0,75 quedó como
  candidato provisional, sin congelar una línea base.
- Se comprobó que el contacto trasero reaparece durante el ascenso, por lo que
  el problema no responde principalmente al parámetro de descenso.
- Se implementó una relación independiente de liberación trasera, se cribaron
  siete valores y se ensayó el máximo aceptado, 0,80, durante 15 ciclos.
- Se prepararon fichas cerrables para caracterización física y aprobación del
  protocolo.
- Se consolidó la matriz de transición del anteproyecto al documento final del
  Taller 2 en un informe reproducible de 14 páginas.
- Se sustituyeron dos servos por limitaciones físicas y se reforzaron los
  acoples para reducir holguras; su identificación y validación están pendientes.

### Evidencia

- `Experimentos/exploracion_curvas_descenso_gazebo_20260827/`
- `Experimentos/liberacion_trasera_cartesiana_20260831/`
- `Experimentos/analisis/liberacion_trasera_f020_r075_l080_valida_20260831/`
- `Documentacion/FICHA_CARACTERIZACION_FISICA.md`
- `Documentacion/FICHA_APROBACION_PROTOCOLO.md`
- `ProyectoII_Clases/31_08_2026/INFORME_TALLER_2_31_08_2026.pdf`
- `Raspberry/INTERVENCION_MECANICA_2026-08-31.md`

### Problemas o decisiones

El candidato 0,80 redujo el adelanto de contacto trasero solo unos 0,016 s y
obtuvo 23,644 % de coincidencia, inferior al 23,855 % de 0,20/0,75. Se rechaza.
Valores desde 0,85 exceden el límite articular implementado. Las actividades de
caracterización y aprobación vencieron sin evidencia suficiente y permanecen
abiertas explícitamente.

El ensamble físico sigue incompleto mientras se imprime la tapa izquierda del
fémur. Los dos servos sustituidos requieren calibración desde cero y el refuerzo
de acoples debe verificarse antes de energizar o ejecutar una marcha.

### Siguiente objetivo

Revisar el criterio temporal de contacto y la liberación mecánica de las patas
traseras; completar en presencia del robot la ficha física y llevar al profesor
la ficha de decisiones del protocolo.
