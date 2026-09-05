(() => {
  const reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  const revealItems = Array.from(document.querySelectorAll('[data-strategy-reveal]'));
  const scanDemo = document.querySelector('[data-strategy-scan]');
  const roadmapDemo = document.querySelector('[data-strategy-roadmap]');
  const hero = document.querySelector('.strategy-hero');

  document.documentElement.classList.add('strategy-motion-ready');

  if (reducedMotion) {
    revealItems.forEach(item => item.classList.add('is-visible'));
    scanDemo?.classList.add('is-running');
    roadmapDemo?.classList.add('is-running');
    return;
  }

  const revealObserver = new IntersectionObserver(entries => {
    entries.forEach(entry => {
      if (!entry.isIntersecting) return;
      entry.target.classList.add('is-visible');
      revealObserver.unobserve(entry.target);
    });
  }, { threshold: 0.14, rootMargin: '0px 0px -8% 0px' });

  revealItems.forEach((item, index) => {
    item.style.setProperty('--strategy-delay', `${Math.min(index % 4, 3) * 70}ms`);
    revealObserver.observe(item);
  });

  const demoObserver = new IntersectionObserver(entries => {
    entries.forEach(entry => {
      entry.target.classList.toggle('is-running', entry.isIntersecting);
    });
  }, { threshold: 0.35 });

  if (scanDemo) demoObserver.observe(scanDemo);
  if (roadmapDemo) demoObserver.observe(roadmapDemo);

  const scanRows = scanDemo ? Array.from(scanDemo.querySelectorAll('li')) : [];
  let activeRow = 0;

  if (scanRows.length) {
    window.setInterval(() => {
      if (!scanDemo.classList.contains('is-running')) return;
      scanRows[activeRow].classList.remove('is-active');
      activeRow = (activeRow + 1) % scanRows.length;
      scanRows[activeRow].classList.add('is-active');
    }, 1400);
  }

  hero?.addEventListener('pointermove', event => {
    const bounds = hero.getBoundingClientRect();
    const x = ((event.clientX - bounds.left) / bounds.width - 0.5) * 16;
    const y = ((event.clientY - bounds.top) / bounds.height - 0.5) * 12;
    hero.style.setProperty('--strategy-field-x', `${x}px`);
    hero.style.setProperty('--strategy-field-y', `${y}px`);
  });

  hero?.addEventListener('pointerleave', () => {
    hero.style.setProperty('--strategy-field-x', '0px');
    hero.style.setProperty('--strategy-field-y', '0px');
  });
})();
