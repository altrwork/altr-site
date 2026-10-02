(function () {
  const bookingBaseUrl = "https://cal.com/altr-ai/intro";
  const triggerSelector = 'a[href="start-a-conversation.html"]';
  let lastFocusedElement = null;

  function buildModal() {
    const modal = document.createElement("div");
    modal.className = "intake-modal";
    modal.id = "intake-modal";
    modal.setAttribute("aria-hidden", "true");
    modal.innerHTML = `
      <div class="intake-modal-backdrop" data-intake-close></div>
      <div class="intake-modal-dialog" role="dialog" aria-modal="true" aria-labelledby="intake-modal-title">
        <button class="intake-modal-close" type="button" aria-label="Close intake form" data-intake-close>&times;</button>
        <div class="intake-modal-copy">
          <div class="section-kicker">Book an intro</div>
          <h2 id="intake-modal-title">Tell us what you want to discuss.</h2>
          <p>Share the company and the workflow, agent, demo, or enablement topic. Then choose a time with Kara, or ask for a call now.</p>
        </div>
        <form class="intake-form" id="intake-modal-form">
          <label>
            <span>Company name</span>
            <input id="intake-modal-company" name="company" type="text" autocomplete="organization" placeholder="Company or team name" required />
          </label>
          <label>
            <span>What are you interested in solving?</span>
            <textarea id="intake-modal-interest" name="interest" rows="6" placeholder="Describe the workflow, agentic coding system, demo, or AI enablement need you want to discuss." required></textarea>
          </label>
          <div class="intake-actions">
            <button class="button primary" type="submit">Choose a time</button>
            <a href="start-a-conversation.html#call-now" data-call-now>Call me now</a>
          </div>
        </form>
      </div>
    `;

    document.body.appendChild(modal);
    return modal;
  }

  function getModal() {
    return document.getElementById("intake-modal") || buildModal();
  }

  function openModal() {
    const modal = getModal();
    lastFocusedElement = document.activeElement;
    modal.classList.add("is-open");
    modal.setAttribute("aria-hidden", "false");
    document.body.classList.add("intake-modal-open");
    window.setTimeout(() => {
      document.getElementById("intake-modal-company")?.focus();
    }, 0);
  }

  function closeModal() {
    const modal = getModal();
    modal.classList.remove("is-open");
    modal.setAttribute("aria-hidden", "true");
    document.body.classList.remove("intake-modal-open");
    if (lastFocusedElement && typeof lastFocusedElement.focus === "function") {
      lastFocusedElement.focus();
    }
  }

  function bookingUrl(company, interest) {
    return `${bookingBaseUrl}?company=${encodeURIComponent(company)}&notes=${encodeURIComponent(interest)}`;
  }

  function trackLeadAndNavigate(destination) {
    let navigated = false;
    const navigate = () => {
      if (navigated) return;
      navigated = true;
      window.location.assign(destination);
    };

    if (typeof window.gtag !== "function") {
      navigate();
      return;
    }

    window.gtag("event", "generate_lead", {
      lead_type: "consultation",
      form_location: "intake_modal",
      transport_type: "beacon",
      event_callback: navigate,
      event_timeout: 1200
    });
    window.setTimeout(navigate, 1400);
  }

  document.addEventListener("click", (event) => {
    const callNow = event.target.closest("[data-call-now]");
    if (callNow) {
      event.preventDefault();
      const company = document.getElementById("intake-modal-company")?.value.trim() || "";
      const interest = document.getElementById("intake-modal-interest")?.value.trim() || "";
      window.location.assign(`start-a-conversation.html?company=${encodeURIComponent(company)}&notes=${encodeURIComponent(interest)}#call-now`);
      return;
    }

    const trigger = event.target.closest(triggerSelector);
    if (trigger) {
      event.preventDefault();
      openModal();
      return;
    }

    if (event.target.closest("[data-intake-close]")) {
      closeModal();
    }
  });

  document.addEventListener("submit", (event) => {
    if (event.target.id !== "intake-modal-form") return;
    event.preventDefault();
    if (!event.target.reportValidity()) return;

    const company = document.getElementById("intake-modal-company").value.trim();
    const interest = document.getElementById("intake-modal-interest").value.trim();
    trackLeadAndNavigate(bookingUrl(company, interest));
  });

  document.addEventListener("keydown", (event) => {
    const modal = document.getElementById("intake-modal");
    if (event.key === "Escape" && modal?.classList.contains("is-open")) {
      closeModal();
    }
  });
})();
