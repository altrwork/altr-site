(function () {
  const serviceDetails = {
    enablement: {
      kicker: "AI Enablement",
      title: "Workshops that turn AI from a loose idea into a team habit.",
      body: [
        "Enablement starts with the work your team already handles every week. We look at the documents, messages, decisions, handoffs, and review steps that slow people down, then build demos around those real patterns.",
        "The workshop gives people a practical way to use AI without guessing. We show where it helps, where it should stay out of the way, and how to review the output with the same judgment your team already uses.",
        "Teams leave with examples they can reuse, clearer rules for when to use AI, and a short list of workflows that are ready for deeper automation."
      ],
      action: "Book enablement"
    },
    automation: {
      kicker: "AI Automation",
      title: "Automations and agents built around how your team actually operates.",
      body: [
        "Automation takes the best opportunities from discovery or enablement and turns them into working systems. That can mean a workflow automation, a custom agent, a coding-agent setup, reporting flow, or a review process that helps the team move faster without losing control.",
        "We design around the tools, permissions, data, and approval paths already inside the business. The goal is to make the system useful in daily work, not impressive in a demo and awkward everywhere else.",
        "A good automation gives the team a repeatable way to get work done with less manual drag. People still own the decisions, while the system handles context gathering, drafting, routing, review support, and other steps that should not require constant human effort."
      ],
      action: "Book automation"
    }
  };

  let lastFocusedElement = null;

  function buildModal() {
    const modal = document.createElement("div");
    modal.className = "service-detail-modal";
    modal.id = "service-detail-modal";
    modal.setAttribute("aria-hidden", "true");
    modal.innerHTML = `
      <div class="service-detail-backdrop" data-service-detail-close></div>
      <div class="service-detail-dialog" role="dialog" aria-modal="true" aria-labelledby="service-detail-title">
        <button class="service-detail-close" type="button" aria-label="Close service details" data-service-detail-close>&times;</button>
        <div class="section-kicker" id="service-detail-kicker"></div>
        <h2 id="service-detail-title"></h2>
        <div class="service-detail-body" id="service-detail-body"></div>
        <a class="button primary service-detail-book" href="start-a-conversation.html"></a>
      </div>
    `;
    document.body.appendChild(modal);
    return modal;
  }

  function getModal() {
    return document.getElementById("service-detail-modal") || buildModal();
  }

  function openDetailModal(serviceKey) {
    const detail = serviceDetails[serviceKey];
    if (!detail) return;

    const modal = getModal();
    lastFocusedElement = document.activeElement;
    document.getElementById("service-detail-kicker").textContent = detail.kicker;
    document.getElementById("service-detail-title").textContent = detail.title;
    const detailBody = document.getElementById("service-detail-body");
    detailBody.replaceChildren();
    detail.body.forEach((paragraph) => {
      const element = document.createElement("p");
      element.textContent = paragraph;
      detailBody.appendChild(element);
    });
    document.querySelector(".service-detail-book").textContent = detail.action;

    modal.classList.add("is-open");
    modal.setAttribute("aria-hidden", "false");
    document.body.classList.add("service-detail-modal-open");
    window.setTimeout(() => {
      document.querySelector(".service-detail-close")?.focus();
    }, 0);
  }

  function closeDetailModal() {
    const modal = getModal();
    modal.classList.remove("is-open");
    modal.setAttribute("aria-hidden", "true");
    document.body.classList.remove("service-detail-modal-open");
    if (lastFocusedElement && typeof lastFocusedElement.focus === "function") {
      lastFocusedElement.focus();
    }
  }

  document.addEventListener("click", (event) => {
    const bookLink = event.target.closest(".service-detail-book");
    if (bookLink) {
      closeDetailModal();
      return;
    }

    if (event.target.closest("[data-service-detail-close]")) {
      closeDetailModal();
      return;
    }

    if (event.target.closest("a")) return;

    const serviceCard = event.target.closest("[data-service-detail]");
    if (!serviceCard) return;

    openDetailModal(serviceCard.dataset.serviceDetail);
  });

  document.addEventListener("keydown", (event) => {
    // links nested inside the card keep their own Enter behavior, same as the click path
    if (event.target.closest?.("a")) return;

    const serviceCard = event.target.closest?.("[data-service-detail]");
    if (serviceCard && (event.key === "Enter" || event.key === " ")) {
      event.preventDefault();
      openDetailModal(serviceCard.dataset.serviceDetail);
      return;
    }

    const modal = document.getElementById("service-detail-modal");
    if (event.key === "Escape" && modal?.classList.contains("is-open")) {
      closeDetailModal();
    }
  });
})();
