/* Boceto prospecto-03 · Propuesta H. Sin librerías.
   Todo el contenido está en el HTML: esto agrega el menú, la hora de Bucaramanga con el estado del
   horario y la aparición de los bloques. Con "reducir movimiento" todo aparece quieto. */
(function () {
  "use strict";

  function seguro(fn, nombre) {
    try { fn(); } catch (e) { if (window.console) console.warn("[" + nombre + "]", e); }
  }
  var reducir = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  /* ---------- Menú móvil ---------- */
  seguro(function () {
    var encabezado = document.querySelector(".encabezado");
    var boton = document.querySelector(".menu-boton");
    if (!encabezado || !boton) return;
    function poner(abierto) {
      encabezado.classList.toggle("menu-abierto", abierto);
      boton.setAttribute("aria-expanded", String(abierto));
      boton.textContent = abierto ? "Cerrar" : "Menú";
    }
    boton.addEventListener("click", function () { poner(!encabezado.classList.contains("menu-abierto")); });
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape" && encabezado.classList.contains("menu-abierto")) { poner(false); boton.focus(); }
    });
  }, "menu");

  /* ---------- Hora de Bucaramanga y estado del horario ----------
     Horario del perfil de Google: lunes a sábado 8:00–20:00, domingo 9:00–20:00. Se actualiza cada 30 s. */
  var HORARIO = { 0: [9, 20], 1: [8, 20], 2: [8, 20], 3: [8, 20], 4: [8, 20], 5: [8, 20], 6: [8, 20] };
  var DIAS = ["domingo", "lunes", "martes", "miércoles", "jueves", "viernes", "sábado"];
  function formato(h) { return h === 12 ? "12:00 m." : (h > 12 ? (h - 12) + ":00 p. m." : h + ":00 a. m."); }
  function reloj() {
    var m = {};
    new Intl.DateTimeFormat("en-US", { timeZone: "America/Bogota", weekday: "short", hour: "numeric", minute: "2-digit", hour12: false })
      .formatToParts(new Date()).forEach(function (p) { m[p.type] = p.value; });
    var dia = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"].indexOf(m.weekday);
    if (dia < 0) return;
    var h = parseInt(m.hour, 10) % 24, min = m.minute;
    var hora = h + parseInt(min, 10) / 60;
    var hoy = HORARIO[dia], abierto = hora >= hoy[0] && hora < hoy[1], texto;
    if (abierto) texto = "Abierto · cierra a las " + formato(hoy[1]);
    else if (hora < hoy[0]) texto = "Cerrado · abre hoy a las " + formato(hoy[0]);
    else { var sig = (dia + 1) % 7; texto = "Cerrado · abre el " + DIAS[sig] + " a las " + formato(HORARIO[sig][0]); }
    var h12 = h % 12 === 0 ? 12 : h % 12;
    var ahora = h12 + ":" + min + (h < 12 ? " a. m." : " p. m.");
    document.querySelectorAll("[data-estado]").forEach(function (el) {
      el.querySelector("[data-estado-texto]").textContent = texto;
      el.classList.toggle("estado--abierto", abierto);
      el.classList.toggle("estado--cerrado", !abierto);
      el.hidden = false;
    });
    document.querySelectorAll("[data-reloj]").forEach(function (el) {
      el.querySelector("[data-reloj-texto]").textContent = ahora;
      el.hidden = false;
    });
    document.querySelectorAll(".horario tr[data-dia]").forEach(function (tr) {
      tr.classList.toggle("hoy", tr.getAttribute("data-dia") === String(dia));
    });
  }
  seguro(function () { reloj(); setInterval(function () { seguro(reloj, "reloj"); }, 30000); }, "reloj");

  /* ---------- Aparición al bajar ---------- */
  seguro(function () {
    var elementos = document.querySelectorAll(".aparecer, .cortina");
    function todo() { elementos.forEach(function (el) { el.classList.add("visible"); }); }
    if (reducir || !("IntersectionObserver" in window)) { todo(); return; }
    var obs = new IntersectionObserver(function (entradas) {
      entradas.forEach(function (e) {
        if (!e.isIntersecting) return;
        (cortinas.get(e.target) || []).forEach(function (c) { c.classList.add("visible"); });
        if (e.target.classList.contains("aparecer")) e.target.classList.add("visible");
        obs.unobserve(e.target);
      });
    }, { threshold: 0.01, rootMargin: "0px 0px -6% 0px" });
    // Los títulos con cortina están recortados del todo al inicio, y un elemento recortado no "se ve" para el
    // observador: por eso se observa su contenedor y se marca el título.
    var cortinas = new Map();
    elementos.forEach(function (el) {
      if (el.classList.contains("cortina") && el.parentElement) {
        var lista = cortinas.get(el.parentElement) || [];
        lista.push(el);
        cortinas.set(el.parentElement, lista);
        obs.observe(el.parentElement);
      } else obs.observe(el);
    });
    setTimeout(function () {
      document.querySelectorAll(".aparecer:not(.visible), .cortina:not(.visible)").forEach(function (el) {
        var caja = (el.classList.contains("cortina") && el.parentElement ? el.parentElement : el).getBoundingClientRect();
        if (caja.top < window.innerHeight) el.classList.add("visible");
      });
    }, 6000);
    window.addEventListener("beforeprint", todo);
  }, "aparecer");
})();
