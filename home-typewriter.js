(() => {
  const statement = document.querySelector('[data-typewriter]');
  if (!statement) return;

  const prompt = document.querySelector('[data-prompt-typewriter]');
  const thinking = document.querySelector('[data-thinking]');
  const fullText = statement.textContent.trim();
  const promptText = prompt?.textContent.trim() || '';
  const reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  if (reducedMotion) return;

  if (prompt) prompt.textContent = '';
  statement.textContent = '';
  statement.classList.add('is-waiting');

  const typeText = (element, text, delayForCharacter, onComplete) => {
    let characterIndex = 0;
    element.classList.add('is-typing');

    const typeNextCharacter = () => {
      characterIndex += 1;
      element.textContent = text.slice(0, characterIndex);

      if (characterIndex >= text.length) {
        element.classList.remove('is-typing');
        onComplete?.();
        return;
      }

      window.setTimeout(typeNextCharacter, delayForCharacter(text[characterIndex - 1]));
    };

    typeNextCharacter();
  };

  const typeAnswer = () => {
    if (thinking) thinking.hidden = false;

    window.setTimeout(() => {
      if (thinking) thinking.hidden = true;
      statement.classList.remove('is-waiting');
      typeText(
        statement,
        fullText,
        character => character === '.' ? 220 : character === ',' || character === ':' ? 120 : 34
      );
    }, 1250);
  };

  const startConversation = () => {
    if (!prompt || !promptText) {
      typeAnswer();
      return;
    }

    window.setTimeout(() => {
      typeText(prompt, promptText, () => 92, () => window.setTimeout(typeAnswer, 420));
    }, 520);
  };

  if (!('IntersectionObserver' in window)) {
    startConversation();
    return;
  }

  const observer = new IntersectionObserver(entries => {
    if (!entries.some(entry => entry.isIntersecting)) return;
    observer.disconnect();
    startConversation();
  }, { threshold: 0.35 });

  observer.observe(prompt || statement);
})();
