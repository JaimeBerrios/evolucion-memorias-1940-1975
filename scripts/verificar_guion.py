"""Comprueba reparto, notas, guion HTML, PDF y ubicación de las grabaciones."""
from pathlib import Path
from html.parser import HTMLParser
import json,re,subprocess,unicodedata
ROOT=Path(__file__).resolve().parents[1]
S=json.loads((ROOT/'documentos/intervenciones.json').read_text());E=json.loads((ROOT/'documentos/equipo.json').read_text());R=json.loads((ROOT/'documentos/roles-equipo-1.json').read_text())
class Parse(HTMLParser):
 def __init__(self):super().__init__();self.sections=[];self.notes=[];self.speeches=[];self.target=None;self.videos=[];self.recordings=0
 def handle_starttag(self,t,a):
  d=dict(a)
  if t=='section':self.sections.append(d)
  if t=='aside'and d.get('class')=='notes':self.notes.append('');self.target='notes'
  if t=='p'and d.get('class')=='speech':self.speeches.append('');self.target='speeches'
  if t=='p'and d.get('class')=='recording':self.recordings+=1
  if 'data-video'in d:self.videos.append((len(self.sections),d['data-video']))
 def handle_endtag(self,t):
  if t in ['aside','p']:self.target=None
 def handle_data(self,d):
  if self.target:getattr(self,self.target)[-1]+=d
web=Parse();web.feed((ROOT/'index.html').read_text());script=Parse();script.feed((ROOT/'documentos/guion-equipo-1.html').read_text())
assert len(S)==len(web.sections)==len(web.notes)==len(script.speeches)==19
assert [i for i,z in enumerate(S,1)if z['who']==0]==[3,5,8,10]
assert [i for i,u in web.videos]==[3,5,8,10]
assert script.recordings==4
for z,section,note,speech in zip(S,web.sections,web.notes,script.speeches):
 assert section['data-expositor']==E[z['who']]['nombre']
 assert note.startswith(z['text']) and speech==z['text']
 assert z['role']==E[z['who']]['rol']
 assert bool(z.get('recording'))==(z['who']==0)
for i,r in enumerate(R):
 assert r['nombre']==E[i]['nombre'] and r['rol']==E[i]['rol']
 assert r['segundos_estimados']==sum(z['dur']for z in S if z['who']==i)
 assert [e['lamina']for e in r['evidencias']]==[k for k,z in enumerate(S,1)if z['who']==i]
def normalized(t):return ' '.join(unicodedata.normalize('NFKC',t).split())
raw=subprocess.check_output(['pdftotext',str(ROOT/'documentos/guion-equipo-1.pdf'),'-'],text=True);pdf=normalized(raw)
for i,z in enumerate(S,1):
 assert normalized(z['text'])in pdf,f'Falta discurso completo: lámina {i}'
 assert normalized(E[z['who']]['nombre'])in pdf
 if z.get('recording'):assert z['recording']['archivo'].split('/')[-1]in pdf
assert raw.count('LÁMINA ')==19
assert 'Preguntas para sostener'not in raw and 'Responsabilidades y evidencia'not in raw
print('OK: 19 discursos completos e idénticos en notas, HTML y PDF; 6 roles; 4 grabaciones de Carlos en 3, 5, 8 y 10.')
