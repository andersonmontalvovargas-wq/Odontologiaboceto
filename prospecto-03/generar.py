"""Genera las 5 páginas del boceto con encabezado y pie compartidos.

Uso: python3 prospecto-03/generar.py prospecto-03/sitio
Los textos se cambian aquí, no en los HTML, para no tener que repetir el cambio en cada página.
"""
import json, sys, urllib.parse
from pathlib import Path

DESTINO = Path(sys.argv[1])

NOMBRE = "Dra. Vanesa Gutiérrez"
CONSULTORIO = "Consultorio Dra. Vanesa Gutiérrez"
TEL_VISIBLE = "324 492 5383"
TEL = "+573244925383"
WA = "573244925383"
DIRECCION = "Cra. 34 # 36-31, local 2, Edificio Alto Prado"
CIUDAD = "Bucaramanga, Santander"
MAPS = "https://www.google.com/maps/search/?api=1&query=" + urllib.parse.quote("Consultorio Dra Vanesa Gutiérrez Cra 34 36-31 Bucaramanga")
WAZE = "https://waze.com/ul?q=" + urllib.parse.quote("Carrera 34 #36-31 Bucaramanga") + "&navigate=yes"
NOTA = "5,0"
OPINIONES = 61
FECHA_NOTA = "octubre de 2026"

def wa(msg="Hola, Dra. Vanesa. Quiero agendar una valoración."):
    return f"https://wa.me/{WA}?text=" + urllib.parse.quote(msg)

# ---------- Íconos ----------
I_WA = '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2Zm0 18.2c-1.6 0-3.1-.4-4.4-1.2l-.3-.2-3 .8.8-2.9-.2-.3A8.2 8.2 0 1 1 12 20.2Zm4.5-6.1c-.2-.1-1.5-.7-1.7-.8-.2-.1-.4-.1-.6.1l-.8 1c-.1.2-.3.2-.5.1a6.7 6.7 0 0 1-3.3-2.9c-.3-.4.3-.4.7-1.3.1-.2 0-.3 0-.4l-.8-1.8c-.2-.5-.4-.4-.6-.4h-.5a1 1 0 0 0-.7.3 3 3 0 0 0-.9 2.2c0 1.3.9 2.5 1 2.7.1.2 1.8 2.8 4.4 3.9 1.6.7 2.3.8 3.1.6.5-.1 1.5-.6 1.7-1.2.2-.6.2-1.1.2-1.2-.1-.1-.3-.2-.5-.3Z"/></svg>'
I_TEL = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 3.5h3.2l1.6 4.2-2.1 1.4a11 11 0 0 0 7.2 7.2l1.4-2.1 4.2 1.6V19a1.6 1.6 0 0 1-1.7 1.6A16.6 16.6 0 0 1 3.4 5.2 1.6 1.6 0 0 1 5 3.5Z"/></svg>'
I_PIN = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 21.5s7-6.1 7-11.9a7 7 0 1 0-14 0c0 5.8 7 11.9 7 11.9Z"/><circle cx="12" cy="9.6" r="2.6"/></svg>'
I_RELOJ = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" aria-hidden="true"><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3.2 2"/></svg>'
I_GORRO = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M2.5 9 12 4.5 21.5 9 12 13.5Z"/><path d="M6.5 11v4.5c0 1.4 2.5 3 5.5 3s5.5-1.6 5.5-3V11"/></svg>'
I_DIENTE = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round" aria-hidden="true"><path d="M8 3.5c-2.4 0-4 1.8-4 4.4 0 3 1.6 5 2.2 8 .5 2.5 1.1 4.6 2.4 4.6 1.6 0 1.7-3.1 2.6-5.3.3-.8.6-1.2.8-1.2s.5.4.8 1.2c.9 2.2 1 5.3 2.6 5.3 1.3 0 1.9-2.1 2.4-4.6.6-3 2.2-5 2.2-8 0-2.6-1.6-4.4-4-4.4-2 0-2.6 1-4 1s-2-1-4-1Z"/></svg>'
ESTRELLA = '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M12 2.8l2.8 5.8 6.3.9-4.6 4.4 1.1 6.3L12 17.2l-5.6 3 1.1-6.3L2.9 9.5l6.3-.9Z"/></svg>'
ESTRELLAS = '<span class="estrellas">' + ESTRELLA * 5 + '</span>'

# Arco de sonrisa: espacio reservado para la foto real (no simula a la doctora)
def retrato(nota, alto=500, prioridad=False):
    dientes = ""
    import math
    n = 8
    for i in range(n):
        t = (i + .5) / n
        x = 60 + t * 280
        y = 250 + 60 * math.sin(math.pi * t)
        ancho = 30 if i in (0, n - 1) else (34 if i in (1, n - 2) else 38)
        alto_d = 54 if i in (0, n - 1) else (62 if i in (1, n - 2) else 74)
        ang = (t - .5) * 50
        dientes += (f'<rect x="{x - ancho/2:.1f}" y="{y - alto_d/2:.1f}" width="{ancho}" height="{alto_d}" rx="{ancho/2.4:.1f}" '
                    f'transform="rotate({ang:.1f} {x:.1f} {y:.1f})" fill="#FFFFFF" stroke="#D9C3B0" stroke-width="1.5"/>')
    return f'''<div class="retrato">
        <svg viewBox="0 0 400 500" preserveAspectRatio="xMidYMid slice" aria-hidden="true" focusable="false">
          <circle cx="200" cy="170" r="120" fill="#FFFFFF" opacity=".35"/>
          <path d="M40 230c50 120 270 120 320 0" fill="none" stroke="#B08A57" stroke-width="1.5" stroke-dasharray="2 7" stroke-linecap="round"/>
          {dientes}
          <path d="M70 352c60 40 200 40 260 0" fill="none" stroke="#7B2D3B" stroke-opacity=".35" stroke-width="2" stroke-linecap="round"/>
        </svg>
        <!-- PENDIENTE: foto real de la {NOMBRE} en su consultorio (WebP, 800x1000, width/height declarados{', fetchpriority="high", sin lazy' if prioridad else ', loading="lazy"'}). -->
        <p class="retrato-nota">{nota}</p>
      </div>'''

PAGINAS = [
    ("index.html", "Inicio"),
    ("tratamientos.html", "Tratamientos"),
    ("la-doctora.html", "La doctora"),
    ("preguntas.html", "Preguntas frecuentes"),
    ("contacto.html", "Contacto y horario"),
]

HORARIO = [("Lunes", "8:00 a. m. – 8:00 p. m."), ("Martes", "8:00 a. m. – 8:00 p. m."), ("Miércoles", "8:00 a. m. – 8:00 p. m."),
           ("Jueves", "8:00 a. m. – 8:00 p. m."), ("Viernes", "8:00 a. m. – 8:00 p. m."), ("Sábado", "8:00 a. m. – 8:00 p. m."),
           ("Domingo", "9:00 a. m. – 8:00 p. m.")]

def tabla_horario():
    filas = "".join(f"<tr><th scope=\"row\">{d}</th><td>{h}</td></tr>" for d, h in HORARIO)
    return f'<table class="tabla-horario"><caption class="sr">Horario de atención</caption><tbody>{filas}</tbody></table>\n      <p class="nota">En festivos el horario puede variar. Confírmalo por WhatsApp antes de ir.</p>'

JSONLD = {
    "@context": "https://schema.org",
    "@type": "Dentist",
    "name": CONSULTORIO,
    "telephone": TEL,
    "address": {"@type": "PostalAddress", "streetAddress": "Carrera 34 # 36-31, local 2, Edificio Alto Prado",
                "addressLocality": "Bucaramanga", "addressRegion": "Santander", "addressCountry": "CO"},
    "openingHoursSpecification": [
        {"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"], "opens": "08:00", "closes": "20:00"},
        {"@type": "OpeningHoursSpecification", "dayOfWeek": "Sunday", "opens": "09:00", "closes": "20:00"},
    ],
    "employee": {"@type": "Person", "name": "Vanesa Gutiérrez", "jobTitle": "Odontóloga"},
}

def pagina(archivo, titulo, descripcion, cuerpo, jsonld=False):
    nav = "".join(
        f'<li><a href="{a}"{" aria-current=\"page\"" if a == archivo else ""}>{n}</a></li>'
        for a, n in PAGINAS[1:]
    )
    nav_movil = "".join(
        f'<li><a href="{a}"{" aria-current=\"page\"" if a == archivo else ""}>{n}</a></li>'
        for a, n in PAGINAS
    )
    ld = ""
    if jsonld:
        ld = ('\n<!-- Dentist (LocalBusiness). PENDIENTE: url, geo con 5 decimales e image cuando haya dominio y fotos reales. Sin aggregateRating: las opiniones son de Google. -->\n'
              '<script type="application/ld+json">' + json.dumps(JSONLD, ensure_ascii=False) + '</script>')
    return f'''<!doctype html>
<html lang="es-CO">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<!-- Boceto: no indexar. Quitar en el sitio final (CLAUDE.md, sección 2). -->
<meta name="robots" content="noindex">
<title>{titulo}</title>
<meta name="description" content="{descripcion}">
<meta name="theme-color" content="#4A1B25">
<meta property="og:type" content="website">
<meta property="og:locale" content="es_CO">
<meta property="og:title" content="{titulo}">
<meta property="og:description" content="{descripcion}">
<!-- PENDIENTE: og:image (1200x630, foto real o logo) y og:url cuando el sitio tenga dominio. -->
<link rel="icon" href="assets/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Figtree:wght@400;500;600;700&family=Fraunces:ital,opsz,wght@0,9..144,400..600;1,9..144,400..600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="css/estilos.css">
<script>document.documentElement.classList.add("js")</script>
<script src="js/main.js" defer></script>{ld}
</head>
<body>
<a class="sr" href="#contenido">Saltar al contenido</a>
<div class="aviso-propuesta" role="note"><strong>Propuesta de diseño</strong> para el {CONSULTORIO}. No es el sitio oficial.</div>
<header class="encabezado">
  <div class="contenedor">
    <a class="marca" href="index.html" aria-label="{NOMBRE}, ir al inicio">
      <!-- PENDIENTE: monograma provisional; reemplazar por el logo real si lo tiene. -->
      <span class="monograma" aria-hidden="true">VG</span>
      <span class="marca-texto">{NOMBRE}<small>Estética dental · Bucaramanga</small></span>
    </a>
    <nav class="nav" aria-label="Principal"><ul>{nav}</ul></nav>
    <a class="btn btn--sm" href="{wa()}" target="_blank" rel="noopener">{I_WA}Escribir por WhatsApp</a>
    <button class="menu-boton" type="button" aria-expanded="false" aria-controls="menu-movil">Menú</button>
  </div>
  <nav class="menu-movil" id="menu-movil" aria-label="Menú móvil"><ul>{nav_movil}</ul></nav>
</header>
<main id="contenido">
{cuerpo}
</main>
<footer class="pie">
  <div class="contenedor">
    <div class="pie-grid">
      <div>
        <h2>{CONSULTORIO}</h2>
        <p>Odontología y estética dental en Bucaramanga.<br>{DIRECCION}.<br>{CIUDAD}.</p>
        <p><a href="tel:{TEL}">{TEL_VISIBLE}</a> · <a href="{wa()}" target="_blank" rel="noopener">WhatsApp</a></p>
      </div>
      <div>
        <h2>Horario</h2>
        <p>Lunes a sábado: 8:00 a. m. – 8:00 p. m.<br>Domingo: 9:00 a. m. – 8:00 p. m.<br>En festivos puede variar.</p>
      </div>
      <div>
        <h2>Páginas</h2>
        <ul>{nav_movil}</ul>
      </div>
    </div>
    <!-- PENDIENTE: enlace a la Política de tratamiento de datos (Ley 1581 de 2012) del consultorio. -->
    <p class="pie-legal">Este sitio no tiene formularios ni recoge datos personales. La información de contacto y el horario se tomaron del perfil público del consultorio en Google ({FECHA_NOTA}).</p>
  </div>
</footer>
<a class="wa-flotante" href="{wa()}" target="_blank" rel="noopener" aria-label="Escribir por WhatsApp a la {NOMBRE}">{I_WA}WhatsApp</a>
</body>
</html>
'''

# ---------- Tratamientos ----------
TRAT = [
    ("diseno-de-sonrisa", "Diseño de sonrisa",
     "Es un plan para cambiar la forma, el color, el tamaño o la proporción de los dientes que se ven al sonreír. Se planea según tu cara, tus labios y tus encías, y puede combinar varios tratamientos: carillas, blanqueamiento, resinas o coronas.",
     "Smile design, perfeccionamiento de sonrisa, estética dental",
     "Hola, Dra. Vanesa. Quiero información sobre diseño de sonrisa."),
    ("carillas", "Carillas y lentes cerámicos",
     "Son láminas delgadas que se adhieren a la cara visible de los dientes. Pueden ser de cerámica (porcelana), también llamadas lentes cerámicos, o de resina. En la valoración se revisa si tus dientes y encías permiten ponerlas y qué material conviene en tu caso.",
     "Carillas de porcelana, porcelain veneers, carillas en resina, bordes en resina",
     "Hola, Dra. Vanesa. Quiero información sobre carillas y lentes cerámicos."),
    ("blanqueamiento", "Blanqueamiento dental",
     "Aclara el color natural de los dientes con un gel que aplica la odontóloga. Antes se revisa que no haya caries ni sensibilidad que tratar primero. El blanqueamiento no cambia el color de resinas, coronas ni carillas que ya tengas.",
     "Aclaramiento dental",
     "Hola, Dra. Vanesa. Quiero información sobre blanqueamiento dental."),
    ("implantes-y-coronas", "Implantes dentales y coronas",
     "Un implante reemplaza la raíz de un diente perdido, y sobre él se pone una corona. Las coronas también sirven para cubrir y proteger un diente muy desgastado o tratado. Antes de un implante se estudia el hueso con imágenes radiográficas.",
     "Implante, rehabilitación oral, coronas en cerámica",
     "Hola, Dra. Vanesa. Quiero información sobre implantes y coronas."),
    ("ortodoncia", "Ortodoncia y brackets",
     "Corrige la posición de los dientes y la mordida. En el consultorio se ofrecen brackets de autoligado y brackets de zafiro, que son transparentes.",
     "Brackets, autoligado, brackets de zafiro",
     "Hola, Dra. Vanesa. Quiero información sobre ortodoncia y brackets."),
    ("conductos", "Tratamiento de conductos",
     "Cuando el nervio de un diente está inflamado o infectado, se limpia por dentro y se sella para conservar el diente. Si un diente con conductos tratados vuelve a dar molestias, se puede hacer un retratamiento.",
     "Endodoncia, conductos, retratamientos",
     "Hola, Dra. Vanesa. Quiero información sobre tratamiento de conductos."),
    ("limpieza-y-encias", "Limpieza dental y encías",
     "La limpieza retira la placa y el sarro (detartraje). Si tus encías sangran o se retraen, se hace una limpieza profunda y el control de las encías, que es el campo de la periodoncia.",
     "Limpieza profunda, detartraje, periodoncia, periodoncista",
     "Hola, Dra. Vanesa. Quiero agendar una limpieza dental."),
    ("odontologia-general", "Odontología general y cirugía oral",
     "Revisión de tu boca, calzas en resina del color del diente y procedimientos de cirugía oral. En la valoración se define qué necesitas y en qué orden.",
     "Odontóloga, calzas, resinas, cirugía oral",
     "Hola, Dra. Vanesa. Quiero agendar una valoración general."),
]

def tarjetas():
    out = []
    for i, (id_, nombre, texto, _, _) in enumerate(TRAT):
        clase = " tratamiento--destacado" if i == 0 else ""
        corto = texto.split(". ")[0] + "."
        out.append(f'''<li class="tratamiento{clase} revelar">
          <span class="numero">{i+1:02d}</span>
          <h3>{nombre}</h3>
          <p>{corto}</p>
          <a href="tratamientos.html#{id_}">Ver {nombre.lower()} <span aria-hidden="true">→</span></a>
        </li>''')
    return "\n        ".join(out)

def bloque_ubicacion(h="h2"):
    return f'''<div class="ubicacion">
      <div>
        <{h}>Dónde atendemos</{h}>
        <p class="direccion">{DIRECCION}<br>{CIUDAD}</p>
        <div class="acciones">
          <a class="btn" href="{MAPS}" target="_blank" rel="noopener">{I_PIN}Abrir en Google Maps</a>
          <a class="btn btn--linea" href="{WAZE}" target="_blank" rel="noopener">Abrir en Waze</a>
        </div>
        <!-- PENDIENTE: confirmar la placa exacta (en Google aparecen 36-31 local 2 y 36-33), si hay parqueadero y acceso para silla de ruedas. -->
      </div>
      <div>
        <{h}>Horario de atención</{h}>
        {tabla_horario()}
      </div>
    </div>'''

# ---------- index.html ----------
inicio = f'''
<section class="heroe">
  <div class="contenedor heroe-grid">
    <div>
      <p class="antetitulo">Odontología estética en Bucaramanga</p>
      <h1>{NOMBRE}: <em>diseño de sonrisa</em> y lentes cerámicos</h1>
      <p class="intro">Odontóloga con especialización en estética de la UNICID (São Paulo, Brasil). En su consultorio también se atiende odontología general, ortodoncia, implantes, conductos y encías.</p>
      <div class="acciones">
        <a class="btn" href="{wa()}" target="_blank" rel="noopener">{I_WA}Agenda tu valoración por WhatsApp</a>
        <a class="btn btn--linea" href="tel:{TEL}">{I_TEL}Llamar al {TEL_VISIBLE}</a>
      </div>
      <a class="calificacion" href="{MAPS}" target="_blank" rel="noopener">{ESTRELLAS}<span><strong>{NOTA}</strong> en Google · Mira sus {OPINIONES} opiniones</span></a>
    </div>
    {retrato("Espacio para una foto real de la doctora", prioridad=True)}
  </div>
</section>

<section class="datos" aria-label="Datos de contacto">
  <ul class="contenedor">
    <li>{I_PIN}<span><strong>Dirección</strong>{DIRECCION}, {CIUDAD}</span></li>
    <li>{I_TEL}<span><strong>Teléfono y WhatsApp</strong><a href="tel:{TEL}">{TEL_VISIBLE}</a></span></li>
    <li>{I_RELOJ}<span><strong>Horario</strong>Lunes a sábado 8 a. m. – 8 p. m.<br>Domingo 9 a. m. – 8 p. m.</span></li>
  </ul>
</section>

<section class="seccion" aria-labelledby="t-tratamientos">
  <div class="contenedor">
    <div class="seccion-cabeza revelar">
      <h2 id="t-tratamientos">Tratamientos del consultorio</h2>
      <p>La estética dental es el centro de la consulta, pero no lo único. Estos son los tratamientos que ofrece el consultorio, con el nombre con que los conoces.</p>
    </div>
    <ul class="tratamientos">
        {tarjetas()}
    </ul>
  </div>
</section>

<section class="seccion seccion--arena" aria-labelledby="t-doctora">
  <div class="contenedor doctora">
    {retrato("Espacio para una foto de la doctora atendiendo")}
    <div class="revelar">
      <p class="antetitulo">Quién te atiende</p>
      <h2 id="t-doctora">Conoce a la {NOMBRE}</h2>
      <p>Es odontóloga y se especializó en estética dental en Brasil. Su trabajo se concentra en el diseño de sonrisa, las carillas y los lentes cerámicos.</p>
      <ul class="formacion">
        <li>{I_GORRO}<span><strong>Especialización en Estética</strong><span>UNICID, Universidade Cidade de São Paulo (Brasil)</span></span></li>
        <!-- PENDIENTE: universidad del pregrado en Odontología y año; registro profesional (ReTHUS) si quiere mostrarlo. -->
      </ul>
      <a class="btn btn--linea" href="la-doctora.html">Más sobre la doctora</a>
    </div>
  </div>
</section>

<section class="seccion seccion--vino" aria-labelledby="t-pasos">
  <div class="contenedor">
    <div class="seccion-cabeza revelar">
      <h2 id="t-pasos">Así es tu primera cita</h2>
      <p>No necesitas saber qué tratamiento quieres. Para eso es la valoración.</p>
    </div>
    <!-- PENDIENTE: confirmar con la doctora cómo es la valoración, cuánto cuesta y si incluye radiografías. -->
    <ol class="pasos">
      <li class="revelar"><h3>Escribes o llamas</h3><p>Por WhatsApp o al {TEL_VISIBLE}. Cuéntanos qué te gustaría mejorar y elige el día.</p></li>
      <li class="revelar"><h3>Valoración</h3><p>La doctora revisa tus dientes y encías y escucha lo que quieres cambiar de tu sonrisa.</p></li>
      <li class="revelar"><h3>Tu plan</h3><p>Te explica las opciones, los tiempos y el costo antes de empezar cualquier tratamiento.</p></li>
    </ol>
    <div class="acciones"><a class="btn" style="background:#FFFFFF;color:#4A1B25;border-color:#FFFFFF" href="{wa()}" target="_blank" rel="noopener">{I_WA}Pedir mi valoración</a></div>
  </div>
</section>

<section class="seccion" aria-labelledby="t-opiniones">
  <div class="contenedor opiniones">
    <div class="nota-grande revelar">
      <div class="cifra">{NOTA}</div>
      {ESTRELLAS}
      <small>{OPINIONES} opiniones en Google<br>({FECHA_NOTA})</small>
    </div>
    <div class="revelar">
      <h2 id="t-opiniones">Lo que dicen sus pacientes en Google</h2>
      <p>El consultorio tiene una calificación de {NOTA} sobre 5 con {OPINIONES} opiniones en su perfil de Google. Puedes leerlas todas allí, escritas por los mismos pacientes.</p>
      <!-- PENDIENTE: 3 opiniones reales copiadas de Google, con nombre del autor, enlace a la reseña original y la marca Google. Sin datos estructurados de estrellas. -->
      <a class="btn btn--linea" href="{MAPS}" target="_blank" rel="noopener">Mira sus {OPINIONES} opiniones en Google</a>
    </div>
  </div>
</section>

<section class="seccion seccion--arena" aria-label="Ubicación y horario">
  <div class="contenedor">
    {bloque_ubicacion()}
  </div>
</section>
'''

# ---------- tratamientos.html ----------
detalles = "\n".join(f'''    <article class="detalle" id="{id_}">
      <span class="numero">{i+1:02d}</span>
      <div>
        <h2>{nombre}</h2>
        <p>{texto}</p>
        <p class="tambien"><strong>También lo buscas como:</strong> {tambien}.</p>
        <a class="btn btn--sm" href="{wa(msg)}" target="_blank" rel="noopener">{I_WA}Preguntar por {nombre.lower()}</a>
      </div>
    </article>''' for i, (id_, nombre, texto, tambien, msg) in enumerate(TRAT))
indice = "".join(f'<li><a href="#{id_}">{n}</a></li>' for id_, n, *_ in TRAT)
tratamientos = f'''
<section class="cabecera-pagina">
  <div class="contenedor">
    <p class="antetitulo">Tratamientos</p>
    <h1>Tratamientos de odontología y <em>estética dental</em></h1>
    <p class="intro">Qué es cada tratamiento, explicado en pocas palabras. El costo y los tiempos dependen de cada caso y se definen en la valoración.</p>
    <ul class="indice">{indice}</ul>
  </div>
</section>
<section class="seccion" style="padding-top:16px">
  <div class="contenedor">
    <!-- PENDIENTE: que la doctora revise y firme estos textos (tema de salud), y confirme qué tratamientos hace ella y cuáles un especialista aliado. -->
{detalles}
  </div>
</section>
'''

# ---------- la-doctora.html ----------
doctora = f'''
<section class="cabecera-pagina">
  <div class="contenedor doctora">
    {retrato("Espacio para una foto real de la doctora", prioridad=True)}
    <div>
      <p class="antetitulo">La doctora</p>
      <h1>{NOMBRE}, odontóloga especialista en <em>estética</em></h1>
      <p class="intro">Atiende en su consultorio del Edificio Alto Prado, en Bucaramanga. Su trabajo se concentra en el diseño de sonrisa, las carillas y los lentes cerámicos.</p>
      <div class="acciones">
        <a class="btn" href="{wa()}" target="_blank" rel="noopener">{I_WA}Agenda tu valoración</a>
      </div>
    </div>
  </div>
</section>
<section class="seccion">
  <div class="contenedor" style="max-width:820px">
    <h2>Formación</h2>
    <ul class="formacion">
      <li>{I_GORRO}<span><strong>Especialización en Estética</strong><span>UNICID, Universidade Cidade de São Paulo (Brasil)</span></span></li>
      <li>{I_DIENTE}<span><strong>Odontóloga</strong><span>Atiende odontología general y estética dental</span></span></li>
      <!-- PENDIENTE: universidad del pregrado, año de grado, cursos y registro profesional (ReTHUS). Solo lo que se pueda comprobar. -->
    </ul>
    <h2>En qué se enfoca</h2>
    <p>La estética dental: cambiar la forma, el color o la proporción de los dientes para que la sonrisa se vea en armonía con la cara. Para eso usa carillas y lentes cerámicos, resinas y blanqueamiento, según lo que cada paciente necesite.</p>
    <p>En el consultorio también se atiende ortodoncia, implantes y coronas, tratamiento de conductos, limpieza y encías. Puedes ver cada uno en <a href="tratamientos.html">Tratamientos</a>.</p>
    <!-- PENDIENTE: un texto corto escrito por la doctora, en primera persona: por qué eligió la estética dental y cómo trabaja con sus pacientes. -->
    <h2>Opiniones de sus pacientes</h2>
    <p>Su consultorio tiene una calificación de {NOTA} sobre 5 con {OPINIONES} opiniones en Google ({FECHA_NOTA}).</p>
    <a class="btn btn--linea" href="{MAPS}" target="_blank" rel="noopener">Mira sus {OPINIONES} opiniones en Google</a>
  </div>
</section>
'''

# ---------- preguntas.html ----------
PREG = [
    ("¿Qué son los lentes cerámicos?",
     "Son carillas de cerámica: láminas muy delgadas de porcelana que se pegan a la cara visible de los dientes para cambiar su color, forma o tamaño. En otros países se conocen como <em>porcelain veneers</em>."),
    ("¿Carillas de cerámica o de resina: cuál es la diferencia?",
     "La cerámica mantiene mejor el color con el tiempo y es más resistente a las manchas. La resina suele costar menos y es más fácil de reparar. Cuál te conviene depende de tus dientes, tu mordida y lo que buscas; eso se define en la valoración."),
    ("¿Hay que desgastar los dientes para poner carillas?",
     "Depende de cada caso. A veces se necesita un desgaste mínimo y a veces ninguno. La doctora te lo explica en la valoración, antes de decidir."),
    ("¿Cuánto cuesta un diseño de sonrisa?",
     "Depende de cuántos dientes se tratan y del material. Por eso el costo se da después de la valoración, cuando ya se sabe qué necesitas."),
    ("¿El blanqueamiento daña los dientes?",
     "Hecho y controlado por un odontólogo, el blanqueamiento no debería dañar el esmalte. Puede dar sensibilidad durante unos días. Antes se revisa que no haya caries ni encías inflamadas."),
    ("¿Atienden ortodoncia, implantes y otros tratamientos además de estética?",
     'Sí. El consultorio atiende ortodoncia con brackets de autoligado y de zafiro, implantes y coronas, tratamiento de conductos, limpieza, encías y odontología general. Mira la lista completa en <a href="tratamientos.html">Tratamientos</a>.'),
    ("¿Dónde queda el consultorio?",
     f'En la {DIRECCION}, {CIUDAD}. Puedes <a href="{MAPS}" target="_blank" rel="noopener">abrir la ubicación en Google Maps</a>.'),
    ("¿Cuál es el horario?",
     "Lunes a sábado de 8:00 a. m. a 8:00 p. m. y domingo de 9:00 a. m. a 8:00 p. m. En festivos puede variar."),
    ("¿Cómo pido una cita?",
     f'Escribe por <a href="{wa()}" target="_blank" rel="noopener">WhatsApp</a> o llama al <a href="tel:{TEL}">{TEL_VISIBLE}</a>.'),
]
preguntas_html = "\n".join(f'''      <article class="pregunta">
        <h2>{q}</h2>
        <p>{a}</p>
      </article>''' for q, a in PREG)
preguntas = f'''
<section class="cabecera-pagina">
  <div class="contenedor">
    <p class="antetitulo">Preguntas frecuentes</p>
    <h1>Preguntas frecuentes sobre <em>carillas</em>, blanqueamiento y citas</h1>
    <p class="intro">Respuestas cortas a lo que más se pregunta antes de la primera cita.</p>
  </div>
</section>
<section class="seccion" style="padding-top:24px">
  <div class="contenedor">
    <!-- PENDIENTE: que la doctora revise estas respuestas (tema de salud) y agregue precio de la valoración, formas de pago y financiación. -->
    <div class="preguntas">
{preguntas_html}
    </div>
    <div class="acciones"><a class="btn" href="{wa('Hola, Dra. Vanesa. Tengo una pregunta.')}" target="_blank" rel="noopener">{I_WA}¿Otra pregunta? Escríbenos</a></div>
  </div>
</section>
'''

# ---------- contacto.html ----------
contacto = f'''
<section class="cabecera-pagina">
  <div class="contenedor">
    <p class="antetitulo">Contacto</p>
    <h1>Contacto, <em>dirección</em> y horario</h1>
    <p class="intro">Escribe, llama o visita el consultorio en el Edificio Alto Prado, Bucaramanga.</p>
  </div>
</section>
<section class="seccion">
  <div class="contenedor">
    <div class="contacto-grid">
      <div class="contacto-tarjeta">{I_WA}<h2>WhatsApp</h2><p>La forma más rápida de agendar o resolver una duda.</p><a class="btn" href="{wa()}" target="_blank" rel="noopener">Escribir por WhatsApp</a></div>
      <div class="contacto-tarjeta">{I_TEL}<h2>Teléfono</h2><p>{TEL_VISIBLE}</p><a class="btn btn--linea" href="tel:{TEL}">Llamar ahora</a></div>
      <div class="contacto-tarjeta">{I_PIN}<h2>Dirección</h2><p>{DIRECCION}, {CIUDAD}.</p><a class="btn btn--linea" href="{MAPS}" target="_blank" rel="noopener">Cómo llegar</a></div>
    </div>
  </div>
</section>
<section class="seccion seccion--arena" aria-label="Ubicación y horario">
  <div class="contenedor">
    {bloque_ubicacion()}
  </div>
</section>
'''

DESC = {
    "index.html": ("Dra. Vanesa Gutiérrez | Diseño de sonrisa y lentes cerámicos en Bucaramanga",
                   "Odontóloga con especialización en estética (UNICID, Brasil). Diseño de sonrisa, carillas, lentes cerámicos, blanqueamiento e implantes en Bucaramanga. Agenda por WhatsApp."),
    "tratamientos.html": ("Tratamientos de odontología y estética dental | Dra. Vanesa Gutiérrez",
                          "Diseño de sonrisa, carillas y lentes cerámicos, blanqueamiento, implantes, ortodoncia, conductos y limpieza en Bucaramanga, explicados en pocas palabras."),
    "la-doctora.html": ("Dra. Vanesa Gutiérrez, odontóloga especialista en estética | Bucaramanga",
                        "Conoce a la Dra. Vanesa Gutiérrez: odontóloga con especialización en estética de la UNICID (Brasil). Consultorio en el Edificio Alto Prado, Bucaramanga."),
    "preguntas.html": ("Preguntas frecuentes sobre carillas, blanqueamiento y citas | Dra. Vanesa Gutiérrez",
                       "Qué son los lentes cerámicos, diferencia entre carillas de cerámica y resina, costo del diseño de sonrisa, horario y cómo pedir una cita."),
    "contacto.html": ("Contacto, dirección y horario | Dra. Vanesa Gutiérrez, Bucaramanga",
                      "Cra. 34 # 36-31, local 2, Edificio Alto Prado, Bucaramanga. Teléfono y WhatsApp 324 492 5383. Lunes a sábado 8 a. m. – 8 p. m., domingo 9 a. m. – 8 p. m."),
}
CUERPOS = {"index.html": inicio, "tratamientos.html": tratamientos, "la-doctora.html": doctora,
           "preguntas.html": preguntas, "contacto.html": contacto}

for archivo, cuerpo in CUERPOS.items():
    t, d = DESC[archivo]
    (DESTINO / archivo).write_text(pagina(archivo, t, d, cuerpo, jsonld=archivo in ("index.html", "contacto.html")), encoding="utf-8")
print("ok")
