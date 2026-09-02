# Calibración y pruebas de servos MG996R

Calibrar canal por canal, comenzando por los dos servos sustituidos. Usar una
fuente regulada externa; no alimentar V+ desde la Raspberry. Registrar el
identificador del servo, lote y canal PCA9685.

1. Con el servo sin carga y el brazo retirado, aplicar únicamente un pulso
   central corto (1000–2000 µs como rango de prueba, no como límite final).
2. Encontrar el centro mecánico con incrementos ≤5 µs; registrar repetibilidad
   en tres ciclos y el sentido positivo.
3. Con tope mecánico identificado, buscar mínimo y máximo en pasos de 5 µs,
   deteniendo antes del ruido, atasco o aumento de corriente. Nunca forzar el
   tope para ampliar el rango.
4. Medir corriente en reposo, movimiento y carga estática; medir temperatura
   de carcasa al inicio y tras 60 s. Dejar enfriar entre pruebas.
5. Medir tiempo de 30° y 60° en ambos sentidos sin extrapolar el catálogo a par
   continuo. Repetir tres veces.
6. Confirmar que OE corta el PWM y que el servo queda sin torque antes de
   desmontar.

El rango final se escribe en `calibracion_servos_fisica.csv` y solo se copia a
la configuración ROS después de una revisión independiente.
