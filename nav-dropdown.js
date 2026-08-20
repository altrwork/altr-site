// The Resources dropdown was removed in the paper redesign; the nav is now
// four flat links. Only the mobile menu toggle remains.
document.querySelectorAll('.nav').forEach(nav => {
  const navLinks = nav.querySelector('.nav-links');

  if (!navLinks) return;

  const menuToggle = document.createElement('button');
  menuToggle.className = 'nav-menu-toggle';
  menuToggle.type = 'button';
  menuToggle.setAttribute('aria-expanded', 'false');
  menuToggle.setAttribute('aria-label', 'Open navigation menu');
  menuToggle.innerHTML = '<span></span><span></span>';
  nav.insertBefore(menuToggle, navLinks);

  const setMenuOpen = isOpen => {
    nav.classList.toggle('is-menu-open', isOpen);
    menuToggle.setAttribute('aria-expanded', String(isOpen));
    menuToggle.setAttribute('aria-label', isOpen ? 'Close navigation menu' : 'Open navigation menu');
  };

  menuToggle.addEventListener('click', event => {
    event.stopPropagation();
    setMenuOpen(!nav.classList.contains('is-menu-open'));
  });

  navLinks.addEventListener('click', event => {
    if (event.target.closest('a')) setMenuOpen(false);
  });

  nav.addEventListener('keydown', event => {
    if (event.key === 'Escape' && nav.classList.contains('is-menu-open')) {
      setMenuOpen(false);
      menuToggle.focus();
    }
  });

  document.addEventListener('click', event => {
    if (!nav.contains(event.target)) setMenuOpen(false);
  });
});
