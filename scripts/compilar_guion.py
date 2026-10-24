"""Punto de entrada único: sincroniza, compila y verifica el guion, sin instalar paquetes."""
from pathlib import Path
import subprocess,sys
ROOT=Path(__file__).resolve().parents[1]
for name in ['sincronizar_presentacion.py','generar_guion.py','verificar_guion.py']:
 subprocess.run([sys.executable,str(ROOT/'scripts'/name)],cwd=ROOT,check=True)
print('Listo: documentos/guion-equipo-1.pdf y documentos/guion-equipo-1.html; notas sincronizadas en index.html.')
