# 📊 Presentación con Reveal.js · UNAB

<p align="center">
  <img src="assets/institucional/isotipo-azul.png" alt="Universidad Dr. Andrés Bello" width="120" style="vertical-align: middle; margin-right: 25px;">
  <img src="assets/institucional/logo-facultad.png" alt="Facultad de Tecnología e Innovación" width="130" style="vertical-align: middle;">
</p>

<p align="center">
  <strong>Presentación web interactiva basada en Reveal.js con identidad institucional de la Universidad Dr. Andrés Bello.</strong>
</p>

---

## 📌 Entregables del Proyecto

- **[index.html](index.html)**: Presentación principal interactiva con Reveal.js, navegación, índice, notas de orador y tema institucional UNAB.
- **[documentos/guion-equipo-1.pdf](documentos/guion-equipo-1.pdf)** y **[documentos/guion-equipo-1.html](documentos/guion-equipo-1.html)**: Guion conciso para la defensa por lámina.

---

## 🚀 Cómo Visualizar la Presentación

Puedes abrir directamente el archivo HTML en tu navegador web favorito:

1. **Directo en el navegador**: Haz doble clic en `index.html`.
2. **Servidor local (recomendado)**:
   - Con Python:
     ```bash
     python3 -m http.server 8000
     ```
     Luego visita `http://localhost:8000`.
   - Con la extensión **Live Server** de VS Code: Clic derecho en `index.html` → *Open with Live Server*.

---

## ⌨️ Atajos y Controles

| Tecla | Función |
|---|---|
| `→` / `Espacio` | Avanzar a la siguiente diapositiva |
| `←` | Retroceder a la diapositiva anterior |
| `Esc` | Vista panorámica de todas las diapositivas (overview) |
| `F` | Activar / desactivar pantalla completa |
| `S` | Abrir ventana de notas del expositor (Speaker Notes) |
| `B` / `.` | Pausar presentación (pantalla en negro) |
| `Ctrl` + `Shift` + `F` | Buscar texto en las diapositivas |
| `Alt` + Clic *(Ctrl en Linux)* | Zoom interactivo en cualquier elemento |
| `H` | Mostrar u ocultar barra de herramientas flotante |

---

## 📁 Estructura del Proyecto

```text
.
├── index.html                  # Presentación principal
├── css/
│   ├── unab.css                # Estilo y colores institucionales UNAB (#173864)
│   └── presentacion.css        # Ajustes de láminas, herramientas e índice
├── js/
│   ├── presentacion.js         # Inicialización de Reveal.js y pie dinámico
│   └── interacciones.js        # Índice, atajos y pantalla completa
├── assets/
│   ├── institucional/          # Logos e insignias oficiales de la UNAB
│   ├── contenido/              # Imágenes y diagramas propios del tema
│   └── iconos/                 # SVGs de FontAwesome para uso sin conexión
├── documentos/                 # Guion (HTML/PDF), reparto y datos de intervenciones
└── vendor/
    └── reveal.js/              # Biblioteca Reveal.js y plugins locales
```

## Equipo 1 · Guion definitivo por lámina

`index.html` conserva 19 láminas, eje temporal proporcional de 1940 a 1975, formato 16:9 y paleta azul UNAB/blanco. El reparto aprobado está en `documentos/equipo.json` y la fuente del discurso en `documentos/intervenciones.json`.

- Carlos: historiador (3, 5, 8, 10), con cuatro espacios audiovisuales.
- Néstor: hardware (6, 9, 11, 14).
- Kevin: lógica y dirección (7, 15, 16).
- Ricardo: campo y casos comerciales (4, 12, 13).
- Salvador: mapa y síntesis visual (2, 17).
- Jaime: vocero (1, 18, 19).

El guion PDF tiene 9 páginas: qué decir en cada lámina, una pauta breve y las instrucciones para las cuatro grabaciones de Carlos. Sin portada extensa ni anexos teóricos. El mismo discurso está en el guion HTML y las notas Reveal (S). Duración orientativa: 10–11 minutos, pendiente de ensayo.

Para compilar y verificar:

```bash
python3 scripts/compilar_guion.py
```

Documentación de uso: `documentos/instrucciones-compilacion.md`. Prompt para continuar con Antigravity: `documentos/prompt-antigravity.md`. Matriz de tiempos y reparto: `documentos/reparto-equipo-1.md`.

Las cuatro imágenes necesarias ya están extraídas en `assets/contenido/imagenes/`, con atribución y procedencia. No hace falta descargar otras para completar el contenido actual. Las fotografías de EPROM corresponden a ejemplares posteriores y se utilizan para ilustrar la ventana de cuarzo.

El comando de compilación verifica igualdad de los 19 discursos en las notas, el HTML y el texto extraído del PDF; correspondencia de expositores y roles; y ubicación de los videos en 3, 5, 8 y 10. Se renderizaron e inspeccionaron las nueve páginas del PDF. La revisión visual e interactiva de las láminas en un navegador real y la reproducción de los videos finales siguen pendientes.

### Apertura participativa y continuidad del equipo

La primera lámina muestra un 1, permite ocultarlo y pregunta dónde guardarlo sin chips. El símbolo continúa en el eje temporal y el cierre recupera el experimento. El discurso inicia con la acción del grupo y no con una lista de tecnologías.

Salvador mantiene sus responsabilidades de mapa y síntesis (láminas 2 y 17). Si no participa, Jaime lee esos mismos textos. La apertura y los relevos no dependen de anunciar a Salvador. Se conserva toda la cobertura del diseño visual y no se eliminan láminas.

Antes de exponer, abrir Ayuda y pulsar «Activar suplencia de Salvador», o abrir `index.html?suplencia=1`. Los pies y las etiquetas de expositor de las dos láminas pasan a Jaime. El botón permite restaurar a Salvador. El guion PDF y HTML indican esta alternativa junto a cada intervención; la matriz de reparto la documenta.

Se verificó la lógica de ocultar/mostrar el bit, su reinicio y los dos modos de suplencia con un DOM simulado. La comprobación visual en navegador real y el ensayo del grupo continúan pendientes.

### Guion fácil de seguir

El gancho del 1 va primero. Después Jaime saluda al ingeniero y al grupo, identifica al equipo y presenta el recorrido. Las 19 intervenciones tienen tres bloques cortos y hasta 80 palabras. Las tres claves de cada intervención aparecen en la lámina, el guion y las notas para ayudar a retomar el hilo.

El PDF tiene nueve páginas y conserva las pautas, las cuatro grabaciones de Carlos y la suplencia de Jaime en 2 y 17. El discurso total tiene unas mil palabras; el tiempo orientativo, incluidas las pausas de trabajo, es de 10–11 minutos y debe confirmarse en ensayo. No se ha fijado una duración mínima de la consigna.

### Diseño de la presentación

La hoja `css/presentacion.css` usa una composición única de 1280 × 720: encabezado, contenido central, eje cronológico inferior y tres palabras clave. Las fotografías conservan su proporción; las cuatro grabaciones tienen marco 16:9. El mecanismo de PROM agrupa diagrama y pasos en una misma columna.

`js/diseno.js` coordina entradas de 320 ms y retrasos de hasta 220 ms por grupos. Reveal Auto-Animate conserva las posiciones de las fechas y mueve el bit y el progreso del eje. Las entradas no bloquean los controles, no se repiten en bucle y se cancelan al navegar, pausar o abrir la vista general. Se respeta la preferencia de movimiento reducido. El cierre no exige clics adicionales para mostrar sus tres capacidades.

Se comprobó que los textos de las 19 láminas, discursos, claves, pautas y roles permanecen iguales; el PDF y el guion HTML conservan su contenido y sus archivos sin modificaciones. Se verificaron la sintaxis JavaScript y la lógica de las animaciones con un DOM simulado. El intento de abrir Chrome headless falló por una restricción del entorno (`shutdown: Operation not permitted`), por lo que la inspección visual en navegador real continúa pendiente.
