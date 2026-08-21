(() => {
  const grid = document.getElementById('impact-grid');
  if (!grid) return;

  const cards = Array.from(grid.querySelectorAll('.impact-card'));
  const realEstateSection = document.querySelector('.real-estate-section');
  const realEstateCards = Array.from(document.querySelectorAll('.real-estate-card'));
  const searchInput = document.querySelector('.impact-search');
  const checkboxes = Array.from(document.querySelectorAll('.impact-filter-check'));
  const clearBtn = document.getElementById('impact-clear');
  const viewBtns = document.querySelectorAll('.impact-view-btn');
  const emptyMsg = document.querySelector('.tutorials-empty');
  const filterGroupToggle = document.querySelector('.tutorials-filter-group-toggle');
  const filterOptions = document.querySelector('.tutorials-filter-options');

  let activeFilters = new Set();
  let searchQuery = '';

  function applyFilters() {
    let visible = 0;
    cards.forEach(card => {
      const cat = card.dataset.category;
      const title = card.dataset.title || '';
      const desc = card.querySelector('.impact-card-desc')?.textContent.toLowerCase() || '';
      const matchesFilter = activeFilters.size === 0 || activeFilters.has(cat);
      const matchesSearch = !searchQuery || title.includes(searchQuery) || desc.includes(searchQuery);
      const show = matchesFilter && matchesSearch;
      card.classList.toggle('is-hidden', !show);
      if (show) visible++;
    });

    let visibleRealEstate = 0;
    realEstateCards.forEach(card => {
      const cat = card.dataset.category;
      const title = card.dataset.title || '';
      const desc = card.querySelector('p')?.textContent.toLowerCase() || '';
      const matchesFilter = activeFilters.size === 0 || activeFilters.has(cat);
      const matchesSearch = !searchQuery || title.includes(searchQuery) || desc.includes(searchQuery);
      const show = matchesFilter && matchesSearch;
      card.classList.toggle('is-hidden', !show);
      if (show) visibleRealEstate++;
    });

    if (realEstateSection) realEstateSection.hidden = visibleRealEstate === 0;
    visible += visibleRealEstate;
    emptyMsg.hidden = visible > 0;
    if (clearBtn) clearBtn.hidden = activeFilters.size === 0 && !searchQuery;
  }

  checkboxes.forEach(cb => {
    cb.addEventListener('change', () => {
      if (cb.checked) activeFilters.add(cb.dataset.filter);
      else activeFilters.delete(cb.dataset.filter);
      applyFilters();
    });
  });

  clearBtn?.addEventListener('click', () => {
    activeFilters.clear();
    checkboxes.forEach(cb => { cb.checked = false; });
    searchInput.value = '';
    searchQuery = '';
    applyFilters();
  });

  let debounceTimer;
  searchInput?.addEventListener('input', () => {
    clearTimeout(debounceTimer);
    debounceTimer = setTimeout(() => {
      searchQuery = searchInput.value.toLowerCase().trim();
      applyFilters();
    }, 180);
  });

  viewBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      const view = btn.dataset.view;
      viewBtns.forEach(b => {
        b.classList.toggle('is-active', b === btn);
        b.setAttribute('aria-pressed', String(b === btn));
      });
      grid.classList.toggle('is-list', view === 'list');
    });
  });

  filterGroupToggle?.addEventListener('click', () => {
    const expanded = filterGroupToggle.getAttribute('aria-expanded') === 'true';
    filterGroupToggle.setAttribute('aria-expanded', String(!expanded));
    filterOptions.hidden = expanded;
    filterGroupToggle.querySelector('svg').style.transform = expanded ? 'rotate(0deg)' : 'rotate(180deg)';
  });
})();
