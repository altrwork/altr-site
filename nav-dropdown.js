document.querySelectorAll('.nav-dropdown').forEach(dropdown => {
  const trigger = dropdown.querySelector('.nav-dropdown-trigger');

  trigger.addEventListener('click', e => {
    e.stopPropagation();
    const isOpen = dropdown.classList.contains('is-open');
    document.querySelectorAll('.nav-dropdown.is-open').forEach(d => d.classList.remove('is-open'));
    if (!isOpen) {
      dropdown.classList.add('is-open');
      trigger.setAttribute('aria-expanded', 'true');
    } else {
      trigger.setAttribute('aria-expanded', 'false');
    }
  });

  dropdown.addEventListener('keydown', e => {
    if (e.key === 'Escape') {
      dropdown.classList.remove('is-open');
      trigger.setAttribute('aria-expanded', 'false');
      trigger.focus();
    }
  });
});

document.addEventListener('click', () => {
  document.querySelectorAll('.nav-dropdown.is-open').forEach(d => {
    d.classList.remove('is-open');
    d.querySelector('.nav-dropdown-trigger').setAttribute('aria-expanded', 'false');
  });
});
