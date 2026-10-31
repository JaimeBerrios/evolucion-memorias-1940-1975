// No descarga recursos externos. Los archivos ausentes conservan su marcador.
document.querySelectorAll('[data-video]').forEach(slot => {
  const player = document.createElement('video');
  player.controls = true;
  player.preload = 'metadata';
  player.playsInline = true;
  player.setAttribute('aria-label', slot.textContent.trim());
  player.addEventListener('loadedmetadata', () => slot.replaceChildren(player), {once:true});
  player.src = slot.dataset.video;
});
Reveal.on('slidechanged', () => document.querySelectorAll('video').forEach(v => v.pause()));
document.querySelectorAll('[data-answer]').forEach(button => {
  button.addEventListener('click', () => {
    document.querySelectorAll('[data-answer]').forEach(b => b.classList.remove('selected'));
    button.classList.add('selected');
    document.getElementById('quiz-feedback').textContent = button.dataset.answer === 'yes'
      ? 'Correcto: EPROM conserva el programa al apagar y permite borrarlo con UV para reprogramarlo.'
      : button.textContent === 'DRAM' ? 'La DRAM pierde el contenido al apagar. Prueba otra opción.' : 'La PROM de fusibles no se puede borrar y reprogramar. Prueba otra opción.';
  });
});

// Lectura y escritura: modelo conceptual, sin simular una tecnología física.
const memoryCells = [...document.querySelectorAll('[data-address]')];
let selectedAddress = 0;
const memoryInput = document.getElementById('memory-value');
const memoryStatus = document.getElementById('memory-status');
function chooseAddress(button) {
  selectedAddress = Number(button.dataset.address);
  memoryCells.forEach(cell => {
    const selected = cell === button;
    cell.classList.toggle('selected', selected);
    cell.setAttribute('aria-pressed', String(selected));
  });
  memoryStatus.textContent = `Dirección ${selectedAddress.toString(2).padStart(2, '0')} seleccionada. Leer consulta el contenido; escribir guarda el dato introducido.`;
}
memoryCells.forEach(button => button.addEventListener('click', () => chooseAddress(button)));
if (memoryInput) {
  document.getElementById('memory-read').addEventListener('click', () => {
    const value = memoryCells[selectedAddress].querySelector('b').textContent;
    memoryInput.value = value;
    memoryStatus.textContent = `Lectura: dirección ${selectedAddress.toString(2).padStart(2, '0')} → ${value}.`;
  });
  document.getElementById('memory-write').addEventListener('click', () => {
    const value = memoryInput.value.trim();
    if (!/^[01]{8}$/.test(value)) {
      memoryStatus.textContent = 'Introduce exactamente 8 bits: solo ceros y unos.';
      memoryInput.focus();
      return;
    }
    memoryCells[selectedAddress].querySelector('b').textContent = value;
    memoryStatus.textContent = `Escritura: ${value} guardado en la dirección ${selectedAddress.toString(2).padStart(2, '0')}. Pulsa Leer para comprobar.`;
  });
}

// Ampliar las evidencias mantiene atribución, teclado y paleta institucional.
const evidenceDialog = document.getElementById('evidence-dialog');
if (evidenceDialog) {
  document.querySelectorAll('[data-evidence]').forEach(button => {
    button.addEventListener('click', () => {
      const source = button.querySelector('img');
      const target = evidenceDialog.querySelector('img');
      target.src = button.dataset.evidence;
      target.alt = source.alt;
      evidenceDialog.querySelector('figcaption').textContent = button.closest('figure').querySelector('figcaption').textContent;
      evidenceDialog.showModal();
    });
  });
  evidenceDialog.querySelector('.close-evidence').addEventListener('click', () => evidenceDialog.close());
  evidenceDialog.addEventListener('click', event => { if (event.target === evidenceDialog) evidenceDialog.close(); });
  evidenceDialog.addEventListener('keydown', event => event.stopPropagation());
  Reveal.on('slidechanged', () => { if (evidenceDialog.open) evidenceDialog.close(); });
}

// El reinicio también restablece las demostraciones y los reproductores.
document.getElementById('reiniciar-presentacion').addEventListener('click', () => {
  const initial = ['10100101', '00111100', '11110000', '00001111'];
  memoryCells.forEach((cell, i) => { cell.querySelector('b').textContent = initial[i]; });
  if (memoryCells.length) {
    chooseAddress(memoryCells[0]);
    memoryInput.value = initial[0];
    memoryStatus.textContent = 'Dirección 00 seleccionada. Pulsa Leer.';
  }
  document.querySelectorAll('[data-answer]').forEach(button => button.classList.remove('selected'));
  document.getElementById('quiz-feedback').textContent = 'Debe conservar el programa al apagar y permitir volver a grabarlo.';
  document.querySelectorAll('video').forEach(player => { player.pause(); player.currentTime = 0; });
});

// La apertura oculta un símbolo; no pretende simular un corte eléctrico real.
const openingBit = document.getElementById('opening-bit');
const openingButton = document.getElementById('toggle-opening-bit');
const openingStatus = document.getElementById('opening-status');
function resetOpeningBit() {
  if (!openingBit) return;
  openingBit.classList.remove('concealed');
  openingBit.setAttribute('aria-hidden', 'false');
  openingButton.setAttribute('aria-pressed', 'false');
  openingButton.textContent = 'Ocultar el bit';
  openingStatus.textContent = 'Recuerden este número.';
}
if (openingButton) {
  openingButton.addEventListener('click', () => {
    const concealed = openingButton.getAttribute('aria-pressed') !== 'true';
    openingBit.classList.toggle('concealed', concealed);
    openingBit.setAttribute('aria-hidden', String(concealed));
    openingButton.setAttribute('aria-pressed', String(concealed));
    openingButton.textContent = concealed ? 'Volver a mostrar' : 'Ocultar el bit';
    openingStatus.textContent = concealed ? 'Ya no se ve. ¿Dónde quedó guardado?' : 'Recuerden este número.';
  });
  document.getElementById('reiniciar-presentacion').addEventListener('click', resetOpeningBit);
}
