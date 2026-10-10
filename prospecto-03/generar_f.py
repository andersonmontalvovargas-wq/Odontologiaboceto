"""Genera la propuesta F (Porcelana: durazno y cacao) con los mismos textos y datos de generar.py.

Uso: python3 prospecto-03/generar_f.py prospecto-03/sitio-f
Los textos de tratamientos, preguntas, horario y contacto viven en generar.py; aquí solo cambia la estructura.
Rasgos propios: portada con foto en óvalo, tratamientos como un muestrario de colores dentales que se
desliza de lado, página de tratamientos con foto fija que cambia al bajar y la primera cita en una línea
que se llena con el desplazamiento.
"""
import json, sys
from pathlib import Path

DESTINO = Path(sys.argv[1])

sys.path.insert(0, str(Path(__file__).parent))
_argv, sys.argv = sys.argv, [sys.argv[0]]
import generar as g  # noqa: E402  (solo se reutilizan sus datos)
sys.argv = _argv

VERSION = "20261010"  # Se cambia en cada publicación para que el navegador no use CSS o JS viejos.
FUENTES = "family=Cormorant:ital,wght@0,500;0,600;1,500;1,600&family=Manrope:wght@400;500;600;700"
TEMA = "#34202A"

# Fotos de referencia (Pexels). 11956948 no se usó en A–E.
g.FOTO_DESC[11956948] = "Labios de una mujer sonriendo"
HEROE, DOCTORA, BLANQUEAMIENTO = 11956948, 6812479, 3762400
NOTA_REF = "Foto de referencia, de un banco de imágenes"
NOTA_DOCTORA = "Foto de referencia del consultorio · aquí va la foto real de la doctora"

# Tonos de una guía de color dental, de más claro a más cálido: uno por tratamiento.
TONOS = ["#FBF6EE", "#F6EDDF", "#F2E5D2", "#EEDDC6", "#EAD5BA", "#E5CCAE", "#E0C3A3", "#DBBA98"]

PAGINAS = [("index.html", "Inicio"), ("tratamientos.html", "Tratamientos"), ("la-doctora.html", "La doctora"),
           ("preguntas.html", "Preguntas frecuentes"), ("contacto.html", "Contacto")]

PASOS = [
    ("Escribes o llamas", f"Por WhatsApp o al {g.TEL_VISIBLE}. Cuéntanos qué te gustaría mejorar y elige el día."),
    ("Valoración", "La doctora revisa tus dientes y encías y escucha lo que quieres cambiar de tu sonrisa."),
    ("Tu plan", "Te explica las opciones, los tiempos y el costo antes de empezar cualquier tratamiento."),
]

I_FLECHA = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6"/></svg>'
I_IZQ = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M19 12H5M11 6l-6 6 6 6"/></svg>'


def foto_trat(id_):
    return g.FOTO_TRAT.get(id_) or BLANQUEAMIENTO


def figura(id_, clase, w, h, nota, prioridad=False):
    """Foto de referencia con su descripción visible. Si no carga, queda el fondo de color y el texto."""
    return (f'<figure class="{clase}">{g.img(id_, "foto", w, h, prioridad)}'
            f'<figcaption><span>{nota}</span>{g.FOTO_DESC[id_]}</figcaption></figure>')


def corto(texto):
    return texto.split(". ")[0] + "."


def estado_horario():
    # Lo completa js/main.js con la hora de Bogotá. Sin JavaScript no se muestra y el horario sigue visible.
    return '<p class="estado" data-estado hidden><span class="estado-punto" aria-hidden="true"></span><span data-estado-texto></span></p>'


def semana():
    """Horario como tabla con una barra por día. js/main.js marca el día de hoy."""
    filas = []
    for i, (dia, horas) in enumerate(g.HORARIO):
        abre = 9 if dia == "Domingo" else 8
        # La barra va de 6 a. m. a 10 p. m.: inicio y ancho en porcentaje.
        izq, ancho = (abre - 6) / 16 * 100, (20 - abre) / 16 * 100
        num = (i + 1) % 7  # 0 = domingo, como Date.getDay()
        filas.append(f'<tr data-dia="{num}"><th scope="row">{dia}</th><td><span class="semana-horas">{horas}</span>'
                     f'<span class="semana-barra" aria-hidden="true"><span style="left:{izq:.1f}%;width:{ancho:.1f}%"></span></span></td></tr>')
    return (f'<table class="semana"><caption class="sr">Horario de atención</caption><tbody>{"".join(filas)}</tbody></table>'
            f'<p class="nota">En festivos el horario puede variar. Confírmalo por WhatsApp antes de ir.</p>')


def ficha_doctora():
    return f'''<dl class="ficha">
        <div><dt>Profesión</dt><dd>Odontóloga</dd></div>
        <div><dt>Especialización</dt><dd>Estética · UNICID, Universidade Cidade de São Paulo (Brasil)</dd></div>
        <div><dt>Enfoque</dt><dd>Diseño de sonrisa, carillas y lentes cerámicos, blanqueamiento</dd></div>
        <div><dt>También atiende</dt><dd>Odontología general, ortodoncia, implantes y coronas, conductos, limpieza y encías</dd></div>
        <div><dt>Consultorio</dt><dd>{g.DIRECCION}, {g.CIUDAD}</dd></div>
        <!-- PENDIENTE: título exacto de la especialización, universidad del pregrado, año de grado y registro profesional (ReTHUS). Solo lo que se pueda comprobar. -->
      </dl>'''


def sello():
    """Sello circular con texto. Gira con el desplazamiento (no solo), así que no necesita botón de pausa."""
    return '''<svg class="sello" viewBox="0 0 200 200" aria-hidden="true" focusable="false">
      <defs><path id="sello-circulo" d="M100 100m-74 0a74 74 0 1 1 148 0a74 74 0 1 1-148 0"/></defs>
      <circle cx="100" cy="100" r="98" fill="currentColor" opacity=".08"/>
      <text font-size="15.5" letter-spacing="3.2"><textPath href="#sello-circulo">DISEÑO DE SONRISA · LENTES CERÁMICOS · BUCARAMANGA ·</textPath></text>
      <path d="M86 76c-9 0-15 7-15 17 0 11 6 19 8 30 2 10 4 17 9 17 6 0 6-12 10-20 1-4 3-5 4-5s3 1 4 5c4 8 4 20 10 20 5 0 7-7 9-17 2-11 8-19 8-30 0-10-6-17-15-17-7 0-10 4-16 4s-9-4-16-4Z" fill="none" stroke="currentColor" stroke-width="3" stroke-linejoin="round"/>
    </svg>'''


def pagina(archivo, titulo, descripcion, cuerpo, jsonld=False):
    nav = "".join(f'<li><a href="{a}"{" aria-current=\"page\"" if a == archivo else ""}>{n}</a></li>' for a, n in PAGINAS[1:])
    nav_movil = "".join(f'<li><a href="{a}"{" aria-current=\"page\"" if a == archivo else ""}>{n}</a></li>' for a, n in PAGINAS)
    ld = ""
    if jsonld:
        ld = ('\n<!-- Dentist (LocalBusiness). PENDIENTE: url, geo con 5 decimales e image cuando haya dominio y fotos reales. Sin aggregateRating: las opiniones son de Google. -->\n'
              '<script type="application/ld+json">' + json.dumps(g.JSONLD, ensure_ascii=False) + '</script>')
    return f'''<!doctype html>
<html lang="es-CO">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<!-- Boceto: no indexar. Quitar en el sitio final (CLAUDE.md, sección 2). -->
<meta name="robots" content="noindex">
<title>{titulo}</title>
<meta name="description" content="{descripcion}">
<meta name="theme-color" content="{TEMA}">
<meta property="og:type" content="website">
<meta property="og:locale" content="es_CO">
<meta property="og:title" content="{titulo}">
<meta property="og:description" content="{descripcion}">
<!-- PENDIENTE: og:image (1200x630, foto real o logo) y og:url cuando el sitio tenga dominio. -->
<link rel="icon" href="assets/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="preconnect" href="https://images.pexels.com">
<link href="https://fonts.googleapis.com/css2?{FUENTES}&display=swap" rel="stylesheet">
<link rel="stylesheet" href="css/estilos.css?v={VERSION}">
<script>document.documentElement.classList.add("js")</script>
<script src="js/main.js?v={VERSION}" defer></script>{ld}
</head>
<body>
<a class="sr sr-foco" href="#contenido">Saltar al contenido</a>
<div class="aviso-propuesta" role="note"><strong>Propuesta de diseño F</strong> para el {g.CONSULTORIO}. No es el sitio oficial.</div>
<header class="encabezado">
  <div class="encabezado-barra">
    <a class="marca" href="index.html" aria-label="{g.CONSULTORIO}, ir al inicio">
      <!-- PENDIENTE: monograma provisional; reemplazar por el logo real si lo tiene. -->
      <span class="monograma" aria-hidden="true">VG</span>
      <span class="marca-texto">{g.CONSULTORIO}<small>Estética dental · Bucaramanga</small></span>
    </a>
    <nav class="nav" aria-label="Principal"><ul>{nav}</ul></nav>
    <a class="btn btn--sm btn--encabezado" href="{g.wa()}" target="_blank" rel="noopener">{g.I_WA}Agendar por WhatsApp</a>
    <button class="menu-boton" type="button" aria-expanded="false" aria-controls="menu-movil">Menú</button>
  </div>
  <nav class="menu-movil" id="menu-movil" aria-label="Menú móvil"><ul>{nav_movil}</ul>
    <a class="btn" href="{g.wa()}" target="_blank" rel="noopener">{g.I_WA}Agendar por WhatsApp</a>
    <a class="btn btn--linea" href="tel:{g.TEL}">{g.I_TEL}Llamar al {g.TEL_VISIBLE}</a>
  </nav>
</header>
<main id="contenido">
{cuerpo}
</main>
<footer class="pie">
  <div class="contenedor pie-grid">
    <div>
      <p class="pie-marca">{g.CONSULTORIO}</p>
      <p>Odontología y estética dental en Bucaramanga.<br>{g.DIRECCION}.<br>{g.CIUDAD}.</p>
      <p><a href="tel:{g.TEL}">{g.TEL_VISIBLE}</a> · <a href="{g.wa()}" target="_blank" rel="noopener">WhatsApp</a></p>
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
  <div class="contenedor">
    <!-- PENDIENTE: enlace a la Política de tratamiento de datos (Ley 1581 de 2012) del consultorio. -->
    <p class="pie-legal">Este sitio no tiene formularios ni recoge datos personales. La información de contacto y el horario se tomaron del perfil público del consultorio en Google ({g.FECHA_NOTA}). {g.AVISO_FOTOS}</p>
  </div>
</footer>
<a class="wa-flotante" href="{g.wa()}" target="_blank" rel="noopener" aria-label="Escribir por WhatsApp al {g.CONSULTORIO}">{g.I_WA}<span>WhatsApp</span></a>
</body>
</html>
'''


# ---------- Bloques compartidos ----------
def ubicacion(h="h2"):
    return f'''<div class="ubicacion">
      <div class="ubicacion-direccion revelar">
        <p class="antetitulo">Dónde atendemos</p>
        <{h}>Edificio Alto Prado, Bucaramanga</{h}>
        <p>El consultorio aparece en Google con dos placas del mismo edificio:</p>
        <ul class="placas">
          <li><span>Cra. 34</span># 36-31, local 2</li>
          <li><span>Cra. 34</span># 36-33</li>
        </ul>
        <p class="nota">{g.CIUDAD}.</p>
        <div class="acciones">
          <a class="btn" href="{g.MAPS}" target="_blank" rel="noopener">{g.I_PIN}Abrir en Google Maps</a>
          <a class="btn btn--linea" href="{g.WAZE}" target="_blank" rel="noopener">Abrir en Waze</a>
        </div>
        <!-- PENDIENTE: confirmar si hay parqueadero y acceso para silla de ruedas. -->
      </div>
      <div class="ubicacion-horario revelar">
        <p class="antetitulo">Horario</p>
        <{h}>Abierto los siete días</{h}>
        {estado_horario()}
        {semana()}
      </div>
    </div>'''


def opiniones(h="h2"):
    return f'''<div class="opiniones revelar">
      <div class="opiniones-cifra" aria-hidden="true"><span>{g.NOTA}</span>{g.ESTRELLAS}</div>
      <div>
        <p class="antetitulo">Opiniones en Google</p>
        <{h} id="t-opiniones">{g.OPINIONES} pacientes ya la calificaron</{h}>
        <p>El consultorio tiene una calificación de {g.NOTA} sobre 5 con {g.OPINIONES} opiniones en su perfil de Google ({g.FECHA_NOTA}). Puedes leerlas todas allí, escritas por los mismos pacientes.</p>
        <!-- PENDIENTE: 3 opiniones reales copiadas de Google, con nombre del autor, enlace a la reseña original y la marca Google. Sin datos estructurados de estrellas. -->
        <a class="btn btn--claro" href="{g.MAPS}" target="_blank" rel="noopener">Mira sus {g.OPINIONES} opiniones en Google{I_FLECHA}</a>
      </div>
    </div>'''


def pasos(h="h2"):
    items = "".join(f'<li class="revelar"><span class="paso-num" aria-hidden="true">{i}</span><h3>{t}</h3><p>{p}</p></li>'
                    for i, (t, p) in enumerate(PASOS, 1))
    return f'''<div class="pasos-grid">
      <div class="pasos-cabeza">
        <p class="antetitulo">Primera cita</p>
        <{h} id="t-pasos">Así es tu primera cita</{h}>
        <p>No necesitas saber qué tratamiento quieres. Para eso es la valoración.</p>
        <a class="btn" href="{g.wa()}" target="_blank" rel="noopener">{g.I_WA}Pedir mi valoración</a>
      </div>
      <!-- PENDIENTE: confirmar con la doctora cómo es la valoración, cuánto cuesta y si incluye radiografías. -->
      <ol class="pasos" data-progreso>{items}</ol>
    </div>'''


def cierre():
    return f'''<section class="cierre" aria-labelledby="t-cierre">
  <div class="contenedor cierre-caja revelar">
    <h2 id="t-cierre">Agenda tu valoración</h2>
    <p>Escribe por WhatsApp con un mensaje ya listo, o llama. Lunes a sábado de 8 a. m. a 8 p. m. y domingo de 9 a. m. a 8 p. m.</p>
    <div class="acciones acciones--centro">
      <a class="btn btn--claro" href="{g.wa()}" target="_blank" rel="noopener">{g.I_WA}Agenda tu valoración por WhatsApp</a>
      <a class="btn btn--linea-claro" href="tel:{g.TEL}">{g.I_TEL}Llamar al {g.TEL_VISIBLE}</a>
    </div>
  </div>
</section>'''


# ---------- Inicio ----------
def muestrario():
    tarjetas = "\n".join(f'''        <li class="muestra" style="--tono:{TONOS[i]}">
          <div class="muestra-tono"><span class="muestra-num">{i+1:02d}</span><span class="muestra-chip" aria-hidden="true"></span></div>
          {figura(foto_trat(id_), "muestra-foto", 560, 420, NOTA_REF)}
          <h3>{nombre}</h3>
          <p>{corto(texto)}</p>
          <p class="tambien"><span>También lo buscas como:</span> {tambien}</p>
          <a class="enlace" href="tratamientos.html#{id_}">Ver {nombre.lower()}{I_FLECHA}</a>
        </li>''' for i, (id_, nombre, texto, tambien, _) in enumerate(g.TRAT))
    return f'''<section class="seccion" aria-labelledby="t-tratamientos">
  <div class="contenedor seccion-cabeza seccion-cabeza--fila">
    <div class="revelar">
      <p class="antetitulo">Muestrario de tratamientos</p>
      <h2 id="t-tratamientos">Tratamientos del consultorio</h2>
      <p>La estética dental es el centro de la consulta, pero no lo único. Estos son los tratamientos que ofrece el consultorio, con el nombre con que los conoces.</p>
    </div>
    <div class="riel-controles" data-riel-controles hidden>
      <button type="button" class="riel-boton" data-riel="-1" aria-label="Ver tratamientos anteriores">{I_IZQ}</button>
      <button type="button" class="riel-boton" data-riel="1" aria-label="Ver más tratamientos">{I_FLECHA}</button>
    </div>
  </div>
  <ol class="riel" data-riel-lista aria-label="Tratamientos, deslizar de lado para ver los 8">
{tarjetas}
  </ol>
  <div class="contenedor"><a class="enlace" href="tratamientos.html">Ver los 8 tratamientos explicados{I_FLECHA}</a></div>
</section>'''


inicio = f'''
<section class="portada" aria-labelledby="t-portada">
  <div class="portada-texto">
    <p class="antetitulo">Odontología estética en Bucaramanga</p>
    <h1 id="t-portada"><span class="h1-chico">Consultorio</span> <span class="h1-nombre">Dra. Vanesa Gutiérrez</span><span class="sr">:</span> <em>diseño de sonrisa y lentes cerámicos</em></h1>
    <p class="intro">Odontóloga con especialización en estética de la UNICID (São Paulo, Brasil). En su consultorio también se atiende odontología general, ortodoncia, implantes, conductos y encías.</p>
    <!-- PENDIENTE: confirmar el título exacto de la especialización (el dato público dice "ESP. ESTÉTICA · UNICID"). -->
    <div class="acciones">
      <a class="btn" href="{g.wa()}" target="_blank" rel="noopener">{g.I_WA}Agenda tu valoración por WhatsApp</a>
      <a class="btn btn--linea" href="tel:{g.TEL}">{g.I_TEL}Llamar al {g.TEL_VISIBLE}</a>
    </div>
    <a class="calificacion" href="{g.MAPS}" target="_blank" rel="noopener">{g.ESTRELLAS}<strong>{g.NOTA} en Google</strong> · Mira sus {g.OPINIONES} opiniones</a>
  </div>
  <div class="portada-visual">
    <div class="ovalo" data-parallax>
      {figura(HEROE, "ovalo-foto", 720, 960, NOTA_REF, prioridad=True)}
    </div>
    <div class="sello-caja" data-sello>{sello()}</div>
  </div>
</section>

<section class="ficha-rapida" aria-label="Datos de contacto">
  <div class="contenedor ficha-rapida-grid">
    <div class="dato">{g.I_PIN}<div><h2>Dirección</h2><p>{g.DIRECCION}, {g.CIUDAD}</p><a href="{g.MAPS}" target="_blank" rel="noopener">Cómo llegar</a></div></div>
    <div class="dato">{g.I_WA}<div><h2>Teléfono y WhatsApp</h2><p><a href="tel:{g.TEL}">{g.TEL_VISIBLE}</a></p><a href="{g.wa()}" target="_blank" rel="noopener">Escribir por WhatsApp</a></div></div>
    <div class="dato">{g.I_RELOJ}<div><h2>Horario</h2><p>Lunes a sábado 8:00 a. m. – 8:00 p. m.<br>Domingo 9:00 a. m. – 8:00 p. m.</p>{estado_horario()}</div></div>
  </div>
</section>

{muestrario()}

<section class="seccion seccion--durazno" aria-labelledby="t-doctora">
  <div class="contenedor doctora">
    <div class="doctora-foto revelar">
      {figura(DOCTORA, "marco-arco", 800, 1000, NOTA_DOCTORA)}
      <!-- PENDIENTE: foto real de la {g.NOMBRE} (WebP, width/height declarados, loading="lazy"). -->
    </div>
    <div class="doctora-texto revelar">
      <p class="antetitulo">La doctora</p>
      <h2 id="t-doctora">Conoce a la Dra. Vanesa Gutiérrez</h2>
      <p class="destacado">Es odontóloga y se especializó en estética dental en Brasil. Su trabajo se concentra en el diseño de sonrisa, las carillas y los lentes cerámicos.</p>
      {ficha_doctora()}
      <a class="enlace" href="la-doctora.html">Su formación y su enfoque{I_FLECHA}</a>
    </div>
  </div>
</section>

<section class="seccion" aria-labelledby="t-pasos">
  <div class="contenedor">
    {pasos()}
  </div>
</section>

<section class="seccion seccion--cacao" aria-labelledby="t-opiniones">
  <div class="contenedor">
    {opiniones()}
  </div>
</section>

<section class="seccion" aria-label="Ubicación y horario">
  <div class="contenedor">
    {ubicacion()}
  </div>
</section>

{cierre()}
'''


# ---------- tratamientos.html: foto fija que cambia al bajar ----------
def tratamientos_f():
    chips = "".join(f'<li><a href="#{id_}" data-chip="{id_}">{nombre}</a></li>' for id_, nombre, *_ in g.TRAT)
    escenario = "".join(
        f'<figure class="escenario-foto{" activa" if i == 0 else ""}" data-escena="{id_}">'
        f'<img class="foto" src="{g.pexels(foto_trat(id_), 900, 1100)}" alt="" width="900" height="1100" loading="lazy" decoding="async" onerror="this.remove()">'
        f'<figcaption><span>{NOTA_REF}</span>{g.FOTO_DESC[foto_trat(id_)]}</figcaption></figure>'
        for i, (id_, *_) in enumerate(g.TRAT))
    articulos = "\n".join(f'''      <article class="trat" id="{id_}" data-trat="{id_}" style="--tono:{TONOS[i]}">
        {figura(foto_trat(id_), "trat-foto", 800, 560, NOTA_REF)}
        <p class="trat-num"><span class="muestra-chip" aria-hidden="true"></span>{i+1:02d} de 08</p>
        <h2>{nombre}</h2>
        <p>{texto}</p>
        <p class="tambien"><span>También lo buscas como:</span> {tambien}</p>
        <a class="btn btn--linea" href="{g.wa(msg)}" target="_blank" rel="noopener">{g.I_WA}Preguntar por {nombre.lower()}</a>
      </article>''' for i, (id_, nombre, texto, tambien, msg) in enumerate(g.TRAT))
    return f'''
<section class="cabecera-pagina">
  <div class="contenedor">
    <p class="antetitulo">Tratamientos</p>
    <h1>Tratamientos de odontología y <em>estética dental</em></h1>
    <p class="intro">La estética dental es el centro de la consulta, pero no lo único. Estos son los tratamientos que ofrece el consultorio, con el nombre con que los conoces.</p>
  </div>
</section>
<nav class="chips" aria-label="Ir a un tratamiento"><ul class="contenedor">{chips}</ul></nav>
<section class="seccion seccion--pegada">
  <div class="contenedor tratamientos">
    <!-- PENDIENTE: que la doctora revise y firme estos textos (tema de salud) y confirme qué tratamientos hace ella y cuáles un especialista aliado. -->
    <div class="escenario" aria-hidden="true">{escenario}</div>
    <div class="trat-lista">
{articulos}
    </div>
  </div>
</section>
{cierre()}
'''


# ---------- la-doctora.html ----------
doctora = f'''
<section class="cabecera-pagina cabecera-pagina--doctora">
  <div class="contenedor doctora">
    <div class="doctora-foto">
      {figura(DOCTORA, "marco-arco", 800, 1000, NOTA_DOCTORA, prioridad=True)}
      <!-- PENDIENTE: foto real de la {g.NOMBRE} (WebP, width/height declarados, fetchpriority="high", sin lazy). -->
    </div>
    <div class="doctora-texto">
      <p class="antetitulo">La doctora</p>
      <h1>Dra. Vanesa Gutiérrez, <em>odontóloga especialista en estética</em></h1>
      <p class="destacado">Es odontóloga y se especializó en estética dental en Brasil. Su trabajo se concentra en el diseño de sonrisa, las carillas y los lentes cerámicos.</p>
      {ficha_doctora()}
      <div class="acciones"><a class="btn" href="{g.wa()}" target="_blank" rel="noopener">{g.I_WA}Agenda tu valoración por WhatsApp</a></div>
    </div>
  </div>
</section>
<section class="seccion">
  <div class="contenedor enfoque">
    <div class="revelar">
      <h2>En qué se enfoca</h2>
      <p>La estética dental: cambiar la forma, el color o la proporción de los dientes para que la sonrisa se vea en armonía con la cara. Para eso usa carillas y lentes cerámicos, resinas y blanqueamiento, según lo que cada paciente necesite.</p>
    </div>
    <div class="revelar">
      <h2>También atiende</h2>
      <p>En el consultorio también se atiende ortodoncia, implantes y coronas, tratamiento de conductos, limpieza y encías. Puedes ver cada uno en <a href="tratamientos.html">Tratamientos</a>.</p>
    </div>
    <!-- PENDIENTE: un texto corto escrito por la doctora, en primera persona: por qué eligió la estética dental y cómo trabaja con sus pacientes. -->
  </div>
</section>
<section class="seccion seccion--durazno" aria-labelledby="t-pasos">
  <div class="contenedor">
    {pasos()}
  </div>
</section>
<section class="seccion seccion--cacao" aria-labelledby="t-opiniones">
  <div class="contenedor">
    {opiniones()}
  </div>
</section>
'''


# ---------- preguntas.html ----------
preguntas_lista = "\n".join(f'''      <article class="pregunta revelar">
        <span class="pregunta-num" aria-hidden="true">{i:02d}</span>
        <h2>{q}</h2>
        <p>{a}</p>
      </article>''' for i, (q, a) in enumerate(g.PREG, 1))
preguntas = f'''
<section class="seccion preguntas-pagina">
  <div class="contenedor preguntas-grid">
    <div class="preguntas-lateral">
      <p class="antetitulo">Preguntas frecuentes</p>
      <h1>Preguntas frecuentes sobre <em>carillas</em>, blanqueamiento y citas</h1>
      <p class="intro">Respuestas cortas a lo que más se pregunta antes de la primera cita.</p>
      <a class="btn" href="{g.wa('Hola, Dra. Vanesa. Tengo una pregunta.')}" target="_blank" rel="noopener">{g.I_WA}¿Otra pregunta? Escríbenos</a>
    </div>
    <!-- PENDIENTE: que la doctora revise estas respuestas (tema de salud) y agregue precio de la valoración, formas de pago y financiación. -->
    <div class="preguntas">
{preguntas_lista}
    </div>
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
    <div class="canales">
      <a class="canal canal--wa" href="{g.wa()}" target="_blank" rel="noopener">{g.I_WA}<span><strong>WhatsApp</strong>La forma más rápida de agendar o resolver una duda.</span>{I_FLECHA}</a>
      <a class="canal" href="tel:{g.TEL}">{g.I_TEL}<span><strong>Llamar al <span class="nowrap">{g.TEL_VISIBLE}</span></strong>Teléfono del consultorio, el mismo del WhatsApp.</span>{I_FLECHA}</a>
    </div>
  </div>
</section>
<section class="seccion seccion--durazno" aria-label="Ubicación y horario">
  <div class="contenedor">
    {ubicacion()}
  </div>
</section>
'''


CUERPOS = {"index.html": inicio, "tratamientos.html": tratamientos_f(), "la-doctora.html": doctora,
           "preguntas.html": preguntas, "contacto.html": contacto}

if __name__ == "__main__":
    for archivo, cuerpo in CUERPOS.items():
        t, d = g.DESC[archivo]
        (DESTINO / archivo).write_text(pagina(archivo, t, d, cuerpo, jsonld=archivo in ("index.html", "contacto.html")), encoding="utf-8")
    (DESTINO / "assets").mkdir(parents=True, exist_ok=True)
    (DESTINO / "assets" / "favicon.svg").write_text(
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><ellipse cx="32" cy="32" rx="26" ry="30" fill="#FBE4D8" stroke="#34202A" stroke-width="3"/>'
        '<text x="32" y="41" text-anchor="middle" font-family="Georgia, serif" font-style="italic" font-size="22" fill="#A3354B">VG</text></svg>\n', encoding="utf-8")
    print("ok f")
