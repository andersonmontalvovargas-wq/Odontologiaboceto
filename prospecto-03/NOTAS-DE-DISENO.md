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
