# Estado de campaña nominal–PPO

Se habilitó Gazebo con sockets DDS y se verificó que la marcha nominal produce
referencias cada 0,18 s. La primera corrida nominal y las corridas PPO 01 y 02
contienen tres ciclos analizables. Otras corridas se invalidaron porque el
grabador no recibió la ventana completa de referencias; no se incluyen en
promedios ni se presentan como resultados.

| Condición | Corridas válidas | Corridas inválidas | Causa de exclusión |
|---|---:|---:|---|
| Nominal | 1 | 1 | descubrimiento DDS de la orden final |
| PPO | 2 | 2 | retransmisión/descubrimiento incompleto |

El procedimiento de cinco segundos de espera DDS queda fijado para la próxima
iteración. La política sí está conectada al canal nominal, pero la campaña de
cinco pares no se considera concluida hasta disponer de cinco bolsas válidas
por condición. Las bolsas y análisis válidos se conservan en esta carpeta.
