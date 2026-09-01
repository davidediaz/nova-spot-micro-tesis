# Índice de evidencias visuales

Actualización: 1 de septiembre de 2026.

| Figura del PDF | Archivo | Datos de origen | Qué evidencia | Limitación explícita |
|---|---|---|---|---|
| Arquitectura funcional | `Figures` mediante TikZ en `Chapters/9 Desarrollo.tex` | Nodos y tópicos implementados | Flujo entre mando, controlador, simuladores, sensores, análisis, supervisor y registro | Es arquitectura lógica; no demuestra integración eléctrica completa |
| Series del gateo | `Figures/Resultados/gateo_series_temporales.png` | `linea_base_cadencia_corregida_20260814_1049` | Avance y comportamiento periódico de posición, altura, roll y pitch | Un ensayo en Gazebo; no representa hardware |
| Reproducibilidad del gateo | `Figures/Resultados/gateo_reproducibilidad.png` | Dos bolsas de cadencia corregida | Similitud ciclo a ciclo y transitorio inicial | Dos ejecuciones no demuestran equivalencia estadística formal |
| Series de marcha paso | `Figures/Resultados/paso_series_temporales.png` | `paso_linea_base_20260814` | Avance y respuesta periódica de la marcha paso en Gazebo | No contiene mediciones físicas |
| Reproducibilidad de marcha paso | `Figures/Resultados/paso_reproducibilidad.png` | Línea base y repetición de paso | Comparación de dos ensayos independientes | Se limita a la configuración simulada ensayada |
| Seguimiento en MuJoCo | `Figures/Resultados/paso_mujoco_seguimiento.png` | `metricas_mujoco_por_ciclo.csv` | Error RMS/máximo articular y error de cadencia en 12 ciclos | El adaptador no publicó pose o estabilidad corporal equivalente |
| Persistencia del contacto | `Figures/Resultados/contacto_persistencia_cruda.png` | `episodios_sin_contacto_crudo.csv` | Las pérdidas RL/RR permanecen debajo de 0,12 s | Contacto de Gazebo; no sustituye un sensor físico calibrado |

Las dos últimas gráficas se regeneran mediante
`generar_figuras_resultados.py`. Las otras cuatro son salidas directas de los
analizadores reproducibles conservados en `Experimentos/`.
