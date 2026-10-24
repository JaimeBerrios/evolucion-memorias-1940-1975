# Cómo compilar el guion

Desde la carpeta del proyecto:

```bash
python3 scripts/compilar_guion.py
```

También funciona desde otra ubicación:

```bash
python3 /home/jaimeberrios/Proyectos/UNAB/Ciclo-6/Sistemas-Digitales/LineaTiempo/scripts/compilar_guion.py
```

El comando sincroniza los discursos y expositores de las 19 láminas, genera `documentos/guion-equipo-1.html` y `documentos/guion-equipo-1.pdf`, actualiza la matriz y verifica el resultado. Usa Python 3, Cairo y pdftotext, ya disponibles en el entorno utilizado. No instala paquetes ni necesita red.

La fuente editable es `documentos/intervenciones.json`; los nombres y roles están en `documentos/equipo.json`. Si cambian las asignaciones o tiempos, actualizar también `documentos/roles-equipo-1.json`; el verificador detecta diferencias. Los ajustes visuales del guion HTML van en `scripts/sincronizar_presentacion.py`; el diseño del PDF, en `scripts/generar_guion.py`.

Para pedirlo a Codex, basta con:

> Compila el guion de este proyecto con `python3 scripts/compilar_guion.py`. Confirma que los 19 discursos coincidan en PDF, HTML y notas de Reveal, y que Carlos tenga sus cuatro grabaciones en las láminas 3, 5, 8 y 10. Revisa el PDF y reporta el resultado sin modificar el reparto ni extender el guion.

Para continuar con la revisión visual en Antigravity, abrir la misma carpeta y copiar el bloque de `documentos/prompt-antigravity.md`.

La compilación comprueba también la suplencia de Jaime en las láminas 2 y 17. El guion conserva a Salvador como titular e indica qué hacer si falta. Para activar ese reparto en la presentación: Ayuda → Activar suplencia de Salvador, o `index.html?suplencia=1`.
