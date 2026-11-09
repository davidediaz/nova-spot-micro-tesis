# Cámaras y caminatas del robot físico

Aquí se graban las caminatas del robot suspendido. Cada caminata guarda los sensores, las órdenes y hasta 5 cámaras
sincronizadas en el mismo reloj, y después se analiza.

## Programas principales

| Programa | Qué hace |
|---|---|
| `grabar_caminata.py` | Lanza la caminata (`ejecutar_politica_robot.py`) y graba todas las cámaras. Uso: `grabar_caminata.py --nombre <n> -- --duracion-s 60 --politica <policy.zip>`. |
| `vista_vivo.py`, `vista_camaras.py` | Ver las cámaras en vivo: durante la caminata, o para encuadrar. |
| `diagnostico_caminata.py` | Seguimiento de cada articulación (r, error, deriva), coxas, temporización y calidad de cada cámara. |
| `protocolo_repetibilidad.py`, `analizar_repetibilidad.py`, `ciclo_mejora.py` | Repeticiones alternadas nominal/PPO y el ciclo de mejora en el robot. |
| `analizar_video_patas.py`, `analizar_colores_patas.py`, `identificar_pata_camara.py` | Análisis de video: movimiento por pata y piezas identificadas por color. |
| `video_evidencia.py` | Video de evidencia: 4 cámaras en mosaico con rótulo. |
| `comprimir_videos.py`, `catalogo_caminatas.py` | Compresión de los videos y catálogo de todas las caminatas (`grabaciones/catalogo.csv`). |

## `grabaciones/<caminata>/`

- `caminata.csv`: cada ~33 ms, la hora, la fase, las 12 órdenes, la marcha nominal, todas las lecturas de sensores
  y la corrección de la política.
- `caminata.config.json`: marcha, política, calibración y argumentos exactos.
- `diagnostico.json`, `comparacion_sim_real.json` y otros: resultados de los análisis.
- `remota/` y `extra_*/`: hora del primer fotograma y desfase de cada cámara. Los videos (`*.mkv`) y las copias
  de `caminata.csv`, `caminata.config.json` y `caminata.inicio.txt` que el análisis de video deja en cada cámara no
  se suben, porque son idénticas a las de la carpeta de la caminata. Para reanalizar un video, se copian desde ahí.

Prefijos de las carpetas: `rep_<sesión>_…` son repeticiones de comparación; `robot28_…` y `robot05_…`, las pruebas del
28-oct y del 5-nov; `evidencia_…`, las caminatas de los videos de evidencia del 5-nov. Los archivos
`repetibilidad_<sesión>.csv` y `.json` resumen cada sesión.

## `informes/`

Informes de sesiones concretas: el ciclo de mejora del 21-oct (`INFORME_CICLO3_2026-10-21.md`, con su historial
de grabaciones) y el historial de análisis de ese día.
