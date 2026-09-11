/* Opens and closes the nav. The nav itself is static HTML on every page, so
   crawlers and users see the same links; this only handles the toggling. */
document.querySelectorAll('.nav').forEach(nav => {
  const toggle = nav.querySelector('.nav-menu-toggle');
  const dropdowns = Array.from(nav.querySelectorAll('.nav-dropdown'));

  const setOpen = (dropdown, isOpen) => {
    dropdown.classList.toggle('is-open', isOpen);
    dropdown.querySelector('.nav-dropdown-trigger')
      .setAttribute('aria-expanded', String(isOpen));
  };
  const closeAll = except => dropdowns.forEach(d => { if (d !== except) setOpen(d, false); });

  const setMenuOpen = isOpen => {
    nav.classList.toggle('is-menu-open', isOpen);
    toggle?.setAttribute('aria-expanded', String(isOpen));
    toggle?.setAttribute('aria-label', isOpen ? 'Close navigation menu' : 'Open navigation menu');
  };

  dropdowns.forEach(d => {
    d.querySelector('.nav-dropdown-trigger')?.addEventListener('click', event => {
      event.stopPropagation();
      const willOpen = !d.classList.contains('is-open');
      closeAll(d);
      setOpen(d, willOpen);
    });
  });

  toggle?.addEventListener('click', event => {
    event.stopPropagation();
    setMenuOpen(!nav.classList.contains('is-menu-open'));
  });

  nav.querySelector('.nav-links')?.addEventListener('click', event => {
    if (event.target.closest('a')) {
      closeAll();
      setMenuOpen(false);
    }
  });

  nav.addEventListener('keydown', event => {
    if (event.key !== 'Escape') return;
    const open = dropdowns.find(d => d.classList.contains('is-open'));
    if (open) {
      setOpen(open, false);
      open.querySelector('.nav-dropdown-trigger').focus();
    } else {
      setMenuOpen(false);
    }
  });

  document.addEventListener('click', event => {
    if (!nav.contains(event.target)) {
      closeAll();
      setMenuOpen(false);
    }
  });
});
