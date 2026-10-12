/* Boceto prospecto-03 · Propuestas D y E: menú móvil, aparición suave y estado del horario. Sin librerías. */
(function () {
  "use strict";

  /* ---------- Menú móvil ---------- */
  var encabezado = document.querySelector(".encabezado");
  var boton = document.querySelector(".menu-boton");
  if (encabezado && boton) {
    boton.addEventListener("click", function () {
      var abierto = encabezado.classList.toggle("menu-abierto");
      boton.setAttribute("aria-expanded", String(abierto));
      boton.textContent = abierto ? "Cerrar" : "Menú";
    });
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape" && encabezado.classList.contains("menu-abierto")) {
        encabezado.classList.remove("menu-abierto");
        boton.setAttribute("aria-expanded", "false");
        boton.textContent = "Menú";
        boton.focus();
      }
    });
  }

  /* ---------- Abierto o cerrado ahora, con la hora de Bogotá ----------
     Horario del perfil de Google: lunes a sábado 8:00–20:00, domingo 9:00–20:00. */
  var HORARIO = { 0: [9, 20], 1: [8, 20], 2: [8, 20], 3: [8, 20], 4: [8, 20], 5: [8, 20], 6: [8, 20] };
  var DIAS = ["domingo", "lunes", "martes", "miércoles", "jueves", "viernes", "sábado"];
  function horaBogota() {
    try {
      var partes = new Intl.DateTimeFormat("en-US", { timeZone: "America/Bogota", weekday: "short", hour: "numeric", minute: "numeric", hour12: false }).formatToParts(new Date());
      var m = {};
      partes.forEach(function (p) { m[p.type] = p.value; });
      var dia = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"].indexOf(m.weekday);
      return { dia: dia, hora: (parseInt(m.hour, 10) % 24) + parseInt(m.minute, 10) / 60 };
    } catch (e) { return null; }
  }
  function formato(h) { return h === 12 ? "12:00 m." : (h > 12 ? (h - 12) + ":00 p. m." : h + ":00 a. m."); }
  var ahora = horaBogota();
  if (ahora && ahora.dia >= 0) {
    var hoy = HORARIO[ahora.dia], texto, abierto = ahora.hora >= hoy[0] && ahora.hora < hoy[1];
    if (abierto) {
      texto = "Abierto ahora · cierra a las " + formato(hoy[1]);
    } else if (ahora.hora < hoy[0]) {
      texto = "Cerrado ahora · abre hoy a las " + formato(hoy[0]);
    } else {
      var manana = (ahora.dia + 1) % 7;
      texto = "Cerrado ahora · abre el " + DIAS[manana] + " a las " + formato(HORARIO[manana][0]);
    }
    document.querySelectorAll("[data-estado]").forEach(function (el) {
      el.querySelector("[data-estado-texto]").textContent = texto;
      el.classList.add(abierto ? "estado--abierto" : "estado--cerrado");
      el.hidden = false;
    });
  }

  /* ---------- Aparición suave al hacer scroll ---------- */
  var elementos = document.querySelectorAll(".revelar");
  var reducir = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  if (reducir || !("IntersectionObserver" in window)) {
    elementos.forEach(function (el) { el.classList.add("visible"); });
    return;
  }
  var observador = new IntersectionObserver(function (entradas) {
    entradas.forEach(function (entrada) {
      if (entrada.isIntersecting) { entrada.target.classList.add("visible"); observador.unobserve(entrada.target); }
    });
  }, { rootMargin: "0px 0px -8% 0px" });
  elementos.forEach(function (el) { observador.observe(el); });
})();
