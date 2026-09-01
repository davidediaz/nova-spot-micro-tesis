# Estado de los cinco puntos de la ruta

| Punto | Estado | Evidencia |
|---|---|---|
| Comparar contactos nominal/0,75/0,80 | Completado | `comparacion_contactos_liberacion_20260901.md` |
| Seleccionar configuración de gateo | Decisión provisional | 0,80 queda como candidato de trabajo; no se demostró vuelo trasero sostenido |
| Paradas restantes del supervisor | Parcial | Referencia inválida demostrada; margen/contacto/datos requieren nodo aislado y reloj controlado |
| Preparar y entrenar PPO | Preparación completada | `PROTOCOLO_PPO_RESIDUAL.md`; no existe política entrenada |
| Caracterización física | Pendiente externo | Requiere mediciones reales de masas, geometría, servos, calibración y pruebas sobre suelo |

La matriz evita presentar como resultados las actividades que todavía no tienen
una medición reproducible. La siguiente acción de software es construir el nodo
de prueba aislado del supervisor; la siguiente acción experimental del gateo es
modificar la trayectoria para buscar despegue trasero real. La caracterización
física solo podrá cerrarse con acceso al robot.
