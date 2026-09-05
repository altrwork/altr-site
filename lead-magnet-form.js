(() => {
  const form = document.querySelector('.lead-magnet-form[data-netlify="true"]');
  if (!form) return;

  const localHosts = new Set(['localhost', '127.0.0.1', '::1']);
  form.addEventListener('submit', event => {
    if (!form.reportValidity()) return;

    if (typeof window.gtag === 'function') {
      window.gtag('event', 'generate_lead', {
        lead_type: 'field_guide',
        form_location: 'ai_real_estate_guide',
        transport_type: 'beacon'
      });
    }

    if (localHosts.has(window.location.hostname)) {
      event.preventDefault();
      const destination = new URL(form.getAttribute('action'), window.location.href);
      window.location.assign(destination.href);
    }
  });
})();
