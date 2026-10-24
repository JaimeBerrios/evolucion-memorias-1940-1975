"""Guion conciso: discurso y pauta por lámina; indicaciones de grabación solo para Carlos."""
from pathlib import Path
import json,cairo
ROOT=Path(__file__).resolve().parents[1]
S=json.loads((ROOT/'documentos/intervenciones.json').read_text())
E=json.loads((ROOT/'documentos/equipo.json').read_text())
BLUE=(23/255,56/255,100/255)
surface=cairo.PDFSurface(str(ROOT/'documentos/guion-equipo-1.pdf'),595,842)
surface.set_metadata(cairo.PDF_METADATA_TITLE,'Guion por lámina · Equipo 1')
surface.set_metadata(cairo.PDF_METADATA_AUTHOR,'Equipo 1 · Sistemas Digitales · UNAB')
c=cairo.Context(surface);page=0;y=0

def wrap(text,size,bold=False):
 c.select_font_face('sans-serif',cairo.FONT_SLANT_NORMAL,cairo.FONT_WEIGHT_BOLD if bold else cairo.FONT_WEIGHT_NORMAL);c.set_font_size(size)
 rows=[];row=''
 for w in text.split():
  candidate=(row+' '+w).strip()
  if c.text_extents(candidate).x_advance>495 and row:rows.append(row);row=w
  else:row=candidate
 if row:rows.append(row)
 return rows

def paragraph(text,size=11,bold=False):
 global y
 rows=wrap(text,size,bold)
 for row in rows:
  c.set_source_rgb(*BLUE);c.move_to(50,y);c.show_text(row);y+=size*1.45
 y+=8

def newpage():
 global page,y
 if page:surface.show_page()
 page+=1;y=42
 paragraph('UNAB / SISTEMAS DIGITALES / EQUIPO 1',9,True)
 paragraph('Guion por lámina · La era clásica (1940–1975)',13,True)
 c.set_source_rgb(*BLUE);c.set_line_width(1);c.move_to(50,77);c.line_to(545,77);c.stroke()
 c.set_font_size(8);c.move_to(50,811);c.show_text('Leer el discurso. Las pautas e indicaciones de grabación no se dicen en voz alta.');c.move_to(530,811);c.show_text(str(page));y=103

for i,s in enumerate(S,1):
 blocks=[(f'LÁMINA {i:02} · {s["dur"]} s aprox.',9,True),(s['title'],15,True),(E[s['who']]['nombre']+' · '+s['role'],10,True),('Claves: '+' / '.join(s['memory_keys']),10,True)]
 blocks.extend((part,11,False) for part in s['speech_parts'])
 blocks.append(('Pauta: '+s['cue'],9,False))
 if s.get('fallback'):blocks.append((s['fallback']['instruccion'],9,True))
 if s.get('recording'):blocks.append((s['recording']['instruccion'],9,True))
 h=sum(len(wrap(t,size,bold))*size*1.45+8 for t,size,bold in blocks)
 if not page or y+h>775:newpage()
 assert h<672, f'Intervención demasiado larga: {i}'
 for block in blocks:paragraph(*block)
 y+=12;c.set_source_rgba(*BLUE,.2);c.move_to(50,y-8);c.line_to(545,y-8);c.stroke()
surface.finish();print(f'PDF generado: {page} páginas, {len(S)} intervenciones.')
