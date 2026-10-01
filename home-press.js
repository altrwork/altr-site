/* The homepage press: an 18th-century printing press (Encyclopédie,
   Imprimerie, pl. XV) that runs itself. The frisket folds onto the
   tympan, both swing over onto the bed along the engraver's own dotted
   arcs, a printed sheet lifts off and settles on a stack, and the frames
   swing back. Pauses off-screen; reduced motion shows the press at rest. */
(() => {
  const press = document.querySelector('[data-press]');
  if (!press) return;
  if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;

  const tympan = press.querySelector('.pp-press-tympan');
  const frisket = press.querySelector('.pp-press-frisket');
  const sheet = press.querySelector('.pp-press-sheet');
  const stack = press.querySelector('.pp-press-stack');
  const LOOP = 11000;
  const ease = t => (t < 0.5 ? 4 * t * t * t : 1 - Math.pow(-2 * t + 2, 3) / 2);
  const span = (t, a, b) => Math.min(1, Math.max(0, (t - a) / (b - a)));

  let start = performance.now();
  let running = false;
  let raf = 0;
  let printed = 0;
  let lastCycle = -1;

  const addSheet = () => {
    printed = printed >= 6 ? 1 : printed + 1;
    stack.querySelectorAll('rect').forEach((r, i) => r.style.opacity = i < printed ? 1 : 0);
  };

  const frame = now => {
    const elapsed = now - start;
    const cycle = Math.floor(elapsed / LOOP);
    const t = (elapsed % LOOP) / 1000;

    // 0.6-1.8s frisket folds onto the tympan; 1.8-3.4s both swing onto the bed
    const fold = ease(span(t, 0.6, 1.8)) - ease(span(t, 7.2, 8.4));
    const swing = ease(span(t, 1.8, 3.4)) - ease(span(t, 6.0, 7.6));
    frisket.style.transform = `rotate(${fold * 151}deg)`;
    tympan.style.transform = `rotate(${swing * 153}deg)`;

    // 3.8-6.0s the printed sheet lifts off the bed and settles on the stack
    const lift = span(t, 3.8, 6.0);
    if (lift > 0 && lift < 1) {
      const e = ease(lift);
      const x = -251 * e;
      const y = -190 * Math.sin(Math.PI * e) + 264 * e;
      const s = 0.25 + 0.75 * Math.sin(Math.PI * Math.min(1, e * 1.15));
      sheet.style.opacity = String(Math.min(1, lift * 6, (1 - lift) * 8));
      sheet.style.transform = `translate(${x}px, ${y}px) rotate(${-14 * Math.sin(Math.PI * e)}deg) scale(1, ${s})`;
    } else {
      sheet.style.opacity = '0';
    }
    if (t >= 6.0 && cycle !== lastCycle) {
      lastCycle = cycle;
      addSheet();
    }
    raf = requestAnimationFrame(frame);
  };

  const play = () => {
    if (running) return;
    running = true;
    start = performance.now() - (start ? 0 : 0);
    raf = requestAnimationFrame(frame);
  };
  const pause = () => {
    running = false;
    cancelAnimationFrame(raf);
  };

  new IntersectionObserver(entries => {
    entries.forEach(entry => (entry.isIntersecting ? play() : pause()));
  }, { threshold: 0.15 }).observe(press);

  document.addEventListener('visibilitychange', () => (document.hidden ? pause() : play()));
})();
