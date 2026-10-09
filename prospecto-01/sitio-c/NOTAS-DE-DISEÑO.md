# Notas de diseño: versión C ("Consultorio claro")

Misma estructura, páginas, textos y huecos que las versiones A y B. Solo cambia el diseño.

## Paleta (azul, gris y blanco)
| Token | Color | Uso |
|---|---|---|
| `--azul` | `#1D4F91` | Único color de marca: azul medio-oscuro |
| `--azul-900` | `#163C6E` | Pie de página, hover de botones |
| `--azul-50` / `--azul-100` | `#EEF3FA` / `#DCE7F5` | Fondos de íconos y realces suaves |
| `--gris-fondo` | `#F3F5F8` | Secciones alternas |
| `--gris-linea` | `#DDE3EA` | Líneas finas que estructuran la página |
| `--tinta` | `#1E2A38` | Texto principal (13:1) |
| `--tinta-suave` | `#485565` | Texto secundario (7:1) |

Contraste: blanco sobre azul 8.1:1, azul sobre blanco 8.1:1, texto secundario sobre gris 7:1, texto claro sobre azul 6.2:1 (todo AA, la mayoría AAA).

## Tipografía
- **Lexend** para titulares, en peso medio: fue diseñada para facilitar la lectura y se ve limpia, sin ser pesada.
- **Source Sans 3** para el texto, a 18 px: muy legible en celular.
- Los titulares van en peso 500 (el principal en 600), para que no se vean demasiado remarcados.

## Estilo
- Secciones rectas a todo el ancho, separadas por líneas finas grises (sin curvas ni bloques flotantes).
- Esquinas casi rectas (6 a 10 px) y botones rectangulares con una flecha que aparece al pasar el mouse.
- Servicios en cuadrícula con líneas compartidas; al pasar el mouse aparece una línea azul arriba.
- Pasos de la valoración como línea de tiempo (vertical en celular, horizontal en computador).
- Preguntas frecuentes como lista con líneas, sin tarjetas.
- Textura de cuadrícula fina tipo papel milimetrado, muy sutil.
- Movimiento: aparición deslizando desde la izquierda y subrayados que crecen.
