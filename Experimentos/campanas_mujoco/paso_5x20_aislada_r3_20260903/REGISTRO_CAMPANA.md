# Campaña MuJoCo aislada 5x20 — marcha paso

Fecha: 3 de septiembre de 2026, America/Bogota.

## Configuración y validez

- Marcha: `paso`.
- Ensayos independientes: 5.
- Ciclos programados por ensayo: 20.
- Muestras por ciclo: 32.
- Duración nominal por muestra: 0,18 s.
- Factor de ejecución física MuJoCo: 4,0.
- `ROS_DOMAIN_ID`: 111.
- Una instancia y un grupo de procesos nuevos por ensayo.
- El ciclo 1 se conserva como transitorio; el resumen usa los ciclos 2--20.
- Se capturaron 21 ciclos por bolsa debido al margen temporal; el ciclo 21 no
  entra en las medias comparables.

Cada repetición almacenó nueve marcadores (tres `stand`, tres `paso` y tres
`stand`), 672 referencias y 21 ciclos completos. No hubo activaciones del
supervisor ni avisos `Moved backwards in time`. Al finalizar no quedaron
procesos ROS 2 o MuJoCo de la campaña.

| Ensayo | Mensajes | Duración bolsa (s) | Ciclos | Referencias |
|---|---:|---:|---:|---:|
| paso_r1 | 356.660 | 128,719751 | 21 | 672 |
| paso_r2 | 364.261 | 130,870953 | 21 | 672 |
| paso_r3 | 355.395 | 128,305262 | 21 | 672 |
| paso_r4 | 367.443 | 133,762021 | 21 | 672 |
| paso_r5 | 355.679 | 128,651131 | 21 | 672 |

## Resultado entre ensayos

| Magnitud | Media | Desviación estándar muestral | CV (%) |
|---|---:|---:|---:|
| Avance (m/ciclo) | 0,002701937 | 0,000000555 | 0,020555 |
| Roll máximo (grados) | 0,646314 | 0,000019 | 0,002895 |
| Pitch máximo (grados) | 1,787264 | 0,000061 | 0,003397 |
| Error RMS articular (rad) | 0,010531 | 0,000000 | 0,000000 |
| Coincidencia simultánea de contactos (%) | 0,000 | — | — |

La repetibilidad numérica es alta en esta simulación determinista. El avance
es muy inferior al de Gazebo y los cuatro pies permanecen apoyados según el
monitor, por lo que el 0 % de coincidencia confirma la limitación dinámica ya
observada: esta campaña no demuestra equivalencia física entre simuladores.

## Integridad de las bolsas

- `paso_r1_0.db3`: `eae862cb215691dfd64d3e9fab2e4486dc56447288d169776cade846faede5a1`
- `paso_r2_0.db3`: `26ea5c74112b6b512d59a06a56f8ba01173be36f5c32726bc9232bcc9142edd9`
- `paso_r3_0.db3`: `10ba62a74e623c2605f8a4ed16f1bff434e7c02a682875ede056cbbf9d28cb49`
- `paso_r4_0.db3`: `2f0281de705ad9fbfdb506f3344e7c7a5fcc4a82c505fd331f8dee00b025ddd5`
- `paso_r5_0.db3`: `20ddbd72a799b8b8cd6df4a0d86791cc3abf5c581aec98a4d909b2491e7776d8`

Las bases SQLite3 y los logs pesados se conservan localmente. Los informes,
CSV, metadatos y este registro constituyen la evidencia ligera publicable.
