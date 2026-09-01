# Ensayo inválido: cierre sin marcador `stand`

El controlador ejecutó la trayectoria modificada y su registro mostró tres
órdenes `gateo` y la transición a `stand`. Sin embargo, la bolsa no conservó
una orden `stand/stop` posterior en `/nova/gait_command`, por lo que los
analizadores no pueden delimitar una ventana completa. No se incorporan
métricas. El cierre debe repetirse confirmando el suscriptor del grabador antes
de publicar la orden final.
