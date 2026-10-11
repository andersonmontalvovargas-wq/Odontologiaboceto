"""Genera la propuesta H (Retícula: estilo suizo tipográfico) con los textos de generar.py.

Uso: python3 prospecto-03/generar_h.py prospecto-03/sitio-h
Rasgos propios: retícula de 12 columnas con líneas finas visibles, titulares en mayúsculas extendidas
(Archivo con el eje de ancho), etiquetas y datos en letra monoespaciada (JetBrains Mono), fotos numeradas
como figuras ("Fig. 01"), ficha técnica con la hora de Bucaramanga, tratamientos en una tabla de 4 × 2 y
preguntas en filas. Esquinas rectas, sin sombras.
"""
import json, sys
from pathlib import Path

DESTINO = Path(sys.argv[1])
sys.path.insert(0, str(Path(__file__).parent))
_argv, sys.argv = sys.argv, [sys.argv[0]]
import generar as g  # noqa: E402  (solo se reutilizan sus datos)
sys.argv = _argv

VERSION = "20261010h"
FUENTES = "family=Archivo:ital,wdth,wght@0,62..125,400..800;1,100,400..600&family=JetBrains+Mono:wght@400;500"
TEMA = "#171415"
HEROE, DOCTORA, BLANQUEAMIENTO = 3762400, 6812453, 3762408
CITA, CONTACTO = 4269276, 30902075
NOTA_REF = "Foto de referencia, de un banco de imágenes"
NOTA_DOCTORA = "Foto de referencia del consultorio · aquí va la foto real de la doctora"

PAGINAS = [("index.html", "Inicio"), ("tratamientos.html", "Tratamientos"), ("la-doctora.html", "La doctora"),
           ("preguntas.html", "Preguntas frecuentes"), ("contacto.html", "Contacto")]
PASOS = [
    ("Escribes o llamas", f"Por WhatsApp o al {g.TEL_VISIBLE}. Cuéntanos qué te gustaría mejorar y elige el día."),
    ("Valoración", "La doctora revisa tus dientes y encías y escucha lo que quieres cambiar de tu sonrisa."),
    ("Tu plan", "Te explica las opciones, los tiempos y el costo antes de empezar cualquier tratamiento."),
]
FLECHA = '<span class="flecha" aria-hidden="true">→</span>'

_fig = [0]


def foto_trat(id_):
    return g.FOTO_TRAT.get(id_) or BLANQUEAMIENTO


def figura(id_, clase, w, h, nota, prioridad=False):
    """Foto numerada como figura, con su descripción en letra monoespaciada."""
    _fig[0] += 1
    return (f'<figure class="{clase}"><div class="marco">{g.img(id_, "foto", w, h, prioridad)}</div>'
            f'<figcaption><span>Fig. {_fig[0]:02d}</span>{g.FOTO_DESC[id_]} · {nota}</figcaption></figure>')


def corto(texto):
    return texto.split(". ")[0] + "."


def estado():
    return '<span class="estado" data-estado hidden><span class="estado-punto" aria-hidden="true"></span><span data-estado-texto></span></span>'


def horario_tabla():
    filas = []
    for i, (dia, horas) in enumerate(g.HORARIO):
        abre = 9 if dia == "Domingo" else 8
        izq, ancho = (abre - 6) / 16 * 100, (20 - abre) / 16 * 100
        filas.append(f'<tr data-dia="{(i + 1) % 7}"><th scope="row">{dia}</th><td class="mono">{horas}</td>'
                     f'<td class="barra-celda" aria-hidden="true"><span class="barra"><span style="left:{izq:.1f}%;width:{ancho:.1f}%"></span></span></td></tr>')
    return (f'<table class="horario"><caption class="sr">Horario de atención</caption>'
            f'<thead><tr><th scope="col">Día</th><th scope="col">Horas</th><th scope="col" class="barra-celda"><span class="sr">Franja del día, de 6 a. m. a 10 p. m.</span>'
            f'<span class="escala-horas" aria-hidden="true"><span>6</span><span>12</span><span>18</span><span>22</span></span></th></tr></thead>'
            f'<tbody>{"".join(filas)}</tbody></table>'
            '<p class="nota">En festivos el horario puede variar. Confírmalo por WhatsApp antes de ir.</p>')


def ficha_tecnica():
    return f'''<dl class="tecnica">
        <div><dt>Profesional</dt><dd>Dra. Vanesa Gutiérrez, odontóloga</dd></div>
        <div><dt>Especialización</dt><dd>Estética · UNICID (São Paulo, Brasil)</dd></div>
        <div><dt>Dirección</dt><dd>{g.DIRECCION}, Bucaramanga</dd></div>
        <div><dt>Teléfono</dt><dd><a href="tel:{g.TEL}">{g.TEL_VISIBLE}</a> · WhatsApp</dd></div>
        <div><dt>Horario</dt><dd>Lun–sáb 8:00 a. m. – 8:00 p. m.<br>Dom 9:00 a. m. – 8:00 p. m.</dd></div>
        <div data-reloj hidden><dt>Hora en Bucaramanga</dt><dd><span data-reloj-texto></span> {estado()}</dd></div>
      </dl>
      <!-- PENDIENTE: confirmar el título exacto de la especialización (el dato público dice "ESP. ESTÉTICA · UNICID"). -->'''


def pagina(archivo, titulo, descripcion, cuerpo, jsonld=False):
    nav = "".join(f'<li><a href="{a}"{" aria-current=\"page\"" if a == archivo else ""}><span class="mono">{i:02d}</span>{n}</a></li>'
                  for i, (a, n) in enumerate(PAGINAS[1:], 1))
    nav_movil = "".join(f'<li><a href="{a}"{" aria-current=\"page\"" if a == archivo else ""}><span class="mono">{i:02d}</span>{n}</a></li>'
                        for i, (a, n) in enumerate(PAGINAS))
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
<div class="aviso-propuesta" role="note"><span class="mono">Boceto</span> <strong>Propuesta de diseño H</strong> para el {g.CONSULTORIO}. No es el sitio oficial.</div>
<header class="encabezado">
  <div class="reticula encabezado-fila">
    <a class="marca" href="index.html" aria-label="{g.CONSULTORIO}, ir al inicio">
      <!-- PENDIENTE: monograma provisional; reemplazar por el logo real si lo tiene. -->
      <span class="monograma" aria-hidden="true">VG</span>
      <span class="marca-texto">Consultorio<br>Dra. Vanesa Gutiérrez</span>
    </a>
    <nav class="nav" aria-label="Principal"><ul>{nav}</ul></nav>
    <a class="boton boton--sm" href="{g.wa()}" target="_blank" rel="noopener">{g.I_WA}Agendar</a>
    <button class="menu-boton" type="button" aria-expanded="false" aria-controls="menu-movil">Menú</button>
  </div>
  <nav class="menu-movil" id="menu-movil" aria-label="Menú móvil"><ul>{nav_movil}</ul></nav>
</header>
<main id="contenido">
{cuerpo}
</main>
<footer class="pie">
  <div class="reticula pie-fila">
    <div class="pie-marca"><p class="extendida">Consultorio Dra. Vanesa Gutiérrez</p><p>Odontología y estética dental en Bucaramanga.</p></div>
    <div><h2 class="mono">Dirección</h2><p>{g.DIRECCION}.<br>{g.CIUDAD}.</p></div>
    <div><h2 class="mono">Contacto</h2><p><a href="tel:{g.TEL}">{g.TEL_VISIBLE}</a><br><a href="{g.wa()}" target="_blank" rel="noopener">WhatsApp</a></p></div>
    <div><h2 class="mono">Horario</h2><p>Lunes a sábado: 8:00 a. m. – 8:00 p. m.<br>Domingo: 9:00 a. m. – 8:00 p. m.<br>En festivos puede variar.</p></div>
    <div><h2 class="mono">Páginas</h2><ul>{nav_movil}</ul></div>
  </div>
  <div class="reticula">
    <!-- PENDIENTE: enlace a la Política de tratamiento de datos (Ley 1581 de 2012) del consultorio. -->
    <p class="pie-legal">Este sitio no tiene formularios ni recoge datos personales. La información de contacto y el horario se tomaron del perfil público del consultorio en Google ({g.FECHA_NOTA}). {g.AVISO_FOTOS}</p>
  </div>
</footer>
<a class="wa-flotante" href="{g.wa()}" target="_blank" rel="noopener" aria-label="Escribir por WhatsApp al {g.CONSULTORIO}">{g.I_WA}<span>WhatsApp</span></a>
</body>
</html>
'''


# ---------- Bloques ----------
def cabeza(num, titulo, texto="", id_=None, h="h2"):
    ide = f' id="{id_}"' if id_ else ""
    parrafo = f'<p class="cabeza-texto">{texto}</p>' if texto else ""
    return f'''<div class="reticula cabeza">
    <p class="cabeza-num mono" aria-hidden="true">{num}</p>
    <{h}{ide} class="extendida cortina">{titulo}</{h}>
    {parrafo}
  </div>'''


def tabla_tratamientos():
    celdas = "\n".join(f'''      <li class="celda aparecer">
        <p class="mono celda-num">{i+1:02d} / 08</p>
        {figura(foto_trat(id_), "celda-foto", 600, 600, NOTA_REF)}
        <h3>{nombre}</h3>
        <p>{corto(texto)}</p>
        <p class="tambien"><span class="mono">También lo buscas como</span> {tambien}</p>
        <a class="enlace" href="tratamientos.html#{id_}">Ver detalle{FLECHA}<span class="sr"> de {nombre.lower()}</span></a>
      </li>''' for i, (id_, nombre, texto, tambien, _) in enumerate(g.TRAT))
    return f'''<section class="seccion" aria-labelledby="t-tratamientos">
  {cabeza("08", "Tratamientos del consultorio", "La estética dental es el centro de la consulta, pero no lo único. Estos son los tratamientos que ofrece el consultorio, con el nombre con que los conoces.", "t-tratamientos")}
  <div class="reticula"><ol class="tabla">
{celdas}
  </ol></div>
</section>'''


def doctora_bloque(h="h2", prioridad=False):
    etiqueta = "h1" if h == "h1" else "h2"
    titulo = ("Dra. Vanesa Gutiérrez, <em>odontóloga especialista en estética</em>" if h == "h1"
              else "Conoce a la Dra. Vanesa Gutiérrez")
    return f'''<section class="seccion seccion--malva" aria-labelledby="t-doctora">
  <div class="reticula doctora">
    <div class="doctora-foto aparecer">
      {figura(DOCTORA, "foto-recta", 800, 1000, NOTA_DOCTORA, prioridad=prioridad)}
      <!-- PENDIENTE: foto real de la {g.NOMBRE} (WebP, width/height declarados{', fetchpriority="high", sin lazy' if prioridad else ', loading="lazy"'}). -->
    </div>
    <div class="doctora-texto">
      <p class="mono etiqueta">La doctora</p>
      <{etiqueta} id="t-doctora" class="extendida cortina">{titulo}</{etiqueta}>
      <p class="destacado">Es odontóloga y se especializó en estética dental en Brasil. Su trabajo se concentra en el diseño de sonrisa, las carillas y los lentes cerámicos.</p>
      <dl class="tecnica tecnica--malva">
        <div><dt>Profesión</dt><dd>Odontóloga</dd></div>
        <div><dt>Especialización</dt><dd>Estética · UNICID, Universidade Cidade de São Paulo (Brasil)</dd></div>
        <div><dt>Enfoque</dt><dd>Diseño de sonrisa, carillas y lentes cerámicos, blanqueamiento</dd></div>
        <div><dt>También atiende</dt><dd>Odontología general, ortodoncia, implantes y coronas, conductos, limpieza y encías</dd></div>
        <!-- PENDIENTE: título exacto de la especialización, universidad del pregrado, año de grado y registro profesional (ReTHUS). Solo lo que se pueda comprobar. -->
      </dl>
      {'' if h == 'h1' else f'<a class="enlace" href="la-doctora.html">Su formación y su enfoque{FLECHA}</a>'}
      {f'<div class="acciones"><a class="boton" href="{g.wa()}" target="_blank" rel="noopener">{g.I_WA}Agenda tu valoración por WhatsApp</a></div>' if h == 'h1' else ''}
    </div>
  </div>
</section>'''


def pasos():
    items = "".join(f'<li class="paso aparecer"><span class="paso-num extendida" aria-hidden="true">{i}</span><h3>{t}</h3><p>{p}</p></li>'
                    for i, (t, p) in enumerate(PASOS, 1))
    return f'''<section class="seccion" aria-labelledby="t-pasos">
  {cabeza("03", "Así es tu primera cita", "No necesitas saber qué tratamiento quieres. Para eso es la valoración.", "t-pasos")}
  <!-- PENDIENTE: confirmar con la doctora cómo es la valoración, cuánto cuesta y si incluye radiografías. -->
  <div class="reticula"><ol class="pasos">{items}</ol></div>
  <div class="reticula pasos-pie">
    <div class="acciones"><a class="boton" href="{g.wa()}" target="_blank" rel="noopener">{g.I_WA}Pedir mi valoración</a></div>
    {figura(CITA, "foto-recta foto-recta--ancha aparecer", 1200, 600, NOTA_REF)}
  </div>
</section>'''


def opiniones():
    return f'''<section class="seccion seccion--tinta" aria-labelledby="t-opiniones">
  <div class="reticula opiniones">
    <p class="cifra extendida" aria-hidden="true">{g.NOTA}<span class="mono">/ 5</span></p>
    <div>
      <p class="mono etiqueta">Opiniones en Google</p>
      <h2 id="t-opiniones" class="extendida cortina">{g.OPINIONES} opiniones de pacientes</h2>
      {g.ESTRELLAS}
      <p>El consultorio tiene una calificación de {g.NOTA} sobre 5 con {g.OPINIONES} opiniones en su perfil de Google ({g.FECHA_NOTA}). Puedes leerlas todas allí, escritas por los mismos pacientes.</p>
      <!-- PENDIENTE: 3 opiniones reales copiadas de Google, con nombre del autor, enlace a la reseña original y la marca Google. Sin datos estructurados de estrellas. -->
      <a class="boton boton--claro" href="{g.MAPS}" target="_blank" rel="noopener">Mira sus {g.OPINIONES} opiniones en Google{FLECHA}</a>
    </div>
  </div>
</section>'''


def ubicacion():
    return f'''<section class="seccion" aria-labelledby="t-ubicacion">
  {cabeza("02", "Dónde atendemos", f"Edificio Alto Prado, {g.CIUDAD}. Abierto los siete días.", "t-ubicacion")}
  <div class="reticula ubicacion">
    <div class="aparecer">
      <p class="mono etiqueta">Dirección · dos placas del mismo edificio</p>
      <ul class="placas">
        <li class="extendida">Cra. 34 # 36-31, local 2</li>
        <li class="extendida">Cra. 34 # 36-33</li>
      </ul>
      <p>Edificio Alto Prado, {g.CIUDAD}.</p>
      <div class="acciones">
        <a class="boton" href="{g.MAPS}" target="_blank" rel="noopener">{g.I_PIN}Abrir en Google Maps</a>
        <a class="boton boton--linea" href="{g.WAZE}" target="_blank" rel="noopener">Abrir en Waze</a>
      </div>
      <!-- PENDIENTE: confirmar si hay parqueadero y acceso para silla de ruedas. -->
    </div>
    <div class="aparecer">
      <p class="mono etiqueta">Horario de atención {estado()}</p>
      {horario_tabla()}
    </div>
  </div>
</section>'''


def cierre():
    return f'''<section class="cierre" aria-labelledby="t-cierre">
  <div class="reticula cierre-fila">
    <h2 id="t-cierre" class="extendida cortina">Agenda tu valoración</h2>
    <div>
      <p>Escribe por WhatsApp con un mensaje ya listo, o llama. Lunes a sábado de 8 a. m. a 8 p. m. y domingo de 9 a. m. a 8 p. m.</p>
      <div class="acciones">
        <a class="boton boton--blanco" href="{g.wa()}" target="_blank" rel="noopener">{g.I_WA}Agenda tu valoración por WhatsApp</a>
        <a class="boton boton--linea-blanca" href="tel:{g.TEL}">{g.I_TEL}Llamar al {g.TEL_VISIBLE}</a>
      </div>
    </div>
  </div>
</section>'''


# ---------- Inicio ----------
def inicio():
    _fig[0] = 0
    return f'''
<section class="portada" aria-labelledby="t-portada">
  <div class="reticula portada-meta mono" aria-hidden="true"><span>Odontología estética</span><span>Bucaramanga, Colombia</span><span>Diseño de sonrisa · Lentes cerámicos</span></div>
  <div class="reticula">
    <h1 id="t-portada" class="portada-titulo"><span class="extendida">Consultorio Dra. Vanesa Gutiérrez</span><span class="sr">:</span> <span class="portada-lema">diseño de sonrisa y lentes cerámicos</span></h1>
  </div>
  <div class="reticula portada-cuerpo">
    <div class="portada-texto">
      <p class="intro">Odontóloga con especialización en estética de la UNICID (São Paulo, Brasil). En su consultorio también se atiende odontología general, ortodoncia, implantes, conductos y encías.</p>
      <div class="acciones">
        <a class="boton" href="{g.wa()}" target="_blank" rel="noopener">{g.I_WA}Agenda tu valoración por WhatsApp</a>
        <a class="boton boton--linea" href="tel:{g.TEL}">{g.I_TEL}Llamar al {g.TEL_VISIBLE}</a>
      </div>
      <a class="calificacion" href="{g.MAPS}" target="_blank" rel="noopener"><span class="extendida">{g.NOTA}</span>{g.ESTRELLAS}<span>en Google · Mira sus {g.OPINIONES} opiniones</span></a>
    </div>
    <div class="portada-ficha">
      <p class="mono etiqueta">Ficha del consultorio</p>
      {ficha_tecnica()}
    </div>
    {figura(HEROE, "portada-foto", 700, 900, NOTA_REF, prioridad=True)}
  </div>
</section>
{tabla_tratamientos()}
{doctora_bloque()}
{pasos()}
{opiniones()}
{ubicacion()}
{cierre()}
'''


# ---------- tratamientos.html ----------
def tratamientos_pagina():
    _fig[0] = 0
    indice = "".join(f'<li><a href="#{id_}"><span class="mono">{i+1:02d}</span>{nombre}</a></li>' for i, (id_, nombre, *_) in enumerate(g.TRAT))
    fichas = "\n".join(f'''  <article class="reticula trat aparecer" id="{id_}" aria-labelledby="t-{id_}">
    <div class="trat-lado">
      <p class="mono trat-num">{i+1:02d} / 08</p>
      {figura(foto_trat(id_), "foto-recta", 700, 700, NOTA_REF)}
    </div>
    <div class="trat-cuerpo">
      <h2 id="t-{id_}" class="extendida">{nombre}</h2>
      <dl class="tecnica">
        <div><dt>Qué es</dt><dd>{texto}</dd></div>
        <div><dt>También lo buscas como</dt><dd>{tambien}</dd></div>
      </dl>
      <div class="acciones"><a class="boton" href="{g.wa(msg)}" target="_blank" rel="noopener">{g.I_WA}Preguntar por {nombre.lower()}</a></div>
    </div>
  </article>''' for i, (id_, nombre, texto, tambien, msg) in enumerate(g.TRAT))
    return f'''
<section class="portada portada--pagina" aria-labelledby="t-pagina">
  <div class="reticula portada-meta mono" aria-hidden="true"><span>01 · Tratamientos</span><span>8 tratamientos</span><span>Bucaramanga</span></div>
  <div class="reticula">
    <h1 id="t-pagina" class="portada-titulo"><span class="extendida">Tratamientos de odontología</span> <span class="portada-lema">y estética dental</span></h1>
    <p class="intro intro--ancha">La estética dental es el centro de la consulta, pero no lo único. Estos son los tratamientos que ofrece el consultorio, con el nombre con que los conoces.</p>
    <nav aria-label="Ir a un tratamiento"><ol class="indice">{indice}</ol></nav>
  </div>
</section>
<section class="seccion seccion--sin-arriba">
  <!-- PENDIENTE: que la doctora revise y firme estos textos (tema de salud) y confirme qué tratamientos hace ella y cuáles un especialista aliado. -->
{fichas}
</section>
{cierre()}
'''


# ---------- la-doctora.html ----------
def doctora_pagina():
    _fig[0] = 0
    return f'''
{doctora_bloque(h="h1", prioridad=True)}
<section class="seccion" aria-label="Enfoque">
  <div class="reticula enfoque">
    <div class="aparecer"><p class="mono etiqueta">01 · Enfoque</p><h2 class="extendida">En qué se enfoca</h2><p>La estética dental: cambiar la forma, el color o la proporción de los dientes para que la sonrisa se vea en armonía con la cara. Para eso usa carillas y lentes cerámicos, resinas y blanqueamiento, según lo que cada paciente necesite.</p></div>
    <div class="aparecer"><p class="mono etiqueta">02 · Consultorio</p><h2 class="extendida">También atiende</h2><p>En el consultorio también se atiende ortodoncia, implantes y coronas, tratamiento de conductos, limpieza y encías. Puedes ver cada uno en <a href="tratamientos.html">Tratamientos</a>.</p></div>
    <!-- PENDIENTE: un texto corto escrito por la doctora, en primera persona: por qué eligió la estética dental y cómo trabaja con sus pacientes. -->
  </div>
</section>
{pasos()}
{opiniones()}
'''


# ---------- preguntas.html ----------
def preguntas_pagina():
    filas = "\n".join(f'''    <article class="pregunta aparecer">
      <p class="mono pregunta-num" aria-hidden="true">P.{i:02d}</p>
      <h2>{q}</h2>
      <p>{a}</p>
    </article>''' for i, (q, a) in enumerate(g.PREG, 1))
    return f'''
<section class="portada portada--pagina" aria-labelledby="t-pagina">
  <div class="reticula portada-meta mono" aria-hidden="true"><span>03 · Preguntas</span><span>9 respuestas cortas</span><span>Antes de la primera cita</span></div>
  <div class="reticula">
    <h1 id="t-pagina" class="portada-titulo"><span class="extendida">Preguntas frecuentes</span> <span class="portada-lema">sobre carillas, blanqueamiento y citas</span></h1>
    <p class="intro intro--ancha">Respuestas cortas a lo que más se pregunta antes de la primera cita.</p>
  </div>
</section>
<section class="seccion seccion--sin-arriba">
  <!-- PENDIENTE: que la doctora revise estas respuestas (tema de salud) y agregue precio de la valoración, formas de pago y financiación. -->
  <div class="reticula preguntas">
{filas}
  </div>
  <div class="reticula"><div class="acciones"><a class="boton" href="{g.wa('Hola, Dra. Vanesa. Tengo una pregunta.')}" target="_blank" rel="noopener">{g.I_WA}¿Otra pregunta? Escríbenos</a></div></div>
</section>
'''


# ---------- contacto.html ----------
def contacto_pagina():
    _fig[0] = 0
    return f'''
<section class="portada portada--pagina" aria-labelledby="t-pagina">
  <div class="reticula portada-meta mono" aria-hidden="true"><span>04 · Contacto</span><span>Edificio Alto Prado</span><span>Bucaramanga</span></div>
  <div class="reticula">
    <h1 id="t-pagina" class="portada-titulo"><span class="extendida">Contacto, dirección</span> <span class="portada-lema">y horario</span></h1>
    <p class="intro intro--ancha">Escribe, llama o visita el consultorio en el Edificio Alto Prado, Bucaramanga.</p>
  </div>
  <div class="reticula canales">
    <a class="canal" href="tel:{g.TEL}"><span class="mono etiqueta">Llamar</span><span class="extendida canal-num">{g.TEL_VISIBLE}</span><span>Teléfono del consultorio, el mismo del WhatsApp.{FLECHA}</span></a>
    <a class="canal canal--wa" href="{g.wa()}" target="_blank" rel="noopener"><span class="mono etiqueta">WhatsApp</span><span class="extendida canal-num">Escribir</span><span>La forma más rápida de agendar o resolver una duda.{FLECHA}</span></a>
  </div>
  <div class="reticula">
    {figura(CONTACTO, "foto-recta foto-recta--ancha", 1400, 600, NOTA_REF)}
    <!-- PENDIENTE: foto real de la fachada o la entrada del Edificio Alto Prado. -->
  </div>
</section>
{ubicacion()}
'''


CUERPOS = {"index.html": inicio, "tratamientos.html": tratamientos_pagina, "la-doctora.html": doctora_pagina,
           "preguntas.html": preguntas_pagina, "contacto.html": contacto_pagina}

if __name__ == "__main__":
    for archivo, hacer in CUERPOS.items():
        t, d = g.DESC[archivo]
        (DESTINO / archivo).write_text(pagina(archivo, t, d, hacer(), jsonld=archivo in ("index.html", "contacto.html")), encoding="utf-8")
    (DESTINO / "assets").mkdir(parents=True, exist_ok=True)
    (DESTINO / "assets" / "favicon.svg").write_text(
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><rect width="64" height="64" fill="#171415"/>'
        '<rect x="0" y="48" width="64" height="16" fill="#C8284F"/><text x="32" y="38" text-anchor="middle" font-family="Arial Black, Arial, sans-serif" '
        'font-weight="900" font-size="24" fill="#F3EFE8">VG</text></svg>\n', encoding="utf-8")
    print("ok h")
