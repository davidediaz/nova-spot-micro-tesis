# Exploración Gazebo de curvas de descenso del gateo

Fecha: 27 de agosto de 2026, America/Bogota.

## Objetivo y configuración congelada

Se comparó el control nominal con tres candidatos de la criba cartesiana sin
modificar 24 muestras, paso de 0,018 m, elevación de 0,014 m, cadencia de
0,18 s, transferencia lateral de 0,004 m ni transferencia longitudinal de
0,008 m. El supervisor de contactos permaneció informativo.

Cada fila procede de una bolsa independiente con marcadores redundantes
`gateo` y `stand`, salvo el nominal, que conserva un marcador de cada tipo. El
análisis estricto exigió ambos marcadores. No hubo activaciones del supervisor.

| Relación delantera/trasera | Ciclos completos | Coincidencia simultánea | Despegue FL/FR (s) | Despegue RL/RR (s) | Aterrizaje FL/FR (s) | Aterrizaje RL/RR (s) |
|---|---:|---:|---:|---:|---:|---:|
| nominal 0,7071/0,7071 | 13 | 20,949 % | 0,136826 / 0,137179 | 0,139378 / 0,141574 | 0,497227 / 0,512263 | -0,323550 / -0,324463 |
| 0,20/0,75 | 10 | **23,855 %** | 0,139431 / 0,135283 | 0,142308 / 0,143420 | **0,436068 / 0,460010** | -0,326231 / -0,321033 |
| 0,20/0,80 | 10 | 23,721 % | 0,137465 / 0,136060 | 0,141181 / 0,141263 | 0,445507 / 0,459791 | -0,324589 / -0,325523 |
| 0,50/0,75 | 11 | 21,728 % | 0,133251 / 0,132274 | 0,137653 / 0,137636 | 0,474507 / 0,498197 | -0,325862 / -0,327101 |

Los retardos positivos son transiciones posteriores a lo previsto; los
negativos, transiciones anteriores. Los valores son descriptivos y no deben
interpretarse como réplicas estadísticas independientes.

## Decisión exploratoria

`0,20/0,75` es el candidato provisional: obtuvo la mayor coincidencia
simultánea y los menores retardos delanteros, sin degradación material de los
despegues. Su ventaja sobre `0,20/0,80` es de solo 0,134 puntos porcentuales y
no justifica todavía congelar una nueva línea base.

El cambio corrige parcialmente el aterrizaje delantero, pero no desplaza el
aterrizaje trasero hacia su instante previsto. La siguiente iteración debe
mantener 0,20 delante y estudiar el descenso trasero con un parámetro que actúe
antes del contacto físico, o revisar la definición temporal de `touchdown`.
Después debe repetirse una comparación desde estados iniciales equivalentes y,
solo si la mejora se sostiene, congelar parámetros y grabar una línea base.

## Evidencia

- Bolsas: `Experimentos/rosbag2/curva_descenso_*_20260827`.
- Análisis por condición: subdirectorios `nominal`, `f020_r075`, `f020_r080` y
  `f050_r075` de este directorio.
- SHA-256 SQLite nominal: `2d614328d8fb94199332e73fd42a29f5ba3281f77de464c7b65ddaf9000f3005`.
- SHA-256 SQLite 0,20/0,75: `1dc7f655235b03b116cb1b7e52bce0b498d0f69bf87630d91865200e92dd6a69`.
- SHA-256 SQLite 0,20/0,80: `04eba395407e4fe8f6d091a65871bdfc36788220ffaf5a28b9e171c1195adc70`.
- SHA-256 SQLite 0,50/0,75: `4ba258491d6e6ab6a9bc0a03bc27ba2bbc4c21ff324d070ee02cffd0ad4752f6`.

Dos tentativas 0,20/0,75 en `/tmp` perdieron el marcador `stand` y se
excluyeron. Permitieron identificar que una sola publicación efímera no era
suficientemente robusta; los ensayos posteriores publicaron cinco marcadores.
