# Análisis de contactos medidos durante gateo

- Bolsa: `Experimentos/rosbag2/velocidad_gateo_150_20260901`.
- Ventana gateo--stand: 83.199698 s.
- Ciclos completos según `/nova/gait_phase`: 28.
- Índices de ciclo completos: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27].
- Estados comprimidos analizados: 688.
- Coincidencia simultánea filtrada de las cuatro patas: 6.747 %.

## Resultado por pata

| Pata | Coincidencia | Retardo despegue medio | Retardo aterrizaje medio |
|---|---:|---:|---:|
| fl | 50.312 % | 0.264577 s | 1.160816 s |
| fr | 50.867 % | 0.270061 s | 1.161813 s |
| rl | 89.470 % | 0.230781 s | -0.072632 s |
| rr | 89.314 % | 0.230995 s | -0.073626 s |

## Comparación crudo frente a filtrado

- Coincidencia simultánea cruda: 15.200 %.
- Coincidencia simultánea filtrada: 6.747 %.

| Pata | Coincidencia cruda | Coincidencia filtrada |
|---|---:|---:|
| fl | 55.672 % | 50.312 % |
| fr | 56.293 % | 50.867 % |
| rl | 92.552 % | 89.470 % |
| rr | 92.444 % | 89.314 % |

| Pata | Transición | Retardo crudo medio | Retardo filtrado medio |
|---|---|---:|---:|
| fl | liftoff | 0.141561 s | 0.264577 s |
| fl | landing | 1.071898 s | 1.160816 s |
| fr | liftoff | 0.146928 s | 0.270061 s |
| fr | landing | 1.128135 s | 1.161813 s |
| rl | liftoff | 0.111031 s | 0.230781 s |
| rl | landing | -0.106304 s | -0.072632 s |
| rr | liftoff | 0.108257 s | 0.230995 s |
| rr | landing | -0.106569 s | -0.073626 s |

Persistencia cruda exigida para declarar vuelo filtrado: 0.120 s.

| Pata | Episodios acotados | Duración media | Duración máxima | Episodios que superan el umbral |
|---|---:|---:|---:|---:|
| fl | 30 | 1.302123 s | 1.512904 s | 29 |
| fr | 28 | 1.340911 s | 1.351196 s | 28 |
| rl | 28 | 0.143557 s | 0.158831 s | 26 |
| rr | 30 | 0.141916 s | 0.157614 s | 29 |

Un retardo positivo indica que la transición medida ocurrió después de la prevista; uno negativo indica que ocurrió antes. Los pares se buscan dentro de ±1,8 s. Los porcentajes están ponderados por tiempo, no por número de mensajes.

El análisis es descriptivo y no activa decisiones del supervisor.
