/* Home hero background: a field of keycaps with a travelling press wave.
   The brand is a keycap and the design language says motion should reference
   pressing a key, so the hero moves by pressing rather than by drifting blobs.
   No image or video asset: the whole background is drawn here. */
(function () {
  const canvas = document.getElementById("hero-keys");
  if (!canvas) return;

  const ctx = canvas.getContext("2d");
  const reduced = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  const strategyVariant = canvas.dataset.heroKeysVariant === "strategy";

  const CELL = strategyVariant ? 72 : 58;
  const GAP = strategyVariant ? 12 : 9;
  const RADIUS = strategyVariant ? 10 : 8;
  const INK = "26, 23, 20";
  const COPPER = "166, 85, 41";

  let width = 0;
  let height = 0;
  let cols = 0;
  let rows = 0;
  let frame = 0;
  let running = false;
  let startedAt = 0;

  // pointer light, smoothed so the pressed pool trails the cursor slightly
  let pointerX = -9999;
  let pointerY = -9999;
  let poolX = -9999;
  let poolY = -9999;

  function resize() {
    const rect = canvas.getBoundingClientRect();
    const dpr = Math.min(window.devicePixelRatio || 1, 2);
    width = rect.width;
    height = rect.height;
    canvas.width = Math.round(width * dpr);
    canvas.height = Math.round(height * dpr);
    ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
    cols = Math.ceil(width / CELL) + 2;
    rows = Math.ceil(height / CELL) + 2;
  }

  function keycap(x, y, size, fill, edge) {
    ctx.beginPath();
    ctx.roundRect(x, y, size, size, RADIUS);
    ctx.fillStyle = fill;
    ctx.fill();
    ctx.strokeStyle = edge;
    ctx.lineWidth = 1;
    ctx.stroke();
  }

  function render(elapsed) {
    ctx.clearRect(0, 0, width, height);

    // the pool eases toward the cursor: 0.08 keeps the trail readable at 60fps
    poolX += (pointerX - poolX) * 0.08;
    poolY += (pointerY - poolY) * 0.08;

    const size = CELL - GAP;
    const inset = GAP / 2;

    for (let row = 0; row < rows; row++) {
      // rows step sideways like the staggered rows of a real keyboard
      const offsetX = ((row % 4) * CELL) / 4 - CELL;

      for (let col = 0; col < cols; col++) {
        const x = col * CELL + offsetX + inset;
        const y = row * CELL - CELL + inset;

        // one diagonal band of pressed keys sweeping down and right
        const phase = (x + y * (strategyVariant ? 1.12 : 1.35)) / (strategyVariant ? 780 : 640)
          - elapsed * (strategyVariant ? 0.1 : 0.13);
        const wave = Math.max(0, Math.sin(phase * Math.PI * 2));
        let press = wave * wave * wave;

        const dx = x + size / 2 - poolX;
        const dy = y + size / 2 - poolY;
        const reach = 1 - Math.min(1, Math.hypot(dx, dy) / (strategyVariant ? 250 : 210));
        press = Math.min(1, press + reach * reach * (strategyVariant ? 0.68 : 0.85));

        const drop = press * (strategyVariant ? 2.5 : 3);
        const face = (strategyVariant ? 0.012 : 0.018) + press * (strategyVariant ? 0.032 : 0.042);
        const edge = (strategyVariant ? 0.035 : 0.045) + press * (strategyVariant ? 0.075 : 0.1);

        keycap(
          x,
          y + drop,
          size,
          `rgba(${INK}, ${face.toFixed(3)})`,
          `rgba(${INK}, ${edge.toFixed(3)})`
        );

        // the deepest presses pick up the copper accent, used sparingly
        if (press > 0.55) {
          const heat = (press - 0.55) / 0.45;
          keycap(
            x,
            y + drop,
            size,
            `rgba(${COPPER}, ${(heat * (strategyVariant ? 0.035 : 0.05)).toFixed(3)})`,
            `rgba(${COPPER}, ${(heat * (strategyVariant ? 0.12 : 0.16)).toFixed(3)})`
          );
        }
      }
    }
  }

  function loop(now) {
    if (!running) return;
    render((now - startedAt) / 1000);
    frame = requestAnimationFrame(loop);
  }

  function start() {
    if (running || reduced) return;
    running = true;
    startedAt = performance.now() - 4200; // open mid-sweep, not on a blank grid
    frame = requestAnimationFrame(loop);
  }

  function stop() {
    running = false;
    cancelAnimationFrame(frame);
  }

  resize();
  render(4.2);

  if (reduced) return;

  window.addEventListener("resize", () => {
    resize();
    if (!running) render(4.2);
  });

  if (window.matchMedia("(pointer: fine)").matches) {
    canvas.parentElement.addEventListener("pointermove", (event) => {
      const rect = canvas.getBoundingClientRect();
      pointerX = event.clientX - rect.left;
      pointerY = event.clientY - rect.top;
    });
    canvas.parentElement.addEventListener("pointerleave", () => {
      pointerX = -9999;
      pointerY = -9999;
    });
  }

  document.addEventListener("visibilitychange", () => {
    if (document.hidden) stop();
    else start();
  });

  // stop drawing once the hero scrolls away
  new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => (entry.isIntersecting ? start() : stop()));
    },
    { threshold: 0 }
  ).observe(canvas);
})();
