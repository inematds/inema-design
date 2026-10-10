// Count a number up once, when it scrolls into view.
// Use: <span data-count="1280">0</span>
(() => {
  const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
  const ease = t => 1 - Math.pow(1 - t, 3);                      // ease-out
  const run = el => {
    const to = +el.dataset.count, ms = 900, start = performance.now();
    if (reduce) { el.textContent = to.toLocaleString(); return; }
    const tick = now => {
      const t = Math.min(1, (now - start) / ms);
      el.textContent = Math.round(to * ease(t)).toLocaleString();
      if (t < 1) requestAnimationFrame(tick);
    };
    requestAnimationFrame(tick);
  };
  const io = new IntersectionObserver(entries => entries.forEach(e => {
    if (e.isIntersecting) { run(e.target); io.unobserve(e.target); }
  }), { threshold: .4 });
  document.querySelectorAll('[data-count]').forEach(el => io.observe(el));
})();