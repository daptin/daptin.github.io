(function () {
  document.documentElement.classList.add("js");
  const button = document.querySelector(".nav-toggle");
  const nav = document.querySelector(".desktop-nav");

  if (!button || !nav) return;

  function closeMenu() {
    button.setAttribute("aria-expanded", "false");
    nav.removeAttribute("data-open");
  }

  button.addEventListener("click", function () {
    const open = button.getAttribute("aria-expanded") === "true";
    button.setAttribute("aria-expanded", String(!open));
    if (open) nav.removeAttribute("data-open");
    else nav.setAttribute("data-open", "");
  });

  document.addEventListener("keydown", function (event) {
    if (event.key === "Escape" && nav.hasAttribute("data-open")) {
      closeMenu();
      button.focus();
    }
  });

  document.addEventListener("click", function (event) {
    if (!nav.hasAttribute("data-open")) return;
    if (nav.contains(event.target) || button.contains(event.target)) return;
    closeMenu();
  });

  window.addEventListener("resize", function () {
    if (window.matchMedia("(min-width: 901px)").matches) closeMenu();
  });
})();
