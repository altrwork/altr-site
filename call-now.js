(function () {
  const form = document.getElementById("call-now-form");
  if (!form) return;

  const status = document.getElementById("call-now-status");
  const submit = form.querySelector('button[type="submit"]');

  function showStatus(message, ok) {
    status.textContent = message;
    status.dataset.state = ok ? "success" : "error";
  }

  form.addEventListener("submit", async (event) => {
    event.preventDefault();
    if (!form.reportValidity()) return;

    if (!["altrwork.com", "www.altrwork.com"].includes(window.location.hostname)) {
      showStatus("Call requests are available on altrwork.com. This preview will not place a call.", false);
      return;
    }

    const token = form.querySelector('[name="cf-turnstile-response"]')?.value || "";
    if (!token) {
      showStatus("Please complete the verification before requesting a call.", false);
      return;
    }

    const fields = new FormData(form);
    const payload = {
      name: String(fields.get("name") || "").trim(),
      email: String(fields.get("email") || "").trim(),
      phone: String(fields.get("phone") || "").trim(),
      company: String(fields.get("company") || "").trim(),
      notes: String(fields.get("notes") || "").trim(),
      consent: fields.get("consent") === "on",
      timeZone: Intl.DateTimeFormat().resolvedOptions().timeZone,
      turnstileToken: token
    };

    if (!payload.consent) {
      showStatus("Please agree to the recorded call before continuing.", false);
      return;
    }

    submit.disabled = true;
    showStatus("Requesting your call…", true);
    try {
      const response = await fetch("https://kara-intake.weathered-boat-4f14.workers.dev/call-now", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(payload)
      });
      const result = await response.json();
      const ok = response.ok && result.ok === true;
      showStatus(typeof result.message === "string" && result.message ? result.message : "The call request could not be completed. Please try again.", ok);
      if (!ok && window.turnstile) window.turnstile.reset();
    } catch (_error) {
      showStatus("The call request could not be completed. Please try again or choose a time instead.", false);
      if (window.turnstile) window.turnstile.reset();
    } finally {
      submit.disabled = false;
    }
  });
})();
