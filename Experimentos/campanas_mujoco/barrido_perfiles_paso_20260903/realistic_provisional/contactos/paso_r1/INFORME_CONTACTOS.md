# Análisis de contactos medidos durante marcha paso

- Bolsa: `Experimentos/campanas_mujoco/barrido_perfiles_paso_20260903/realistic_provisional/rosbag2/paso_r1`.
- Ventana paso--stand: 31.838302 s.
- Ciclos completos según `/nova/gait_phase`: 5.
- Índices de ciclo completos: [0, 1, 2, 3, 4].
- Estados comprimidos analizados: 78.
- Coincidencia simultánea filtrada de las cuatro patas: 0.000 %.

## Resultado por pata

| Pata | Coincidencia | Retardo despegue medio | Retardo aterrizaje medio |
|---|---:|---:|---:|
| fl | 66.228 % | sin pares | 1.674460 s |
| fr | 70.804 % | sin pares | 1.675950 s |
| rl | 22.585 % | sin pares | sin pares |
| rr | 27.110 % | sin pares | sin pares |

## Comparación crudo frente a filtrado

- Coincidencia simultánea cruda: 0.000 %.
- Coincidencia simultánea filtrada: 0.000 %.

| Pata | Coincidencia cruda | Coincidencia filtrada |
|---|---:|---:|
| fl | 65.860 % | 66.228 % |
| fr | 70.377 % | 70.804 % |
| rl | 22.585 % | 22.585 % |
| rr | 27.110 % | 27.110 % |

| Pata | Transición | Retardo crudo medio | Retardo filtrado medio |
|---|---|---:|---:|
| fl | liftoff | 0.265797 s | sin pares |
| fl | landing | 0.504153 s | 1.674460 s |
| fr | liftoff | sin pares | sin pares |
| fr | landing | 1.664354 s | 1.675950 s |
| rl | liftoff | sin pares | sin pares |
| rl | landing | sin pares | sin pares |
| rr | liftoff | sin pares | sin pares |
| rr | landing | sin pares | sin pares |

Persistencia cruda exigida para declarar vuelo filtrado: 0.120 s.

| Pata | Episodios acotados | Duración media | Duración máxima | Episodios que superan el umbral |
|---|---:|---:|---:|---:|
| fl | 9 | 0.219968 s | 0.394185 s | 5 |
| fr | 7 | 0.296393 s | 0.392654 s | 6 |
| rl | 0 | sin episodios | sin episodios | 0 |
| rr | 0 | sin episodios | sin episodios | 0 |

Un retardo positivo indica que la transición medida ocurrió después de la prevista; uno negativo indica que ocurrió antes. Los pares se buscan dentro de ±1,8 s. Los porcentajes están ponderados por tiempo, no por número de mensajes.

El análisis es descriptivo y no activa decisiones del supervisor.
