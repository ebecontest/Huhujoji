/* Empayar Batik Exclusive — site behaviour (no dependencies) */
(function () {
  'use strict';
  var doc = document;
  var $ = function (s, c) { return (c || doc).querySelector(s); };
  var $$ = function (s, c) { return Array.prototype.slice.call((c || doc).querySelectorAll(s)); };

  /* ----- Header state + scroll progress ----- */
  var header = $('.header');
  var bar = $('.progress');
  function onScroll() {
    var y = window.pageYOffset || doc.documentElement.scrollTop;
    if (header) header.classList.toggle('scrolled', y > 8);
    if (bar) {
      var h = doc.documentElement.scrollHeight - window.innerHeight;
      bar.style.width = (h > 0 ? (y / h) * 100 : 0) + '%';
    }
  }
  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();

  /* ----- Mobile drawer ----- */
  var burger = $('.burger');
  var drawer = $('.drawer');
  function setMenu(open) {
    if (!burger || !drawer) return;
    burger.setAttribute('aria-expanded', open ? 'true' : 'false');
    burger.setAttribute('aria-label', open ? 'Close menu' : 'Open menu');
    drawer.classList.toggle('open', open);
    doc.body.classList.toggle('menu-open', open);
  }
  if (burger) {
    burger.addEventListener('click', function () { setMenu(burger.getAttribute('aria-expanded') !== 'true'); });
    $$('a', drawer).forEach(function (a) { a.addEventListener('click', function () { setMenu(false); }); });
    window.addEventListener('resize', function () { if (window.innerWidth > 1100) setMenu(false); });
  }

  /* ----- Broken image fallback (keeps layout elegant if a photo fails) ----- */
  function markBroken(img) {
    var host = img.closest('a, .ph, .ph-img, figure') || img.parentNode;
    if (host) host.classList.add('is-broken');
  }
  $$('img[data-fb]').forEach(function (img) {
    if (img.complete && img.naturalWidth === 0) markBroken(img);
    img.addEventListener('error', function () { markBroken(img); });
  });
  // Logo: fall back to a typographic wordmark
  var logo = $('.brand img');
  if (logo) {
    var noLogo = function () { logo.parentNode.classList.add('no-logo'); };
    if (logo.complete && logo.naturalWidth === 0) noLogo();
    logo.addEventListener('error', noLogo);
  }

  /* ----- Reveal on scroll ----- */
  var reveals = $$('.reveal');
  if ('IntersectionObserver' in window && reveals.length) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); }
      });
    }, { rootMargin: '0px 0px -8% 0px', threshold: 0.06 });
    reveals.forEach(function (el) { io.observe(el); });
  } else {
    reveals.forEach(function (el) { el.classList.add('in'); });
  }

  /* ----- Hero slideshow ----- */
  var slides = $$('.hero-slides img');
  var dots = $$('.hero-dots button');
  if (slides.length > 1) {
    var cur = 0, timer = null;
    var show = function (i) {
      slides[cur].classList.remove('active');
      if (dots[cur]) dots[cur].classList.remove('active');
      cur = (i + slides.length) % slides.length;
      slides[cur].classList.add('active');
      if (dots[cur]) { void dots[cur].offsetWidth; dots[cur].classList.add('active'); }
    };
    var start = function () { stop(); timer = setInterval(function () { show(cur + 1); }, 5800); };
    var stop = function () { if (timer) clearInterval(timer); };
    dots.forEach(function (d, i) { d.addEventListener('click', function () { show(i); start(); }); });
    if (!window.matchMedia('(prefers-reduced-motion: reduce)').matches) start();
    doc.addEventListener('visibilitychange', function () { if (doc.hidden) stop(); else start(); });
  }

  /* ----- Lightbox ----- */
  var items = $$('a[data-lb]');
  if (items.length) {
    var lb = doc.createElement('div');
    lb.className = 'lb';
    lb.setAttribute('role', 'dialog');
    lb.setAttribute('aria-modal', 'true');
    lb.setAttribute('aria-label', 'Image viewer');
    lb.innerHTML =
      '<button class="x" aria-label="Close"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M5 5l14 14M19 5L5 19"/></svg></button>' +
      '<button class="prev" aria-label="Previous"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M15 5l-7 7 7 7"/></svg></button>' +
      '<figure><img alt=""><figcaption></figcaption></figure>' +
      '<button class="next" aria-label="Next"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M9 5l7 7-7 7"/></svg></button>';
    doc.body.appendChild(lb);
    var lbImg = $('img', lb), lbCap = $('figcaption', lb);
    var group = [], idx = 0, lastFocus = null;

    var render = function () {
      var a = group[idx];
      var im = $('img', a);
      lbImg.src = a.getAttribute('href');
      lbImg.alt = im ? im.alt : '';
      lbCap.textContent = (im ? im.alt : '') + (group.length > 1 ? '   ·   ' + (idx + 1) + ' / ' + group.length : '');
      var multi = group.length > 1;
      $('.prev', lb).style.display = multi ? '' : 'none';
      $('.next', lb).style.display = multi ? '' : 'none';
    };
    var open = function (a) {
      var g = a.getAttribute('data-lb');
      group = items.filter(function (x) { return x.getAttribute('data-lb') === g; });
      idx = group.indexOf(a);
      lastFocus = doc.activeElement;
      render();
      lb.classList.add('open');
      doc.body.classList.add('lb-open');
      $('.x', lb).focus();
    };
    var close = function () {
      lb.classList.remove('open');
      doc.body.classList.remove('lb-open');
      lbImg.removeAttribute('src');
      if (lastFocus) lastFocus.focus();
    };
    var step = function (d) { idx = (idx + d + group.length) % group.length; render(); };

    items.forEach(function (a) {
      a.addEventListener('click', function (e) { e.preventDefault(); open(a); });
    });
    $('.x', lb).addEventListener('click', close);
    $('.prev', lb).addEventListener('click', function () { step(-1); });
    $('.next', lb).addEventListener('click', function () { step(1); });
    lb.addEventListener('click', function (e) { if (e.target === lb) close(); });
    doc.addEventListener('keydown', function (e) {
      if (!lb.classList.contains('open')) return;
      if (e.key === 'Escape') close();
      else if (e.key === 'ArrowLeft' && group.length > 1) step(-1);
      else if (e.key === 'ArrowRight' && group.length > 1) step(1);
    });
    var tx = null;
    lb.addEventListener('touchstart', function (e) { tx = e.touches[0].clientX; }, { passive: true });
    lb.addEventListener('touchend', function (e) {
      if (tx === null || group.length < 2) return;
      var dx = e.changedTouches[0].clientX - tx;
      if (Math.abs(dx) > 50) step(dx < 0 ? 1 : -1);
      tx = null;
    });
  }

  /* ----- WhatsApp enquiry form (contact page) ----- */
  var form = $('#enquiry');
  if (form) {
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var v = function (n) { return (form.elements[n] && form.elements[n].value || '').trim(); };
      var target = v('branch') || '601156774731';
      var lines = [
        'Hello Empayar Batik Exclusive,',
        '',
        'Name: ' + v('name'),
        'Interested in: ' + v('collection'),
        v('message') ? 'Message: ' + v('message') : ''
      ].filter(function (l, i) { return l !== '' || i === 1; });
      window.open('https://wa.me/' + target + '?text=' + encodeURIComponent(lines.join('\n')), '_blank', 'noopener');
    });
  }
})();
