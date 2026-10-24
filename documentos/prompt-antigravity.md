# Prompt para continuar en Antigravity

Abre en Antigravity la carpeta del proyecto y pega el siguiente texto:

```text
Continúa el proyecto existente en:
/home/jaimeberrios/Proyectos/UNAB/Ciclo-6/Sistemas-Digitales/LineaTiempo

Lee AGENTS.md. No regeneres el concepto desde cero. Conserva las 19 láminas, el eje cronológico proporcional 1940–1975, formato 16:9, azul UNAB #173864 y blanco, logos y funcionamiento offline.

El reparto aprobado está en documentos/equipo.json:
- Carlos: historiador, láminas 3, 5, 8 y 10. Participa mediante cuatro videos.
- Néstor: hardware, láminas 6, 9, 11 y 14.
- Kevin: lógica y dirección, láminas 7, 15 y 16.
- Ricardo: especialista de campo, láminas 4, 12 y 13.
- Salvador: mapa y síntesis visual, láminas 2 y 17. Si falta, Jaime dice los mismos textos; no eliminar contenido. Activar suplencia en Ayuda o con index.html?suplencia=1.
- Jaime: vocero, láminas 1, 18 y 19.

La primera lámina abre con un 1 que el público recuerda y el presentador oculta; el mismo bit recorre la cronología y vuelve en el cierre. Conservar el orden: gancho del 1, saludo al ingeniero y al grupo, identificación del equipo y recorrido. Evitar rótulos académicos de preparación en pantalla. Cada intervención tiene tres bloques breves (speech_parts) y tres claves (memory_keys) compartidas por lámina, notas y guion. Conservar ese lenguaje sencillo y los relevos. No ampliar los discursos ni exigir memorizar párrafos largos.

La fuente del discurso es documentos/intervenciones.json. Conserva el texto natural y breve, los relevos entre compañeros y las precisiones técnicas. El guion debe incluir solo qué decir por lámina, una pauta breve y, para Carlos, qué grabar y con qué nombre guardarlo. No agregues portada extensa, banco de preguntas ni apartados teóricos al guion.

Revisa la presentación en un navegador real: las 19 láminas, fragmentos, escala del eje, desbordamientos, imágenes ampliables, lectura/escritura de la demo didáctica de memoria, respuesta del reto, ocultar/mostrar el bit y suplencia de las láminas 2 y 17. Si encuentras problemas visuales, corrígelos sin cambiar el contenido aprobado ni el reparto. Aprovecha Reveal.js sin añadir dependencias externas. No instales paquetes sin avisarme antes y obtener autorización.

Las cuatro imágenes necesarias ya están en assets/contenido/imagenes/ y su procedencia está en procedencia.json. Conserva atribuciones y duotono institucional. No presentes las fotografías de EPROM posteriores como una Intel 1702 de 1971.

Los videos del historiador deben permanecer en las láminas 3, 5, 8 y 10, con estos archivos:
assets/contenido/videos/carlos-01-1940s.mp4
assets/contenido/videos/carlos-02-ferrita.mp4
assets/contenido/videos/carlos-03-prom.mp4
assets/contenido/videos/carlos-04-dram.mp4
Si faltan, conserva sus marcadores. No los coloques en las láminas de Néstor.

Para sincronizar y compilar, ejecuta desde el proyecto:
python3 scripts/compilar_guion.py

Este comando actualiza index.html y sus notas, el guion HTML, la matriz de reparto y el PDF, y después verifica la igualdad de los 19 discursos y los cuatro videos de Carlos. Usa los generadores existentes; no edites solo el HTML generado porque la siguiente compilación lo reemplazará. Los cambios de contenido van en documentos/intervenciones.json y los ajustes del generador en scripts/sincronizar_presentacion.py.

Inspecciona el PDF final y reporta qué verificaste realmente, qué sigue pendiente y los archivos actualizados. No afirmes haber probado un navegador o un video si no pudiste ejecutarlo. No hagas commits, push ni publicaciones.
```
