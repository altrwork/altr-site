(function () {
  const hero = document.querySelector(".hero");
  const nav = document.querySelector(".nav");
  const heroKeyButton = document.querySelector(".hero-key-button");
  const typedHeroText = document.getElementById("typed-hero-text");
  const prefersReducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  const heroPhrase = "the way you work.";
  let heroTypingTimer = null;

  function typeHeroPhrase() {
    if (!typedHeroText) return;
    window.clearTimeout(heroTypingTimer);
    typedHeroText.textContent = "";
    typedHeroText.classList.remove("is-complete");

    let index = 0;

    function typeNextCharacter() {
      typedHeroText.textContent = heroPhrase.slice(0, index + 1);
      index += 1;

      if (index >= heroPhrase.length) {
        typedHeroText.classList.add("is-complete");
        return;
      }

      const currentCharacter = heroPhrase[index - 1];
      const nextDelay = currentCharacter === " " ? 115 : 42 + Math.round(Math.random() * 56);
      heroTypingTimer = window.setTimeout(typeNextCharacter, nextDelay);
    }

    heroTypingTimer = window.setTimeout(typeNextCharacter, 90);
  }

  function playHeroIntro() {
    if (!heroKeyButton) return;

    if (prefersReducedMotion) {
      hero?.classList.add("has-typed");
      if (typedHeroText) {
        typedHeroText.textContent = heroPhrase;
        typedHeroText.classList.add("is-complete");
      }
      return;
    }

    hero?.classList.remove("has-typed");
    heroKeyButton.classList.remove("is-pressed");
    void heroKeyButton.offsetWidth;
    heroKeyButton.classList.add("is-pressed");
    window.setTimeout(() => {
      hero?.classList.add("has-typed");
      typeHeroPhrase();
    }, 640);
  }

  function updateHeroScrollState() {
    if (!hero) return;
    const keyOnlyThreshold = Math.min(260, hero.offsetHeight * 0.32);
    const lockupIsCompact = window.scrollY > keyOnlyThreshold;
    hero.classList.toggle("is-key-only", lockupIsCompact);
    nav?.classList.toggle("has-hero-lockup", lockupIsCompact);
  }

  window.addEventListener("load", playHeroIntro);
  window.addEventListener("load", updateHeroScrollState);
  window.addEventListener("scroll", updateHeroScrollState, { passive: true });
  heroKeyButton?.addEventListener("click", playHeroIntro);
})();
