/* Entradas de exposición. El carril y el bit pertenecen a Auto-Animate de Reveal. */
(() => {
  const preference = window.matchMedia('(prefers-reduced-motion: reduce)');
  const running = new Map();
  const profiles = {
    portada: '.opening-copy, .opening-bit-stage',
    mapa: '.map-question, .map-key > span',
    cuarenta: '.historical-evidence article, .historical-evidence .takeaway',
    ferrita: '.historical-evidence article, .historical-evidence .takeaway',
    prom: '.historical-evidence article, .historical-evidence .hint',
    dram: '.historical-evidence article, .historical-evidence .takeaway',
    'campo-retardo': '.product-wordmark, .fact',
    'campo-silicio': '.product-wordmark, .fact',
    'carlos-01': '.mechanism-diagram, .process li',
    'carlos-02': '.mechanism-diagram, .process li',
    'carlos-prom': '.evidence-figure, .mechanism-panel',
    'carlos-03': '.evidence-figure, .mechanism-stages p',
    direccion: '.address-proof, .memory-demo',
    eprom: '.evidence-figure, .photo-argument',
    comparacion: '.decision-table',
    reto: '.quiz button, #quiz-feedback',
    balance: '.legacy-track > div',
    cierre: '.closing p, .takeaway',
    referencias: '.reference-columns'
  };
  function stop() {
    running.forEach(animations => animations.forEach(animation => animation.cancel()));
    running.clear();
  }
  function enter(slide) {
    stop();
    if (!slide || preference.matches || Reveal.isOverview() || Reveal.isPaused()) return;
    const targets = slide.querySelectorAll(profiles[slide.id] || '.era-content > *');
    const animations = [];
    targets.forEach((target, index) => {
      if (typeof target.animate !== 'function') return;
      // Solo desplazamientos cortos y opacidad; sin zoom, giros ni bucles.
      const animation = target.animate(
        [{ opacity: .65, transform: 'translateY(12px)' }, { opacity: 1, transform: 'translateY(0)' }],
        { duration: 320, delay: Math.min(index * 55, 220), easing: 'cubic-bezier(.2,.7,.2,1)' }
      );
      animations.push(animation);
    });
    running.set(slide, animations);
  }
  Reveal.on('ready', event => enter(event.currentSlide));
  Reveal.on('slidechanged', event => enter(event.currentSlide));
  Reveal.on('overviewshown', stop);
  Reveal.on('paused', stop);
  preference.addEventListener('change', stop);
  if (Reveal.isReady()) enter(Reveal.getCurrentSlide());
})();
