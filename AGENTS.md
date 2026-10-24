# Instrucciones para el Asistente (Codex / Antigravity)

## Propósito del Proyecto

Este repositorio es un proyecto de presentación web interactiva basada en **Reveal.js**, adaptado con la identidad visual institucional de la Universidad Dr. Andrés Bello (UNAB).
Está enfocado exclusivamente en la elaboración y visualización de la presentación (por ejemplo, para la Línea de Tiempo de Sistemas Digitales).

## Estructura de Archivos

- `index.html`: Diapositivas principales de la presentación con Reveal.js.
- `css/unab.css`: Tema y estilos institucionales UNAB (color `#173864`, tipografía, tarjetas y bloques).
- `css/presentacion.css`: Estilos específicos de navegación, herramientas de exposición y diseño de láminas.
- `js/presentacion.js`: Inicialización de Reveal.js, configuración y sincronización de pie de diapositiva.
- `js/interacciones.js`: Atajos de teclado, índice interactivo, pantalla completa y modo de exposición.
- `assets/institucional/`: Logotipos, isotipos y sellos oficiales UNAB.
- `assets/contenido/`: Carpeta para imágenes, diagramas y evidencias del tema.
- `assets/iconos/`: Iconos SVG (Font Awesome) para uso local sin conexión.
- `vendor/reveal.js/`: Biblioteca Reveal.js y sus plugins (zoom, notes, search, highlight, markdown).

## Pautas de Edición

1. **Edición directa en HTML**: Las diapositivas se agregan y modifican dentro de `<div class="slides">` en `index.html`.
2. **Funcionamiento 100% offline**: Todos los recursos (estilos, scripts, iconos y fuentes) se resuelven de forma local. No agregues dependencias externas por CDN que rompan la visualización sin conexión.
3. **Identidad UNAB**: Conservar el azul institucional `#173864`, los logos en la portada y proporciones 16:9.
4. **Presentador por lámina**: Usar el atributo `data-expositor="Nombre"` en cada `<section>` para actualizar el pie de lámina dinámicamente.
5. **Atajos**:
   - `→` / `Espacio`: Avanzar diapositiva.
   - `←`: Retroceder.
   - `Esc`: Vista general (overview).
   - `F`: Pantalla completa.
   - `S`: Modo orador / notas del expositor.
   - `B`: Pausar pantalla.
   - `H`: Ocultar o mostrar barra de herramientas.
