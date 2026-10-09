# Notas de diseño — Dr. Mauricio Soto (boceto v2)

**Páginas:** `index.html` (Inicio) · `servicios.html` · `nosotros.html` (titulada "Conoce al doctor": hay un solo odontólogo) · `preguntas.html` (hay más de 4 preguntas) · `contacto.html` · `english.html` (una página en inglés para pacientes del exterior, porque el cliente pidió español e inglés).

**Canal de contacto:** WhatsApp +57 318 708 0343 (`https://wa.me/573187080343`), con mensaje precargado según el servicio. Sin formularios.

**Paleta:** verde petróleo profundo `#1F3D3B` (principal, sereno y distinto del "azul clínico"), durazno `#F2B08A` (acento; viene del color de resaltado del sitio actual), terracota `#96481F` (acento para textos pequeños, cumple AA), fondo hueso `#FBF7F2`, crema `#F5E8DE`, texto `#1F2A29` y `#4A5654`. Todos los pares de texto cumplen AA (mínimo 4,5:1).

**Fuentes:** *Cormorant Garamond* para titulares, porque da continuidad con la serif elegante del sitio actual y transmite estética; *Figtree* para el texto, una sans cálida y muy legible en el celular. Ninguna de las dos es Inter, Roboto ni Arial.

**Decisiones:**
- Actualicé `CONTENIDO.md` (sección 7) con las páginas internas que entregó el usuario antes de construir, para que siga siendo la fuente única.
- No hay fotos disponibles (la red del entorno bloquea el sitio viejo): en su lugar uso marcos en arco con textura de grano y monograma "MS", y formas orgánicas en SVG. No uso fotos de stock.
- No hay precios en ninguna página (decisión del cliente). Se dice "el valor se define en la valoración" y se menciona que hay financiación.
- Los años de experiencia y el número de casos no aparecen porque el sitio actual los contradice.
- Botón flotante de WhatsApp en escritorio; en el celular lo reemplaza una barra fija abajo (WhatsApp + Cómo llegar), para no tapar contenido con dos elementos.
- El escudo de la Universidad Nacional no se usa (es una marca de la universidad); la credencial va en texto.
- Doctor SEO Labs y los precios de los cursos no aparecen en el sitio para pacientes; los cursos van como enlace en el pie.
- El mapa usa la dirección (`maps?q=…&output=embed`); "Cómo llegar" abre el perfil de Google confirmado (`cid=6574127976607366725`).
- Testimonios: sección con estado vacío elegante y botón a las reseñas de Google; no hay reseñas de ejemplo.
- Animaciones: View Transitions entre páginas, aparición al hacer scroll con IntersectionObserver, encabezado que se compacta, preguntas con apertura animada. Todo se apaga con `prefers-reduced-motion`. Sin JavaScript, el contenido se ve igual (las animaciones solo se activan si JS carga).
- Git: la carpeta `sitio/` vive dentro del repositorio existente `Odontologiaboceto`, así que hice el commit ahí en vez de crear un repositorio anidado. Para GitHub Pages, la carpeta `sitio/` puede subirse tal cual como raíz de un repositorio propio.
- Imagen para compartir el link (`assets/compartir.png`, 1200×630): se generó desde el mismo diseño; la ruta es relativa y debe pasar a absoluta cuando haya dominio.
