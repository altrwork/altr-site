/* Plate & Press behaviour: reveal-on-view, the nav, its dropdowns and the
   phone menu sheet. Pages render complete without this file; the dropdowns
   are <details> and open on their own. */
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

  /* -- which button sent someone to book: page + label in GA ------- */
  document.addEventListener('click', event => {
    const link = event.target.closest('a[href*="start-a-conversation"]');
    if (link && typeof window.gtag === 'function') {
      window.gtag('event', 'cta_click', { link_text: link.textContent.trim(), cta_page: location.pathname, transport_type: 'beacon' });
    }
  });

  /* -- nav: tint once scrolled, hide on the way down ---------------- */
  const nav = document.querySelector('.nav');
  if (!nav) return;
  let lastY = 0;
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
  // first read waits a frame: reading scrollY now, right after the headline
  // and menu writes, would force a synchronous layout
  window.requestAnimationFrame(() => {
    lastY = window.scrollY;
    onScroll();
  });

  /* -- dropdowns: one open at a time; outside click or Escape shuts -- */
  const drops = [...nav.querySelectorAll('.pp-dd')];
  drops.forEach(dd => dd.addEventListener('toggle', () => {
    if (dd.open) drops.forEach(other => { if (other !== dd) other.open = false; });
  }));
  document.addEventListener('click', event => {
    if (!event.target.closest('.pp-dd')) drops.forEach(dd => { dd.open = false; });
  });

  /* -- menu sheet (900px and under) --------------------------------- */
  const button = nav.querySelector('.pp-menu-btn');
  const menu = document.getElementById('pp-menu');
  if (!button || !menu) return;
  const label = button.querySelector('span');
  const narrow = window.matchMedia('(max-width: 900px)');

  const focusables = () => [...menu.querySelectorAll('summary, a')].filter(el => el.offsetParent);

  const setOpen = open => {
    root.classList.toggle('pp-menu-open', open);
    button.setAttribute('aria-expanded', String(open));
    if (label) label.textContent = open ? 'Close' : 'Menu';
    menu.inert = narrow.matches && !open;
    document.body.style.overflow = open ? 'hidden' : '';
    nav.classList.remove('is-hidden');
    if (open) window.setTimeout(() => focusables()[0]?.focus({ preventScroll: true }), 60);
  };

  setOpen(false);
  const onNarrowChange = () => setOpen(false);
  if (narrow.addEventListener) narrow.addEventListener('change', onNarrowChange);
  else narrow.addListener(onNarrowChange); // Safari 13 and older
  button.addEventListener('click', () => setOpen(!root.classList.contains('pp-menu-open')));
  menu.addEventListener('click', event => {
    if (event.target.closest('a')) setOpen(false);
  });

  document.addEventListener('keydown', event => {
    if (event.key === 'Escape') {
      const openDrop = drops.find(dd => dd.open);
      if (openDrop && !narrow.matches) {
        openDrop.open = false;
        openDrop.querySelector('summary').focus();
        return;
      }
    }
    if (!root.classList.contains('pp-menu-open')) return;
    if (event.key === 'Escape') {
      setOpen(false);
      button.focus();
      return;
    }
    if (event.key !== 'Tab') return;
    // keep focus inside the sheet and its toggle while it is open
    // the button sits after the sheet in the header, so it closes the loop
    const items = [...focusables(), button];
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
