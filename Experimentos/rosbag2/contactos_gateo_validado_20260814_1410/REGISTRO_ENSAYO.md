# Registro del ensayo validado de contactos

- Fecha: 14 de agosto de 2026, America/Bogota.
- Bolsa: `contactos_gateo_validado_20260814_1410`.
- Ventana entre último `gateo` y primer `stand`: 329,856750034 s.
- Ciclos completos: 76.
- Parámetros congelados: 24 muestras, 0,18 s por muestra, paso 0,018 m y
  elevación 0,014 m.
- Mensajes: 176.657; tamaño: 142,6 MiB.
- Marcadores: tres `gateo` y tres `stand`.
- Activaciones verdaderas del supervisor: cero.

## Resultados de contacto

- Coincidencia simultánea de las cuatro patas: 32,550 %.
- FL: coincidencia 59,671 %, despegue 0,380297 s tarde y aterrizaje
  1,364317 s tarde.
- FR: coincidencia 59,788 %, despegue 0,381066 s tarde y aterrizaje
  1,364194 s tarde.
- RL y RR: no presentaron transiciones medidas de despegue; permanecieron en
  contacto y su coincidencia individual fue 75,121 % y 74,972 %.

El resultado demuestra que la marcha visualmente estable no ejecuta el patrón
de contacto discreto supuesto: las patas delanteras permanecen en vuelo más
tiempo del previsto y las traseras deslizan sin despegar. No se activaron
paradas automáticas.

## Resultados de movimiento

El ciclo observado medio fue 4,320002 s, el avance medio 0,022970 m/ciclo, la
velocidad 0,005317 m/s, el roll máximo medio 2,232345 grados y el pitch máximo
medio 4,396561 grados. Se completaron 76 ciclos y 1,745713 m acumulados según
las ventanas por ciclo.

## Archivos de análisis

- `../../analisis/contactos_gateo_validado_20260814_1410`.
- `../../analisis_movimiento/contactos_gateo_validado_20260814_1410`.

## SHA-256

- `gaits.yaml`: `f63802b62e4eae267bfa0aab7dedc35107e1622592318e0449a12192b42853ce`
- `contact_monitor.py`: `e32fd0072eb978df094720f9d9aa3dbd5a92b6c501e8b8a4ea6293a8f1ecaaeb`
- `contact_comparator.py`: `05acd15031a20b1f5430f149423e41eabd32b7dfb3f76aed17ec9e6c538ec26a`
- `analizar_contactos_rosbag.py`: `d60912cdc3345d2fb09c38e7b5a20dcca84e617a95f32612146ef8609dc4899c`
- base SQLite: `dbf05b65eea54002c954c37e494c211bb171c7077114d5a1978d4bfe60c5c959`

Las tres tentativas anteriores se conservan y están marcadas inválidas porque
permitieron detectar saturación, omisión de fases y pérdida de marcadores.
