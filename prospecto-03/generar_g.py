"""Genera la propuesta G (Nácar: transiciones al estilo de una página de producto) con los textos de generar.py.

Uso: python3 prospecto-03/generar_g.py prospecto-03/sitio-g
Rasgos propios: mucho blanco, una sola familia tipográfica (Geist), barra secundaria fija con el botón de
agendar, foto que crece hasta llenar la pantalla al bajar, texto que se ilumina palabra por palabra,
tratamientos que pasan de lado mientras se baja y fichas grises redondeadas.
Sin JavaScript (o con movimiento reducido) todo se ve como una página normal, de arriba abajo.
"""
import json, sys
from pathlib import Path

DESTINO = Path(sys.argv[1])
sys.path.insert(0, str(Path(__file__).parent))
_argv, sys.argv = sys.argv, [sys.argv[0]]
import generar as g  # noqa: E402  (solo se reutilizan sus datos)
sys.argv = _argv

VERSION = "20261010g"
FUENTES = "family=Geist:wght@400;500;600;700"
TEMA = "#FBFBFD"
HEROE, DOCTORA, BLANQUEAMIENTO = 30902075, 4269276, 3762408
CITA, PREGUNTAS, CONTACTO = 3845682, 6812479, 6812453
NOTA_REF = "Foto de referencia, de un banco de imágenes."
NOTA_DOCTORA = "Foto de referencia del consultorio. Aquí va la foto real de la doctora."

PAGINAS = [("index.html", "Inicio"), ("tratamientos.html", "Tratamientos"), ("la-doctora.html", "La doctora"),
           ("preguntas.html", "Preguntas frecuentes"), ("contacto.html", "Contacto")]
NOMBRE_SUB = {"index.html": "Dra. Vanesa Gutiérrez", "tratamientos.html": "Tratamientos", "la-doctora.html": "La doctora",
              "preguntas.html": "Preguntas frecuentes", "contacto.html": "Contacto"}
PASOS = [
    ("Escribes o llamas", f"Por WhatsApp o al {g.TEL_VISIBLE}. Cuéntanos qué te gustaría mejorar y elige el día."),
    ("Valoración", "La doctora revisa tus dientes y encías y escucha lo que quieres cambiar de tu sonrisa."),
    ("Tu plan", "Te explica las opciones, los tiempos y el costo antes de empezar cualquier tratamiento."),
]
CHEVRON = '<span class="chev" aria-hidden="true">›</span>'


def foto_trat(id_):
    return g.FOTO_TRAT.get(id_) or BLANQUEAMIENTO


def figura(id_, clase, w, h, nota, prioridad=False):
    """Foto con su descripción debajo, en texto gris pequeño."""
    return (f'<figure class="{clase}"><div class="marco">{g.img(id_, "foto", w, h, prioridad)}</div>'
            f'<figcaption>{g.FOTO_DESC[id_]}. {nota}</figcaption></figure>')


def corto(texto):
    return texto.split(". ")[0] + "."


def estado():
    return '<p class="estado" data-estado hidden><span class="estado-punto" aria-hidden="true"></span><span data-estado-texto></span></p>'


def horario_lista():
    filas = "".join(f'<li data-dia="{(i + 1) % 7}"><span>{d}</span><span>{h}</span></li>' for i, (d, h) in enumerate(g.HORARIO))
    return (f'<ul class="horario" aria-label="Horario de atención">{filas}</ul>'
            '<p class="nota">En festivos el horario puede variar. Confírmalo por WhatsApp antes de ir.</p>')


def especificaciones():
    return f'''<dl class="specs">
          <div><dt>Profesión</dt><dd>Odontóloga</dd></div>
          <div><dt>Especialización</dt><dd>Estética · UNICID, Universidade Cidade de São Paulo (Brasil)</dd></div>
          <div><dt>Enfoque</dt><dd>Diseño de sonrisa, carillas y lentes cerámicos, blanqueamiento</dd></div>
          <div><dt>También atiende</dt><dd>Odontología general, ortodoncia, implantes y coronas, conductos, limpieza y encías</dd></div>
          <div><dt>Consultorio</dt><dd>{g.DIRECCION}, {g.CIUDAD}</dd></div>
          <!-- PENDIENTE: título exacto de la especialización, universidad del pregrado, año de grado y registro profesional (ReTHUS). Solo lo que se pueda comprobar. -->
        </dl>'''


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
<div class="aviso-propuesta" role="note"><strong>Propuesta de diseño G</strong> para el {g.CONSULTORIO}. No es el sitio oficial.</div>
<header class="global">
  <div class="global-barra">
    <a class="marca" href="index.html" aria-label="{g.CONSULTORIO}, ir al inicio">
      <!-- PENDIENTE: monograma provisional; reemplazar por el logo real si lo tiene. -->
      <span class="monograma" aria-hidden="true">VG</span><span class="marca-texto">{g.CONSULTORIO}</span>
    </a>
    <nav class="nav" aria-label="Principal"><ul>{nav}</ul></nav>
    <button class="menu-boton" type="button" aria-expanded="false" aria-controls="menu-movil">Menú</button>
  </div>
  <nav class="menu-movil" id="menu-movil" aria-label="Menú móvil"><ul>{nav_movil}</ul></nav>
</header>
<div class="subnav">
  <div class="subnav-barra">
    <p class="subnav-titulo">{NOMBRE_SUB[archivo]}</p>
    <a class="subnav-tel" href="tel:{g.TEL}">{g.TEL_VISIBLE}</a>
    <a class="pildora pildora--sm" href="{g.wa()}" target="_blank" rel="noopener">Agendar</a>
  </div>
</div>
<main id="contenido">
{cuerpo}
</main>
<footer class="pie">
  <div class="contenedor">
    <p class="pie-nota">{g.AVISO_FOTOS} La información de contacto y el horario se tomaron del perfil público del consultorio en Google ({g.FECHA_NOTA}). Este sitio no tiene formularios ni recoge datos personales.</p>
    <div class="pie-grid">
      <div><h2>{g.CONSULTORIO}</h2><p>Odontología y estética dental en Bucaramanga.<br>{g.DIRECCION}.<br>{g.CIUDAD}.</p></div>
      <div><h2>Contacto</h2><p><a href="tel:{g.TEL}">{g.TEL_VISIBLE}</a><br><a href="{g.wa()}" target="_blank" rel="noopener">WhatsApp</a></p></div>
      <div><h2>Horario</h2><p>Lunes a sábado: 8:00 a. m. – 8:00 p. m.<br>Domingo: 9:00 a. m. – 8:00 p. m.<br>En festivos puede variar.</p></div>
      <div><h2>Páginas</h2><ul>{nav_movil}</ul></div>
    </div>
    <!-- PENDIENTE: enlace a la Política de tratamiento de datos (Ley 1581 de 2012) del consultorio. -->
  </div>
</footer>
<a class="wa-flotante" href="{g.wa()}" target="_blank" rel="noopener" aria-label="Escribir por WhatsApp al {g.CONSULTORIO}">{g.I_WA}</a>
</body>
</html>
'''


# ---------- Bloques ----------
def luz(texto, clase="luz"):
    """Párrafo que se ilumina palabra por palabra al bajar. El texto está completo en el HTML."""
    return f'<p class="{clase}" data-luz>{texto}</p>'


def datos():
    return f'''<section class="seccion seccion--gris" aria-label="Datos de contacto">
  <div class="contenedor fichas fichas--3">
    <div class="ficha aparecer"><p class="ficha-etiqueta">Dirección</p><h2>Edificio Alto Prado</h2><p>{g.DIRECCION}, {g.CIUDAD}.</p><a class="enlace" href="{g.MAPS}" target="_blank" rel="noopener">Cómo llegar {CHEVRON}</a></div>
    <div class="ficha aparecer"><p class="ficha-etiqueta">Teléfono y WhatsApp</p><h2><a class="sin-linea" href="tel:{g.TEL}">{g.TEL_VISIBLE}</a></h2><p>Escribe o llama para agendar tu valoración.</p><a class="enlace" href="{g.wa()}" target="_blank" rel="noopener">Escribir por WhatsApp {CHEVRON}</a></div>
    <div class="ficha aparecer"><p class="ficha-etiqueta">Horario</p><h2>Abierto los siete días</h2><p>Lunes a sábado 8:00 a. m. – 8:00 p. m.<br>Domingo 9:00 a. m. – 8:00 p. m.</p>{estado()}</div>
  </div>
</section>'''


def pasos():
    items = "".join(f'<li class="ficha aparecer"><span class="paso-num" aria-hidden="true">{i}</span><h3>{t}</h3><p>{p}</p></li>'
                    for i, (t, p) in enumerate(PASOS, 1))
    return f'''<section class="seccion" aria-labelledby="t-pasos">
  <div class="contenedor">
    <div class="cabeza aparecer">
      <h2 id="t-pasos">Así es tu primera cita</h2>
      <p>No necesitas saber qué tratamiento quieres. Para eso es la valoración.</p>
    </div>
    <!-- PENDIENTE: confirmar con la doctora cómo es la valoración, cuánto cuesta y si incluye radiografías. -->
    <ol class="fichas fichas--3 pasos">{items}</ol>
    <div class="acciones acciones--centro"><a class="pildora" href="{g.wa()}" target="_blank" rel="noopener">{g.I_WA}Pedir mi valoración</a></div>
    {figura(CITA, "foto-ancha aparecer", 1400, 700, NOTA_REF)}
  </div>
</section>'''


def opiniones():
    return f'''<section class="seccion seccion--negra" aria-labelledby="t-opiniones">
  <div class="contenedor centro">
    <p class="cifra aparecer" aria-hidden="true">{g.NOTA}</p>
    <div class="aparecer">{g.ESTRELLAS}</div>
    <h2 id="t-opiniones" class="aparecer">{g.OPINIONES} opiniones en Google.</h2>
    <p class="aparecer texto-medio">El consultorio tiene una calificación de {g.NOTA} sobre 5 con {g.OPINIONES} opiniones en su perfil de Google ({g.FECHA_NOTA}). Puedes leerlas todas allí, escritas por los mismos pacientes.</p>
    <!-- PENDIENTE: 3 opiniones reales copiadas de Google, con nombre del autor, enlace a la reseña original y la marca Google. Sin datos estructurados de estrellas. -->
    <a class="enlace enlace--claro aparecer" href="{g.MAPS}" target="_blank" rel="noopener">Mira sus {g.OPINIONES} opiniones en Google {CHEVRON}</a>
  </div>
</section>'''


def ubicacion():
    return f'''<section class="seccion seccion--gris" aria-labelledby="t-ubicacion">
  <div class="contenedor">
    <div class="cabeza aparecer"><h2 id="t-ubicacion">Dónde atendemos.</h2><p>Edificio Alto Prado, {g.CIUDAD}.</p></div>
    <div class="fichas fichas--2">
      <div class="ficha aparecer">
        <p class="ficha-etiqueta">Dirección</p>
        <h3>Dos placas, un mismo edificio</h3>
        <p>El consultorio aparece en Google con las dos:</p>
        <ul class="placas"><li>Cra. 34 # 36-31, local 2</li><li>Cra. 34 # 36-33</li></ul>
        <div class="acciones">
          <a class="pildora" href="{g.MAPS}" target="_blank" rel="noopener">{g.I_PIN}Abrir en Google Maps</a>
          <a class="pildora pildora--linea" href="{g.WAZE}" target="_blank" rel="noopener">Abrir en Waze</a>
        </div>
        <!-- PENDIENTE: confirmar si hay parqueadero y acceso para silla de ruedas. -->
      </div>
      <div class="ficha aparecer">
        <p class="ficha-etiqueta">Horario</p>
        <h3>Abierto los siete días</h3>
        {estado()}
        {horario_lista()}
      </div>
    </div>
  </div>
</section>'''


def cierre():
    return f'''<section class="seccion cierre" aria-labelledby="t-cierre">
  <div class="contenedor centro aparecer">
    <h2 id="t-cierre" class="titulo-grande"><span class="degradado">Agenda tu valoración.</span></h2>
    <p class="texto-medio">Escribe por WhatsApp con un mensaje ya listo, o llama. Lunes a sábado de 8 a. m. a 8 p. m. y domingo de 9 a. m. a 8 p. m.</p>
    <div class="acciones acciones--centro">
      <a class="pildora" href="{g.wa()}" target="_blank" rel="noopener">{g.I_WA}Agenda tu valoración por WhatsApp</a>
      <a class="enlace" href="tel:{g.TEL}">Llamar al {g.TEL_VISIBLE} {CHEVRON}</a>
    </div>
  </div>
</section>'''


def tratamientos_desfile():
    """Inicio: las 8 tarjetas pasan de lado mientras se baja (en computador). En celular, una debajo de otra."""
    tarjetas = "\n".join(f'''        <li class="panel">
          {figura(foto_trat(id_), "panel-foto", 900, 700, NOTA_REF)}
          <div class="panel-texto">
            <p class="panel-num">{i+1:02d} / 08</p>
            <h3>{nombre}</h3>
            <p>{corto(texto)}</p>
            <p class="tambien"><span>También lo buscas como:</span> {tambien}</p>
            <a class="enlace" href="tratamientos.html#{id_}">Ver {nombre.lower()} {CHEVRON}</a>
          </div>
        </li>''' for i, (id_, nombre, texto, tambien, _) in enumerate(g.TRAT))
    return f'''<section class="desfile-seccion" aria-labelledby="t-tratamientos">
  <div class="contenedor cabeza aparecer">
    <h2 id="t-tratamientos">Tratamientos del consultorio.</h2>
    <p>La estética dental es el centro de la consulta, pero no lo único. Estos son los tratamientos que ofrece el consultorio, con el nombre con que los conoces.</p>
  </div>
  <div class="desfile" data-desfile>
    <div class="desfile-pegado">
      <ol class="desfile-pista" data-desfile-pista>
{tarjetas}
      </ol>
      <div class="desfile-barra" aria-hidden="true"><span></span></div>
    </div>
  </div>
  <div class="contenedor centro"><a class="enlace" href="tratamientos.html">Ver los 8 tratamientos explicados {CHEVRON}</a></div>
</section>'''


# ---------- Inicio ----------
inicio = f'''
<section class="heroe centro" aria-labelledby="t-heroe">
  <div class="contenedor">
    <p class="heroe-ante">Odontología estética en Bucaramanga</p>
    <h1 id="t-heroe"><span class="h1-marca">Consultorio Dra. Vanesa Gutiérrez</span><span class="sr">:</span> <span class="h1-lema degradado">Diseño de sonrisa y lentes cerámicos.</span></h1>
    <p class="texto-medio">Odontóloga con especialización en estética de la UNICID (São Paulo, Brasil). En su consultorio también se atiende odontología general, ortodoncia, implantes, conductos y encías.</p>
    <!-- PENDIENTE: confirmar el título exacto de la especialización (el dato público dice "ESP. ESTÉTICA · UNICID"). -->
    <div class="acciones acciones--centro">
      <a class="pildora" href="{g.wa()}" target="_blank" rel="noopener">{g.I_WA}Agenda tu valoración por WhatsApp</a>
      <a class="enlace" href="tel:{g.TEL}">Llamar al {g.TEL_VISIBLE} {CHEVRON}</a>
    </div>
    <a class="calificacion" href="{g.MAPS}" target="_blank" rel="noopener">{g.ESTRELLAS}<span><strong>{g.NOTA} en Google</strong> · Mira sus {g.OPINIONES} opiniones</span></a>
  </div>
</section>

<section class="escala" data-escala aria-label="El consultorio">
  <div class="escala-pegado">
    {figura(HEROE, "escala-foto", 1600, 1000, NOTA_REF, prioridad=True)}
  </div>
</section>

{datos()}

<section class="seccion seccion--negra" aria-labelledby="t-doctora">
  <div class="contenedor angosto">
    <p class="ficha-etiqueta ficha-etiqueta--claro aparecer">La doctora</p>
    <h2 id="t-doctora" class="aparecer">Conoce a la Dra. Vanesa Gutiérrez.</h2>
    {luz("Es odontóloga y se especializó en estética dental en Brasil. Su trabajo se concentra en el diseño de sonrisa, las carillas y los lentes cerámicos.")}
    <a class="enlace enlace--claro aparecer" href="la-doctora.html">Su formación y su enfoque {CHEVRON}</a>
  </div>
</section>

{tratamientos_desfile()}

{pasos()}

{opiniones()}

{ubicacion()}

{cierre()}
'''


# ---------- tratamientos.html ----------
def tratamientos_pagina():
    indice = "".join(f'<li><a href="#{id_}"><span>{i+1:02d}</span>{nombre}</a></li>' for i, (id_, nombre, *_) in enumerate(g.TRAT))
    capitulos = "\n".join(f'''<section class="capitulo{" seccion--gris" if i % 2 else ""}" id="{id_}" aria-labelledby="t-{id_}">
  <div class="contenedor centro angosto">
    <p class="ficha-etiqueta aparecer">{i+1:02d} de 08</p>
    <h2 id="t-{id_}" class="aparecer">{nombre}.</h2>
    <p class="texto-medio aparecer">{texto}</p>
    <p class="tambien aparecer"><span>También lo buscas como:</span> {tambien}</p>
    <div class="acciones acciones--centro aparecer"><a class="pildora" href="{g.wa(msg)}" target="_blank" rel="noopener">{g.I_WA}Preguntar por {nombre.lower()}</a></div>
  </div>
  <div class="contenedor">{figura(foto_trat(id_), "foto-ancha crecer", 1400, 760, NOTA_REF)}</div>
</section>''' for i, (id_, nombre, texto, tambien, msg) in enumerate(g.TRAT))
    return f'''
<section class="heroe heroe--pagina centro">
  <div class="contenedor">
    <h1><span class="degradado">Tratamientos</span> de odontología y estética dental</h1>
    <p class="texto-medio">La estética dental es el centro de la consulta, pero no lo único. Estos son los tratamientos que ofrece el consultorio, con el nombre con que los conoces.</p>
    <nav aria-label="Ir a un tratamiento"><ol class="indice">{indice}</ol></nav>
  </div>
</section>
<!-- PENDIENTE: que la doctora revise y firme estos textos (tema de salud) y confirme qué tratamientos hace ella y cuáles un especialista aliado. -->
{capitulos}
{cierre()}
'''


# ---------- la-doctora.html ----------
doctora = f'''
<section class="heroe heroe--pagina centro">
  <div class="contenedor">
    <p class="heroe-ante">La doctora</p>
    <h1>Dra. Vanesa Gutiérrez, <span class="degradado">odontóloga especialista en estética</span></h1>
    <p class="texto-medio">Es odontóloga y se especializó en estética dental en Brasil. Su trabajo se concentra en el diseño de sonrisa, las carillas y los lentes cerámicos.</p>
    <div class="acciones acciones--centro"><a class="pildora" href="{g.wa()}" target="_blank" rel="noopener">{g.I_WA}Agenda tu valoración por WhatsApp</a></div>
  </div>
  <div class="contenedor">
    {figura(DOCTORA, "foto-ancha", 1400, 760, NOTA_DOCTORA, prioridad=True)}
    <!-- PENDIENTE: foto real de la {g.NOMBRE} (WebP, width/height declarados, fetchpriority="high", sin lazy). -->
  </div>
</section>
<section class="seccion seccion--negra" aria-labelledby="t-enfoque">
  <div class="contenedor angosto">
    <h2 id="t-enfoque" class="aparecer">En qué se enfoca.</h2>
    {luz("La estética dental: cambiar la forma, el color o la proporción de los dientes para que la sonrisa se vea en armonía con la cara. Para eso usa carillas y lentes cerámicos, resinas y blanqueamiento, según lo que cada paciente necesite.")}
    <p class="texto-medio texto-gris aparecer">En el consultorio también se atiende ortodoncia, implantes y coronas, tratamiento de conductos, limpieza y encías. Puedes ver cada uno en <a class="enlace--claro" href="tratamientos.html">Tratamientos</a>.</p>
    <!-- PENDIENTE: un texto corto escrito por la doctora, en primera persona: por qué eligió la estética dental y cómo trabaja con sus pacientes. -->
  </div>
</section>
<section class="seccion" aria-labelledby="t-specs">
  <div class="contenedor angosto">
    <h2 id="t-specs" class="aparecer">Formación y consultorio.</h2>
    <div class="aparecer">{especificaciones()}</div>
  </div>
</section>
{pasos()}
{opiniones()}
'''


# ---------- preguntas.html ----------
preguntas_fichas = "\n".join(f'''      <article class="ficha aparecer">
        <h2>{q}</h2>
        <p>{a}</p>
      </article>''' for q, a in g.PREG)
preguntas = f'''
<section class="heroe heroe--pagina centro">
  <div class="contenedor">
    <h1>Preguntas frecuentes sobre <span class="degradado">carillas, blanqueamiento y citas</span></h1>
    <p class="texto-medio">Respuestas cortas a lo que más se pregunta antes de la primera cita.</p>
  </div>
</section>
<section class="seccion seccion--gris seccion--pegada">
  <div class="contenedor">
    <!-- PENDIENTE: que la doctora revise estas respuestas (tema de salud) y agregue precio de la valoración, formas de pago y financiación. -->
    <div class="fichas fichas--2 preguntas">
{preguntas_fichas}
    </div>
    <div class="acciones acciones--centro"><a class="pildora" href="{g.wa('Hola, Dra. Vanesa. Tengo una pregunta.')}" target="_blank" rel="noopener">{g.I_WA}¿Otra pregunta? Escríbenos</a></div>
    {figura(PREGUNTAS, "foto-ancha aparecer", 1400, 700, NOTA_REF)}
  </div>
</section>
'''


# ---------- contacto.html ----------
contacto = f'''
<section class="heroe heroe--pagina centro">
  <div class="contenedor">
    <h1>Contacto, <span class="degradado">dirección</span> y horario</h1>
    <p class="texto-medio">Escribe, llama o visita el consultorio en el Edificio Alto Prado, Bucaramanga.</p>
  </div>
  <div class="contenedor fichas fichas--2">
    <a class="ficha ficha--negra ficha--enlace" href="{g.wa()}" target="_blank" rel="noopener">{g.I_WA}<h2>WhatsApp</h2><p>La forma más rápida de agendar o resolver una duda.</p><span class="enlace enlace--claro">Escribir {CHEVRON}</span></a>
    <a class="ficha ficha--enlace" href="tel:{g.TEL}">{g.I_TEL}<h2>{g.TEL_VISIBLE}</h2><p>Teléfono del consultorio, el mismo del WhatsApp.</p><span class="enlace">Llamar {CHEVRON}</span></a>
  </div>
  <div class="contenedor">
    {figura(CONTACTO, "foto-ancha", 1400, 700, NOTA_REF)}
    <!-- PENDIENTE: foto real de la fachada o la entrada del Edificio Alto Prado. -->
  </div>
</section>
{ubicacion()}
'''

CUERPOS = {"index.html": inicio, "tratamientos.html": tratamientos_pagina(), "la-doctora.html": doctora,
           "preguntas.html": preguntas, "contacto.html": contacto}

if __name__ == "__main__":
    for archivo, cuerpo in CUERPOS.items():
        t, d = g.DESC[archivo]
        (DESTINO / archivo).write_text(pagina(archivo, t, d, cuerpo, jsonld=archivo in ("index.html", "contacto.html")), encoding="utf-8")
    (DESTINO / "assets").mkdir(parents=True, exist_ok=True)
    (DESTINO / "assets" / "favicon.svg").write_text(
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><defs><linearGradient id="d" x1="0" y1="0" x2="1" y2="1">'
        '<stop offset="0" stop-color="#B0246A"/><stop offset="1" stop-color="#7A3FB5"/></linearGradient></defs>'
        '<rect width="64" height="64" rx="16" fill="url(#d)"/><text x="32" y="41" text-anchor="middle" font-family="Helvetica, Arial, sans-serif" '
        'font-weight="600" font-size="22" fill="#FFFFFF">VG</text></svg>\n', encoding="utf-8")
    print("ok g")
