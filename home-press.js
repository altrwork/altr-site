/* The homepage press: an 18th-century printing press (Encyclopedie,
   Imprimerie, pl. XV) that runs itself. The frisket folds onto the
   tympan and both swing over onto the bed along the engraver's own
   dotted arcs, rest, and swing back. Pauses off-screen; reduced motion
   shows the press at rest. */
(() => {
  const press = document.querySelector('[data-press]');
  if (!press) return;
  if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;

  const tympan = press.querySelector('.pp-press-tympan');
  const frisket = press.querySelector('.pp-press-frisket');
  const LOOP = 13000;
  const ease = t => (t < 0.5 ? 4 * t * t * t : 1 - Math.pow(-2 * t + 2, 3) / 2);
  const span = (t, a, b) => Math.min(1, Math.max(0, (t - a) / (b - a)));
  let t0 = performance.now();
  let raf = 0;
  let running = false;

  const frame = now => {
    const t = ((now - t0) % LOOP) / 1000;
    const fold = ease(span(t, 1.0, 2.6)) - ease(span(t, 8.6, 10.2));
    const swing = ease(span(t, 2.6, 4.8)) - ease(span(t, 6.4, 8.6));
    frisket.style.transform = `rotate(${fold * 151}deg)`;
    tympan.style.transform = `rotate(${swing * 153}deg)`;
    raf = requestAnimationFrame(frame);
  };
  const play = () => { if (!running) { running = true; raf = requestAnimationFrame(frame); } };
  const pause = () => { running = false; cancelAnimationFrame(raf); };

  new IntersectionObserver(entries => {
    entries.forEach(entry => (entry.isIntersecting ? play() : pause()));
  }, { threshold: 0.15 }).observe(press);
  document.addEventListener('visibilitychange', () => (document.hidden ? pause() : play()));
})();
