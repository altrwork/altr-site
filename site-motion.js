(function () {
  const reducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  const revealSelectors = [
    ".hero-kicker",
    ".hero-headline span",
    ".hero-copy",
    ".hero-actions",
    ".ai-gap-card",
    ".page-hero > .section-kicker",
    ".page-hero h1",
    ".page-hero p",
    ".page-hero-actions",
    ".section-header > *",
    ".service-arm",
    ".gap-grid article",
    ".framework-step",
    ".engagement-item",
    ".text-block",
    ".impact-card",
    ".trust-panel",
    ".services-cta",
    ".content-panel",
    ".resource-item",
    ".featured-work-card",
    ".work-list-item",
    ".founder-card",
    ".about-beliefs",
    ".globe-panel",
    ".impact-detail",
    ".impact-study-copy > *",
    ".impact-article-heading",
    ".impact-article-image",
    ".impact-study-image",
    ".learning-brief",
    ".learning-feature-card",
    ".learning-tabs",
    ".intake-form",
    ".intake-note"
  ];

  function collectRevealElements() {
    const elements = new Set();
    revealSelectors.forEach((selector) => {
      document.querySelectorAll(selector).forEach((element) => elements.add(element));
    });
    return Array.from(elements);
  }

  function showImmediately(elements) {
    elements.forEach((element) => element.classList.add("is-visible"));
  }

  function setupReveal() {
    const elements = collectRevealElements();
    if (!elements.length) return;

    elements.forEach((element, index) => {
      element.classList.add("reveal-on-scroll");
      element.style.setProperty("--reveal-delay", `${(index % 4) * 70}ms`);
    });

    if (!("IntersectionObserver" in window)) {
      showImmediately(elements);
      return;
    }

    const observer = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (!entry.isIntersecting) return;
          entry.target.classList.add("is-visible");
          observer.unobserve(entry.target);
        });
      },
      {
        rootMargin: "0px 0px -8% 0px",
        threshold: 0.12
      }
    );

    requestAnimationFrame(() => {
      elements.forEach((element) => observer.observe(element));
    });
  }

  if (reducedMotion) return;

  document.body.classList.add("motion-ready");
  setupReveal();
})();
