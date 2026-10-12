/* Boceto prospecto-03 · Propuesta F. Sin librerías.
   Todo el contenido está en el HTML: esto solo agrega menú, estado del horario y movimiento.
   Cada parte va en su propio try/catch para que un error no apague las demás. */
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
    function cerrar() {
      encabezado.classList.remove("menu-abierto");
      boton.setAttribute("aria-expanded", "false");
      boton.textContent = "Menú";
    }
    boton.addEventListener("click", function () {
      var abierto = encabezado.classList.toggle("menu-abierto");
      boton.setAttribute("aria-expanded", String(abierto));
      boton.textContent = abierto ? "Cerrar" : "Menú";
    });
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape" && encabezado.classList.contains("menu-abierto")) { cerrar(); boton.focus(); }
    });
  }, "menu");

  /* ---------- Abierto o cerrado ahora, con la hora de Bogotá ----------
     Horario del perfil de Google: lunes a sábado 8:00–20:00, domingo 9:00–20:00. */
  seguro(function () {
    var HORARIO = { 0: [9, 20], 1: [8, 20], 2: [8, 20], 3: [8, 20], 4: [8, 20], 5: [8, 20], 6: [8, 20] };
    var DIAS = ["domingo", "lunes", "martes", "miércoles", "jueves", "viernes", "sábado"];
    var partes = new Intl.DateTimeFormat("en-US", { timeZone: "America/Bogota", weekday: "short", hour: "numeric", minute: "numeric", hour12: false }).formatToParts(new Date());
    var m = {};
    partes.forEach(function (p) { m[p.type] = p.value; });
    var dia = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"].indexOf(m.weekday);
    if (dia < 0) return;
    var hora = (parseInt(m.hour, 10) % 24) + parseInt(m.minute, 10) / 60;
    function formato(h) { return h === 12 ? "12:00 m." : (h > 12 ? (h - 12) + ":00 p. m." : h + ":00 a. m."); }
    var hoy = HORARIO[dia], abierto = hora >= hoy[0] && hora < hoy[1], texto;
    if (abierto) texto = "Abierto ahora · cierra a las " + formato(hoy[1]);
    else if (hora < hoy[0]) texto = "Cerrado ahora · abre hoy a las " + formato(hoy[0]);
    else { var manana = (dia + 1) % 7; texto = "Cerrado ahora · abre el " + DIAS[manana] + " a las " + formato(HORARIO[manana][0]); }
    document.querySelectorAll("[data-estado]").forEach(function (el) {
      el.querySelector("[data-estado-texto]").textContent = texto;
      el.classList.add(abierto ? "estado--abierto" : "estado--cerrado");
      el.hidden = false;
    });
    document.querySelectorAll('.semana tr[data-dia="' + dia + '"]').forEach(function (tr) { tr.classList.add("hoy"); });
  }, "horario");

  /* ---------- Aparición suave al bajar (con red de seguridad) ---------- */
  seguro(function () {
    var elementos = document.querySelectorAll(".revelar");
    function mostrarTodo() { elementos.forEach(function (el) { el.classList.add("visible"); }); }
    if (reducir || !("IntersectionObserver" in window)) { mostrarTodo(); return; }
    var observador = new IntersectionObserver(function (entradas) {
      entradas.forEach(function (entrada) {
        if (entrada.isIntersecting) { entrada.target.classList.add("visible"); observador.unobserve(entrada.target); }
      });
    }, { threshold: 0.01, rootMargin: "0px 0px -6% 0px" });
    elementos.forEach(function (el) { observador.observe(el); });
    // Si algo falla (pestaña en segundo plano, impresión), a los 6 s se muestra todo.
    setTimeout(function () { document.querySelectorAll(".revelar:not(.visible)").forEach(function (el) { if (el.getBoundingClientRect().top < window.innerHeight) el.classList.add("visible"); }); }, 6000);
    window.addEventListener("beforeprint", mostrarTodo);
  }, "revelar");

  /* ---------- Movimiento ligado al desplazamiento ----------
     El sello gira y el óvalo se acerca solo mientras la persona baja; nada se mueve solo. */
  seguro(function () {
    var encabezado = document.querySelector(".encabezado");
    var sello = document.querySelector("[data-sello] .sello");
    var ovalo = document.querySelector("[data-parallax]");
    var pasos = document.querySelectorAll("[data-progreso]");
    var pendiente = false;
    function actualizar() {
      pendiente = false;
      var y = window.scrollY || window.pageYOffset;
      if (encabezado) encabezado.classList.toggle("con-sombra", y > 8);
      if (reducir) return;
      if (sello) sello.style.setProperty("--giro", (y * 0.25) + "deg");
      if (ovalo) ovalo.style.setProperty("--escala", String(1 + Math.min(y, 600) / 6000));
      pasos.forEach(function (ol) {
        var r = ol.getBoundingClientRect(), vh = window.innerHeight;
        var p = (vh * 0.7 - r.top) / Math.max(r.height, 1);
        ol.style.setProperty("--progreso", String(Math.max(0, Math.min(1, p))));
      });
    }
    window.addEventListener("scroll", function () { if (!pendiente) { pendiente = true; requestAnimationFrame(actualizar); } }, { passive: true });
    window.addEventListener("resize", actualizar);
    actualizar();
  }, "desplazamiento");

  /* ---------- Muestrario de tratamientos: botones anterior y siguiente ---------- */
  seguro(function () {
    var lista = document.querySelector("[data-riel-lista]");
    var controles = document.querySelector("[data-riel-controles]");
    if (!lista || !controles) return;
    var botones = controles.querySelectorAll("[data-riel]");
    function estado() {
      var max = lista.scrollWidth - lista.clientWidth - 4;
      botones[0].disabled = lista.scrollLeft <= 4;
      botones[1].disabled = lista.scrollLeft >= max;
      controles.hidden = max <= 0;
    }
    botones.forEach(function (b) {
      b.addEventListener("click", function () {
        var tarjeta = lista.querySelector(".muestra");
        var paso = tarjeta ? tarjeta.getBoundingClientRect().width + 22 : 320;
        lista.scrollBy({ left: paso * Number(b.getAttribute("data-riel")), behavior: reducir ? "auto" : "smooth" });
      });
    });
    lista.addEventListener("scroll", function () { requestAnimationFrame(estado); }, { passive: true });
    window.addEventListener("resize", estado);
    estado();
  }, "riel");

  /* ---------- Tratamientos: la foto fija cambia con el tratamiento que se está leyendo ---------- */
  seguro(function () {
    var articulos = document.querySelectorAll("[data-trat]");
    if (!articulos.length || !("IntersectionObserver" in window)) return;
    var escenas = {}, chips = {};
    document.querySelectorAll("[data-escena]").forEach(function (f) { escenas[f.getAttribute("data-escena")] = f; });
    document.querySelectorAll("[data-chip]").forEach(function (c) { chips[c.getAttribute("data-chip")] = c; });
    // Las fotos del escenario se cargan antes de llegar, para que el cambio no muestre un hueco.
    // En celular el escenario está oculto y no se carga nada de más.
    var escenario = document.querySelector(".escenario");
    if (escenario && getComputedStyle(escenario).display !== "none") {
      Object.keys(escenas).forEach(function (k) { var i = escenas[k].querySelector("img"); if (i) i.loading = "eager"; });
    }
    var actual = null;
    function activar(id) {
      if (id === actual) return;
      actual = id;
      Object.keys(escenas).forEach(function (k) { escenas[k].classList.toggle("activa", k === id); });
      Object.keys(chips).forEach(function (k) {
        var activo = k === id;
        chips[k].classList.toggle("activo", activo);
        if (activo) {
          chips[k].setAttribute("aria-current", "true");
          var ul = chips[k].closest("ul");
          if (ul) ul.scrollTo({ left: chips[k].offsetLeft - ul.offsetLeft - 16, behavior: reducir ? "auto" : "smooth" });
        } else chips[k].removeAttribute("aria-current");
      });
    }
    var observador = new IntersectionObserver(function (entradas) {
      entradas.forEach(function (e) { if (e.isIntersecting) activar(e.target.getAttribute("data-trat")); });
    }, { rootMargin: "-45% 0px -50% 0px" });
    articulos.forEach(function (a) { observador.observe(a); });
  }, "tratamientos");
})();
