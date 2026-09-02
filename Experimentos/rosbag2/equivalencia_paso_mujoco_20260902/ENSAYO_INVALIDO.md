# Ensayo inválido

La bolsa conserva los tópicos equivalentes y 12 ciclos con cadencia correcta,
pero no se usa para comparar locomoción. Se ordenó `stand` antes de llamar
`reset_world`; el reinicio borró la referencia de los actuadores y el robot
cayó antes de `paso`. Durante la ventana registró aproximadamente 0,037 m de
altura y 180 grados de roll. La repetición debe invertir el orden: reiniciar,
publicar `stand`, verificar pose sostenida y solo entonces grabar.
