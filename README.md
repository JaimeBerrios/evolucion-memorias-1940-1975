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
- **[demo.html](demo.html)** (o `ejemplos/reveal-demo.html`): Demostración oficial de características avanzadas de Reveal.js (animaciones, diapositivas verticales, transiciones, etc.).

---

## 🚀 Cómo Visualizar la Presentación

Puedes abrir directamente los archivos HTML en tu navegador web favorito:

1. **Directo en el navegador**: Haz doble clic en `index.html` (o `demo.html`).
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
├── demo.html                   # Demo oficial de Reveal.js
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
├── ejemplos/
│   └── reveal-demo.html        # Copia de respaldo de la demo Reveal.js
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

El guion PDF tiene 7 páginas: qué decir en cada lámina, una pauta breve y las instrucciones para las cuatro grabaciones de Carlos. Sin portada extensa ni anexos teóricos. El mismo discurso está en el guion HTML y las notas Reveal (S). Duración orientativa: unos 14 minutos, pendiente de ensayo.

Para compilar y verificar:

```bash
python3 scripts/compilar_guion.py
```

Documentación de uso: `documentos/instrucciones-compilacion.md`. Prompt para continuar con Antigravity: `documentos/prompt-antigravity.md`. Matriz de tiempos y reparto: `documentos/reparto-equipo-1.md`.

Las cuatro imágenes necesarias ya están extraídas en `assets/contenido/imagenes/`, con atribución y procedencia. No hace falta descargar otras para completar el contenido actual. Las fotografías de EPROM corresponden a ejemplares posteriores y se utilizan para ilustrar la ventana de cuarzo.

El comando de compilación verifica igualdad de los 19 discursos en las notas, el HTML y el texto extraído del PDF; correspondencia de expositores y roles; y ubicación de los videos en 3, 5, 8 y 10. Se renderizaron e inspeccionaron las siete páginas del PDF. La revisión visual e interactiva de las láminas en un navegador real y la reproducción de los videos finales siguen pendientes.
