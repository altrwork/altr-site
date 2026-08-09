import { animate } from "https://cdn.jsdelivr.net/npm/motion@13.0.0/+esm";

const graphics = document.querySelectorAll(".ai-gap-graphic");

graphics.forEach((graphic) => {
  const reducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  if (!reducedMotion) {
    const axes = graphic.querySelector('[data-motion="axes"]');
    const today = graphic.querySelector('[data-motion="today"]');
    const adoption = graphic.querySelector('[data-motion="adoption"]');
    const capability = graphic.querySelector('[data-motion="capability"]');
    const gap = graphic.querySelector('[data-motion="gap"]');
    const years = graphic.querySelector('[data-motion="years"]');
    const adoptionLabel = graphic.querySelector('[data-motion="adoption-label"]');
    const modelLabel = graphic.querySelector('[data-motion="model-label"]');
    const callout = graphic.querySelector('[data-motion="callout"]');
    let hasPlayed = false;

    graphic.classList.add("is-motion-ready");

    const play = () => {
      if (hasPlayed) return;
      hasPlayed = true;

      animate([
        [axes, { opacity: [0, 1] }, { duration: 0.45, ease: "easeOut" }],
        [today, { opacity: [0, 1] }, { at: 0.2, duration: 0.4, ease: "easeOut" }],
        [years, { opacity: [0, 1] }, { at: 0.2, duration: 0.4, ease: "easeOut" }],
        [adoption, { opacity: [0, 1] }, { at: 0.5, duration: 0.08, ease: "linear" }],
        [adoption, { pathLength: [0, 1] }, { at: 0.5, duration: 2.15, ease: "linear" }],
        [adoptionLabel, { opacity: [0, 1] }, { at: 2.65, duration: 0.42, ease: "easeOut" }],
        [capability, { opacity: [0, 1] }, { at: 2.85, duration: 0.08, ease: "linear" }],
        [capability, { pathLength: [0, 1] }, { at: 2.85, duration: 2.75, ease: "linear" }],
        [modelLabel, { opacity: [0, 1] }, { at: 5.6, duration: 0.42, ease: "easeOut" }],
        [gap, { opacity: [0, 1] }, { at: 5.78, duration: 0.82, ease: "easeOut" }],
        [callout, { opacity: [0, 1] }, { at: 6.42, duration: 0.5, ease: "easeOut" }]
      ]);
    };

    if (!("IntersectionObserver" in window)) {
      play();
    } else {
      const observer = new IntersectionObserver((entries) => {
        entries.forEach((entry) => {
          if (!entry.isIntersecting) return;
          play();
          observer.disconnect();
        });
      }, { threshold: 0.35 });

      observer.observe(graphic);
    }
  }
});
