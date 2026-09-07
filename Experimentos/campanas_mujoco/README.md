# Campañas MuJoCo — septiembre de 2026

Este directorio conserva los resultados analizables de las campañas ejecutadas
el 2 y 3 de septiembre: informes Markdown, métricas CSV, resúmenes JSON y
metadatos YAML. Las bolsas `rosbag2`, logs e imágenes de diagnóstico permanecen
localmente porque ocupan aproximadamente 5,6 GB y no son adecuadas para el
repositorio Git.

Las campañas cubren barridos de altura, fricción, ganancias, perfiles y
transferencia; validaciones de aislamiento, publicador, grupos y cierre;
perturbaciones de 2, 10 y 30 N; y ensayos nominales, ajustados y aislados de
paso y gateo. Los informes de cada subdirectorio indican configuración, métricas,
limitaciones y criterio de validez.

Para consultar una campaña, comenzar por `resumen_campana.json`,
`resumen_ensayos.csv` e `INFORME_ANALISIS.md` o `INFORME_MUJOCO.md`. La matriz
documental que relaciona estas evidencias con los objetivos está en
[`Documento_TESIS/MATRIZ_OBJETIVO_EVIDENCIA.md`](../../Documento_TESIS/MATRIZ_OBJETIVO_EVIDENCIA.md).

La ausencia de una bolsa local en Git no elimina la evidencia: se conserva en
el equipo de trabajo y cada informe mantiene la configuración y las métricas
necesarias para identificarla.
