# Notas de diseño: versión B (estilo de bloques redondeados, en azul, gris y blanco)

Misma estructura, páginas, textos y huecos que la versión A (`../sitio/`). Primero se hizo en ciruela y menta; a pedido del cliente se pasó a azul, gris y blanco, manteniendo el estilo.

## Paleta
| Token | Color | Uso |
|---|---|---|
| `--azul` | `#1D4F91` | Principal: azul medio-oscuro (ni celeste ni azul marino) |
| `--azul-900` | `#163C6E` | Pie de página y fondos más profundos |
| `--acento` | `#B4D2F6` | Azul claro: solo como detalle sobre fondos azules (íconos, botones claros) |
| `--acento-100` | `#D3E3F8` | Resaltador de titulares y fondo de íconos |
| `--fondo` | `#F3F5F8` | Gris muy claro de fondo; los bloques van en blanco |
| `--tinta` | `#1E2A38` | Texto principal (13:1) |
| `--tinta-suave` | `#485565` | Texto secundario (7:1): legible, sin verse pálido |

Contraste: blanco sobre azul 8.1:1, texto azul sobre gris 7.5:1, etiquetas azules sobre su fondo claro 5.3:1, azul claro sobre azul profundo 8:1 (todo AA).

## Legibilidad
- Títulos un grado más livianos que en la primera versión de B (700 → 600, y 800 → 700 en el principal), para que no se vean demasiado remarcados.
- El texto secundario se oscureció para que no quede "clarito".

## Tipografía
- **Bricolage Grotesque** para titulares y **Atkinson Hyperlegible** para el texto (máxima legibilidad en celular).

## Estilo
Encabezado flotante redondeado, secciones en bloques con esquinas suaves, resaltador bajo las palabras destacadas, pasos en cuadros unidos por línea punteada y barra de WhatsApp flotante en celular.
