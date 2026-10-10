"""Genera las 5 páginas del boceto de prospecto-04 con encabezado y pie compartidos.

Uso: python3 prospecto-04/generar.py prospecto-04/sitio-a a   (variantes: a, b, c)
Los textos se cambian aquí, no en los HTML. Las tres propuestas comparten textos y páginas;
cambian la primera pantalla, la forma de mostrar las especialidades, la ilustración y el CSS.
"""
import json, sys, urllib.parse
from pathlib import Path

DESTINO = Path(sys.argv[1])
VARIANTE = sys.argv[2] if len(sys.argv) > 2 else "a"

CONF = {
    "a": {"fuentes": "family=Manrope:wght@400;500;600;700&family=Sora:wght@500;600;700",
          "tema": "#0E4A55", "favicon": ("#0E4A55", "#FFFFFF")},
    "b": {"fuentes": "family=Plus+Jakarta+Sans:wght@400;500;600;700;800",
          "tema": "#16294A", "favicon": ("#FFFFFF", "#1F5FAF")},
    "c": {"fuentes": "family=Albert+Sans:wght@400;500;600&family=Instrument+Serif:ital@0;1",
          "tema": "#1E3F33", "favicon": ("#1E3F33", "#E2C48F")},
}[VARIANTE]

# ---------- Datos reales (ver CONTENIDO.md) ----------
MARCA = "Clínica Vía Oral"
NOMBRE_GOOGLE = "Clínica Odontológica Vía Oral"
TEL_VISIBLE = "314 394 3828"
TEL = "+573143943828"
WA = "573143943828"
DIRECCION = "Calle 43 # 34-31, Cabecera del Llano"
CIUDAD = "Bucaramanga, Santander"
MAPS = "https://maps.google.com/?cid=8339109239465121267"
WAZE = "https://waze.com/ul?q=" + urllib.parse.quote("Calle 43 #34-31, Bucaramanga") + "&navigate=yes"
INSTAGRAM = "https://www.instagram.com/clinicaviaoralbga/"
NOTA = "5,0"
OPINIONES = 322
FECHA = "octubre de 2026"

def wa(msg="Hola, Clínica Vía Oral. Quiero agendar una valoración."):
    return f"https://wa.me/{WA}?text=" + urllib.parse.quote(msg)

HORARIO = [("Lunes a viernes", "7:00 a. m. – 12:00 m.<br>2:00 – 7:00 p. m."),
           ("Sábado", "8:00 a. m. – 12:00 m."),
           ("Domingo", "Cerrado")]
HORARIO_CORTO = "Lun a vie 7–12 y 2–7 · Sáb 8–12"
NOTA_FESTIVOS = "En festivos el horario puede cambiar: confírmalo por WhatsApp antes de ir."

# ---------- Íconos (dibujados para este boceto) ----------
def ico(cuerpo, relleno=False):
    attrs = 'fill="currentColor"' if relleno else 'fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"'
    return f'<svg viewBox="0 0 24 24" {attrs} aria-hidden="true" focusable="false">{cuerpo}</svg>'

I_WA = ico('<path d="M12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2Zm0 18.2c-1.6 0-3.1-.4-4.4-1.2l-.3-.2-3 .8.8-2.9-.2-.3A8.2 8.2 0 1 1 12 20.2Zm4.5-6.1c-.2-.1-1.5-.7-1.7-.8-.2-.1-.4-.1-.6.1l-.8 1c-.1.2-.3.2-.5.1a6.7 6.7 0 0 1-3.3-2.9c-.3-.4.3-.4.7-1.3.1-.2 0-.3 0-.4l-.8-1.8c-.2-.5-.4-.4-.6-.4h-.5a1 1 0 0 0-.7.3 3 3 0 0 0-.9 2.2c0 1.3.9 2.5 1 2.7.1.2 1.8 2.8 4.4 3.9 1.6.7 2.3.8 3.1.6.5-.1 1.5-.6 1.7-1.2.2-.6.2-1.1.2-1.2-.1-.1-.3-.2-.5-.3Z"/>', True)
I_TEL = ico('<path d="M6.2 3.8h2.6l1.4 3.8-1.8 1.3a10.5 10.5 0 0 0 6.7 6.7l1.3-1.8 3.8 1.4v2.6a1.8 1.8 0 0 1-1.9 1.8A15.6 15.6 0 0 1 4.4 5.7a1.8 1.8 0 0 1 1.8-1.9Z"/>')
I_PIN = ico('<path d="M12 21s6.5-5.7 6.5-11a6.5 6.5 0 1 0-13 0c0 5.3 6.5 11 6.5 11Z"/><circle cx="12" cy="10" r="2.4"/>')
I_RELOJ = ico('<circle cx="12" cy="12" r="8.5"/><path d="M12 7.5V12l3 1.8"/>')
I_IG = ico('<rect x="3.5" y="3.5" width="17" height="17" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.2" cy="6.8" r=".9" fill="currentColor" stroke="none"/>')
I_FLECHA = ico('<path d="M5 12h14M13 6l6 6-6 6"/>')
ESTRELLA = '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true" focusable="false"><path d="M12 2.8l2.8 5.8 6.3.9-4.6 4.4 1.1 6.3L12 17.2l-5.6 3 1.1-6.3L2.9 9.5l6.3-.9Z"/></svg>'
ESTRELLAS = '<span class="estrellas">' + ESTRELLA * 5 + '</span>'

I_GRUPO = {
    "sonrisa": ico('<path d="M4 10.5c2.2 5.6 13.8 5.6 16 0"/><path d="M7 12.6v1.8M10.3 13.6v2M13.7 13.6v2M17 12.6v1.8"/><path d="M5.5 6.5l1 1M18.5 6.5l-1 1M12 4.5V6"/>'),
    "ortodoncia": ico('<path d="M3.5 9.5c3 6 14 6 17 0"/><path d="M3.5 9.5c3 3.2 14 3.2 17 0" opacity=".55"/><rect x="6.2" y="11" width="2.6" height="2.6" rx=".5"/><rect x="10.7" y="12" width="2.6" height="2.6" rx=".5"/><rect x="15.2" y="11" width="2.6" height="2.6" rx=".5"/>'),
    "conservar": ico('<path d="M8.2 3.5c-2.2 0-3.7 1.7-3.7 4.1 0 2.7 1.4 4.5 2 7.2.5 2.3 1 4.2 2.2 4.2 1.4 0 1.5-2.8 2.4-4.8.3-.7.6-1.1.9-1.1s.6.4.9 1.1c.9 2 1 4.8 2.4 4.8 1.2 0 1.7-1.9 2.2-4.2.6-2.7 2-4.5 2-7.2 0-2.4-1.5-4.1-3.7-4.1-1.8 0-2.4.9-3.8.9s-2-.9-3.8-.9Z"/><path d="M12 9.2v3.6"/>'),
    "reemplazar": ico('<path d="M8 3.5h8c1.2 0 2 .9 2 2.1 0 2.6-2.4 3.9-6 3.9s-6-1.3-6-3.9c0-1.2.8-2.1 2-2.1Z"/><path d="M9 12h6M9.6 15h4.8M10.2 18h3.6M12 9.5V21"/>'),
}

# ---------- Especialidades (lista de la ficha de Google), agrupadas por lo que busca el paciente ----------
GRUPOS = [
    ("sonrisa", "Mejorar cómo se ve tu sonrisa", [
        ("diseno-de-sonrisa", "Diseño de sonrisa",
         "Un plan que cambia la forma, el color o el tamaño de los dientes que se ven al sonreír, pensado según tu cara, tus labios y tus encías. Puede combinar blanqueamiento, carillas, coronas o resinas.",
         "estética dental, sonrisa estética"),
        ("carillas-y-coronas", "Carillas y coronas",
         "Las carillas son láminas delgadas que cubren la cara visible del diente. Las coronas cubren el diente completo y se usan cuando está muy desgastado, fracturado o ya tuvo tratamiento de conductos.",
         "lentes cerámicos, carillas de porcelana, carillas en resina, fundas"),
        ("blanqueamiento", "Blanqueamiento dental",
         "Aclara el color natural de los dientes con un gel aplicado y controlado por el odontólogo. Antes se revisa que no haya caries ni encías inflamadas. No cambia el color de resinas, carillas ni coronas.",
         "aclaramiento dental, dientes blancos"),
    ]),
    ("ortodoncia", "Alinear los dientes", [
        ("ortodoncia-con-alineadores", "Ortodoncia con alineadores",
         "Corrige la posición de los dientes con férulas transparentes que se cambian cada cierto tiempo, en lugar de brackets. Se pueden quitar para comer y cepillarse. En la valoración se revisa si tu caso se puede tratar así.",
         "ortodoncia invisible, alineadores transparentes, ortodoncia sin brackets"),
    ]),
    ("conservar", "Conservar tus dientes", [
        ("endodoncia", "Endodoncia",
         "Cuando el nervio de un diente se inflama o se infecta, se limpia el interior del diente y se sella. Así se puede conservar el diente en lugar de sacarlo.",
         "tratamiento de conductos, matar el nervio"),
        ("periodoncia", "Periodoncia",
         "Trata las encías y el hueso que sostiene los dientes. Si te sangran las encías, se ven retraídas o sientes los dientes flojos, es el especialista que debe revisarte.",
         "encías, limpieza profunda, encías que sangran"),
    ]),
    ("reemplazar", "Reemplazar dientes y cirugía", [
        ("implantes-dentales", "Implantes dentales",
         "Un implante reemplaza la raíz de un diente perdido y sobre él se fija una corona. Antes se estudia el hueso con radiografías para saber si es posible y qué se necesita.",
         "implante, diente fijo"),
        ("rehabilitacion-oral", "Rehabilitación oral",
         "Recupera la función para masticar cuando faltan varios dientes o están muy deteriorados. Puede incluir coronas, puentes, prótesis o implantes, según cada caso.",
         "prótesis dental, puentes, caja de dientes"),
        ("cirugia-oral", "Cirugía oral",
         "Procedimientos dentro de la boca, como sacar dientes que no se pueden conservar o cordales (muelas del juicio) que no salen bien.",
         "extracción, cordales, muelas del juicio"),
    ]),
]
ESPECIALIDADES = [e for _, _, lista in GRUPOS for e in lista]

# ---------- Ilustraciones propias (marcan el espacio de la foto real) ----------
def ilustracion():
    if VARIANTE == "a":
        # La "vía": un camino con paradas, del primer mensaje al control.
        return '''<svg class="ilustracion" viewBox="0 0 480 520" aria-hidden="true" focusable="false">
          <rect width="480" height="520" rx="32" fill="#DDF1EE"/>
          <path d="M70 450C70 340 410 380 410 270S90 220 90 120 300 60 410 70" fill="none" stroke="#0E4A55" stroke-width="3" stroke-dasharray="1 12" stroke-linecap="round"/>
          <g font-family="Sora, sans-serif" font-size="15" font-weight="600" fill="#0E4A55">
            <circle cx="70" cy="450" r="14" fill="#0E4A55"/><text x="96" y="455">Escribes</text>
            <circle cx="300" cy="352" r="14" fill="#FFFFFF" stroke="#0E4A55" stroke-width="3"/><text x="222" y="330">Valoración</text>
            <circle cx="160" cy="190" r="14" fill="#FFFFFF" stroke="#0E4A55" stroke-width="3"/><text x="64" y="232">Tu plan</text>
            <circle cx="410" cy="70" r="14" fill="#E07A5F"/><text x="300" y="44">Tu sonrisa</text>
          </g>
        </svg>'''
    if VARIANTE == "b":
        return '''<svg class="ilustracion" viewBox="0 0 480 400" aria-hidden="true" focusable="false">
          <rect width="480" height="400" rx="28" fill="#E8F0FB"/>
          <g fill="#1F5FAF" opacity=".14">''' + "".join(f'<circle cx="{30 + 35*i}" cy="{30 + 35*j}" r="2.5"/>' for i in range(13) for j in range(11)) + '''</g>
          <path d="M120 170c40 110 200 110 240 0" fill="none" stroke="#1F5FAF" stroke-width="6" stroke-linecap="round"/>
          <path d="M140 172c40 70 160 70 200 0" fill="none" stroke="#1F5FAF" stroke-opacity=".35" stroke-width="4" stroke-linecap="round"/>
          <circle cx="360" cy="110" r="34" fill="#FFFFFF"/><path d="M346 110l10 10 18-20" fill="none" stroke="#1F7A5A" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/>
        </svg>'''
    return '''<svg class="ilustracion" viewBox="0 0 1200 440" preserveAspectRatio="xMidYMid slice" aria-hidden="true" focusable="false">
          <rect width="1200" height="440" fill="#264D3F"/>
          <path d="M-20 360C250 360 330 120 600 120S950 360 1220 360" fill="none" stroke="#E2C48F" stroke-width="2" stroke-opacity=".7"/>
          <path d="M-20 400C250 400 330 170 600 170S950 400 1220 400" fill="none" stroke="#E2C48F" stroke-width="1" stroke-opacity=".35"/>
          <circle cx="600" cy="120" r="6" fill="#E2C48F"/>
        </svg>'''

def espacio_foto(texto, comentario):
    return f'<figure class="espacio-foto">{ilustracion()}<figcaption>{texto}</figcaption><!-- PENDIENTE: {comentario} --></figure>'

# ---------- Páginas ----------
PAGINAS = [
    ("index.html", "Inicio"),
    ("especialidades.html", "Especialidades"),
    ("la-clinica.html", "La clínica"),
    ("preguntas.html", "Preguntas frecuentes"),
    ("contacto.html", "Contacto"),
]

JSONLD = {
    "@context": "https://schema.org",
    "@type": "Dentist",
    "name": NOMBRE_GOOGLE,
    "alternateName": MARCA,
    "telephone": TEL,
    "address": {"@type": "PostalAddress", "streetAddress": "Calle 43 # 34-31, Cabecera del Llano",
                "addressLocality": "Bucaramanga", "addressRegion": "Santander", "addressCountry": "CO"},
    "openingHoursSpecification": [
        {"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"], "opens": "07:00", "closes": "12:00"},
        {"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"], "opens": "14:00", "closes": "19:00"},
        {"@type": "OpeningHoursSpecification", "dayOfWeek": "Saturday", "opens": "08:00", "closes": "12:00"},
    ],
    "sameAs": [INSTAGRAM],
}

def pagina(archivo, titulo, descripcion, cuerpo, jsonld=False):
    def items(desde):
        return "".join(f'<li><a href="{a}"{" aria-current=\"page\"" if a == archivo else ""}>{n}</a></li>' for a, n in PAGINAS[desde:])
    ld = ""
    if jsonld:
        ld = ('\n<!-- Dentist (LocalBusiness). PENDIENTE: url, geo con 5 decimales e image cuando haya dominio y fotos reales. Sin aggregateRating: las opiniones son de Google. -->\n'
              '<script type="application/ld+json">' + json.dumps(JSONLD, ensure_ascii=False) + '</script>')
    barra = ""
    if VARIANTE == "b":
        barra = (f'  <div class="barra-info"><div class="contenedor"><a href="tel:{TEL}">{I_TEL}{TEL_VISIBLE}</a>'
                 f'<span>{I_RELOJ}{HORARIO_CORTO}</span><span>{I_PIN}Cabecera, Bucaramanga</span></div></div>\n')
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
<link href="https://fonts.googleapis.com/css2?{CONF['fuentes']}&display=swap" rel="stylesheet">
<link rel="stylesheet" href="css/estilos.css">
<script>document.documentElement.classList.add("js")</script>
<script src="js/main.js" defer></script>{ld}
</head>
<body>
<a class="sr" href="#contenido">Saltar al contenido</a>
<div class="aviso-propuesta" role="note"><strong>Propuesta de diseño {VARIANTE.upper()}</strong> para la {MARCA}. No es el sitio oficial.</div>
<header class="encabezado">
{barra}  <div class="contenedor">
    <a class="marca" href="index.html" aria-label="{MARCA}, ir al inicio">
      <!-- PENDIENTE: monograma provisional; reemplazar por el logo real de la clínica. -->
      <span class="monograma" aria-hidden="true">VO</span>
      <span class="marca-texto">{MARCA}<small>Especialidades odontológicas</small></span>
    </a>
    <nav class="nav" aria-label="Principal"><ul>{items(1)}</ul></nav>
    <a class="btn btn--sm" href="{wa()}" target="_blank" rel="noopener">{I_WA}Agendar por WhatsApp</a>
    <button class="menu-boton" type="button" aria-expanded="false" aria-controls="menu-movil">Menú</button>
  </div>
  <nav class="menu-movil" id="menu-movil" aria-label="Menú móvil"><ul>{items(0)}</ul></nav>
</header>
<main id="contenido">
{cuerpo}
</main>
<footer class="pie">
  <div class="contenedor">
    <div class="pie-grid">
      <div>
        <h2>{MARCA}</h2>
        <p>Especialidades odontológicas en Bucaramanga.<br>{DIRECCION}.<br>{CIUDAD}.</p>
        <p><a href="tel:{TEL}">{TEL_VISIBLE}</a> · <a href="{wa()}" target="_blank" rel="noopener">WhatsApp</a> · <a href="{INSTAGRAM}" target="_blank" rel="noopener">Instagram</a></p>
      </div>
      <div>
        <h2>Horario</h2>
        <p>Lunes a viernes: 7:00 a. m. – 12:00 m. y 2:00 – 7:00 p. m.<br>Sábado: 8:00 a. m. – 12:00 m.<br>Domingo: cerrado.</p>
      </div>
      <div>
        <h2>Páginas</h2>
        <ul>{items(0)}</ul>
      </div>
    </div>
    <!-- PENDIENTE: enlace a la Política de tratamiento de datos (Ley 1581 de 2012) de la clínica. -->
    <p class="pie-legal">Este sitio no tiene formularios ni recoge datos personales. La dirección, el teléfono, el horario y la lista de especialidades se tomaron del perfil público de la clínica en Google y de su Instagram ({FECHA}).</p>
  </div>
</footer>
<a class="wa-flotante" href="{wa()}" target="_blank" rel="noopener" aria-label="Escribir por WhatsApp a la {MARCA}">{I_WA}<span>WhatsApp</span></a>
</body>
</html>
'''

def tabla_horario():
    filas = "".join(f'<tr><th scope="row">{d}</th><td>{h}</td></tr>' for d, h in HORARIO)
    return f'<table class="tabla-horario"><caption class="sr">Horario de atención</caption><tbody>{filas}</tbody></table>\n        <p class="nota">{NOTA_FESTIVOS}</p>'

def bloque_ubicacion():
    return f'''<div class="ubicacion">
      <div>
        <h2>Cómo llegar</h2>
        <p class="direccion">{DIRECCION}<br>{CIUDAD}</p>
        <div class="acciones">
          <a class="btn" href="{MAPS}" target="_blank" rel="noopener">{I_PIN}Abrir en Google Maps</a>
          <a class="btn btn--linea" href="{WAZE}" target="_blank" rel="noopener">Abrir en Waze</a>
        </div>
        <!-- PENDIENTE: piso o local, referencias para llegar, parqueadero y si la entrada es accesible en silla de ruedas (confirmar con la clínica). -->
      </div>
      <div>
        <h2>Horario de atención</h2>
        {tabla_horario()}
      </div>
    </div>'''

def chip_opiniones():
    return f'<a class="calificacion" href="{MAPS}" target="_blank" rel="noopener">{ESTRELLAS}<span><strong>{NOTA}</strong> en Google · Mira nuestras más de 300 reseñas</span></a>'

# ---------- Especialidades en el inicio: cambia la forma según la propuesta ----------
def especialidades_inicio():
    if VARIANTE == "a":
        bloques = []
        for clave, titulo, lista in GRUPOS:
            enlaces = "".join(f'<li><a href="especialidades.html#{i}">{n}</a></li>' for i, n, *_ in lista)
            bloques.append(f'<li class="grupo revelar"><span class="grupo-icono">{I_GRUPO[clave]}</span><h3>{titulo}</h3><ul>{enlaces}</ul></li>')
        return f'<ul class="grupos">{"".join(bloques)}</ul>'
    if VARIANTE == "b":
        tarjetas = []
        for clave, _, lista in GRUPOS:
            for i, n, texto, _ in lista:
                corto = texto.split(". ")[0] + "."
                tarjetas.append(f'<li class="tile revelar"><span class="tile-icono">{I_GRUPO[clave]}</span><h3><a href="especialidades.html#{i}">{n}</a></h3><p>{corto}</p></li>')
        return f'<ul class="tiles">{"".join(tarjetas)}</ul>'
    filas = []
    k = 0
    for _, titulo, lista in GRUPOS:
        items = ""
        for i, n, *_ in lista:
            k += 1
            items += f'<li><a href="especialidades.html#{i}"><span class="num">{k:02d}</span>{n}{I_FLECHA}</a></li>'
        filas.append(f'<div class="indice-grupo revelar"><h3>{titulo}</h3><ol>{items}</ol></div>')
    return f'<div class="indice-grande">{"".join(filas)}</div>'

def heroe():
    acciones = f'''<div class="acciones">
        <a class="btn" href="{wa()}" target="_blank" rel="noopener">{I_WA}Agenda tu valoración por WhatsApp</a>
        <a class="btn btn--linea" href="tel:{TEL}">{I_TEL}Llamar al {TEL_VISIBLE}</a>
      </div>'''
    h1 = "Odontología con <em>especialistas</em> en Cabecera, Bucaramanga"
    intro = ("En la Clínica Vía Oral te atienden en un solo lugar para ortodoncia con alineadores, endodoncia, "
             "periodoncia, implantes, diseño de sonrisa y las demás especialidades de la odontología.")
    if VARIANTE == "a":
        return f'''<section class="heroe">
  <div class="contenedor heroe-grid">
    <div>
      <p class="antetitulo">{MARCA}</p>
      <h1>{h1}</h1>
      <p class="intro">{intro}</p>
      {acciones}
      {chip_opiniones()}
    </div>
    {espacio_foto("Ilustración provisional · aquí va una foto real de la clínica", 'foto real de la recepción o de un consultorio (WebP, width/height, fetchpriority="high", sin lazy).')}
  </div>
</section>'''
    if VARIANTE == "b":
        return f'''<section class="heroe">
  <div class="contenedor heroe-grid">
    <div>
      <p class="antetitulo">{MARCA} · Bucaramanga</p>
      <h1>{h1}</h1>
      <p class="intro">{intro}</p>
      {acciones}
    </div>
    <div class="heroe-lado">
      {espacio_foto("Ilustración provisional · aquí va una foto real del equipo", 'foto real del equipo de la clínica (WebP, width/height, fetchpriority="high", sin lazy).')}
      <a class="sello" href="{MAPS}" target="_blank" rel="noopener"><span class="sello-cifra">{NOTA}</span>{ESTRELLAS}<span>{OPINIONES} opiniones en Google</span></a>
    </div>
  </div>
</section>'''
    return f'''<section class="heroe">
  <div class="contenedor heroe-centro">
    <p class="antetitulo">{MARCA}</p>
    <h1>{h1}</h1>
    <p class="intro">{intro}</p>
    {acciones}
    {chip_opiniones()}
  </div>
  <div class="contenedor">{espacio_foto("Ilustración provisional · aquí va una foto panorámica de la clínica", 'foto panorámica real de la clínica o la fachada (WebP, width/height, loading="lazy").')}</div>
</section>'''

inicio = f'''
{heroe()}

<section class="datos" aria-label="Datos de contacto">
  <ul class="contenedor">
    <li>{I_PIN}<span><strong>Dirección</strong>{DIRECCION}, Bucaramanga</span></li>
    <li>{I_TEL}<span><strong>Teléfono y WhatsApp</strong><a href="tel:{TEL}">{TEL_VISIBLE}</a></span></li>
    <li>{I_RELOJ}<span><strong>Horario</strong>Lun a vie 7–12 m. y 2–7 p. m.<br>Sábado 8–12 m.</span></li>
  </ul>
</section>

<section class="seccion" aria-labelledby="t-especialidades">
  <div class="contenedor">
    <div class="seccion-cabeza revelar">
      <p class="antetitulo">Especialidades</p>
      <h2 id="t-especialidades">Especialidades odontológicas en un solo lugar</h2>
      <p>Nueve tratamientos, ordenados según lo que necesitas: mejorar cómo se ve tu sonrisa, alinear tus dientes, conservarlos o reemplazar los que faltan.</p>
    </div>
    {especialidades_inicio()}
    <div class="acciones"><a class="btn btn--linea" href="especialidades.html">Ver todas las especialidades</a></div>
  </div>
</section>

<section class="seccion seccion--suave" aria-labelledby="t-alineadores">
  <div class="contenedor destacado">
    <div class="revelar">
      <p class="antetitulo">La especialidad que más destacamos</p>
      <h2 id="t-alineadores">Ortodoncia con alineadores, sin brackets</h2>
      <p>Los alineadores son férulas transparentes hechas a la medida que mueven los dientes poco a poco. Te los quitas para comer y para cepillarte, y casi no se notan al hablar.</p>
      <p>No todos los casos se tratan igual. En la valoración se revisa tu mordida y se te explica si los alineadores son una buena opción para ti y cuánto tiempo tomaría.</p>
      <!-- PENDIENTE: que el ortodoncista de la clínica revise y firme este texto; marca de alineadores que usan, si quieren mostrarla. -->
      <a class="btn" href="{wa('Hola, Clínica Vía Oral. Quiero información sobre ortodoncia con alineadores.')}" target="_blank" rel="noopener">{I_WA}Preguntar por alineadores</a>
    </div>
    <ul class="ventajas revelar">
      <li><strong>Transparentes</strong><span>Se notan muy poco al sonreír y al hablar.</span></li>
      <li><strong>Removibles</strong><span>Te los quitas para comer y para tu limpieza diaria.</span></li>
      <li><strong>Con controles</strong><span>El especialista revisa cómo avanzan tus dientes en cada cita.</span></li>
    </ul>
  </div>
</section>

<section class="seccion" aria-labelledby="t-equipo">
  <div class="contenedor">
    <div class="seccion-cabeza revelar">
      <p class="antetitulo">Quién te atiende</p>
      <h2 id="t-equipo">Nuestro equipo de especialistas</h2>
      <p>Cada tratamiento lo hace el odontólogo formado en esa especialidad.</p>
    </div>
    <!-- PENDIENTE: nombre, especialidad, universidad y foto real de cada odontólogo. No se muestran personas de relleno (CLAUDE.md, sección 3). -->
    <ul class="equipo">
      <li class="pendiente revelar"><span class="avatar" aria-hidden="true">?</span><strong>Nombre del especialista</strong><span>Especialidad · universidad</span><small>Dato pendiente: lo entrega la clínica</small></li>
      <li class="pendiente revelar"><span class="avatar" aria-hidden="true">?</span><strong>Nombre del especialista</strong><span>Especialidad · universidad</span><small>Dato pendiente: lo entrega la clínica</small></li>
      <li class="pendiente revelar"><span class="avatar" aria-hidden="true">?</span><strong>Nombre del especialista</strong><span>Especialidad · universidad</span><small>Dato pendiente: lo entrega la clínica</small></li>
    </ul>
  </div>
</section>

<section class="seccion seccion--oscura" aria-labelledby="t-pasos">
  <div class="contenedor">
    <div class="seccion-cabeza revelar">
      <h2 id="t-pasos">Cómo es tu primera cita</h2>
      <p>No tienes que saber qué tratamiento necesitas. Para eso está la valoración.</p>
    </div>
    <!-- PENDIENTE: confirmar con la clínica cómo es la valoración, su costo y si incluye radiografías. -->
    <ol class="pasos">
      <li class="revelar"><h3>Nos escribes</h3><p>Por WhatsApp o al {TEL_VISIBLE}. Cuéntanos qué te molesta o qué quieres mejorar y eliges el día.</p></li>
      <li class="revelar"><h3>Valoración</h3><p>Revisamos tus dientes, encías y mordida, y escuchamos lo que buscas.</p></li>
      <li class="revelar"><h3>Tu plan de tratamiento</h3><p>Te explicamos las opciones, quién te atiende, cuánto tiempo toma y cuánto cuesta, antes de empezar.</p></li>
    </ol>
    <div class="acciones"><a class="btn btn--claro" href="{wa()}" target="_blank" rel="noopener">{I_WA}Pedir mi valoración</a></div>
  </div>
</section>

<section class="seccion" aria-labelledby="t-opiniones">
  <div class="contenedor opiniones">
    <div class="nota-grande revelar">
      <div class="cifra">{NOTA}</div>
      {ESTRELLAS}
      <small>{OPINIONES} opiniones en Google<br>({FECHA})</small>
    </div>
    <div class="revelar">
      <h2 id="t-opiniones">Lo que dicen nuestros pacientes en Google</h2>
      <p>La clínica tiene una calificación de {NOTA} sobre 5 con {OPINIONES} opiniones en su perfil de Google. Las escriben los mismos pacientes y puedes leerlas todas allí.</p>
      <!-- PENDIENTE: 3 opiniones reales copiadas de Google, con nombre del autor, enlace a la reseña original y la marca Google. Sin datos estructurados de estrellas. -->
      <a class="btn btn--linea" href="{MAPS}" target="_blank" rel="noopener">Mira nuestras más de 300 reseñas en Google</a>
    </div>
  </div>
</section>

<section class="seccion seccion--suave" aria-label="Ubicación y horario">
  <div class="contenedor">
    {bloque_ubicacion()}
  </div>
</section>
'''

# ---------- especialidades.html ----------
def detalle(i, n, texto, tambien):
    return f'''    <article class="detalle" id="{i}">
      <h3>{n}</h3>
      <p>{texto}</p>
      <p class="tambien"><strong>También lo buscas como:</strong> {tambien}.</p>
      <a class="btn btn--sm btn--linea" href="{wa(f'Hola, Clínica Vía Oral. Quiero información sobre {n.lower()}.')}" target="_blank" rel="noopener">{I_WA}Preguntar por {n.lower()}</a>
    </article>'''

grupos_html = "\n".join(f'''  <section class="grupo-detalle" aria-labelledby="g-{clave}">
    <div class="grupo-cabeza"><span class="grupo-icono">{I_GRUPO[clave]}</span><h2 id="g-{clave}">{titulo}</h2></div>
{chr(10).join(detalle(*e) for e in lista)}
  </section>''' for clave, titulo, lista in GRUPOS)
indice = "".join(f'<li><a href="#{i}">{n}</a></li>' for i, n, *_ in ESPECIALIDADES)
especialidades = f'''
<section class="cabecera-pagina">
  <div class="contenedor">
    <p class="antetitulo">Especialidades</p>
    <h1>Especialidades odontológicas de la Clínica Vía Oral</h1>
    <p class="intro">Qué es cada tratamiento, en pocas palabras. El costo y el tiempo dependen de cada caso y se definen en la valoración.</p>
    <ul class="indice">{indice}</ul>
  </div>
</section>
<div class="seccion contenedor lista-detalle">
  <!-- PENDIENTE: que un odontólogo de la clínica revise y firme estos textos (tema de salud), y diga qué especialista hace cada tratamiento. -->
{grupos_html}
</div>
'''

# ---------- la-clinica.html ----------
la_clinica = f'''
<section class="cabecera-pagina">
  <div class="contenedor">
    <p class="antetitulo">La clínica</p>
    <h1>La Clínica Vía Oral y su equipo</h1>
    <p class="intro">Una clínica odontológica en Cabecera del Llano, Bucaramanga, donde trabajan especialistas de distintas áreas de la odontología.</p>
  </div>
</section>
<section class="seccion">
  <div class="contenedor dos-columnas">
    <div>
      <h2>Varias especialidades, una sola historia clínica</h2>
      <p>Muchos tratamientos necesitan más de un especialista: por ejemplo, tratar las encías antes de un diseño de sonrisa, o hacer una endodoncia antes de una corona. En la clínica esos pasos se coordinan en el mismo lugar.</p>
      <!-- PENDIENTE: un texto corto de la dirección de la clínica: desde cuándo atienden y cómo trabajan con sus pacientes. Solo datos comprobables. -->
      <h2>Lo que no te vamos a prometer</h2>
      <p>Cada boca es distinta. Por eso no damos precios ni resultados antes de revisarte: primero la valoración, luego un plan claro con costos y tiempos.</p>
    </div>
    {espacio_foto("Ilustración provisional · aquí va una foto real del consultorio", 'fotos reales: recepción, consultorio y fachada (WebP, width/height, loading="lazy").')}
  </div>
</section>
<section class="seccion seccion--suave" aria-labelledby="t-equipo">
  <div class="contenedor">
    <h2 id="t-equipo">Nuestro equipo</h2>
    <p>Aquí va cada especialista con su nombre, su especialidad, la universidad donde se formó y su foto.</p>
    <!-- PENDIENTE: datos reales y comprobables de cada odontólogo; registro profesional (ReTHUS) si lo quieren mostrar. -->
    <ul class="equipo">
      <li class="pendiente"><span class="avatar" aria-hidden="true">?</span><strong>Ortodoncia</strong><span>Nombre y universidad del especialista</span><small>Dato pendiente</small></li>
      <li class="pendiente"><span class="avatar" aria-hidden="true">?</span><strong>Endodoncia</strong><span>Nombre y universidad del especialista</span><small>Dato pendiente</small></li>
      <li class="pendiente"><span class="avatar" aria-hidden="true">?</span><strong>Periodoncia</strong><span>Nombre y universidad del especialista</span><small>Dato pendiente</small></li>
      <li class="pendiente"><span class="avatar" aria-hidden="true">?</span><strong>Rehabilitación oral e implantes</strong><span>Nombre y universidad del especialista</span><small>Dato pendiente</small></li>
    </ul>
  </div>
</section>
<section class="seccion">
  <div class="contenedor opiniones">
    <div class="nota-grande">
      <div class="cifra">{NOTA}</div>
      {ESTRELLAS}
      <small>{OPINIONES} opiniones en Google<br>({FECHA})</small>
    </div>
    <div>
      <h2>Opiniones de nuestros pacientes</h2>
      <p>Puedes leer todas las opiniones de la clínica en su perfil de Google y ver nuestro trabajo en Instagram.</p>
      <div class="acciones">
        <a class="btn btn--linea" href="{MAPS}" target="_blank" rel="noopener">Mira nuestras más de 300 reseñas en Google</a>
        <a class="btn btn--linea" href="{INSTAGRAM}" target="_blank" rel="noopener">{I_IG}Instagram @clinicaviaoralbga</a>
      </div>
    </div>
  </div>
</section>
'''

# ---------- preguntas.html ----------
PREG = [
    ("¿Cuánto cuesta la valoración?",
     "El valor de la valoración se confirma por WhatsApp al agendar. <!-- PENDIENTE: precio de la valoración y si incluye radiografías. -->El costo de cada tratamiento se da después de revisarte, porque depende de cada caso."),
    ("¿Los alineadores sirven para cualquier caso?",
     "No siempre. Funcionan bien en muchos casos de dientes apiñados o separados, pero algunas mordidas necesitan otro tratamiento. En la valoración te dicen si son una opción para ti."),
    ("¿Qué diferencia hay entre una carilla y una corona?",
     "La carilla cubre solo la cara de adelante del diente y se usa sobre todo por estética. La corona cubre el diente completo y se usa cuando está muy dañado o débil."),
    ("¿Una endodoncia duele?",
     "Se hace con anestesia local. Después es normal sentir el diente sensible unos días; el odontólogo te indica qué tomar y qué cuidados tener."),
    ("¿Cuándo debo ir al periodoncista?",
     "Si te sangran las encías al cepillarte, tienes mal aliento que no se quita, ves las encías retraídas o sientes algún diente flojo."),
    ("¿Cuándo se necesita un implante?",
     "Cuando falta un diente y se quiere reemplazar con uno fijo, sin tocar los dientes vecinos. Antes se revisa con radiografías si hay suficiente hueso."),
    ("¿Atienden los sábados?",
     "Sí, los sábados de 8:00 a. m. a 12:00 m. De lunes a viernes atendemos de 7:00 a. m. a 12:00 m. y de 2:00 a 7:00 p. m. En festivos el horario puede cambiar."),
    ("¿Dónde queda la clínica?",
     f'En la {DIRECCION}, {CIUDAD}. Puedes <a href="{MAPS}" target="_blank" rel="noopener">abrir la ubicación en Google Maps</a>.'),
    ("¿Cómo agendo una cita?",
     f'Escríbenos por <a href="{wa()}" target="_blank" rel="noopener">WhatsApp</a> o llama al <a href="tel:{TEL}">{TEL_VISIBLE}</a>.'),
]
preguntas_html = "\n".join(f'''      <article class="pregunta">
        <h2>{q}</h2>
        <p>{a}</p>
      </article>''' for q, a in PREG)
preguntas = f'''
<section class="cabecera-pagina">
  <div class="contenedor">
    <p class="antetitulo">Preguntas frecuentes</p>
    <h1>Preguntas frecuentes sobre tratamientos, costos y citas</h1>
    <p class="intro">Respuestas cortas a lo que más se pregunta antes de la primera cita.</p>
  </div>
</section>
<section class="seccion seccion--compacta">
  <div class="contenedor">
    <!-- PENDIENTE: que un odontólogo de la clínica revise estas respuestas (tema de salud) y agregue formas de pago y financiación. -->
    <div class="preguntas">
{preguntas_html}
    </div>
    <div class="acciones"><a class="btn" href="{wa('Hola, Clínica Vía Oral. Tengo una pregunta.')}" target="_blank" rel="noopener">{I_WA}¿Otra pregunta? Escríbenos</a></div>
  </div>
</section>
'''

# ---------- contacto.html ----------
contacto = f'''
<section class="cabecera-pagina">
  <div class="contenedor">
    <p class="antetitulo">Contacto</p>
    <h1>Contacto, dirección y horario de la Clínica Vía Oral</h1>
    <p class="intro">Escríbenos, llámanos o visítanos en Cabecera del Llano, Bucaramanga.</p>
  </div>
</section>
<section class="seccion">
  <div class="contenedor">
    <div class="contacto-grid">
      <div class="contacto-tarjeta">{I_WA}<h2>WhatsApp</h2><p>La forma más rápida de agendar o resolver una duda.</p><a class="btn" href="{wa()}" target="_blank" rel="noopener">Escribir por WhatsApp</a></div>
      <div class="contacto-tarjeta">{I_TEL}<h2>Teléfono</h2><p>{TEL_VISIBLE}</p><a class="btn btn--linea" href="tel:{TEL}">Llamar ahora</a></div>
      <div class="contacto-tarjeta">{I_IG}<h2>Instagram</h2><p>@clinicaviaoralbga</p><a class="btn btn--linea" href="{INSTAGRAM}" target="_blank" rel="noopener">Ver Instagram</a></div>
    </div>
  </div>
</section>
<section class="seccion seccion--suave" aria-label="Ubicación y horario">
  <div class="contenedor">
    {bloque_ubicacion()}
  </div>
</section>
'''

DESC = {
    "index.html": ("Clínica Vía Oral | Odontología con especialistas en Cabecera, Bucaramanga",
                   "Ortodoncia con alineadores, endodoncia, periodoncia, implantes, diseño de sonrisa y más en Cabecera del Llano, Bucaramanga. 5,0 en Google. Agenda por WhatsApp."),
    "especialidades.html": ("Especialidades odontológicas en Bucaramanga | Clínica Vía Oral",
                            "Diseño de sonrisa, carillas y coronas, blanqueamiento, alineadores, endodoncia, periodoncia, implantes, rehabilitación oral y cirugía oral, explicados en pocas palabras."),
    "la-clinica.html": ("La clínica y su equipo | Clínica Vía Oral, Bucaramanga",
                        "Clínica odontológica con varias especialidades en Cabecera del Llano, Bucaramanga. Conoce cómo trabajamos y lee las opiniones de nuestros pacientes en Google."),
    "preguntas.html": ("Preguntas frecuentes sobre tratamientos y citas | Clínica Vía Oral",
                       "Costo de la valoración, alineadores, carillas y coronas, endodoncia, implantes, horario de sábado y cómo agendar en la Clínica Vía Oral."),
    "contacto.html": ("Contacto, dirección y horario | Clínica Vía Oral, Bucaramanga",
                      "Calle 43 # 34-31, Cabecera del Llano, Bucaramanga. Teléfono y WhatsApp 314 394 3828. Lunes a viernes 7–12 y 2–7, sábado 8–12."),
}
CUERPOS = {"index.html": inicio, "especialidades.html": especialidades, "la-clinica.html": la_clinica,
           "preguntas.html": preguntas, "contacto.html": contacto}

DESTINO.mkdir(parents=True, exist_ok=True)
for archivo, cuerpo in CUERPOS.items():
    t, d = DESC[archivo]
    (DESTINO / archivo).write_text(pagina(archivo, t, d, cuerpo, jsonld=archivo in ("index.html", "contacto.html")), encoding="utf-8")
fondo, letra = CONF["favicon"]
(DESTINO / "assets").mkdir(parents=True, exist_ok=True)
(DESTINO / "assets" / "favicon.svg").write_text(
    f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><rect x="2" y="2" width="60" height="60" rx="16" fill="{fondo}" stroke="{letra}" stroke-width="3"/>'
    f'<text x="32" y="41" text-anchor="middle" font-family="Arial, sans-serif" font-weight="700" font-size="22" fill="{letra}">VO</text></svg>\n', encoding="utf-8")
# CSS: base compartida + tema de la propuesta. JS: el mismo para las tres.
RAIZ = Path(__file__).parent
(DESTINO / "css").mkdir(exist_ok=True)
(DESTINO / "js").mkdir(exist_ok=True)
(DESTINO / "css" / "estilos.css").write_text(
    (RAIZ / "estilos" / "base.css").read_text(encoding="utf-8") + "\n" + (RAIZ / "estilos" / f"tema-{VARIANTE}.css").read_text(encoding="utf-8"), encoding="utf-8")
(DESTINO / "js" / "main.js").write_text((RAIZ / "js" / "main.js").read_text(encoding="utf-8"), encoding="utf-8")
print("ok", VARIANTE)
