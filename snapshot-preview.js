/* Standalone exported HTML only. Do NOT enqueue in WordPress:
   the plugin already owns carousel initialization there. */
jQuery(function ($) {
  $('.owl-carousel').each(function () {
    const root = this;
    const items = Array.from(root.querySelectorAll('.owl-stage > .owl-item:not(.cloned)'));
    if (!items.length) return;
    const cards = items.map(item => item.firstElementChild).filter(Boolean);
    root.replaceChildren(...cards);
    root.classList.remove('owl-loaded', 'owl-drag', 'owl-hidden', 'owl-refresh');
    let conf = {};
    try { conf = JSON.parse(root.getAttribute('data-conf') || '{}'); } catch (_) {}
    $(root).owlCarousel({
      items: Number(conf.slide_show) || 4,
      loop: conf.loop ?? true,
      nav: conf.arrows ?? true,
      dots: conf.dots ?? true,
      autoplay: false,
      smartSpeed: Number(conf.speed) || 300,
      responsive: {0: {items: 1}, 600: {items: 2}, 1000: {items: Number(conf.slide_show) || 4}}
    });
  });
});
