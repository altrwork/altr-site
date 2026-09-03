document.querySelectorAll('.nav').forEach(nav => {
  const navLinks = nav.querySelector('.nav-links');

  if (!navLinks) return;

  const servicesLink = Array.from(navLinks.children).find(item =>
    item.matches('a[data-nav-services]') ||
    (item.matches('a') && item.textContent.trim() === 'Services')
  );

  let servicesDropdown = null;
  let servicesTrigger = null;

  if (servicesLink) {
    servicesDropdown = document.createElement('div');
    servicesDropdown.className = 'nav-dropdown';
    servicesDropdown.innerHTML = `
      <button class="nav-dropdown-trigger" type="button" aria-expanded="false" aria-controls="services-menu">
        <span>Services</span>
        <span class="nav-dropdown-chevron" aria-hidden="true"></span>
      </button>
      <div class="nav-dropdown-panel" id="services-menu" aria-label="Who we serve">
        <span class="nav-dropdown-label">Who we serve</span>
        <a class="nav-dropdown-item" href="real-estate.html">Real Estate</a>
        <a class="nav-dropdown-item" href="law-firms.html">Law Firms</a>
        <a class="nav-dropdown-item" href="nonprofits.html">Non-profits</a>
        <a class="nav-dropdown-item" href="ecommerce.html">Ecommerce</a>
        <span class="nav-dropdown-label">How we work</span>
        <a class="nav-dropdown-item" href="ai-workshop.html">Claude Workshops</a>
        <a class="nav-dropdown-item" href="ai-enablement-workshop.html">Team Workshops</a>
      </div>
    `;

    servicesTrigger = servicesDropdown.querySelector('.nav-dropdown-trigger');
    if (servicesLink.getAttribute('aria-current') === 'page') {
      servicesTrigger.setAttribute('aria-current', 'page');
    }
    servicesLink.replaceWith(servicesDropdown);
  }

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

  const setServicesOpen = isOpen => {
    if (!servicesDropdown || !servicesTrigger) return;
    servicesDropdown.classList.toggle('is-open', isOpen);
    servicesTrigger.setAttribute('aria-expanded', String(isOpen));
  };

  servicesTrigger?.addEventListener('click', event => {
    event.stopPropagation();
    setServicesOpen(!servicesDropdown.classList.contains('is-open'));
  });

  menuToggle.addEventListener('click', event => {
    event.stopPropagation();
    setMenuOpen(!nav.classList.contains('is-menu-open'));
  });

  navLinks.addEventListener('click', event => {
    if (event.target.closest('a')) {
      setServicesOpen(false);
      setMenuOpen(false);
    }
  });

  nav.addEventListener('keydown', event => {
    if (event.key === 'Escape') {
      if (servicesDropdown?.classList.contains('is-open')) {
        setServicesOpen(false);
        servicesTrigger.focus();
      } else if (nav.classList.contains('is-menu-open')) {
        setMenuOpen(false);
        menuToggle.focus();
      }
    }
  });

  document.addEventListener('click', event => {
    if (!servicesDropdown?.contains(event.target)) setServicesOpen(false);
    if (!nav.contains(event.target)) setMenuOpen(false);
  });
});
