/* The "This week" panel on the homepage. The page renders it finished, so
   crawlers, reduced-motion visitors and anyone without JS see every item in
   its final state. With JS it resets to "To do" and ticks the items over in
   order the first time the panel scrolls into view. */
(() => {
  const panel = document.querySelector('[data-busywork]');
  if (!panel) return;
  if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;
  if (!('IntersectionObserver' in window)) return;

  panel.classList.add('is-pending');

  const observer = new IntersectionObserver(entries => {
    if (!entries.some(entry => entry.isIntersecting)) return;
    observer.disconnect();
    panel.classList.remove('is-pending');
    panel.classList.add('is-playing');
  }, { threshold: 0.45 });

  observer.observe(panel);
})();
