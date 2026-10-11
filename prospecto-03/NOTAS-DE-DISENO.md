# Notas de diseño: tres propuestas con la misma estructura

Mismas páginas, secciones y textos en las tres. Cambia la presentación.

| | A · Rosa empolvado | B · Lavanda clínica | C · Ciruela y oro rosa |
|---|---|---|---|
| Sensación | Cálida, femenina y elegante | Limpia, suave y cercana | Sofisticada, de lujo discreto |
| Colores | Rosa muy claro `#FDF7F7`, frambuesa `#A23E5E`, vino rosado `#5E1F35` | Lila claro `#FAF7FC`, ciruela `#6B3F86`, lavanda `#EFE7F7`, orquídea `#C2649A` | Ciruela profundo `#2A1C24`, marfil rosado `#FBF4F2`, oro rosa `#E0AE9D` |
| Titulares / texto | Fraunces / Figtree | Outfit / Nunito Sans | Bodoni Moda / Jost |
| Primera pantalla | Texto a la izquierda y arco con sonrisa | Barra superior con teléfono y horario; tarjetas de datos sobre la primera pantalla | Centrada sobre fondo oscuro, con banda panorámica para la foto |
| Tratamientos | Tarjetas, la primera destacada | Cuadrícula pareja de 4 | Lista numerada en dos columnas |
| Botones | Redondos | Esquinas suaves | Rectos, en mayúsculas |

Tonos femeninos a pedido del cliente. Contraste comprobado (AA) en todas las combinaciones de texto: el más bajo es 4,7:1 en texto normal.

Fotos de referencia de Pexels en la primera pantalla, en cada tratamiento y en el espacio de la doctora (ver `CREDITOS.md`).

## Propuestas D y E: estructura propia

Mismos textos, datos, horario, fotos con su descripción y las 5 páginas que A, B y C (los textos salen de `generar.py`). Cambia la forma de presentar la información, para que no se vea como una plantilla.

| | D · Editorial | E · Mosaico |
|---|---|---|
| Idea | Revista de salud y estética: mucho aire, líneas finas, tipografía protagonista | Página de producto moderna: bloques redondeados con un dato cada uno |
| Colores | Papel `#F6EFEA`, berenjena `#2B1E2A`, rosa `#A8455F` | Nude `#F4EEEC`, baya `#8E2F55`, rubor `#F6DCE5`, malva `#EADFE6` |
| Titulares / texto | Instrument Serif / Inter Tight | Young Serif / Hanken Grotesk |
| Primera pantalla | Dividida: foto a la izquierda y, a la derecha, el nombre con una ficha de datos (calificación, dirección, teléfono, horario) | Mosaico: título, foto, calificación, horario, dirección y formación, cada uno en su bloque |
| Tratamientos | Índice numerado tipo revista: foto, qué es y "también lo buscas como" en una fila | Mosaico de fotos con la explicación debajo; el diseño de sonrisa ocupa el bloque grande |
| La doctora | Perfil tipo hoja de vida sobre fondo berenjena | Bloque con foto y ficha de datos |
| Primera cita | Línea de tiempo con tres pasos | Tres bloques sobre fondo baya |
| Detalle | Página de tratamientos en zigzag (foto y texto alternados); preguntas en dos columnas | Tratamientos en tarjetas horizontales; preguntas en bloques de dos columnas |

Las dos muestran si el consultorio está **abierto ahora**, calculado con la hora de Bogotá y el horario de Google (`js/main.js`). Sin JavaScript no aparece y el horario sigue visible.
Contraste AA comprobado: el más bajo es 5:1 en texto normal.

## Propuesta F · Porcelana (durazno y cacao)

Mismos textos, datos, horario y 5 páginas (salen de `generar.py`); estructura propia en `generar_f.py`. La idea parte de la guía de color que usa la odontóloga para elegir el tono de una carilla.

| | F · Porcelana |
|---|---|
| Colores | Crema `#FFF8F3`, durazno `#FBE4D8`, cacao `#34202A`, rosa `#A3354B`, coral `#F4B6A6` |
| Titulares / texto | Cormorant / Manrope |
| Primera pantalla | Nombre grande a la izquierda; foto en óvalo que se abre al cargar y un sello circular que gira mientras se baja. Debajo, una franja cacao con dirección, teléfono y horario (con "abierto ahora") |
| Tratamientos (inicio) | Muestrario que se desliza de lado, con botones anterior/siguiente: cada tarjeta lleva un tono de la guía de color, foto con su descripción, qué es y "también lo buscas como" |
| Tratamientos (página) | Foto grande en arco que se queda fija y cambia según el tratamiento que se lee; barra de accesos rápidos a los 8 |
| La doctora | Foto en arco y ficha de datos |
| Primera cita | Línea vertical que se llena al bajar |
| Opiniones | "5,0" grande sobre fondo cacao |
| Ubicación | Las dos placas del Edificio Alto Prado como letreros; horario con una barra por día y el día de hoy marcado |
| Preguntas | Título fijo a la izquierda y las 9 preguntas numeradas a la derecha, todas visibles |

Fotos genéricas de referencia (Pexels) en todas las páginas, cada una con su descripción visible: primera pantalla, los 8 tratamientos, la doctora (foto del consultorio con el letrero de la foto real), primera cita, preguntas frecuentes y contacto. Son las mismas fotos que ya cargaron en A–E.

Nada se mueve solo: el sello y la línea de pasos se mueven con el desplazamiento, así que no necesitan botón de pausa. Con `prefers-reduced-motion` todo queda quieto. Sin JavaScript el contenido se ve completo.
Contraste AA comprobado: el más bajo en texto normal es 5,4:1 (rosa sobre durazno). Los números de las preguntas, en coral, son decorativos (`aria-hidden`).

## Propuestas G y H: dos conceptos distintos de F

Mismos textos, datos, horario y 5 páginas (salen de `generar.py`), con la misma forma de escribir. Cada una tiene su propio generador, CSS y JavaScript.

| | G · Nácar (transiciones tipo página de producto) | H · Retícula (estilo suizo tipográfico) |
|---|---|---|
| Idea | Mucho blanco, una sola tipografía, el contenido aparece con transiciones ligadas al desplazamiento | Retícula de 12 columnas con líneas finas visibles, tipografía protagonista, esquinas rectas y sin sombras |
| Colores | Blanco `#FBFBFD`, gris `#F5F5F7`, negro, orquídea `#B0246A`, degradado orquídea → violeta `#7A3FB5` | Papel `#F3EFE8`, tinta `#171415`, frambuesa `#C8284F`, malva `#DCD3E0` |
| Tipografía | Geist (una sola familia, varios pesos) | Archivo extendida en mayúsculas para titulares, Archivo normal para texto y JetBrains Mono para etiquetas y datos |
| Encabezado | Navegación global y barra secundaria fija con el nombre de la página, el teléfono y el botón "Agendar" | Barra con las páginas numeradas (01–04) separadas por líneas |
| Primera pantalla | Titular centrado con degradado; al bajar, la foto crece hasta llenar la pantalla | Nombre enorme en mayúsculas extendidas; debajo, tres columnas: texto y botones, ficha del consultorio con la hora de Bucaramanga, y la foto como "Fig. 01" |
| Tratamientos (inicio) | Las 8 tarjetas pasan de lado mientras se baja, con una barra de avance (en computador). En celular, una debajo de otra | Tabla de 4 × 2 con líneas; al pasar el cursor, la celda se invierte a tinta |
| La doctora | Párrafo que se ilumina palabra por palabra sobre fondo negro | Bloque malva con foto y ficha técnica |
| Primera cita | Tres fichas grises con números en degradado | Tres columnas con números gigantes en frambuesa |
| Opiniones | "5,0" gigante en degradado sobre negro | "5,0 / 5" gigante sobre tinta |
| Horario | Lista con el día de hoy marcado | Tabla con franja de 6 a. m. a 10 p. m. por día y el día de hoy marcado |
| Página de tratamientos | Índice de 8 fichas y un capítulo por tratamiento; la foto crece al llegar | Índice en retícula y una ficha técnica por tratamiento (Qué es / También lo buscas como) |
| Preguntas | Fichas en dos columnas | Filas: número, pregunta y respuesta |
| WhatsApp en celular | Botón redondo flotante | Barra fija a lo ancho de la pantalla |

Nada se mueve solo: todo lo que se mueve depende del desplazamiento. Con `prefers-reduced-motion`, G se ve como una página normal (sin foto que crece, sin desfile de tarjetas, texto ya iluminado) y H aparece quieta. Sin JavaScript, las dos muestran el contenido completo.
Contraste AA comprobado. El más bajo en texto normal es 4,66:1 en G (gris sobre ficha gris) y 4,73:1 en H (frambuesa sobre papel). Sobre malva, H usa frambuesa oscuro (5,4:1).

