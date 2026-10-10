# Notas de diseño: tres propuestas con los mismos textos

Mismas 5 páginas y mismos textos (`generar.py`). Cambian la primera pantalla, la forma de mostrar las especialidades, los colores y las fuentes.

| | A · La vía | B · Clínica clara | C · Editorial |
|---|---|---|---|
| Sensación | Moderna, cercana y ordenada | Limpia, clínica y confiable | Sobria, de clínica de alto nivel |
| Colores | Menta clara `#F6FBFA`, verde azulado `#0E6170`, coral `#F2A48C` (decorativo) | Blanco, azul `#1F5FAF`, azul marino `#16294A`, verde menta `#7FC8A9` | Marfil `#F7F4EE`, verde bosque `#1E5A46` / `#1E3F33`, dorado `#E2C48F` |
| Titulares / texto | Sora / Manrope | Plus Jakarta Sans (una sola familia) | Instrument Serif / Albert Sans |
| Primera pantalla | Texto a la izquierda; a la derecha la ilustración del "camino" (escribes → valoración → tu plan → tu sonrisa), que juega con el nombre "Vía" | Barra superior con teléfono y horario; sello grande "5,0 · 322 opiniones" sobre la imagen | Centrada sobre fondo verde oscuro, con una banda panorámica para la foto de la clínica |
| Especialidades en el inicio | 4 tarjetas por grupo con enlaces | 9 fichas con ícono y una frase | Índice numerado del 01 al 09, por grupos |
| Botones | Esquinas suaves | Redondos | Rectos, en mayúsculas |

Contraste comprobado (WCAG AA) en todas las combinaciones de texto: el más bajo es 4,9:1 (números de los pasos en A, texto grande).

Elementos comunes: aviso de propuesta, `noindex`, franja con dirección, teléfono y horario bajo la primera pantalla, botón flotante de WhatsApp en celular, horario completo con aviso de festivos y JSON-LD `Dentist` en inicio y contacto.

Archivos: `estilos/base.css` (estructura compartida) + `estilos/tema-a|b|c.css`; `generar.py` los une en `sitio-*/css/estilos.css`.
