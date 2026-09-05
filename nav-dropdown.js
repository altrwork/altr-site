document.querySelectorAll('.nav').forEach(nav => {
  const navLinks = nav.querySelector('.nav-links');

  if (!navLinks) return;

  const currentPage = window.location.pathname.split('/').pop() || 'index.html';
  const isResourcesPage = ['events.html', 'ai-workshop.html', 'tutorials.html'].includes(currentPage);

  const servicesLink = Array.from(navLinks.children).find(item =>
    item.matches('a[data-nav-services]') ||
    (item.matches('a') && item.textContent.trim() === 'Services')
  );

  let servicesDropdown = null;
  let servicesTrigger = null;
  let resourcesDropdown = null;
  let resourcesTrigger = null;

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
        <a class="nav-dropdown-item" href="real-estate.html">Commercial Real Estate</a>
        <a class="nav-dropdown-item" href="nonprofits.html">Non-profits</a>
        <a class="nav-dropdown-item" href="ecommerce.html">Ecommerce</a>
        <span class="nav-dropdown-label">How we altr work</span>
        <a class="nav-dropdown-item" href="how-we-altr-work.html">AI Strategy</a>
      </div>
    `;

    servicesTrigger = servicesDropdown.querySelector('.nav-dropdown-trigger');
    if (!isResourcesPage && servicesLink.getAttribute('aria-current') === 'page') {
      servicesTrigger.setAttribute('aria-current', 'page');
    }
    servicesLink.replaceWith(servicesDropdown);
  }

  const portfolioLink = Array.from(navLinks.children).find(item =>
    item.matches('a[href="impact-studies.html"]')
  );
  const blogLink = Array.from(navLinks.children).find(item =>
    item.matches('a[href="tutorials.html"]')
  );
  let eventsLink = Array.from(navLinks.children).find(item =>
    item.matches('a[data-nav-events]')
  );

  if (portfolioLink) portfolioLink.textContent = 'Work';

  if (!eventsLink) {
    eventsLink = document.createElement('a');
    eventsLink.dataset.navEvents = '';
    eventsLink.href = 'events.html';
    eventsLink.textContent = 'Events';

    if (isResourcesPage) eventsLink.setAttribute('aria-current', 'page');
  }

  if (eventsLink || blogLink) {
    resourcesDropdown = document.createElement('div');
    resourcesDropdown.className = 'nav-dropdown';
    resourcesDropdown.innerHTML = `
      <button class="nav-dropdown-trigger" type="button" aria-expanded="false" aria-controls="resources-menu">
        <span>Resources</span>
        <span class="nav-dropdown-chevron" aria-hidden="true"></span>
      </button>
      <div class="nav-dropdown-panel" id="resources-menu" aria-label="Resources">
        <span class="nav-dropdown-label">Explore</span>
        <a class="nav-dropdown-item" href="ai-workshop.html">Events</a>
        <a class="nav-dropdown-item" href="tutorials.html">Blog</a>
      </div>
    `;

    resourcesTrigger = resourcesDropdown.querySelector('.nav-dropdown-trigger');
    if (isResourcesPage) resourcesTrigger.setAttribute('aria-current', 'page');

    eventsLink?.remove();
    blogLink?.remove();
    if (portfolioLink) {
      portfolioLink.insertAdjacentElement('afterend', resourcesDropdown);
    } else if (servicesDropdown) {
      servicesDropdown.insertAdjacentElement('afterend', resourcesDropdown);
    } else {
      navLinks.prepend(resourcesDropdown);
    }
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

  const setResourcesOpen = isOpen => {
    if (!resourcesDropdown || !resourcesTrigger) return;
    resourcesDropdown.classList.toggle('is-open', isOpen);
    resourcesTrigger.setAttribute('aria-expanded', String(isOpen));
  };

  servicesTrigger?.addEventListener('click', event => {
    event.stopPropagation();
    setResourcesOpen(false);
    setServicesOpen(!servicesDropdown.classList.contains('is-open'));
  });

  resourcesTrigger?.addEventListener('click', event => {
    event.stopPropagation();
    setServicesOpen(false);
    setResourcesOpen(!resourcesDropdown.classList.contains('is-open'));
  });

  menuToggle.addEventListener('click', event => {
    event.stopPropagation();
    setMenuOpen(!nav.classList.contains('is-menu-open'));
  });

  navLinks.addEventListener('click', event => {
    if (event.target.closest('a')) {
      setServicesOpen(false);
      setResourcesOpen(false);
      setMenuOpen(false);
    }
  });

  nav.addEventListener('keydown', event => {
    if (event.key === 'Escape') {
      if (servicesDropdown?.classList.contains('is-open')) {
        setServicesOpen(false);
        servicesTrigger.focus();
      } else if (resourcesDropdown?.classList.contains('is-open')) {
        setResourcesOpen(false);
        resourcesTrigger.focus();
      } else if (nav.classList.contains('is-menu-open')) {
        setMenuOpen(false);
        menuToggle.focus();
      }
    }
  });

  document.addEventListener('click', event => {
    if (!servicesDropdown?.contains(event.target)) setServicesOpen(false);
    if (!resourcesDropdown?.contains(event.target)) setResourcesOpen(false);
    if (!nav.contains(event.target)) setMenuOpen(false);
  });
});
