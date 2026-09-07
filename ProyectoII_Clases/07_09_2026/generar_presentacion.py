from pathlib import Path
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor

OUT=Path(__file__).resolve().parent
prs=Presentation(); prs.slide_width=Inches(13.333); prs.slide_height=Inches(7.5)
BG='101D30'; FG='F3F6FA'; MUTED='B8C6D8'; ACC='4ED3BA'; CARD='1C3049'; WARN='FFD187'
def box(s,x,y,w,h,color):
    sh=s.shapes.add_shape(1, Inches(x), Inches(y), Inches(w), Inches(h)); sh.fill.solid(); sh.fill.fore_color.rgb=RGBColor.from_string(color); sh.line.fill.background(); return sh

def txt(s,x,y,w,h,text,size=21,color=FG,bold=False):
    sh=s.shapes.add_textbox(Inches(x), Inches(y), Inches(w), Inches(h)); tf=sh.text_frame; tf.word_wrap=True
    for i,line in enumerate(text.split('\n')):
        p=tf.paragraphs[0] if i==0 else tf.add_paragraph(); p.text=line; p.font.name='Aptos'; p.font.size=Pt(size); p.font.bold=bold; p.font.color.rgb=RGBColor.from_string(color); p.space_after=Pt(5)
    return sh

def slide(n,title,sub):
    s=prs.slides.add_slide(prs.slide_layouts[6]); s.background.fill.solid(); s.background.fill.fore_color.rgb=RGBColor.from_string(BG)
    box(s,.45,.45,.10,.75,ACC); txt(s,.75,.35,12,.6,title,26,bold=True); txt(s,.78,1.05,11.9,.65,sub,16,MUTED)
    txt(s,.75,7.08,11,.24,'NOVA SPOT MICRO  ·  Proyecto de Grado II  ·  07 septiembre 2026',10,MUTED); txt(s,12,7.04,.7,.3,f'{n}/6',12,ACC)
    return s

def card(s,x,y,w,h,title,body):
    box(s,x,y,w,h,CARD); txt(s,x+.2,y+.15,w-.4,.55,title,19,ACC,True); txt(s,x+.2,y+.85,w-.4,h-.95,body,17)

s=slide(1,'Control de locomoción: avances y límites','Diseño de un sistema de control para la locomoción y estabilización de un robot cuadrúpedo basado en aprendizaje por refuerzo')
txt(s,.8,1.75,11.8,.9,'Propósito: combinar una marcha convencional con correcciones RL acotadas y evaluar estabilidad y repetibilidad.',25)
card(s,.8,2.95,3.8,2.8,'Implementado','Modelo y cinemática propios\nROS 2 + Gazebo + MuJoCo\nPostura, paso y gateo')
card(s,4.78,2.95,3.8,2.8,'Evaluado','Campañas reproducibles\nSupervisor: 9 escenarios\nPPO entrenado y rechazado')
card(s,8.76,2.95,3.8,2.8,'Fase actual','Integración física inicial\n12 servos respondieron\nPruebas pausadas por sobrecarga')
txt(s,.8,6.05,11.8,.65,'David Esteban Díaz Castro · David Felipe Díaz Suesca',18,MUTED)
s.notes_slide.notes_text_frame.text='Tiempo: 1:10. Explicar que el aporte comprobado es una plataforma de generación, registro y evaluación. La hipótesis de mejora mediante RL todavía no está demostrada. La postura física observada no equivale a una marcha validada.'

s=slide(2,'Cumplimiento de los cinco objetivos','Estimación propuesta: 4 hitos por objetivo, 25 % por hito cerrado; los hitos parciales no suman. Ver rúbrica en el guion.')
rows=[['Objetivo / actividad','Resultado y evidencia','%','Pendiente'],
['OE1 · Modelar y caracterizar','FK/IK y dinámica nominal verificadas.\nModelo matemático, URDF/MJCF y pruebas.','50 %','Medir plataforma e identificar\nparámetros físicos.'],
['OE2 · Integrar y supervisar','ROS 2 y 9 fallos provocados respondieron.\nJSON del supervisor; registro de hardware.','50 %','Potencia, OE, rearme,\ncalibración y prueba física.'],
['OE3 · Implementar locomoción','Postura, paso y gateo; campañas repetibles.\nBolsas, CSV e informes Gazebo/MuJoCo.','75 %','Validar marcha física;\ncerrar diferencias de contacto.'],
['OE4 · Entrenar e integrar RL','Cinco semillas PPO; ninguna aceptada.\nModelos y diagnóstico de escala residual.','50 %','Rediseñar, validar y\ntransferir progresivamente.'],
['OE5 · Comparar nominal vs. RL','Protocolo y comparación exploratoria.\nDiagnóstico PPO y referencia corregida.','25 %','Campaña final emparejada\ny comparación en hardware.']]
table=s.shapes.add_table(6,4, Inches(.8), Inches(1.95), Inches(11.75), Inches(4.55)).table
for c,w in zip(table.columns,[3.05,4.65,.95,3.10]): c.width=Inches(w)
for r,row in enumerate(rows):
    table.rows[r].height=Inches(.48 if r==0 else .8)
    for j,v in enumerate(row):
        cell=table.cell(r,j); cell.text=v; cell.fill.solid(); cell.fill.fore_color.rgb=RGBColor.from_string('28475F' if r==0 else CARD)
        for p in cell.text_frame.paragraphs: p.font.name='Aptos'; p.font.size=Pt(14 if r else 15); p.font.bold=(r==0 or j==2); p.font.color.rgb=RGBColor.from_string(ACC if j==2 else FG)
txt(s,.8,6.55,11.6,.35,'Porcentajes de hitos documentados: no son una calificación ni una medición de éxito experimental.',13,WARN)
s.notes_slide.notes_text_frame.text='Tiempo: 2:00. Recorrer cada objetivo: actividad, resultado, evidencia y faltante. OE3 es el más avanzado por implementación y ensayos en simulación. OE5 es el menor: la comparación exploratoria no cumple el diseño final ni incluye hardware. Rúbrica propuesta para esta exposición, no aprobada por los directores.'

s=slide(3,'Resultados que sí podemos demostrar','Las cifras corresponden a campañas distintas; no se mezclan configuraciones ni se afirma equivalencia dinámica.')
card(s,.8,1.85,5.72,1.95,'Gazebo · gateo nominal','5 ensayos · 23,955 mm/ciclo\n5,545 mm/s · 191 ciclos de régimen')
card(s,6.7,1.85,5.82,1.95,'Supervisor · integración ROS 2','9/9 escenarios provocados: activación,\nmotivo esperado y orden stand')
card(s,.8,4.0,5.72,2.3,'MuJoCo · paso 5×20','Nominal: 2,70 mm/ciclo; contacto 0 %\nAjustado: 9,87 mm/ciclo; 36,58 %\nMejora virtual; no valida el robot físico.')
card(s,6.7,4.0,5.82,2.3,'PPO · resultado negativo útil','5 semillas; ninguna escala positiva aceptada.\nEscala cero: −0,258 % frente al nominal.\nSe bloqueó la transferencia al prototipo.')
txt(s,.8,6.48,11.8,.42,'Fuentes: tesis, cap. Resultados; MUJOCO_CIERRE_2026-09-03; diagnóstico PPO de escala cero (02/09).',12,MUTED)
s.notes_slide.notes_text_frame.text='Tiempo: 2:00. Avance por ciclo indica desplazamiento neto. La coincidencia de contactos es simultánea respecto al plan y no un porcentaje de estabilidad. Las campañas MuJoCo cambian trayectoria y ganancias: no aíslan una sola causa. 5×20 es el diseño; el ejecutor registró 21 ciclos y el análisis comparable usa 2–20. Nueve pruebas prueban reacción lógica, no corte eléctrico. El resultado negativo PPO impide afirmar mejora.'

s=slide(4,'Documento final: avance y actualización','PDF preliminar comprobado: 73 páginas. Documento_TESIS es la base final; tesis_overleaf conserva el anteproyecto.')
card(s,.8,1.9,3.8,4.55,'Ya incorporado','Modelo matemático\nMetodología ejecutada\nArquitectura y desarrollo\nResultados Gazebo y PPO\nProtocolos y anexos\nEstado: versión preliminar')
card(s,4.78,1.9,3.8,4.55,'En construcción','Caracterización física\nCalibración y seguridad\nComparación final\nDiscusión integradora\nConclusiones definitivas\nCierre de los 5 objetivos')
card(s,8.76,1.9,3.8,4.55,'Actualizar ahora','Campañas MuJoCo del 03/09\nHardware y sobrecarga del 04/09\nConclusiones: PPO ya se entrenó\nAlcance del modelo nominal\nCronograma y presupuesto')
s.notes_slide.notes_text_frame.text='Tiempo: 1:10. No hay capítulos declarados definitivamente cerrados. La estructura, métodos y resultados disponibles ya están redactados. El capítulo de conclusiones aún dice que falta entrenar políticas, aunque resultados documenta el entrenamiento: hay que reconciliarlo. El resumen inicial de paso también limita MuJoCo a articulaciones aunque el propio capítulo ya describe pose y contactos. Las campañas del 3 de septiembre y la sobrecarga del 4 deben incorporarse con trazabilidad.'

s=slide(5,'Ruta de cierre: validación física primero','Secuencia propuesta para las próximas semanas; cada etapa depende de superar la anterior.')
card(s,.8,1.9,3.8,3.75,'1 · Diagnóstico y medición','PCA9685 sin carga; revisar CH1\nMedir tensión y consumo\nVerificar parada física/OE\nCompletar masas y geometría\nRiesgo: sobrecarga sin resolver')
card(s,4.78,1.9,3.8,3.75,'2 · Integración progresiva','Calibrar un servo y una pata\nRegistrar ángulo y consumo\nValidar postura y marcha nominal\nIdentificar el modelo físico\nRiesgo: holgura y límites reales')
card(s,8.76,1.9,3.8,3.75,'3 · Evaluación y cierre','Rediseñar y validar PPO\nAcordar métricas y umbrales\nComparar 5 pares × 20 ciclos\nPor marcha; sim. y hardware\nRiesgo: no demostrar mejora RL')
txt(s,.8,5.95,11.75,.85,'Prioridad documental inmediata: integrar evidencias nuevas y corregir contradicciones.\nSi PPO no mejora, reportar el resultado y acordar el alcance final con los directores.',17,WARN)
s.notes_slide.notes_text_frame.text='Tiempo: 1:10. Las semanas son una ruta condicionada, no una promesa de marcha. La prioridad es identificar la causa de sobrecarga, verificar alimentación y seguridad y medir antes de transferir. La siguiente campaña RL requiere una política revisada y criterios acordados. Una conclusión negativa rigurosa es válida como resultado, pero no permite dar por cumplida la integración física prevista.'

s=slide(6,'Compromiso para la siguiente revisión','Propuesta de compromiso del grupo · producto verificable, con datos y límites explícitos')
card(s,.8,1.85,11.72,1.75,'Entregar un informe de diagnóstico físico y la tesis sincronizada','Registro de PCA9685/CH1, tensiones y corriente por canal o grupo ensayado;\nestado de la parada física, evidencia del diagnóstico y capítulos actualizados.')
txt(s,.95,3.92,11.35,1.05,'“Nuestro proyecto todavía no puede darse por terminado porque falta validar la locomoción y la seguridad físicas y cerrar la comparación nominal frente a RL.”',25)
txt(s,.95,5.25,11.35,1.12,'“La evidencia que permitirá demostrar su finalización será una campaña trazable en simulación y hardware, con métricas acordadas y conclusiones respaldadas por resultados.”',25,ACC)
s.notes_slide.notes_text_frame.text='Tiempo: 1:00. Presentar este compromiso como propuesta del grupo a ratificar. Criterio verificable: informe con condiciones, instrumentos, mediciones, incidencias y dictamen de continuar o mantener bloqueo; tesis compilada con los nuevos resultados y las conclusiones corregidas. Si una prueba con carga no puede ejecutarse con seguridad, registrar la causa y el requisito faltante, sin inventar mediciones. No prometer una caminata para la próxima revisión.'
prs.save(OUT/'Primera_entrega_avances.pptx')
print(OUT/'Primera_entrega_avances.pptx')
