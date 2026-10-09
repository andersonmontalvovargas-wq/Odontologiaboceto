/* Boceto prospecto-03 · Menú móvil y aparición suave. Sin librerías. */
(function () {
  "use strict";

  /* ---------- Menú móvil ---------- */
  var encabezado = document.querySelector(".encabezado");
  var boton = document.querySelector(".menu-boton");
  var menu = document.getElementById("menu-movil");
  function cerrar() {
    encabezado.classList.remove("menu-abierto");
    boton.setAttribute("aria-expanded", "false");
    boton.textContent = "Menú";
  }
  if (boton && menu) {
    boton.addEventListener("click", function () {
      var abierto = encabezado.classList.toggle("menu-abierto");
      boton.setAttribute("aria-expanded", String(abierto));
      boton.textContent = abierto ? "Cerrar" : "Menú";
    });
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape" && encabezado.classList.contains("menu-abierto")) { cerrar(); boton.focus(); }
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
      if (entrada.isIntersecting) {
        entrada.target.classList.add("visible");
        observador.unobserve(entrada.target);
      }
    });
  }, { rootMargin: "0px 0px -8% 0px" });
  elementos.forEach(function (el) { observador.observe(el); });
})();
