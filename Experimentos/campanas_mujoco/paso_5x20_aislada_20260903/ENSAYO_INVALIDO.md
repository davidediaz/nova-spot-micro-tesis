# Campaña inválida

El primer ensayo registró 366.435 mensajes y seis órdenes `stand`, pero perdió
las tres publicaciones `paso`. Solo contiene seis referencias articulares y
cero fases, por lo que la campaña se detuvo automáticamente y no entra en
resultados.

La causa fue que el publicador efímero esperaba por defecto un solo suscriptor
y podía enlazarse únicamente con rosbag. Se corrigió para esperar de forma
explícita dos suscriptores, usar QoS volátil y permanecer vivo después del
último marcador.
