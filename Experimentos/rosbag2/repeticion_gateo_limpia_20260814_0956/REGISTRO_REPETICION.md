# Registro de repetición del gateo nominal

- Fecha: 14 de agosto de 2026.
- Bolsa: `repeticion_gateo_limpia_20260814_0956`.
- Duración total: 562,091270146 s.
- Mensajes: 267.218.
- Tamaño: 304,3 MiB.
- Ventana válida entre el último marcador redundante `gateo` y el primer
  marcador `stand`: 174,706623946 s.
- Ciclos ejecutados completos: 36.
- Duración observada media: 4,793341 s/ciclo.
- Activaciones del supervisor: 0.

Se conservaron tres marcadores redundantes de inicio y tres de cierre. La
última orden `gateo` reinicia la fase cero y define el comienzo limpio de la
ventana analizada; la primera orden `stand` define el final.

La configuración se mantuvo congelada en 24 muestras, paso de 0,018 m,
elevación de 0,014 m y duración configurada de 0,18 s por muestra.

## Huellas SHA-256

- Base rosbag2: `12a3060547290682cf9cd754818673f5fce0139785d8c4b45fb09bd7c96026ad`
- `gaits.yaml`: `0772d57faab20f8da50176f4e94fc9d885e618211e230c34511c18256a71990a`
- `gait_controller.py`: `b95718f0f42769ceb68e6cc1dd83805da7c29443c2423d0eea8c16f69eb6e17a`
- `kinematics.py`: `def751c5d58082dfe9c656edcd3c91ebbf66c3d48e0a2ec6a439a55a9a0861df`
- analizador: `f2f1c050e44c3f4fc03c55ee03b548f7769cf150379391e16ef2ab8422e3b2c8`

Resultados asociados:

`../../analisis/repeticion_gateo_limpia_20260814_0956`

Comparación con la primera ejecución:

`../../comparacion_reproducibilidad_20260814`
