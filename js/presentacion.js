// Usa data-expositor="Nombre" en cada lámina; "grupo" toma el valor de datos/datos.md.
function integrarNumeroPagina() {
  const pieDer = document.querySelector(".pie-der");
  const slideNum = document.querySelector(".slide-number");
  if (pieDer && slideNum && slideNum.parentElement !== pieDer) {
    pieDer.appendChild(slideNum);
  }
}

function actualizarPie(event) {
  integrarNumeroPagina();
  const slide = event && event.currentSlide ? event.currentSlide : Reveal.getCurrentSlide();
  if (!slide) return;
  const nombre = slide.dataset.expositor || "";
  const pie = document.querySelector(".pie");
  if (pie) {
    pie.hidden = !nombre;
  }
  const expositorEl = document.querySelector("#expositor");
  if (expositorEl) {
    const grupoEl = document.querySelector('[data-campo="Grupo"]');
    expositorEl.textContent = nombre === "grupo"
      ? (grupoEl ? grupoEl.textContent : nombre)
      : nombre;
  }
}

Reveal.on("ready", actualizarPie);
Reveal.on("slidechanged", actualizarPie);

Reveal.initialize({
  width: 1280,
  height: 720,
  margin: 0.06,
  hash: true,
  slideNumber: "c/t",
  navigationMode: "default",
  // Mantener las láminas 16:9: el modo scroll reconstruye el DOM y sus controles.
  scrollActivationWidth: null,
  controls: true,
  controlsTutorial: true,
  controlsLayout: "bottom-right",
  controlsBackArrows: "faded",
  progress: true,
  center: false,
  transition: "fade",
  transitionSpeed: "fast",
  backgroundTransition: "fade",
  plugins: [RevealNotes, RevealZoom, RevealSearch, RevealHighlight]
});
