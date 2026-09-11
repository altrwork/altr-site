/* Card grid filtering, search and list/grid toggle.
   One file for both the work index and the blog index: they were the same
   75 lines twice, differing only in selector prefixes. */
(() => {
  const VARIANTS = [
    { grid: 'impact-grid', card: 'impact-card', prefix: 'impact' },
    { grid: 'tutorials-grid', card: 'tutorial-card', prefix: 'tutorials' }
  ];
  const v = VARIANTS.find(x => document.getElementById(x.grid));
  if (!v) return;

  const grid = document.getElementById(v.grid);
  const cards = Array.from(grid.querySelectorAll('.' + v.card));
  const searchInput = document.querySelector('.' + v.prefix + '-search');
  const checkboxes = Array.from(document.querySelectorAll('.' + v.prefix + '-filter-check'));
  const clearBtn = document.getElementById(v.prefix + '-clear');
  const viewBtns = document.querySelectorAll('.' + v.prefix + '-view-btn');
  const emptyMsg = document.querySelector('.tutorials-empty');
  const filterGroupToggle = document.querySelector('.tutorials-filter-group-toggle');
  const filterOptions = document.querySelector('.tutorials-filter-options');

  const activeFilters = new Set();
  let searchQuery = '';

  function applyFilters() {
    let visible = 0;
    cards.forEach(card => {
      const cat = card.dataset.category;
      const title = card.dataset.title || '';
      const desc = card.querySelector('.' + v.card + '-desc')?.textContent.toLowerCase() || '';
      const matchesFilter = activeFilters.size === 0 || activeFilters.has(cat);
      const matchesSearch = !searchQuery || title.includes(searchQuery) || desc.includes(searchQuery);
      const show = matchesFilter && matchesSearch;
      card.classList.toggle('is-hidden', !show);
      if (show) visible++;
    });

    if (emptyMsg) emptyMsg.hidden = visible > 0;
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
    if (searchInput) searchInput.value = '';
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
