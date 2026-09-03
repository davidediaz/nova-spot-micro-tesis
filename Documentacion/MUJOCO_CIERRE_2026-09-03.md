# Cierre técnico MuJoCo — 2026-09-03

## Campañas ejecutadas

| Campaña | Configuración | Resultado agregado |
|---|---|---|
| Paso nominal 5×20 | `step_fore_aft_shift=0`, `step_height=0.008`, kp/kv 40/4 | 2.70 mm/ciclo; coincidencia de contacto 0 % |
| Paso ajustado 5×20 | transferencia 15 mm, altura 12 mm, kp/kv 80/8, fricción 0.9 | **9.87 mm/ciclo**, contacto **36.58 %**, roll 1.51°, pitch 3.17°, RMS 0.00595 rad |
| Gateo nominal 5×20 | configuración nominal de gateo | 6.30 mm/ciclo; contacto 67.46 %; roll 1.54°, pitch 3.61° |

La campaña ajustada confirma una mejora clara frente al paso nominal, pero todavía no alcanza los aproximadamente 22 mm/ciclo observados en Gazebo. Por tanto, no se debe declarar equivalencia dinámica.

## Barridos de calibración virtual

- Transferencia longitudinal: 4–15 mm aumentó el avance hasta 4.12 mm/ciclo, sin resolver por sí sola el contacto.
- Altura de paso: 10–20 mm elevó el contacto de 18.1 % a 35.8 %, pero degradó roll/pitch; se seleccionó 12 mm como compromiso.
- Fricción del suelo (0.45–1.20): efecto pequeño; no es la causa principal.
- Ganancias: kp/kv 80/8 dio el mejor compromiso (38.0 % de contacto en el barrido y postura aceptable); 120/12 aumentó el avance, pero empeoró la postura.

## Perturbaciones

Se inyectaron empujes reproducibles de 1, 2 y 3 N mediante `/nova/mujoco/external_wrench` y se registraron en rosbag. No hubo activaciones del supervisor y los indicadores fueron casi idénticos; esto debe considerarse una prueba de trazabilidad del inyector, no una validación de robustez. La integración de ruido y retardos aún está pendiente.

## Perfiles físicos provisionales

Los perfiles con límites de esfuerzo derivados de datos provisionales de servos no lograron sostener la marcha (avance negativo, pitch 35–41°, contacto 0 %). No se deben usar para ajustar el controlador: falta medir masa, inercia, fricción y par real del robot.

## Estado frente al plan

Completado: diagnóstico de contactos, ajuste virtual de trayectoria/ganancias, campaña MuJoCo paso 5×20, campaña gateo 5×20 y prueba inicial de empujes. Pendiente: comparación Gazebo–MuJoCo con configuración idéntica, perturbaciones de ruido/retardo, calibración con mediciones físicas e incorporación final a las tablas/gráficas de la tesis.
