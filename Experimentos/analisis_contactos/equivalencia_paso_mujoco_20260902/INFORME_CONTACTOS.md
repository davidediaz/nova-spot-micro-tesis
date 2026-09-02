# Análisis de contactos medidos durante marcha paso

- Bolsa: `Experimentos/rosbag2/equivalencia_paso_mujoco_20260902`.
- Ventana paso--stand: 73.034778 s.
- Ciclos completos según `/nova/gait_phase`: 12.
- Índices de ciclo completos: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11].
- Estados comprimidos analizados: 51.
- Coincidencia simultánea filtrada de las cuatro patas: 0.000 %.

## Resultado por pata

| Pata | Coincidencia | Retardo despegue medio | Retardo aterrizaje medio |
|---|---:|---:|---:|
| fl | 25.638 % | sin pares | sin pares |
| fr | 25.069 % | sin pares | sin pares |
| rl | 23.675 % | sin pares | sin pares |
| rr | 25.618 % | sin pares | sin pares |

## Comparación crudo frente a filtrado

- Coincidencia simultánea cruda: 0.000 %.
- Coincidencia simultánea filtrada: 0.000 %.

| Pata | Coincidencia cruda | Coincidencia filtrada |
|---|---:|---:|
| fl | 25.638 % | 25.638 % |
| fr | 25.069 % | 25.069 % |
| rl | 23.675 % | 23.675 % |
| rr | 25.618 % | 25.618 % |

| Pata | Transición | Retardo crudo medio | Retardo filtrado medio |
|---|---|---:|---:|
| fl | liftoff | sin pares | sin pares |
| fl | landing | sin pares | sin pares |
| fr | liftoff | sin pares | sin pares |
| fr | landing | sin pares | sin pares |
| rl | liftoff | sin pares | sin pares |
| rl | landing | sin pares | sin pares |
| rr | liftoff | sin pares | sin pares |
| rr | landing | sin pares | sin pares |

Persistencia cruda exigida para declarar vuelo filtrado: 0.120 s.

| Pata | Episodios acotados | Duración media | Duración máxima | Episodios que superan el umbral |
|---|---:|---:|---:|---:|
| fl | 0 | sin episodios | sin episodios | 0 |
| fr | 0 | sin episodios | sin episodios | 0 |
| rl | 0 | sin episodios | sin episodios | 0 |
| rr | 0 | sin episodios | sin episodios | 0 |

Un retardo positivo indica que la transición medida ocurrió después de la prevista; uno negativo indica que ocurrió antes. Los pares se buscan dentro de ±1,8 s. Los porcentajes están ponderados por tiempo, no por número de mensajes.

El análisis es descriptivo y no activa decisiones del supervisor.
