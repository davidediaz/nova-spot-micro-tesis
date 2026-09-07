from pathlib import Path
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor

OUT=Path(__file__).resolve().parent
PHOTOS=OUT.parents[1]/'Github/evidencias/2026-09-07'
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

def photo(s,n,x,y,w,h,caption):
    # Insertar el original completo, conservando proporciones y sin recorte.
    from PIL import Image
    with Image.open(PHOTOS/f'{n}.jpeg') as im: iw,ih=im.size
    scale=min(w/iw,h/ih); pw,ph=iw*scale,ih*scale
    box(s,x,y,w,h,CARD)
    s.shapes.add_picture(str(PHOTOS/f'{n}.jpeg'), Inches(x+(w-pw)/2), Inches(y+(h-ph)/2), width=Inches(pw), height=Inches(ph))
    txt(s,x,y+h+.06,w,.4,caption,11,MUTED)

s=slide(1,'Nuestro robot: qué hemos logrado','Nova Spot Micro · Control del movimiento y del equilibrio')
txt(s,.8,1.8,5.1,1.0,'Buscamos una marcha estable y probar si el robot mejora aprendiendo de sus resultados.',19)
card(s,.8,3.05,5.1,2.95,'Ahora: pruebas del robot real','El robot camina en simulación.\nLos 12 motores respondieron.\nLas pruebas físicas se pausaron por exceso de corriente.\nFalta resolver la causa.')
photo(s,1,6.15,1.85,2.55,4.5,'1 · Vista general del robot')
photo(s,5,8.9,1.85,3.62,2.72,'5 · Electrónica y conexiones en banco')
txt(s,8.9,5.05,3.62,1.35,'Ya tenemos el prototipo.\nFalta comprobar que camina de forma segura.',17,ACC)
txt(s,.8,6.6,11.8,.3,'David Esteban Díaz Castro · David Felipe Díaz Suesca',15,MUTED)
s.notes_slide.notes_text_frame.text='Tiempo: 1:10. Explicar que el aporte comprobado es una plataforma de generación, registro y evaluación. La hipótesis de mejora mediante RL todavía no está demostrada. La postura física observada no equivale a una marcha validada.'

s=slide(2,'¿Cuánto hemos avanzado?','OE = objetivo específico. Los porcentajes son estimaciones basadas en evidencias.')
rows=[['Objetivo','¿Qué hicimos y cómo se demuestra?','%','Pendiente'],
['OE1 · Conocer y modelar el robot','Creamos el modelo matemático.\nEvidencia: código y pruebas.','50 %','Medir el robot real y\ncomprobar el modelo.'],
['OE2 · Controlarlo con seguridad','El programa detectó 9 fallos de prueba.\nEvidencia: registros de cada respuesta.','50 %','Comprobar alimentación,\nprotecciones y motores.'],
['OE3 · Crear sus movimientos','Probamos postura, paso y gateo.\nEvidencia: datos de simulación.','75 %','Probar la marcha real y\nmejorar los apoyos simulados.'],
['OE4 · Aprender correcciones','Entrenamos el algoritmo cinco veces.\nLas evaluaciones no mostraron la mejora buscada.','50 %','Mejorar el aprendizaje y\nprobarlo antes de usarlo.'],
['OE5 · Comparar los resultados','Hicimos una comparación inicial.\nEvidencia: informes y datos.','25 %','Completar pruebas comparables\nen simulación y robot real.']]
table=s.shapes.add_table(6,4, Inches(.8), Inches(1.95), Inches(11.75), Inches(4.55)).table
for c,w in zip(table.columns,[3.05,4.65,.95,3.10]): c.width=Inches(w)
for r,row in enumerate(rows):
    table.rows[r].height=Inches(.48 if r==0 else .8)
    for j,v in enumerate(row):
        cell=table.cell(r,j); cell.text=v; cell.fill.solid(); cell.fill.fore_color.rgb=RGBColor.from_string('28475F' if r==0 else CARD)
        for p in cell.text_frame.paragraphs: p.font.name='Aptos'; p.font.size=Pt(14 if r else 15); p.font.bold=(r==0 or j==2); p.font.color.rgb=RGBColor.from_string(ACC if j==2 else FG)
txt(s,.8,6.55,11.6,.35,'Cálculo propuesto: 4 etapas por objetivo; cada etapa terminada suma 25 %.',13,WARN)
s.notes_slide.notes_text_frame.text='Tiempo: 2:00. Recorrer cada objetivo: actividad, resultado, evidencia y faltante. OE3 es el más avanzado por implementación y ensayos en simulación. OE5 es el menor: la comparación exploratoria no cumple el diseño final ni incluye hardware. Rúbrica propuesta para esta exposición, no aprobada por los directores.'

s=slide(3,'¿Qué mostraron las pruebas?','Gazebo y MuJoCo son los dos simuladores que usamos para probar el movimiento.')
for y,title,body in [
    (1.85,'Gazebo · el robot avanza','En 5 pruebas avanzó unos 2,4 cm\npor cada secuencia completa de gateo.'),
    (2.98,'MuJoCo · logramos mejorar el paso','El avance pasó de 2,7 a 9,9 mm por ciclo.\nFalta mejorar cuándo apoya cada pata.'),
    (4.11,'Seguridad · el programa detectó los fallos','Detectó los 9 fallos que provocamos\ny envió la orden de detener la marcha.'),
    (5.24,'Aprendizaje · todavía no logró la mejora','Entrenamos el algoritmo cinco veces.\nLas correcciones no cumplieron lo esperado.')]:
    box(s,.8,y,7.0,1.06,CARD)
    txt(s,1,y+.07,6.6,.36,title,18,ACC,True)
    body_box=txt(s,1,y+.43,6.6,.65,body,16)
    for paragraph in body_box.text_frame.paragraphs: paragraph.space_after=Pt(0)
s.shapes.add_picture(str(PHOTOS/'gazebo_nova.png'), Inches(8.08), Inches(1.85), width=Inches(4.42), height=Inches(3.38))
txt(s,8.08,5.26,4.42,.4,'Nova Spot Micro · captura real de Gazebo',12,ACC)
photo(s,2,8.08,5.8,1.3,.75,'Ensamble')
photo(s,3,9.62,5.8,1.3,.75,'Articulación')
photo(s,4,11.16,5.8,1.3,.75,'Pieza impresa')
txt(s,.8,6.5,7,.4,'Fuentes: tesis; cierre MuJoCo 03/09; diagnóstico PPO 02/09.',11,MUTED)
s.notes_slide.notes_text_frame.text='Tiempo: 2:00. Avance por ciclo indica desplazamiento neto. La coincidencia de contactos es simultánea respecto al plan y no un porcentaje de estabilidad. Las campañas MuJoCo cambian trayectoria y ganancias: no aíslan una sola causa. 5×20 es el diseño; el ejecutor registró 21 ciclos y el análisis comparable usa 2–20. Nueve pruebas prueban reacción lógica, no corte eléctrico. El resultado negativo PPO impide afirmar mejora.'

s=slide(4,'¿Cómo va la escritura de la tesis?','Tenemos un borrador de 73 páginas. Falta completarlo con las pruebas y resultados pendientes.')
card(s,.8,1.9,3.8,4.55,'Ya está escrito','Modelo matemático\nCómo hicimos las pruebas\nCómo funciona el sistema\nResultados de simulación\nProcedimientos y anexos')
card(s,4.78,1.9,3.8,4.55,'Falta completar','Mediciones del robot real\nPruebas de seguridad\nComparación final\nAnálisis de los resultados\nConclusiones finales')
card(s,8.76,1.9,3.8,4.55,'Hay que actualizar','Nuevas pruebas de MuJoCo\nAvances y fotos del prototipo\nProblema de corriente\nTextos que dicen que aún no entrenamos el algoritmo\nCronograma y presupuesto')
s.notes_slide.notes_text_frame.text='Tiempo: 1:10. No hay capítulos declarados definitivamente cerrados. La estructura, métodos y resultados disponibles ya están redactados. El capítulo de conclusiones aún dice que falta entrenar políticas, aunque resultados documenta el entrenamiento: hay que reconciliarlo. El resumen inicial de paso también limita MuJoCo a articulaciones aunque el propio capítulo ya describe pose y contactos. Las campañas del 3 de septiembre y la sobrecarga del 4 deben incorporarse con trazabilidad.'

s=slide(5,'¿Qué falta hacer y en qué orden?','Primero resolver la parte eléctrica; después probar el movimiento y comparar los resultados.')
card(s,.8,1.9,3.8,3.75,'1 · Revisar la electricidad','Encontrar la causa del exceso de corriente.\nRevisar la placa de control.\nMedir voltaje y consumo.\nComprobar el apagado seguro.')
card(s,4.78,1.9,3.8,3.75,'2 · Probar el movimiento','Ajustar primero un motor.\nDespués probar una pata.\nComprobar postura y marcha.\nMedir los movimientos reales.')
card(s,8.76,1.9,3.8,3.75,'3 · Comparar y concluir','Mejorar el algoritmo de aprendizaje.\nProbar con y sin sus correcciones.\nUsar las mismas condiciones.\nExplicar qué mejoró y qué no.')
txt(s,.8,5.95,11.75,.85,'En paralelo: actualizar la tesis con lo que ya hicimos.\nPrincipal dificultad: faltan pruebas físicas y aún no demostramos la mejora por aprendizaje.',17,WARN)
s.notes_slide.notes_text_frame.text='Tiempo: 1:10. Las semanas son una ruta condicionada, no una promesa de marcha. La prioridad es identificar la causa de sobrecarga, verificar alimentación y seguridad y medir antes de transferir. La siguiente campaña RL requiere una política revisada y criterios acordados. Una conclusión negativa rigurosa es válida como resultado, pero no permite dar por cumplida la integración física prevista.'

s=slide(6,'¿Qué entregaremos en la próxima revisión?','Compromiso propuesto: un informe de revisión eléctrica y el borrador de tesis actualizado.')
card(s,.8,1.85,11.72,1.75,'Un informe con mediciones y una tesis actualizada','Registrar qué revisamos, qué medimos y qué falta resolver.\nIncluir fotos, resultados nuevos y correcciones del documento.')
txt(s,.95,3.92,11.35,1.05,'“Nuestro proyecto todavía no puede darse por terminado porque falta comprobar la marcha segura del robot real y evaluar las correcciones aprendidas.”',25)
txt(s,.95,5.25,11.35,1.12,'“La evidencia que permitirá demostrar su finalización será el registro de pruebas comparables, con mediciones y conclusiones sobre lo que funcionó y lo que no.”',25,ACC)
s.notes_slide.notes_text_frame.text='Tiempo: 1:00. Presentar este compromiso como propuesta del grupo a ratificar. Criterio verificable: informe con condiciones, instrumentos, mediciones, incidencias y dictamen de continuar o mantener bloqueo; tesis compilada con los nuevos resultados y las conclusiones corregidas. Si una prueba con carga no puede ejecutarse con seguridad, registrar la causa y el requisito faltante, sin inventar mediciones. No prometer una caminata para la próxima revisión.'
prs.slides[0].notes_slide.notes_text_frame.text += ' Fotos 1 y 5: vista general y electrónica en banco. Fecha de captura no confirmada; incorporación 07/09/2026.'
prs.slides[2].notes_slide.notes_text_frame.text += ' Fotos 2, 3 y 4: ensamble abierto, articulación y pieza impresa. Son evidencia de construcción; no mediciones de desempeño.'
prs.slides[2].notes_slide.notes_text_frame.text += ' La imagen principal es una captura nativa de Gazebo del 07/09/2026, con el modelo del proyecto; no corresponde a una captura de las campañas históricas citadas.'

# Guion oral en lenguaje sencillo; detalles y fuentes en GUIA_EXPOSICION.md.
prs.slides[0].notes_slide.notes_text_frame.text = 'Nuestro propósito es que el robot camine de forma estable y comprobar si el aprendizaje ayuda a mejorar su movimiento. Ya tenemos el modelo en simulación y el prototipo que se ve en las fotografías. En las pruebas físicas respondieron los doce motores, pero apareció un exceso de corriente y detuvimos las pruebas. Todavía debemos resolver la causa antes de continuar. Las fotografías muestran la construcción; no demuestran por sí solas una marcha segura.'
prs.slides[1].notes_slide.notes_text_frame.text = 'Cada fila corresponde a uno de los cinco objetivos. Para el primero tenemos un modelo matemático, pero falta contrastarlo con mediciones del robot. Para el segundo tenemos un programa que detecta fallos, pero falta comprobar la seguridad eléctrica. En el tercero ya creamos y probamos movimientos en simulación. En el cuarto entrenamos el algoritmo, aunque no logró la mejora buscada. El quinto está menos avanzado porque falta completar la comparación. Estos porcentajes son estimaciones: dividimos cada objetivo en cuatro etapas y cada etapa cerrada suma 25 %. La guía técnica explica cuáles son.'
prs.slides[2].notes_slide.notes_text_frame.text = 'Gazebo y MuJoCo son programas que simulan el robot. En Gazebo hicimos cinco pruebas y el avance medio fue de unos 2,4 centímetros por cada secuencia completa de gateo. En MuJoCo ajustamos el movimiento y el avance pasó de 2,7 a 9,9 milímetros por ciclo. Aún falta mejorar cuándo despega y aterriza cada pata. El programa de seguridad detectó los nueve fallos que provocamos y envió la orden de detener la marcha; falta comprobar la parada eléctrica real. Entrenamos el algoritmo de aprendizaje cinco veces, pero sus correcciones no cumplieron los criterios de mejora. La captura de Gazebo ilustra el modelo actual: los números vienen de los informes de pruebas anteriores.'
prs.slides[3].notes_slide.notes_text_frame.text = 'La tesis ya tiene un borrador de 73 páginas. Están escritos el modelo, los procedimientos, el funcionamiento del sistema y los resultados disponibles. Faltan las mediciones y pruebas del robot real, la comparación final y las conclusiones definitivas. También debemos añadir las nuevas pruebas y fotos. Hay frases antiguas que dicen que no hemos entrenado el algoritmo, aunque ya lo hicimos. Vamos a corregirlas para que el documento refleje el mismo estado en todas sus secciones. Tener los capítulos escritos no significa que la tesis esté terminada.'
prs.slides[4].notes_slide.notes_text_frame.text = 'El orden de trabajo empieza por resolver el exceso de corriente y comprobar el apagado seguro. Después ajustaremos un motor y una pata antes de probar el robot completo. Registraremos sus movimientos y el consumo. Finalmente evaluaremos las correcciones aprendidas frente al movimiento básico, usando las mismas condiciones. La comparación debe mostrar tanto lo que mejora como lo que empeora. En paralelo actualizaremos la tesis. Las principales dificultades son la validación física pendiente y que aún no hemos demostrado la mejora mediante aprendizaje.'
prs.slides[5].notes_slide.notes_text_frame.text = 'Para la próxima revisión proponemos entregar un informe de revisión eléctrica y una versión actualizada de la tesis. El informe debe decir qué revisamos, qué medimos, con qué instrumentos y qué falta. Si una prueba no puede hacerse con seguridad, lo registraremos como pendiente. No prometemos una caminata antes de resolver esos requisitos. Nuestro proyecto todavía no puede darse por terminado porque falta comprobar la marcha segura del robot real y evaluar las correcciones aprendidas. La evidencia de cierre serán pruebas comparables, mediciones y conclusiones que expliquen lo que funcionó y lo que no.'
prs.save(OUT/'Primera_entrega_avances_sencilla.pptx')
print(OUT/'Primera_entrega_avances_sencilla.pptx')
