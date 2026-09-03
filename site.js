const navToggle = document.querySelector('[data-nav-toggle]');
const navLinks = document.querySelector('[data-nav-links]');

if (navToggle && navLinks) {
  navToggle.addEventListener('click', () => {
    const open = navLinks.classList.toggle('open');
    navToggle.setAttribute('aria-expanded', String(open));
  });
  navLinks.querySelectorAll('a').forEach((link) => link.addEventListener('click', () => {
    navLinks.classList.remove('open');
    navToggle.setAttribute('aria-expanded', 'false');
  }));
}

const productMenus = [...document.querySelectorAll('.nav-menu')];
productMenus.forEach((menu) => {
  menu.addEventListener('toggle', () => {
    if (!menu.open) return;
    productMenus.forEach((other) => {
      if (other !== menu) other.open = false;
    });
  });
});

document.addEventListener('click', (event) => {
  productMenus.forEach((menu) => {
    if (menu.open && !menu.contains(event.target)) menu.open = false;
  });
});

document.addEventListener('keydown', (event) => {
  if (event.key !== 'Escape') return;
  productMenus.forEach((menu) => { menu.open = false; });
  if (navLinks?.classList.contains('open')) {
    navLinks.classList.remove('open');
    navToggle?.setAttribute('aria-expanded', 'false');
    navToggle?.focus();
  }
});

const storyTabs = [...document.querySelectorAll('[data-story-tab]')];
storyTabs.forEach((tab, index) => {
  const name = tab.dataset.storyTab;
  const panel = document.querySelector(`[data-story-panel="${name}"]`);
  tab.id = `story-tab-${name}`;
  tab.setAttribute('aria-controls', `story-panel-${name}`);
  tab.tabIndex = index === 0 ? 0 : -1;
  if (panel) {
    panel.id = `story-panel-${name}`;
    panel.setAttribute('aria-labelledby', tab.id);
  }
  tab.addEventListener('click', () => {
    storyTabs.forEach((item) => {
      item.setAttribute('aria-selected', String(item === tab));
      item.tabIndex = item === tab ? 0 : -1;
    });
    document.querySelectorAll('[data-story-panel]').forEach((storyPanel) => storyPanel.classList.toggle('active', storyPanel.dataset.storyPanel === name));
  });
  tab.addEventListener('keydown', (event) => {
    if (!['ArrowLeft', 'ArrowRight', 'Home', 'End'].includes(event.key)) return;
    event.preventDefault();
    const nextIndex = event.key === 'Home' ? 0 : event.key === 'End' ? storyTabs.length - 1 : (index + (event.key === 'ArrowRight' ? 1 : -1) + storyTabs.length) % storyTabs.length;
    storyTabs[nextIndex].focus();
    storyTabs[nextIndex].click();
  });
});

const capabilitySearch = document.querySelector('[data-capability-search]');
if (capabilitySearch) {
  capabilitySearch.addEventListener('input', () => {
    const query = capabilitySearch.value.trim().toLowerCase();
    document.querySelectorAll('[data-capability-item]').forEach((item) => {
      item.hidden = query.length > 0 && !item.textContent.toLowerCase().includes(query);
    });
    document.querySelectorAll('[data-capability-group]').forEach((group) => {
      const visible = [...group.querySelectorAll('[data-capability-item]')].some((item) => !item.hidden);
      group.hidden = !visible;
    });
    const empty = document.querySelector('[data-capability-empty]');
    if (empty) empty.hidden = [...document.querySelectorAll('[data-capability-item]')].some((item) => !item.hidden);
  });
}
