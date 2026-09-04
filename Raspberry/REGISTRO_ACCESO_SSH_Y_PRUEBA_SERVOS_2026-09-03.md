# Registro de acceso SSH y preparación de prueba de servos — 2026-09-03

## Acceso remoto

- Raspberry: Pi 4 Model B Rev 1.5.
- Usuario: `pavilion`.
- Hostname configurado: `cuadrupedo-pi`.
- Nombre mDNS: `cuadrupedo-pi.local`.
- Interfaz: `wlan0` sobre la red `F_DIAZ_D_5G`.
- IP observada por DHCP: `10.58.164.198/24`.
- Puerta de enlace: `10.58.164.87`.
- MAC Wi‑Fi: `d8:3a:dd:48:ba:d5`.
- Servicio SSH habilitado y activo.
- Alias local configurado: `ssh cuadrupedo-pi`.
- Clave usada: `~/.ssh/nova_pi_ed25519`.

La conexión se verificó por SSH y confirmó el modelo de Raspberry. La IP debe
reservarse en el router usando la MAC si se desea conservarla; no se configuró
IP estática en la Raspberry.

## Estado de hardware

- Bus `/dev/i2c-1` disponible.
- PCA9685 detectado en `0x40`.
- Dirección `0x70` también visible en el escaneo I²C (sin modificarla).
- Servos conectados a CH0–CH11 y fuente externa energizada por el usuario.

## Seguridad de la prueba

No se ejecutó todavía ningún barrido ni movimiento de servos. La configuración
del proyecto mantiene `hardware_ready: false`, los límites de movimiento sin
medir y los canales en `FULL_OFF`. El script existente
`control_12_servos_thonny.py` no se debe usar para esta validación porque hace
un barrido continuo únicamente en CH6.

La siguiente acción aprobada es revisar un script secuencial que active un solo
canal a la vez, con pulso central de 1500 µs durante un segundo y apagado antes
de pasar al siguiente canal. La prueba debe hacerse con patas suspendidas,
parada física accesible y supervisión de la fuente.

## Resultado inicial de prueba

- CH0: respondió con movimiento durante la prueba individual.
- Pulso, sentido, recorrido y articulación mecánica: aún no registrados.
- No se autoriza todavía la ejecución de `stand`, `gateo` o `paso`.

## Prueba simultánea reducida

- Fecha de ejecución: 4 de septiembre de 2026.
- Canales: CH0–CH11.
- Secuencia: `1500 → 1450 → 1550 → 1500 µs`.
- Resultado: los doce servos respondieron al movimiento.
- Finalización: salidas PWM apagadas automáticamente.

Este resultado confirma respuesta eléctrica y funcional básica de los doce
canales. No sustituye la calibración de sentido, centro y límites mecánicos.

## Repetición con fuente externa encendida

- Fecha: 4 de septiembre de 2026.
- Secuencia simultánea: `1500 → 1450 → 1550 → 1500 µs`.
- Resultado: los 12 servos respondieron correctamente.
- Conclusión: la falta de respuesta anterior en CH4–CH11 se debió a la fuente
  externa apagada, no a una ausencia de señal del PCA9685.
- Estado final: PWM apagado automáticamente.

## Activación neutra con el robot apoyado

- Fecha: 4 de septiembre de 2026.
- Condición: cuadrúpedo apoyado en el piso, cuerpo sujetado y parada física lista.
- Comando: 12 canales a `1500 µs` durante 1 segundo.
- Resultado: conservó su postura; no se observaron desplazamientos bruscos.
- Estado final: salidas PWM apagadas automáticamente.
