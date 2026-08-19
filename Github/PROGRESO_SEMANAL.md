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

Rediseñar la curva temporal completa de descenso por eje, validar continuidad y
subfases en pruebas cartesianas y después verificarla exploratoriamente en
Gazebo, sin cambiar longitud de paso, altura máxima ni cadencia.

## Semana del 18 al 24 de agosto de 2026

### Realizado hasta ahora

- Se probó un ajuste de altura de aterrizaje por eje (0,20 delante / 0,80
  detrás), pero la mejora fue insuficiente y se descartó.
- Se restauraron los parámetros nominales anteriores para no contaminar la
  evidencia histórica.
- Se preparó una Raspberry Pi con Ubuntu 22.04.5 Desktop ARM64; falta validar
  el primer arranque, red, SSH y expansión del sistema de archivos.
- Se ampliaron y cerraron documentalmente el modelo matemático y sus ejemplos.

### Pendiente

- Ajustar y validar la nueva curva de descenso del gateo.
- Grabar y repetir una bolsa formal de contactos con la nueva versión.
- Completar la validación de la Raspberry Pi.
- Mantener bloqueados la energización del robot y el entrenamiento PPO hasta
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
