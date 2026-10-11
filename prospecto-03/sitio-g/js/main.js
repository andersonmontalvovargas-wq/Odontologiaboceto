/* Boceto prospecto-03 · Propuesta G. Sin librerías.
   Todo el contenido está en el HTML. Esto agrega el menú, el estado del horario y las transiciones
   ligadas al desplazamiento. Con "reducir movimiento" no se activa ninguna transición. */
(function () {
  "use strict";

  function seguro(fn, nombre) {
    try { fn(); } catch (e) { if (window.console) console.warn("[" + nombre + "]", e); }
  }
  var reducir = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  function limitar(v) { return Math.max(0, Math.min(1, v)); }

  /* ---------- Menú móvil ---------- */
  seguro(function () {
    var global = document.querySelector(".global");
    var boton = document.querySelector(".menu-boton");
    if (!global || !boton) return;
    function poner(abierto) {
      global.classList.toggle("menu-abierto", abierto);
      boton.setAttribute("aria-expanded", String(abierto));
      boton.textContent = abierto ? "Cerrar" : "Menú";
    }
    boton.addEventListener("click", function () { poner(!global.classList.contains("menu-abierto")); });
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape" && global.classList.contains("menu-abierto")) { poner(false); boton.focus(); }
    });
  }, "menu");

  /* ---------- Abierto o cerrado ahora (hora de Bogotá) ---------- */
  seguro(function () {
    var HORARIO = { 0: [9, 20], 1: [8, 20], 2: [8, 20], 3: [8, 20], 4: [8, 20], 5: [8, 20], 6: [8, 20] };
    var DIAS = ["domingo", "lunes", "martes", "miércoles", "jueves", "viernes", "sábado"];
    var m = {};
    new Intl.DateTimeFormat("en-US", { timeZone: "America/Bogota", weekday: "short", hour: "numeric", minute: "numeric", hour12: false })
      .formatToParts(new Date()).forEach(function (p) { m[p.type] = p.value; });
    var dia = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"].indexOf(m.weekday);
    if (dia < 0) return;
    var hora = (parseInt(m.hour, 10) % 24) + parseInt(m.minute, 10) / 60;
    function formato(h) { return h === 12 ? "12:00 m." : (h > 12 ? (h - 12) + ":00 p. m." : h + ":00 a. m."); }
    var hoy = HORARIO[dia], abierto = hora >= hoy[0] && hora < hoy[1], texto;
    if (abierto) texto = "Abierto ahora · cierra a las " + formato(hoy[1]);
    else if (hora < hoy[0]) texto = "Cerrado ahora · abre hoy a las " + formato(hoy[0]);
    else { var sig = (dia + 1) % 7; texto = "Cerrado ahora · abre el " + DIAS[sig] + " a las " + formato(HORARIO[sig][0]); }
    document.querySelectorAll("[data-estado]").forEach(function (el) {
      el.querySelector("[data-estado-texto]").textContent = texto;
      el.classList.add(abierto ? "estado--abierto" : "estado--cerrado");
      el.hidden = false;
    });
    document.querySelectorAll('.horario li[data-dia="' + dia + '"]').forEach(function (li) { li.classList.add("hoy"); });
  }, "horario");

  /* ---------- Aparición al bajar ---------- */
  seguro(function () {
    var elementos = document.querySelectorAll(".aparecer, .crecer");
    function todo() { elementos.forEach(function (el) { el.classList.add("visible"); }); }
    if (reducir || !("IntersectionObserver" in window)) { todo(); return; }
    var obs = new IntersectionObserver(function (entradas) {
      entradas.forEach(function (e) { if (e.isIntersecting) { e.target.classList.add("visible"); obs.unobserve(e.target); } });
    }, { threshold: 0.01, rootMargin: "0px 0px -8% 0px" });
    elementos.forEach(function (el) { obs.observe(el); });
    setTimeout(function () {
      document.querySelectorAll(".aparecer:not(.visible), .crecer:not(.visible)").forEach(function (el) {
        if (el.getBoundingClientRect().top < window.innerHeight) el.classList.add("visible");
      });
    }, 6000);
    window.addEventListener("beforeprint", todo);
  }, "aparecer");

  if (reducir) return;

  /* ---------- Texto que se ilumina: se parte en palabras ---------- */
  var parrafos = [];
  seguro(function () {
    document.querySelectorAll("[data-luz]").forEach(function (p) {
      var palabras = p.textContent.trim().split(/\s+/);
      p.textContent = "";
      palabras.forEach(function (w, i) {
        var s = document.createElement("span");
        s.className = "palabra";
        s.textContent = w;
        p.appendChild(s);
        if (i < palabras.length - 1) p.appendChild(document.createTextNode(" "));
      });
      parrafos.push({ el: p, palabras: p.querySelectorAll(".palabra") });
    });
  }, "luz");

  /* ---------- Foto que crece y tratamientos que pasan de lado ---------- */
  var escala = document.querySelector("[data-escala]");
  var desfile = document.querySelector("[data-desfile]");
  var pista = document.querySelector("[data-desfile-pista]");
  var barra = 52; // alto de la barra secundaria fija

  function prepararDesfile() {
    if (!desfile || !pista) return;
    var activo = window.innerWidth > 860 && window.innerHeight > 560;
    desfile.classList.toggle("activo", activo);
    if (!activo) { desfile.style.removeProperty("--alto"); return; }
    pista.querySelectorAll("img").forEach(function (i) { i.loading = "eager"; });
    var recorrido = pista.scrollWidth - window.innerWidth;
    desfile.style.setProperty("--alto", (recorrido + window.innerHeight) + "px");
  }

  function actualizar() {
    var vh = window.innerHeight;
    if (escala) {
      var r = escala.getBoundingClientRect();
      var p = limitar((barra - r.top) / Math.max(r.height - vh, 1) / 0.7);
      escala.style.setProperty("--p", p.toFixed(3));
    }
    if (desfile && desfile.classList.contains("activo")) {
      var rd = desfile.getBoundingClientRect();
      var avance = limitar((barra - rd.top) / Math.max(rd.height - (vh - barra), 1));
      var recorrido = pista.scrollWidth - window.innerWidth;
      pista.style.setProperty("--x", (-avance * recorrido).toFixed(1) + "px");
      desfile.style.setProperty("--avance", avance.toFixed(3));
    }
    parrafos.forEach(function (o) {
      var rp = o.el.getBoundingClientRect();
      var f = limitar((vh * 0.85 - rp.top) / (rp.height + vh * 0.35));
      var n = Math.round(f * o.palabras.length);
      o.palabras.forEach(function (w, i) { w.classList.toggle("encendida", i < n); });
    });
  }

  seguro(function () {
    if (escala) escala.classList.add("activa");
    prepararDesfile();
    var pendiente = false;
    window.addEventListener("scroll", function () {
      if (pendiente) return;
      pendiente = true;
      requestAnimationFrame(function () { pendiente = false; seguro(actualizar, "desplazamiento"); });
    }, { passive: true });
    window.addEventListener("resize", function () { seguro(prepararDesfile, "desfile"); seguro(actualizar, "desplazamiento"); });
    window.addEventListener("load", function () { seguro(prepararDesfile, "desfile"); seguro(actualizar, "desplazamiento"); });
    actualizar();
  }, "transiciones");
})();
