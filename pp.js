/* Plate & Press behaviour: reveal-on-view, the nav, and the menu sheet.
   Pages render complete without this file; it only adds motion and the
   menu toggle. */
(() => {
  const root = document.documentElement;
  const reduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* Type the homepage headline letter by letter, while reserving its full width. */
  const typeHeadline = document.querySelector('[data-type-headline]');
  if (typeHeadline && !reduced) {
    const lines = [...typeHeadline.querySelectorAll('[data-type-line]')].map(line => {
      const value = line.textContent;
      const reserve = document.createElement('span');
      reserve.className = 'ph-type-reserve';
      reserve.textContent = value;
      const live = document.createElement('span');
      live.className = 'ph-type-live';
      line.replaceChildren(reserve, live);
      return { value, live };
    });
    typeHeadline.classList.add('is-typing');
    const typeLine = (lineIndex, charIndex = 0) => {
      if (lineIndex >= lines.length) {
        typeHeadline.classList.add('is-complete');
        return;
      }
      const { value, live } = lines[lineIndex];
      live.classList.add('is-active');
      live.textContent = value.slice(0, charIndex + 1);
      if (charIndex + 1 < value.length) {
        window.setTimeout(() => typeLine(lineIndex, charIndex + 1), 55);
      } else {
        live.classList.remove('is-active');
        window.setTimeout(() => typeLine(lineIndex + 1), 130);
      }
    };
    window.setTimeout(typeLine, 140, 0);
  }

  /* -- reveal: .is-in when an element reaches the viewport ---------- */
  const targets = document.querySelectorAll('[data-settle], [data-pull], [data-rule], [data-build], [data-press], .ln');
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

  /* -- dated items (the next workshop) hide once their date passes -- */
  document.querySelectorAll('[data-until]').forEach(el => {
    const until = Date.parse(el.dataset.until);
    if (!Number.isNaN(until) && Date.now() > until) el.hidden = true;
  });

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
