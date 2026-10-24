"""Sincroniza las láminas, sus notas y el guion HTML desde intervenciones.json."""
from pathlib import Path
import html,json,re
R=Path(__file__).resolve().parents[1]
S=json.loads((R/'documentos/intervenciones.json').read_text())
E=json.loads((R/'documentos/equipo.json').read_text())
N=[e['nombre'] for e in E]
H=[('cuarenta',1948,'1948 / 49','Cargas y ondas'),('ferrita',1953,'1953','Ferrita'),('prom',1956,'1956','PROM'),('dram',1966,'1966','DRAM'),('eprom',1971,'1971','EPROM')]
def x(year):return 4+(year-1940)/35*92

def rail(s):
 active=s['stage'];year=s['year'];mapa=s['id']=='mapa'
 h=f'<nav class="chronology {"chronology-map" if mapa else ""}" aria-label="Línea de tiempo de 1940 a 1975" data-id="chronology"><div class="time-axis" data-id="axis"></div><div class="time-travel" data-id="travel" style="width:{x(year)-4}%"></div><span class="time-bound start">1940</span><span class="time-bound end">1975</span>'
 for i,yy,date,title in H:
  current=active=={'cuarenta':'origen'}.get(i,i)
  h+=f'<a class="time-node {"active" if current else ""} {"past" if yy<year else ""}" href="#/{i}" data-id="node-{i}" style="left:{x(yy):.2f}%" {"aria-current=step" if current else ""}><span class="node-date">{date}</span><span class="node-dot"></span><span class="node-name">{title}</span></a>'
 if s['id']!='portada':h+=f'<span class="travelling-bit" data-id="memory-bit" style="left:{x(year):.2f}%" aria-hidden="true">1</span>'
 h+='</nav>'
 return h
old=(R/'index.html').read_text();a=old.index('    <div class="slides">');b=old.index('    </div>\n\n    <nav class="ruta-exposicion"')
body=''
source={'cuarenta':'CHM · EDSAC (1949) / material docente','ferrita':'CHM · Whirlwind (1953)','prom':'Micron · Hot Chips 2016, cronología','dram':'IBM · DRAM / 1966: idea; 1970: producto','eprom':'CHM · EPROM (1971) / Intel · Dov Frohman'}
for i,s in enumerate(S):
 # Agrupar el mecanismo y sus pasos evita una tercera celda implícita en la cuadrícula.
 visual_body=s['body']
 if s['id']=='carlos-prom':
  start=visual_body.index('<div class="mechanism-diagram">')
  end=visual_body.index('</ol>',start)+len('</ol>')
  visual_body=visual_body[:start]+'<div class="mechanism-panel">'+visual_body[start:end]+'</div>'+visual_body[end:]
 visual_body=visual_body.replace('fragment fade-up','motion-step')
 badge='1940–75' if s['id'] in ['portada','mapa','referencias'] else str(s['year'])
 body+=f'<section id="{s["id"]}" class="era era-{s["stage"]} layout-{s.get("layout","standard")}" style="--event-position:{x(s["year"]):.2f}%" data-expositor="{N[s["who"]]}" data-auto-animate data-auto-animate-duration="0.65" data-auto-animate-unmatched="false" data-auto-animate-easing="cubic-bezier(.2,.7,.2,1)"><p class="eyebrow">EQUIPO 01 <span>/ {s["date"]}</span></p><span class="era-watermark" aria-hidden="true">{badge}</span><p class="role-tag">{s["role"]}</p><h2>{s["title"]}</h2>{rail(s)}<div class="era-content">{visual_body}</div>'
 if s.get('memory_keys'):body+='<div class="argument-strip recall-strip" aria-label="Ideas principales">'+''.join('<span>'+html.escape(k)+'</span>' for k in s['memory_keys'])+'</div>'
 elif s.get('claim'):body+=f'<p class="argument-strip">{html.escape(s["claim"])}</p>'
 if s.get('source'):body+=f'<p class="evidence">{s["source"]}</p>'
 if s.get('fallback'):
  fallback=s['fallback']
  # La etiqueta de sección recibe la identidad de suplencia sin cambiar el reparto habitual.
  marker=f'id="{s["id"]}"'
  body=body.replace(marker,marker+f' data-suplente="{N[fallback["who"]]}" data-rol-suplente="{fallback["role"]}"',1)
 spoken=' '.join('<span>'+html.escape(part)+'</span>' for part in s['speech_parts'])
 body+=f'<aside class="notes">{spoken}<br>CLAVES: {html.escape(" → ".join(s["memory_keys"]))}<br>PAUTA: {html.escape(s["cue"])}</aside></section>\n'
result=old[:a]+'    <div class="slides">'+body+old[b:]
# El índice se genera desde la misma fuente para no conservar enlaces antiguos.
result=re.sub(r'(<nav aria-label="Índice de diapositivas"><ol>).*?(</ol></nav>)',lambda m:m[1]+''.join(f'<li><a href="#/{z["id"]}">{j+1:02} · {z["title"]}</a></li>' for j,z in enumerate(S))+m[2],result,flags=re.S)
filter_markup='<svg class="svg-filters" aria-hidden="true" width="0" height="0"><defs><filter id="tinta-unab" color-interpolation-filters="sRGB"><feColorMatrix type="matrix" values="0.193424 0.650693 0.065687 0 0.090196 0.165910 0.558136 0.056346 0 0.219608 0.129227 0.434729 0.043887 0 0.392157 0 0 0 1 0"/></filter></defs></svg>'
if 'id="tinta-unab"' not in result:result=result.replace('<body>','<body>'+filter_markup)
dialog_markup='<dialog id="evidence-dialog" aria-labelledby="evidence-caption"><button type="button" class="close-evidence" aria-label="Cerrar evidencia">Cerrar ×</button><figure><img class="institutional-image" alt=""><figcaption id="evidence-caption"></figcaption></figure></dialog>'
if 'id="evidence-dialog"' not in result:result=result.replace('  <!-- Scripts Reveal.js y Plugins -->',dialog_markup+'\n  <!-- Scripts Reveal.js y Plugins -->')
if 'id="alternar-suplencia"' not in result:result=result.replace('<button type="button" id="iniciar-exposicion">','<button type="button" id="alternar-suplencia" aria-pressed="false">Activar suplencia de Salvador</button><button type="button" id="iniciar-exposicion">')
if 'src="js/diseno.js"' not in result:result=result.replace('</body>','  <script src="js/diseno.js"></script>\n</body>')
(R/'index.html').write_text(result)
css='''@page{size:A4;margin:18mm}body{font:12pt/1.6 system-ui,sans-serif;color:#173864;max-width:850px;margin:auto;padding:24px;background:#fff}h1{font-size:24pt}h2{font-size:17pt;margin:5px 0}article{border-top:2px solid #173864;padding:20px 0;margin:20px 0;break-inside:avoid}.meta{font-size:10pt}.speech{font-size:13pt;line-height:1.65}.speech-part{display:block;margin-bottom:10px}.keys{font-size:11pt;font-weight:600;border-bottom:1px solid #173864;padding-bottom:8px}.cue,.recording{border-left:3px solid #173864;padding:8px 14px;font-size:10pt;background:rgba(23,56,100,.04)}.recording{font-weight:600}a{color:inherit} @media(max-width:600px){body{padding:15px}} @media print{body{padding:0}article{margin:10px 0}}'''
doc=f'<!doctype html><html lang="es"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Guion por lámina · Equipo 1</title><style>{css}</style><body><h1>Guion por lámina · Equipo 1</h1><p>La era clásica y el nacimiento del silicio · 1940–1975.<br>Duración orientativa: {sum(s["dur"] for s in S)//60}–{sum(s["dur"] for s in S)//60+1} minutos, pendiente de ensayo. Cada intervención tiene tres ideas. Usa las claves para seguir el hilo; las pautas no se dicen en voz alta.</p>'
roles=json.loads((R/'documentos/roles-equipo-1.json').read_text())
for i,s in enumerate(S):
 spoken=' '.join('<span class="speech-part">'+html.escape(part)+'</span>' for part in s['speech_parts'])
 doc+=f'<article id="lamina-{i+1:02}"><p class="meta">LÁMINA {i+1:02} · {s["dur"]} s aprox.</p><h2>{html.escape(s["title"])}</h2><p class="meta"><strong>{N[s["who"]]}</strong> · {s["role"]}</p><p class="keys">{html.escape(" → ".join(s["memory_keys"]))}</p><p class="speech">{spoken}</p><p class="cue"><strong>Pauta:</strong> {html.escape(s["cue"])}</p>'
 if s.get('fallback'):doc+='<p class="fallback">'+html.escape(s['fallback']['instruccion'])+'</p>'
 if s.get('recording'):doc+='<p class="recording">'+html.escape(s['recording']['instruccion'])+'</p>'
 doc+='</article>'
doc+='</body></html>'
(R/'documentos/guion-equipo-1.html').write_text(doc)
print('Sincronizadas:',len(S),'láminas, notas e intervenciones HTML.')

# Matriz revisable de participación, generada con las mismas asignaciones.
rows=['# Reparto y evidencia del equipo 1','', 'La asignación corresponde al reparto indicado por el equipo: Carlos historiador; Néstor hardware; Kevin lógica; Ricardo campo; Salvador diseño; Jaime vocero. Cada rol tiene contenido verificable en la presentación y el guion. El ensayo y la participación real siguen pendientes.', '', '| Integrante | Rol | Qué demuestra | Láminas | Tiempo aprox. |', '|---|---|---|---|---|']
for r in roles:
 rows.append('| '+r['nombre']+' | '+r['rol']+' | '+r['criterio']+' | '+', '.join(str(e['lamina']) for e in r['evidencias'])+' | '+str(r['segundos_estimados']//60)+':'+str(r['segundos_estimados']%60).zfill(2)+' |')
rows+=['', 'Carlos tiene cuatro intervenciones de contexto histórico: limitaciones en 1940s, ferrita, PROM y DRAM.', '', 'Néstor describe los cuatro mecanismos de hardware: magnetismo en ferrita, fusibles en PROM, celda DRAM y compuerta flotante en EPROM.', '', 'Kevin analiza el direccionamiento lógico por buses, la comparativa de operaciones y el reto de selección de memoria.', '', 'Ricardo expone los casos de aplicación comercial: UNIVAC I, serie HP 9800 y EPROM en desarrollo de microprocesadores.', '', 'Salvador guía el mapa cronológico proporcional y la síntesis visual de la línea de tiempo.', '', 'Jaime presenta la era, defiende el argumento ante el grupo y sintetiza la importancia fundacional de esta etapa.']
rows+=['', 'Plan de suplencia: Salvador mantiene el mapa (2) y la síntesis visual (17). Si falta, Jaime lee el mismo discurso en ambas, sin eliminar láminas ni contenidos. En Ayuda, activar «Suplencia de Salvador», o abrir index.html?suplencia=1. La apertura y los relevos funcionan en los dos casos.']
(R/'documentos/reparto-equipo-1.md').write_text('\n'.join(rows)+'\n')
