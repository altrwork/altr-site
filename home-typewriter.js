(() => {
  const statement = document.querySelector('[data-typewriter]');
  if (!statement) return;

  const fullText = statement.textContent.trim();
  const reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  if (reducedMotion) return;

  statement.textContent = '';
  statement.classList.add('is-typing');

  const typeStatement = () => {
    let characterIndex = 0;

    const typeNextCharacter = () => {
      characterIndex += 1;
      statement.textContent = fullText.slice(0, characterIndex);

      if (characterIndex >= fullText.length) {
        statement.classList.remove('is-typing');
        return;
      }

      const character = fullText[characterIndex - 1];
      const delay = character === '.' ? 280 : character === ',' ? 150 : 42;
      window.setTimeout(typeNextCharacter, delay);
    };

    typeNextCharacter();
  };

  if (!('IntersectionObserver' in window)) {
    typeStatement();
    return;
  }

  const observer = new IntersectionObserver(entries => {
    if (!entries.some(entry => entry.isIntersecting)) return;
    observer.disconnect();
    typeStatement();
  }, { threshold: 0.35 });

  observer.observe(statement);
})();
