/* =========================================================
   JO SMILE · Interacción
   ========================================================= */

/* PENDIENTE: número de WhatsApp de la clínica.
   Formato: 57 + celular, sin espacios ni signos. Ejemplo: "573001234567".
   Mientras esté vacío, los botones abren WhatsApp con el mensaje escrito
   y la persona elige el contacto. */
var WHATSAPP_NUMERO = "";

(function () {
  "use strict";
  var raiz = document.documentElement;
  var reducir = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  /* ---------- Enlaces de WhatsApp con mensaje según contexto ---------- */
  function enlaceWA(mensaje) {
    return "https://wa.me/" + WHATSAPP_NUMERO + "?text=" + encodeURIComponent(mensaje);
  }
  document.querySelectorAll("[data-wa]").forEach(function (a) {
    a.href = enlaceWA(a.getAttribute("data-wa"));
    a.target = "_blank";
    a.rel = "noopener";
  });

  /* ---------- Encabezado que cambia al hacer scroll ---------- */
  var encabezado = document.querySelector(".encabezado");
  function alDesplazar() {
    encabezado.classList.toggle("con-scroll", window.scrollY > 12);
  }
  window.addEventListener("scroll", alDesplazar, { passive: true });
  alDesplazar();

  /* ---------- Menú móvil ---------- */
  var boton = document.querySelector(".hamburguesa");
  var menu = document.getElementById("menu-movil");
  function cerrarMenu() {
    encabezado.classList.remove("menu-abierto");
    boton.setAttribute("aria-expanded", "false");
    boton.setAttribute("aria-label", "Abrir menú");
    menu.setAttribute("inert", "");
  }
  if (boton && menu) {
    menu.setAttribute("inert", "");
    boton.addEventListener("click", function () {
      var abierto = encabezado.classList.toggle("menu-abierto");
      boton.setAttribute("aria-expanded", String(abierto));
      boton.setAttribute("aria-label", abierto ? "Cerrar menú" : "Abrir menú");
      if (abierto) menu.removeAttribute("inert"); else menu.setAttribute("inert", "");
    });
    menu.querySelectorAll("a").forEach(function (a) { a.addEventListener("click", cerrarMenu); });
    document.addEventListener("keydown", function (e) { if (e.key === "Escape") cerrarMenu(); });
  }

  /* ---------- Aparición escalonada al hacer scroll ---------- */
  document.querySelectorAll("[data-escalonar]").forEach(function (grupo) {
    Array.prototype.forEach.call(grupo.children, function (hijo, i) {
      hijo.classList.add("revelar");
      hijo.style.setProperty("--i", i % 4);
    });
  });
  var revelar = document.querySelectorAll(".revelar");
  if ("IntersectionObserver" in window && !reducir) {
    var observador = new IntersectionObserver(function (entradas) {
      entradas.forEach(function (e) {
        if (e.isIntersecting) { e.target.classList.add("visible"); observador.unobserve(e.target); }
      });
    }, { threshold: 0.12, rootMargin: "0px 0px -6% 0px" });
    revelar.forEach(function (el) { observador.observe(el); });
  } else {
    revelar.forEach(function (el) { el.classList.add("visible"); });
  }

  /* ---------- Onda al tocar botones ---------- */
  if (!reducir) {
    document.querySelectorAll(".btn").forEach(function (b) {
      b.addEventListener("pointerdown", function (ev) {
        var r = b.getBoundingClientRect();
        var t = Math.max(r.width, r.height);
        var o = document.createElement("span");
        o.className = "onda";
        o.style.width = o.style.height = t + "px";
        o.style.left = ev.clientX - r.left - t / 2 + "px";
        o.style.top = ev.clientY - r.top - t / 2 + "px";
        b.appendChild(o);
        setTimeout(function () { o.remove(); }, 700);
      });
    });
  }

  /* ---------- Preguntas frecuentes con apertura animada ---------- */
  document.querySelectorAll(".faq-item").forEach(function (item) {
    var resumen = item.querySelector("summary");
    var cuerpo = item.querySelector(".faq-cuerpo");
    if (!resumen || !cuerpo) return; // preguntas a la vista: sin desplegable
    var animando = false;
    resumen.addEventListener("click", function (e) {
      if (reducir || !cuerpo.animate) return; // apertura nativa
      e.preventDefault();
      if (animando) return;
      animando = true;
      if (item.open) {
        var alto = cuerpo.offsetHeight;
        cuerpo.animate([{ height: alto + "px", opacity: 1 }, { height: "0px", opacity: 0 }], { duration: 320, easing: "cubic-bezier(.22,.7,.2,1)" })
          .onfinish = function () { item.open = false; animando = false; };
      } else {
        // cerrar las demás del mismo grupo
        var grupo = item.parentElement;
        grupo.querySelectorAll(".faq-item[open]").forEach(function (otro) {
          if (otro !== item) otro.querySelector("summary").click();
        });
        item.open = true;
        var fin = cuerpo.offsetHeight;
        cuerpo.animate([{ height: "0px", opacity: 0 }, { height: fin + "px", opacity: 1 }], { duration: 420, easing: "cubic-bezier(.22,.7,.2,1)" })
          .onfinish = function () { animando = false; };
      }
    });
  });

  /* ---------- Barra móvil: se esconde mientras se ve el botón principal ---------- */
  var barra = document.querySelector(".barra-movil");
  var principal = document.querySelector("[data-cta-principal]");
  if (barra && principal && "IntersectionObserver" in window) {
    new IntersectionObserver(function (e) {
      barra.classList.toggle("oculta", e[0].isIntersecting);
    }).observe(principal);
  }

  /* ---------- Selector "¿Qué te gustaría resolver?" ---------- */
  var chips = document.querySelectorAll(".chip");
  if (chips.length) {
    var resultado = document.querySelector(".selector-resultado");
    var titulo = document.getElementById("selector-titulo");
    var verBtn = document.getElementById("selector-ver");
    var waBtn = document.getElementById("selector-wa");
    chips.forEach(function (chip) {
      chip.addEventListener("click", function () {
        var activo = chip.getAttribute("aria-pressed") === "true";
        chips.forEach(function (c) { c.setAttribute("aria-pressed", "false"); });
        document.querySelectorAll(".servicio.resaltado").forEach(function (s) { s.classList.remove("resaltado"); });
        if (activo) { resultado.classList.remove("abierto"); return; }
        chip.setAttribute("aria-pressed", "true");
        var id = chip.getAttribute("data-servicio");
        var seccion = document.getElementById(id);
        var nombre = seccion.querySelector("h2").textContent;
        seccion.classList.add("resaltado");
        titulo.textContent = "Te puede interesar: " + nombre;
        verBtn.href = "#" + id;
        waBtn.href = enlaceWA("Hola, quiero agendar una valoración. " + chip.getAttribute("data-mensaje"));
        resultado.classList.add("abierto");
      });
    });
  }

  /* ---------- Año del pie de página ---------- */
  var anio = document.getElementById("anio");
  if (anio) anio.textContent = new Date().getFullYear();

  raiz.classList.add("listo");
})();
