(() => {
  const reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  const revealItems = Array.from(document.querySelectorAll('[data-strategy-reveal]'));
  const scanDemo = document.querySelector('[data-strategy-scan]');
  const roadmapDemo = document.querySelector('[data-strategy-roadmap]');

  document.documentElement.classList.add('strategy-motion-ready');

  if (reducedMotion) {
    revealItems.forEach(item => item.classList.add('is-visible'));
    scanDemo?.classList.add('is-running');
    roadmapDemo?.classList.add('is-running');
    scanDemo?.style.setProperty('--scan-progress', '1');
    roadmapDemo?.style.setProperty('--roadmap-progress', '1');
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
    item.style.setProperty('--strategy-delay', `${Math.min(index % 3, 2) * 40}ms`);
    revealObserver.observe(item);
  });

  const runScanSequence = demo => {
    const rows = Array.from(demo.querySelectorAll('li'));
    const stepDuration = 720;

    const play = () => {
      demo.classList.add('is-resetting');
      rows.forEach(row => row.classList.remove('is-active'));
      demo.style.setProperty('--scan-progress', '0');

      window.setTimeout(() => {
        demo.classList.remove('is-resetting');
        rows.forEach((row, index) => {
          window.setTimeout(() => {
            rows.forEach(item => item.classList.remove('is-active'));
            row.classList.add('is-active');
            demo.style.setProperty('--scan-progress', String((index + 1) / rows.length));
          }, 180 + (index * stepDuration));
        });
      }, 90);

      window.setTimeout(play, 180 + (rows.length * stepDuration) + 1500);
    };

    play();
  };

  const runRoadmapSequence = demo => {
    const phases = Array.from(demo.querySelectorAll('ol li'));
    const status = demo.querySelector('[data-roadmap-status]');
    const stepDuration = 980;

    const play = () => {
      demo.classList.add('is-resetting');
      phases.forEach(phase => phase.classList.remove('is-active', 'is-complete'));
      demo.style.setProperty('--roadmap-progress', '0');
      if (status) status.textContent = phases[0]?.querySelector('span')?.textContent || '';

      window.setTimeout(() => {
        demo.classList.remove('is-resetting');
        phases.forEach((phase, index) => {
          window.setTimeout(() => {
            phases.forEach((item, itemIndex) => {
              item.classList.toggle('is-active', itemIndex === index);
              item.classList.toggle('is-complete', itemIndex < index);
            });
            demo.style.setProperty('--roadmap-progress', String((index + 1) / phases.length));
            if (status) status.textContent = phase.querySelector('span')?.textContent || '';
          }, 220 + (index * stepDuration));
        });
      }, 90);

      window.setTimeout(play, 220 + (phases.length * stepDuration) + 1600);
    };

    play();
  };

  const demoObserver = new IntersectionObserver(entries => {
    entries.forEach(entry => {
      if (!entry.isIntersecting) return;
      entry.target.classList.add('is-running');
      if (entry.target === scanDemo) runScanSequence(entry.target);
      if (entry.target === roadmapDemo) runRoadmapSequence(entry.target);
      demoObserver.unobserve(entry.target);
    });
  }, { threshold: 0.35 });

  if (scanDemo) demoObserver.observe(scanDemo);
  if (roadmapDemo) demoObserver.observe(roadmapDemo);
})();
