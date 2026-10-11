(function () {
  /* JO SMILE · Propuesta D · patrón IIFE (sin módulos), cada init protegido con safe() */
  "use strict";

  var BRAND = window.__BRAND__ || { whatsapp: "" };
  var reducir = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  function safe(fn, nombre) {
    try { fn(); } catch (e) { if (window.console) console.warn("[" + nombre + "]", e); }
  }

  /* WhatsApp: todos los enlaces con data-wa usan el número de manifest.js */
  function initWhatsApp() {
    document.querySelectorAll("[data-wa]").forEach(function (a) {
      a.href = "https://wa.me/" + (BRAND.whatsapp || "") + "?text=" + encodeURIComponent(a.getAttribute("data-wa"));
    });
  }

  /* Aparición al hacer scroll: umbral bajo + red de seguridad a los 6 s */
  function initReveals() {
    var els = document.querySelectorAll("[data-reveal]");
    if (!("IntersectionObserver" in window)) {
      els.forEach(function (el) { el.classList.add("is-revealed"); });
      return;
    }
    // Escalonar elementos hermanos dentro de una misma rejilla
    els.forEach(function (el) {
      var hermanos = el.parentElement ? el.parentElement.querySelectorAll(":scope > [data-reveal]") : [];
      if (hermanos.length > 1) {
        var i = Array.prototype.indexOf.call(hermanos, el);
        el.style.setProperty("--retraso", (i % 3) * 0.09 + "s");
      }
    });
    var io = new IntersectionObserver(function (entradas) {
      entradas.forEach(function (e) {
        if (e.isIntersecting) { e.target.classList.add("is-revealed"); io.unobserve(e.target); }
      });
    }, { threshold: 0.01, rootMargin: "0px 0px -2% 0px" });
    els.forEach(function (el) { io.observe(el); });
    setTimeout(function () {
      document.querySelectorAll("[data-reveal]:not(.is-revealed)").forEach(function (el) {
        if (el.getBoundingClientRect().top < window.innerHeight) el.classList.add("is-revealed");
      });
    }, 6000);
  }

  /* Botones magnéticos (catálogo 1.2): solo con mouse y sin movimiento reducido */
  function initMagnetic() {
    if (reducir || !window.matchMedia("(hover: hover) and (pointer: fine)").matches) return;
    document.querySelectorAll("[data-magnetic]").forEach(function (el) {
      if (el.querySelector(".magnetic-inner")) return; // idempotente
      var fuerza = parseFloat(el.getAttribute("data-magnetic-strength") || "0.2");
      var inner = document.createElement("span");
      inner.className = "magnetic-inner";
      while (el.firstChild) inner.appendChild(el.firstChild);
      el.appendChild(inner);
      el.classList.add("has-magnetic");
      var tx = 0, ty = 0, cx = 0, cy = 0, raf = null;
      function loop() {
        cx += (tx - cx) * 0.2; cy += (ty - cy) * 0.2;
        inner.style.transform = "translate3d(" + cx + "px," + cy + "px,0)";
        raf = (Math.abs(tx - cx) > 0.1 || Math.abs(ty - cy) > 0.1) ? requestAnimationFrame(loop) : null;
      }
      el.addEventListener("mousemove", function (e) {
        var r = el.getBoundingClientRect();
        tx = (e.clientX - r.left - r.width / 2) * fuerza;
        ty = (e.clientY - r.top - r.height / 2) * fuerza;
        if (!raf) raf = requestAnimationFrame(loop);
      });
      el.addEventListener("mouseleave", function () { tx = 0; ty = 0; if (!raf) raf = requestAnimationFrame(loop); });
    });
  }

  /* Subrayado que se desliza entre los enlaces del menú y marca la sección visible */
  function initNav() {
    var centro = document.querySelector(".nav-centro");
    var ind = document.querySelector(".nav-indicador");
    if (!centro || !ind) return;
    var enlaces = Array.prototype.slice.call(centro.querySelectorAll("a"));
    var activo = null;
    function mover(a) {
      if (!a) { ind.style.opacity = "0"; return; }
      var rc = centro.getBoundingClientRect(), ra = a.getBoundingClientRect();
      ind.style.width = (ra.width - 28) + "px";
      ind.style.transform = "translateX(" + (ra.left - rc.left + 14) + "px)";
      ind.style.opacity = "1";
    }
    enlaces.forEach(function (a) {
      a.addEventListener("mouseenter", function () { mover(a); });
      a.addEventListener("focus", function () { mover(a); });
    });
    centro.addEventListener("mouseleave", function () { mover(activo); });
    if (!("IntersectionObserver" in window)) return;
    var io = new IntersectionObserver(function (entradas) {
      entradas.forEach(function (e) {
        if (!e.isIntersecting) return;
        enlaces.forEach(function (a) {
          var es = a.getAttribute("href") === "#" + e.target.id;
          a.classList.toggle("activo", es);
          if (es) activo = a;
        });
        mover(activo);
      });
    }, { rootMargin: "-45% 0px -50% 0px" });
    enlaces.forEach(function (a) {
      var s = document.querySelector(a.getAttribute("href"));
      if (s) io.observe(s);
    });
    window.addEventListener("resize", function () { mover(activo); });
  }

  /* Barra de WhatsApp en celular: se esconde mientras se ve el botón principal */
  function initBarra() {
    var barra = document.querySelector(".barra-movil");
    var cta = document.querySelector("[data-cta-principal]");
    if (!barra || !cta || !("IntersectionObserver" in window)) return;
    new IntersectionObserver(function (e) { barra.classList.toggle("oculta", e[0].isIntersecting); }).observe(cta);
  }

  function initAnio() {
    var a = document.getElementById("anio");
    if (a) a.textContent = new Date().getFullYear();
  }

  safe(initWhatsApp, "whatsapp");
  safe(initReveals, "reveals");
  safe(initMagnetic, "magnetic");
  safe(initNav, "nav");
  safe(initBarra, "barra");
  safe(initAnio, "anio");
})();
