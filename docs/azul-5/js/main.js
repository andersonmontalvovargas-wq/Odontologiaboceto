/* Dr. Mauricio Soto · comportamiento compartido (boceto) */
(function () {
  "use strict";

  var WHATSAPP = "573187080343";
  var reducido = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  /* 1. Enlaces de WhatsApp con mensaje según el contexto.
        Uso: <a data-wa="diseño de sonrisa"> o data-wa-texto="mensaje completo" */
  document.querySelectorAll("[data-wa], [data-wa-texto]").forEach(function (a) {
    var texto = a.getAttribute("data-wa-texto");
    if (!texto) {
      var tema = a.getAttribute("data-wa");
      texto = tema
        ? "Hola Dr. Soto, quiero agendar una valoración para " + tema + "."
        : "Hola Dr. Soto, quiero agendar una valoración.";
    }
    a.href = "https://wa.me/" + WHATSAPP + "?text=" + encodeURIComponent(texto);
    a.target = "_blank";
    a.rel = "noopener";
  });

  /* 2. Encabezado que se compacta al hacer scroll */
  var encabezado = document.querySelector(".encabezado");
  if (encabezado) {
    var marcar = function () { encabezado.classList.toggle("compacto", window.scrollY > 24); };
    marcar();
    window.addEventListener("scroll", marcar, { passive: true });
  }

  /* 3. Menú móvil */
  var botonMenu = document.querySelector(".boton-menu");
  if (botonMenu) {
    var cerrar = function () {
      document.body.classList.remove("menu-abierto");
      botonMenu.setAttribute("aria-expanded", "false");
    };
    botonMenu.addEventListener("click", function () {
      var abierto = document.body.classList.toggle("menu-abierto");
      botonMenu.setAttribute("aria-expanded", abierto ? "true" : "false");
    });
    document.querySelectorAll(".panel-menu a").forEach(function (a) { a.addEventListener("click", cerrar); });
    document.addEventListener("keydown", function (e) { if (e.key === "Escape") cerrar(); });
    window.addEventListener("resize", function () { if (window.innerWidth >= 960) cerrar(); });
  }

  /* 4. Aparición al hacer scroll (escalonada en grupos) */
  document.querySelectorAll("[data-escalonado]").forEach(function (grupo) {
    Array.prototype.forEach.call(grupo.children, function (hijo, i) {
      hijo.classList.add("aparecer");
      hijo.style.setProperty("--i", i);
    });
  });
  var elementos = document.querySelectorAll(".aparecer");
  if (reducido || !("IntersectionObserver" in window)) {
    elementos.forEach(function (el) { el.classList.add("visible"); });
  } else {
    var observador = new IntersectionObserver(function (entradas) {
      entradas.forEach(function (entrada) {
        if (entrada.isIntersecting) {
          entrada.target.classList.add("visible");
          observador.unobserve(entrada.target);
        }
      });
    }, { rootMargin: "0px 0px -8% 0px", threshold: 0.08 });
    elementos.forEach(function (el) { observador.observe(el); });
  }

  /* 5. Preguntas frecuentes con apertura animada */
  document.querySelectorAll("details.pregunta").forEach(function (det) {
    var resumen = det.querySelector("summary");
    var cuerpo = det.querySelector(".pregunta__cuerpo");
    if (!resumen || !cuerpo || reducido || !cuerpo.animate) return;
    var animando = false;
    resumen.addEventListener("click", function (e) {
      e.preventDefault();
      if (animando) return;
      animando = true;
      if (det.open) {
        var alto = cuerpo.offsetHeight;
        var a = cuerpo.animate([{ height: alto + "px", opacity: 1 }, { height: "0px", opacity: 0 }],
          { duration: 380, easing: "cubic-bezier(.22,.61,.36,1)" });
        cuerpo.style.overflow = "hidden";
        a.onfinish = function () { det.open = false; cuerpo.style.overflow = ""; animando = false; };
      } else {
        det.open = true;
        var fin = cuerpo.offsetHeight;
        cuerpo.style.overflow = "hidden";
        var b = cuerpo.animate([{ height: "0px", opacity: 0 }, { height: fin + "px", opacity: 1 }],
          { duration: 480, easing: "cubic-bezier(.22,.61,.36,1)" });
        b.onfinish = function () { cuerpo.style.overflow = ""; animando = false; };
      }
    });
  });

  /* 6. Año del pie */
  document.querySelectorAll("[data-anio]").forEach(function (el) { el.textContent = new Date().getFullYear(); });
})();

/* Azul 5: fondos de la portada que aparecen y desaparecen (pausables) */
(function () {
  "use strict";
  var heroe = document.querySelector(".heroe--fondo");
  if (!heroe) return;
  var imgs = Array.prototype.slice.call(heroe.querySelectorAll(".heroe__fondos img"));
  var pausa = heroe.querySelector(".heroe__pausa");
  var puntos = heroe.querySelector(".heroe__puntos");
  var reducido = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  var actual = 0, temporizador = null, detenido = reducido;
  var INTERVALO = 6000;

  function validas() { return imgs.filter(function (im) { return !im.dataset.falla; }); }
  function mostrar(n) {
    imgs.forEach(function (im, k) { im.classList.toggle("activa", k === n); });
    Array.prototype.forEach.call(puntos.children, function (b, k) { b.setAttribute("aria-current", k === n ? "true" : "false"); });
    actual = n;
  }
  function siguiente() {
    if (validas().length < 2) return;
    var n = actual;
    do { n = (n + 1) % imgs.length; } while (imgs[n].dataset.falla);
    if (imgs[n].loading === "lazy") imgs[n].loading = "eager";
    mostrar(n);
  }
  function iniciar() { detener(); if (!detenido) temporizador = setInterval(siguiente, INTERVALO); }
  function detener() { if (temporizador) clearInterval(temporizador); temporizador = null; }

  imgs.forEach(function (im, k) {
    var b = document.createElement("button");
    b.type = "button";
    b.setAttribute("aria-label", "Imagen " + (k + 1) + " de " + imgs.length);
    b.addEventListener("click", function () { if (im.dataset.falla) return; if (im.loading === "lazy") im.loading = "eager"; mostrar(k); iniciar(); });
    puntos.appendChild(b);
    im.addEventListener("error", function () { b.hidden = true; if (k === actual) siguiente(); });
  });
  // Precarga suave de las siguientes imágenes cuando la página ya cargó
  window.addEventListener("load", function () { imgs.forEach(function (im) { im.loading = "eager"; }); });

  function marcarPausa() {
    pausa.setAttribute("aria-pressed", detenido ? "true" : "false");
    pausa.setAttribute("aria-label", detenido ? "Reanudar imágenes de fondo" : "Pausar imágenes de fondo");
  }
  pausa.addEventListener("click", function () { detenido = !detenido; marcarPausa(); iniciar(); });
  document.addEventListener("visibilitychange", function () { if (document.hidden) detener(); else iniciar(); });

  mostrar(0); marcarPausa(); iniciar();
})();
