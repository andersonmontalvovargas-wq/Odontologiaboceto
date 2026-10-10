"""Genera las propuestas D (editorial) y E (mosaico) con los mismos textos y datos de generar.py.

Uso: python3 prospecto-03/generar_de.py prospecto-03/sitio-d d   (variantes: d, e)
Los textos de tratamientos, preguntas, horario y contacto viven en generar.py; aquí solo cambia la estructura.
"""
import json, sys
from pathlib import Path

DESTINO = Path(sys.argv[1])
VARIANTE = sys.argv[2]
assert VARIANTE in ("d", "e"), "variantes: d, e"

sys.path.insert(0, str(Path(__file__).parent))
_argv, sys.argv = sys.argv, [sys.argv[0]]
import generar as g  # noqa: E402  (solo se reutilizan sus datos)
sys.argv = _argv

CONF = {
    "d": {"fuentes": "family=Instrument+Serif:ital@0;1&family=Inter+Tight:wght@400;500;600",
          "tema": "#2B1E2A", "favicon": ("#F6EFEA", "#2B1E2A"), "nombre": "Editorial",
          "heroe": 3762408, "doctora": 30902075, "blanqueamiento": 3762400},
    "e": {"fuentes": "family=Hanken+Grotesk:wght@400;500;600;700&family=Young+Serif",
          "tema": "#8E2F55", "favicon": ("#8E2F55", "#FFFFFF"), "nombre": "Mosaico",
          "heroe": 3762400, "doctora": 4269276, "blanqueamiento": 3762408},
}[VARIANTE]

PAGINAS = [("index.html", "Inicio"), ("tratamientos.html", "Tratamientos"), ("la-doctora.html", "La doctora"),
           ("preguntas.html", "Preguntas frecuentes"), ("contacto.html", "Contacto")]

PASOS = [
    ("Escribes o llamas", f"Por WhatsApp o al {g.TEL_VISIBLE}. Cuéntanos qué te gustaría mejorar y elige el día."),
    ("Valoración", "La doctora revisa tus dientes y encías y escucha lo que quieres cambiar de tu sonrisa."),
    ("Tu plan", "Te explica las opciones, los tiempos y el costo antes de empezar cualquier tratamiento."),
]

def foto_trat(id_):
    return g.FOTO_TRAT.get(id_) or CONF["blanqueamiento"]

def figura(id_, clase, w, h, nota, prioridad=False):
    """Foto de referencia con su letrero visible. Si no carga, queda el fondo de color y el letrero."""
    return (f'<figure class="{clase}">{g.img(id_, "foto", w, h, prioridad)}'
            f'<figcaption>{nota}</figcaption></figure>')

NOTA_REF = "Foto de referencia, de un banco de imágenes"
NOTA_DOCTORA = "Foto de referencia del consultorio · aquí va la foto real de la doctora"

def estado_horario():
    # Lo completa js/main.js con la hora de Bogotá. Sin JavaScript no se muestra.
    return '<p class="estado" data-estado hidden><span class="estado-punto" aria-hidden="true"></span><span data-estado-texto></span></p>'

def tabla_horario():
    filas = "".join(f'<tr><th scope="row">{d}</th><td>{h}</td></tr>' for d, h in g.HORARIO)
    return (f'<table class="tabla-horario"><caption class="sr">Horario de atención</caption><tbody>{filas}</tbody></table>'
            f'<p class="nota">En festivos el horario puede variar. Confírmalo por WhatsApp antes de ir.</p>')

def ficha_doctora():
    return f'''<dl class="ficha">
        <div><dt>Profesión</dt><dd>Odontóloga</dd></div>
        <div><dt>Especialización</dt><dd>Estética · UNICID, Universidade Cidade de São Paulo (Brasil)</dd></div>
        <div><dt>Enfoque</dt><dd>Diseño de sonrisa, carillas y lentes cerámicos, blanqueamiento</dd></div>
        <div><dt>También atiende</dt><dd>Odontología general, ortodoncia, implantes y coronas, conductos, limpieza y encías</dd></div>
        <div><dt>Consultorio</dt><dd>{g.DIRECCION}, {g.CIUDAD}</dd></div>
        <!-- PENDIENTE: universidad del pregrado, año de grado y registro profesional (ReTHUS). Solo lo que se pueda comprobar. -->
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
<meta name="theme-color" content="{CONF['tema']}">
<meta property="og:type" content="website">
<meta property="og:locale" content="es_CO">
<meta property="og:title" content="{titulo}">
<meta property="og:description" content="{descripcion}">
<!-- PENDIENTE: og:image (1200x630, foto real o logo) y og:url cuando el sitio tenga dominio. -->
<link rel="icon" href="assets/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="preconnect" href="https://images.pexels.com">
<link href="https://fonts.googleapis.com/css2?{CONF['fuentes']}&display=swap" rel="stylesheet">
<link rel="stylesheet" href="css/estilos.css">
<script>document.documentElement.classList.add("js")</script>
<script src="js/main.js" defer></script>{ld}
</head>
<body>
<a class="sr" href="#contenido">Saltar al contenido</a>
<div class="aviso-propuesta" role="note"><strong>Propuesta de diseño {VARIANTE.upper()}</strong> para el {g.CONSULTORIO}. No es el sitio oficial.</div>
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
  <nav class="menu-movil" id="menu-movil" aria-label="Menú móvil"><ul>{nav_movil}</ul></nav>
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
<a class="wa-flotante" href="{g.wa()}" target="_blank" rel="noopener" aria-label="Escribir por WhatsApp al {g.CONSULTORIO}">{g.I_WA}WhatsApp</a>
</body>
</html>
'''

# ---------- Bloques compartidos ----------
def ubicacion():
    return f'''<div class="ubicacion">
      <div>
        <h2>Dónde atendemos</h2>
        <p class="direccion">{g.DIRECCION}<br>{g.CIUDAD}</p>
        <div class="acciones">
          <a class="btn" href="{g.MAPS}" target="_blank" rel="noopener">{g.I_PIN}Abrir en Google Maps</a>
          <a class="btn btn--linea" href="{g.WAZE}" target="_blank" rel="noopener">Abrir en Waze</a>
        </div>
        <!-- PENDIENTE: confirmar si hay parqueadero y acceso para silla de ruedas. -->
      </div>
      <div>
        <h2>Horario de atención</h2>
        {estado_horario()}
        {tabla_horario()}
      </div>
    </div>'''

def opiniones():
    return f'''<div class="opiniones">
      <p class="opiniones-cifra" aria-hidden="true">{g.NOTA}</p>
      <div>
        <h2 id="t-opiniones">Lo que dicen sus pacientes en Google</h2>
        {g.ESTRELLAS}
        <p>El consultorio tiene una calificación de {g.NOTA} sobre 5 con {g.OPINIONES} opiniones en su perfil de Google ({g.FECHA_NOTA}). Puedes leerlas todas allí, escritas por los mismos pacientes.</p>
        <!-- PENDIENTE: 3 opiniones reales copiadas de Google, con nombre del autor, enlace a la reseña original y la marca Google. Sin datos estructurados de estrellas. -->
        <a class="btn btn--linea" href="{g.MAPS}" target="_blank" rel="noopener">Mira sus {g.OPINIONES} opiniones en Google</a>
      </div>
    </div>'''

def pasos():
    items = "".join(f'<li><h3>{t}</h3><p>{p}</p></li>' for t, p in PASOS)
    return f'''<div class="seccion-cabeza">
      <h2 id="t-pasos">Así es tu primera cita</h2>
      <p>No necesitas saber qué tratamiento quieres. Para eso es la valoración.</p>
    </div>
    <!-- PENDIENTE: confirmar con la doctora cómo es la valoración, cuánto cuesta y si incluye radiografías. -->
    <ol class="pasos">{items}</ol>
    <div class="acciones"><a class="btn" href="{g.wa()}" target="_blank" rel="noopener">{g.I_WA}Pedir mi valoración</a></div>'''

def corto(texto):
    return texto.split(". ")[0] + "."

# ---------- Inicio D: portada dividida, ficha e índice ----------
def inicio_d():
    filas = "\n".join(f'''        <li class="indice-fila revelar">
          <span class="numero">{i+1:02d}</span>
          {g.img(foto_trat(id_), "indice-foto", 480, 360)}
          <div class="indice-texto">
            <h3>{nombre}</h3>
            <p>{corto(texto)}</p>
          </div>
          <p class="indice-tambien"><span>También:</span> {tambien}</p>
          <a class="indice-enlace" href="tratamientos.html#{id_}" aria-label="Ver {nombre.lower()}"><span aria-hidden="true">→</span></a>
        </li>''' for i, (id_, nombre, texto, tambien, _) in enumerate(g.TRAT))
    return f'''
<section class="portada">
  {figura(CONF["heroe"], "portada-foto", 900, 1200, NOTA_REF, prioridad=True)}
  <div class="portada-texto">
    <p class="antetitulo">Odontología estética · Bucaramanga</p>
    <h1><span class="h1-nombre">{g.CONSULTORIO}:</span> <span class="h1-lema">diseño de sonrisa y <em>lentes cerámicos</em></span></h1>
    <p class="intro">Odontóloga con especialización en estética de la UNICID (São Paulo, Brasil). En su consultorio también se atiende odontología general, ortodoncia, implantes, conductos y encías.</p>
    <div class="acciones">
      <a class="btn" href="{g.wa()}" target="_blank" rel="noopener">{g.I_WA}Agenda tu valoración por WhatsApp</a>
      <a class="btn btn--linea" href="tel:{g.TEL}">{g.I_TEL}Llamar al {g.TEL_VISIBLE}</a>
    </div>
    <dl class="ficha ficha--portada">
      <div><dt>Calificación</dt><dd><a href="{g.MAPS}" target="_blank" rel="noopener">{g.ESTRELLAS} {g.NOTA} en Google · {g.OPINIONES} opiniones</a></dd></div>
      <div><dt>Dirección</dt><dd>{g.DIRECCION}, {g.CIUDAD}</dd></div>
      <div><dt>Teléfono y WhatsApp</dt><dd><a href="tel:{g.TEL}">{g.TEL_VISIBLE}</a></dd></div>
      <div><dt>Horario</dt><dd>Lunes a sábado 8 a. m. – 8 p. m. · Domingo 9 a. m. – 8 p. m.{estado_horario()}</dd></div>
    </dl>
  </div>
</section>

<section class="seccion" aria-labelledby="t-tratamientos">
  <div class="contenedor">
    <div class="seccion-cabeza seccion-cabeza--lado">
      <p class="antetitulo">Índice</p>
      <div>
        <h2 id="t-tratamientos">Tratamientos del consultorio</h2>
        <p>La estética dental es el centro de la consulta, pero no lo único. Estos son los tratamientos que ofrece el consultorio, con el nombre con que los conoces.</p>
        <p class="nota">{g.AVISO_FOTOS}</p>
      </div>
    </div>
    <ol class="indice-trat">
{filas}
    </ol>
  </div>
</section>

<section class="seccion seccion--tinta" aria-labelledby="t-doctora">
  <div class="contenedor perfil">
    {figura(CONF["doctora"], "perfil-foto", 800, 1000, NOTA_DOCTORA)}
    <div class="revelar">
      <p class="antetitulo">Quién te atiende</p>
      <h2 id="t-doctora">Conoce a la {g.NOMBRE}</h2>
      <p>Es odontóloga y se especializó en estética dental en Brasil. Su trabajo se concentra en el diseño de sonrisa, las carillas y los lentes cerámicos.</p>
      {ficha_doctora()}
      <a class="btn btn--claro" href="la-doctora.html">Más sobre la doctora</a>
    </div>
  </div>
</section>

<section class="seccion" aria-labelledby="t-pasos">
  <div class="contenedor">
    {pasos()}
  </div>
</section>

<section class="seccion seccion--suave" aria-labelledby="t-opiniones">
  <div class="contenedor">
    {opiniones()}
  </div>
</section>

<section class="seccion" aria-label="Ubicación y horario">
  <div class="contenedor">
    {ubicacion()}
  </div>
</section>
'''

# ---------- Inicio E: mosaico de bloques ----------
def inicio_e():
    tarjetas = "\n".join(f'''      <li class="mosaico-trat mosaico-trat--{i+1} revelar">
        <a href="tratamientos.html#{id_}">
          {g.img(foto_trat(id_), "foto", 720, 540)}
          <span class="numero">{i+1:02d}</span>
          <span class="mosaico-trat-texto">
            <span class="mosaico-trat-titulo">{nombre}</span>
            <span class="mosaico-trat-desc">{corto(texto)}</span>
            <span class="mosaico-trat-tambien">También: {tambien}</span>
          </span>
        </a>
      </li>''' for i, (id_, nombre, texto, tambien, _) in enumerate(g.TRAT))
    return f'''
<section class="bento contenedor" aria-label="Presentación">
  <div class="bloque bloque--titulo">
    <p class="antetitulo">Odontología estética · Bucaramanga</p>
    <h1>{g.CONSULTORIO}: <em>diseño de sonrisa</em> y lentes cerámicos</h1>
    <p class="intro">Odontóloga con especialización en estética de la UNICID (São Paulo, Brasil). En su consultorio también se atiende odontología general, ortodoncia, implantes, conductos y encías.</p>
    <div class="acciones">
      <a class="btn" href="{g.wa()}" target="_blank" rel="noopener">{g.I_WA}Agenda tu valoración por WhatsApp</a>
      <a class="btn btn--linea" href="tel:{g.TEL}">{g.I_TEL}Llamar al {g.TEL_VISIBLE}</a>
    </div>
  </div>
  {figura(CONF["heroe"], "bloque bloque--foto", 900, 1000, NOTA_REF, prioridad=True)}
  <a class="bloque bloque--dato bloque--calificacion" href="{g.MAPS}" target="_blank" rel="noopener">
    <span class="bloque-etiqueta">Google</span>
    <span class="bloque-cifra">{g.NOTA}</span>{g.ESTRELLAS}
    <span>Mira sus {g.OPINIONES} opiniones</span>
  </a>
  <div class="bloque bloque--dato bloque--horario">
    <span class="bloque-etiqueta">{g.I_RELOJ}Horario</span>
    {estado_horario()}
    <span>Lun a sáb 8 a. m. – 8 p. m.<br>Dom 9 a. m. – 8 p. m.</span>
  </div>
  <a class="bloque bloque--dato bloque--lugar" href="{g.MAPS}" target="_blank" rel="noopener">
    <span class="bloque-etiqueta">{g.I_PIN}Dirección</span>
    <span>{g.DIRECCION}, {g.CIUDAD}</span>
    <span class="bloque-enlace">Cómo llegar <span aria-hidden="true">→</span></span>
  </a>
  <div class="bloque bloque--dato bloque--formacion">
    <span class="bloque-etiqueta">{g.I_GORRO}Formación</span>
    <span><strong>Especialización en Estética</strong><br>UNICID, São Paulo (Brasil)</span>
  </div>
</section>

<section class="seccion" aria-labelledby="t-tratamientos">
  <div class="contenedor">
    <div class="seccion-cabeza">
      <h2 id="t-tratamientos">Tratamientos del consultorio</h2>
      <p>La estética dental es el centro de la consulta, pero no lo único. Estos son los tratamientos que ofrece el consultorio, con el nombre con que los conoces.</p>
      <p class="nota">{g.AVISO_FOTOS}</p>
    </div>
    <ul class="mosaico">
{tarjetas}
    </ul>
  </div>
</section>

<section class="seccion" aria-labelledby="t-doctora">
  <div class="contenedor perfil bloque bloque--perfil">
    {figura(CONF["doctora"], "perfil-foto", 800, 1000, NOTA_DOCTORA)}
    <div class="revelar">
      <p class="antetitulo">Quién te atiende</p>
      <h2 id="t-doctora">Conoce a la {g.NOMBRE}</h2>
      <p>Es odontóloga y se especializó en estética dental en Brasil. Su trabajo se concentra en el diseño de sonrisa, las carillas y los lentes cerámicos.</p>
      {ficha_doctora()}
      <a class="btn btn--linea" href="la-doctora.html">Más sobre la doctora</a>
    </div>
  </div>
</section>

<section class="seccion seccion--color" aria-labelledby="t-pasos">
  <div class="contenedor">
    {pasos()}
  </div>
</section>

<section class="seccion" aria-labelledby="t-opiniones">
  <div class="contenedor bloque bloque--opiniones">
    {opiniones()}
  </div>
</section>

<section class="seccion seccion--sin-arriba" aria-label="Ubicación y horario">
  <div class="contenedor bloque bloque--ubicacion">
    {ubicacion()}
  </div>
</section>
'''

# ---------- Páginas interiores (misma estructura, estilos distintos) ----------
def cabecera(antetitulo, h1, intro, extra=""):
    return f'''<section class="cabecera-pagina">
  <div class="contenedor">
    <p class="antetitulo">{antetitulo}</p>
    <h1>{h1}</h1>
    <p class="intro">{intro}</p>
    {extra}
  </div>
</section>'''

def tratamientos():
    indice = "".join(f'<li><a href="#{id_}">{n}</a></li>' for id_, n, *_ in g.TRAT)
    detalles = "\n".join(f'''    <article class="detalle revelar" id="{id_}">
      {g.img(foto_trat(id_), "detalle-foto", 960, 720)}
      <div class="detalle-texto">
        <span class="numero">{i+1:02d}</span>
        <h2>{nombre}</h2>
        <p>{texto}</p>
        <p class="tambien"><strong>También lo buscas como:</strong> {tambien}.</p>
        <a class="btn btn--sm" href="{g.wa(msg)}" target="_blank" rel="noopener">{g.I_WA}Preguntar por {nombre.lower()}</a>
      </div>
    </article>''' for i, (id_, nombre, texto, tambien, msg) in enumerate(g.TRAT))
    return cabecera("Tratamientos", "Tratamientos de odontología y <em>estética dental</em>",
                    "Qué es cada tratamiento, explicado en pocas palabras. El costo y los tiempos dependen de cada caso y se definen en la valoración.",
                    f'<p class="nota">{g.AVISO_FOTOS}</p><ul class="indice">{indice}</ul>') + f'''
<section class="seccion">
  <div class="contenedor detalles">
    <!-- PENDIENTE: que la doctora revise y firme estos textos (tema de salud), y confirme qué tratamientos hace ella y cuáles un especialista aliado. -->
{detalles}
  </div>
</section>
'''

def doctora():
    return f'''
<section class="cabecera-pagina cabecera-pagina--perfil">
  <div class="contenedor perfil">
    {figura(CONF["doctora"], "perfil-foto", 800, 1000, NOTA_DOCTORA, prioridad=True)}
    <div>
      <p class="antetitulo">La doctora</p>
      <h1>{g.NOMBRE}, odontóloga especialista en <em>estética</em></h1>
      <p class="intro">Atiende en su consultorio del Edificio Alto Prado, en Bucaramanga. Su trabajo se concentra en el diseño de sonrisa, las carillas y los lentes cerámicos.</p>
      <div class="acciones"><a class="btn" href="{g.wa()}" target="_blank" rel="noopener">{g.I_WA}Agenda tu valoración</a></div>
    </div>
  </div>
</section>
<section class="seccion">
  <div class="contenedor texto-largo">
    <h2>Formación y enfoque</h2>
    {ficha_doctora()}
    <h2>En qué se enfoca</h2>
    <p>La estética dental: cambiar la forma, el color o la proporción de los dientes para que la sonrisa se vea en armonía con la cara. Para eso usa carillas y lentes cerámicos, resinas y blanqueamiento, según lo que cada paciente necesite.</p>
    <p>En el consultorio también se atiende ortodoncia, implantes y coronas, tratamiento de conductos, limpieza y encías. Puedes ver cada uno en <a href="tratamientos.html">Tratamientos</a>.</p>
    <!-- PENDIENTE: un texto corto escrito por la doctora, en primera persona: por qué eligió la estética dental y cómo trabaja con sus pacientes. -->
  </div>
</section>
<section class="seccion seccion--suave" aria-labelledby="t-opiniones">
  <div class="contenedor">
    {opiniones()}
  </div>
</section>
'''

def preguntas():
    items = "\n".join(f'''      <article class="pregunta revelar">
        <h2>{q}</h2>
        <p>{a}</p>
      </article>''' for q, a in g.PREG)
    return cabecera("Preguntas frecuentes", "Preguntas frecuentes sobre <em>carillas</em>, blanqueamiento y citas",
                    "Respuestas cortas a lo que más se pregunta antes de la primera cita.") + f'''
<section class="seccion">
  <div class="contenedor">
    <!-- PENDIENTE: que la doctora revise estas respuestas (tema de salud) y agregue precio de la valoración, formas de pago y financiación. -->
    <div class="preguntas">
{items}
    </div>
    <div class="acciones"><a class="btn" href="{g.wa('Hola, Dra. Vanesa. Tengo una pregunta.')}" target="_blank" rel="noopener">{g.I_WA}¿Otra pregunta? Escríbenos</a></div>
  </div>
</section>
'''

def contacto():
    return cabecera("Contacto", "Contacto, <em>dirección</em> y horario",
                    "Escribe, llama o visita el consultorio en el Edificio Alto Prado, Bucaramanga.") + f'''
<section class="seccion">
  <div class="contenedor contacto-grid">
    <div class="contacto-tarjeta">{g.I_WA}<h2>WhatsApp</h2><p>La forma más rápida de agendar o resolver una duda.</p><a class="btn" href="{g.wa()}" target="_blank" rel="noopener">Escribir por WhatsApp</a></div>
    <div class="contacto-tarjeta">{g.I_TEL}<h2>Teléfono</h2><p>{g.TEL_VISIBLE}</p><a class="btn btn--linea" href="tel:{g.TEL}">Llamar ahora</a></div>
  </div>
</section>
<section class="seccion seccion--suave" aria-label="Ubicación y horario">
  <div class="contenedor">
    {ubicacion()}
  </div>
</section>
'''

CUERPOS = {"index.html": inicio_d() if VARIANTE == "d" else inicio_e(), "tratamientos.html": tratamientos(),
           "la-doctora.html": doctora(), "preguntas.html": preguntas(), "contacto.html": contacto()}

for archivo, cuerpo in CUERPOS.items():
    t, d = g.DESC[archivo]
    (DESTINO / archivo).write_text(pagina(archivo, t, d, cuerpo, jsonld=archivo in ("index.html", "contacto.html")), encoding="utf-8")
fondo, letra = CONF["favicon"]
(DESTINO / "assets").mkdir(parents=True, exist_ok=True)
(DESTINO / "assets" / "favicon.svg").write_text(
    f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><rect width="64" height="64" rx="14" fill="{fondo}"/>'
    f'<text x="32" y="41" text-anchor="middle" font-family="Georgia, serif" font-style="italic" font-size="24" fill="{letra}">VG</text></svg>\n', encoding="utf-8")
print("ok", VARIANTE)
