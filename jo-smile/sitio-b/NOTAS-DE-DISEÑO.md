# Notas de diseño: versión B ("Ciruela y menta")

Misma estructura, páginas, textos y huecos que la versión A (`../sitio/`). Solo cambia el diseño.

## Paleta
| Token | Color | Uso |
|---|---|---|
| `--ciruela` | `#3B2150` | Principal: ciruela profunda, seria pero cálida, poco común entre clínicas |
| `--menta` | `#5CC9A7` | Acento: menta, asociada a frescura y limpieza dental (resaltados, íconos, botones secundarios) |
| `--menta-texto` | `#1A7A60` | Menta oscura para texto (4.8:1 sobre el fondo) |
| `--fondo` | `#F5F3F9` | Fondo lavanda grisáceo; los bloques van en blanco |
| `--tinta` | `#21182B` | Texto |

Contraste verificado: blanco sobre ciruela 13.8:1, texto secundario 6.9:1, menta sobre ciruela 6.8:1 (todo AA).

## Tipografía
- **Bricolage Grotesque** para titulares: grotesca moderna con carácter, se siente actual y cercana.
- **Atkinson Hyperlegible** para el texto: diseñada para máxima legibilidad, ideal para leer en celular.

## Diferencias con la versión A
- Encabezado flotante redondeado, con el menú en forma de "pastillas".
- Las secciones son bloques redondeados separados del fondo (sin curvas).
- El acento de los titulares es un resaltador menta que se dibuja al aparecer (en A era cursiva terracota).
- Etiquetas de sección en forma de chip menta, y pasos numerados en cuadros ciruela unidos por una línea punteada.
- Servicios en tarjetas grandes; el selector de servicio va sobre fondo ciruela.
- Barra de WhatsApp flotante en celular, separada de los bordes.
- La textura es una trama de puntos finos (en A era grano de papel).

## Técnica
- El HTML es el de la versión A con los colores de las ilustraciones cambiados; solo el CSS es nuevo.
- `js/main.js` es idéntico al de la versión A; el número de WhatsApp se configura igual.
