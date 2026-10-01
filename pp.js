/* Plate & Press behaviour: reveal-on-view, the nav, and the menu sheet.
   Pages render complete without this file; it only adds motion and the
   menu toggle. */
(() => {
  const root = document.documentElement;
  const reduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* -- reveal: .is-in when an element reaches the viewport ---------- */
  const targets = document.querySelectorAll('[data-settle], [data-pull], [data-rule], .ln');
  const show = el => el.classList.add('is-in');

  document.querySelectorAll('[data-rule]').forEach(list => {
    [...list.children].forEach((li, i) => li.style.setProperty('--i', i));
  });

  if (reduced || !('IntersectionObserver' in window)) {
    targets.forEach(show);
  } else {
    const io = new IntersectionObserver(entries => {
      entries.forEach(entry => {
        if (!entry.isIntersecting) return;
        show(entry.target);
        io.unobserve(entry.target);
      });
    }, { rootMargin: '0px 0px -8% 0px', threshold: 0.12 });
    targets.forEach(el => io.observe(el));
    // never leave anything hidden if an observer misses it
    window.setTimeout(() => targets.forEach(show), 4000);
  }

  /* -- nav: tint once scrolled, hide on the way down ---------------- */
  const nav = document.querySelector('.nav');
  if (!nav) return;
  let lastY = window.scrollY;
  let ticking = false;
  const onScroll = () => {
    const y = window.scrollY;
    nav.classList.toggle('is-scrolled', y > 40);
    if (!root.classList.contains('pp-menu-open')) {
      nav.classList.toggle('is-hidden', y > 240 && y > lastY + 4);
      if (y < lastY - 4) nav.classList.remove('is-hidden');
    }
    lastY = y;
    ticking = false;
  };
  window.addEventListener('scroll', () => {
    if (!ticking) {
      ticking = true;
      window.requestAnimationFrame(onScroll);
    }
  }, { passive: true });
  onScroll();

  /* -- menu sheet ---------------------------------------------------- */
  const button = nav.querySelector('.pp-menu-btn');
  const menu = document.getElementById('pp-menu');
  if (!button || !menu) return;
  const label = button.querySelector('span');

  menu.querySelectorAll('.pp-menu-main li, .pp-menu-cols > div').forEach((el, i) => el.style.setProperty('--i', i));

  const focusables = () => [...menu.querySelectorAll('a, button')];

  const setOpen = open => {
    root.classList.toggle('pp-menu-open', open);
    button.setAttribute('aria-expanded', String(open));
    if (label) label.textContent = open ? 'Close' : 'Menu';
    menu.inert = !open;
    document.body.style.overflow = open ? 'hidden' : '';
    nav.classList.remove('is-hidden');
    if (open) window.setTimeout(() => focusables()[0]?.focus({ preventScroll: true }), 60);
  };

  menu.inert = true;
  button.addEventListener('click', () => setOpen(!root.classList.contains('pp-menu-open')));
  menu.addEventListener('click', event => {
    if (event.target.closest('a')) setOpen(false);
  });

  document.addEventListener('keydown', event => {
    if (!root.classList.contains('pp-menu-open')) return;
    if (event.key === 'Escape') {
      setOpen(false);
      button.focus();
      return;
    }
    if (event.key !== 'Tab') return;
    // keep focus inside the sheet and its toggle while it is open
    const items = [button, ...focusables()];
    const first = items[0];
    const last = items[items.length - 1];
    if (event.shiftKey && document.activeElement === first) {
      event.preventDefault();
      last.focus();
    } else if (!event.shiftKey && document.activeElement === last) {
      event.preventDefault();
      first.focus();
    }
  });
})();
