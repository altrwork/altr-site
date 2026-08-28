(() => {
  const form = document.querySelector('.lead-magnet-form[data-netlify="true"]');
  if (!form) return;

  const localHosts = new Set(['localhost', '127.0.0.1', '::1']);
  if (!localHosts.has(window.location.hostname)) return;

  form.addEventListener('submit', event => {
    event.preventDefault();
    const destination = new URL(form.getAttribute('action'), window.location.href);
    window.location.assign(destination.href);
  });
})();
