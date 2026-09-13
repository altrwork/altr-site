(() => {
  const form = document.querySelector('.lead-magnet-form[data-netlify="true"]');
  if (!form) return;

  const localHosts = new Set(['localhost', '127.0.0.1', '::1']);
  const status = document.getElementById('lead-form-status');
  const submitButton = form.querySelector('button[type="submit"]');
  const downloadPath = '/output/pdf/ai-in-real-estate-field-guide.pdf';

  const trackLead = () => {
    if (typeof window.gtag !== 'function') return;

    window.gtag('event', 'generate_lead', {
      lead_type: 'field_guide',
      form_location: 'ai_real_estate_guide',
      transport_type: 'beacon'
    });
  };

  const showFallback = () => {
    if (!status) return;

    status.replaceChildren(
      document.createTextNode("We couldn't save your email. You can still "),
      Object.assign(document.createElement('a'), {
        href: downloadPath,
        download: 'AI-in-Real-Estate-Field-Guide.pdf',
        textContent: 'download the PDF'
      }),
      document.createTextNode(', or email '),
      Object.assign(document.createElement('a'), {
        href: 'mailto:inquiries@altrwork.com?subject=AI%20in%20Real%20Estate%20field%20guide',
        textContent: 'inquiries@altrwork.com'
      }),
      document.createTextNode(' so we can follow up.')
    );
    status.hidden = false;
  };

  form.addEventListener('submit', async event => {
    event.preventDefault();
    if (!form.reportValidity()) return;

    if (localHosts.has(window.location.hostname)) {
      const destination = new URL(form.getAttribute('action'), window.location.href);
      window.location.assign(destination.href);
      return;
    }

    if (status) status.hidden = true;
    if (submitButton) {
      submitButton.disabled = true;
      submitButton.textContent = 'Sending...';
    }

    try {
      const response = await fetch('/', {
        method: 'POST',
        headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
        body: new URLSearchParams(new FormData(form)).toString()
      });

      if (!response.ok) throw new Error(`Form submission failed: ${response.status}`);

      trackLead();
      window.location.assign(form.getAttribute('action'));
    } catch (error) {
      showFallback();
      if (submitButton) {
        submitButton.disabled = false;
        submitButton.textContent = 'Try again';
      }
    }
  });
})();
