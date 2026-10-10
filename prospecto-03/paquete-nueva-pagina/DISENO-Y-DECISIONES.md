# Diseño: lo que pidió el cliente y lo que ya existe

## Lo que pidió y aprobó el cliente (en orden)

1. **Estructura primero:** cinco páginas — Inicio, Tratamientos, La doctora, Preguntas frecuentes, Contacto. Aprobada.
2. **Nombre:** mostrar "Consultorio Dra. Vanesa Gutiérrez" (no solo "Dra. Vanesa Gutiérrez"). Se dedujo de la respuesta "Consultorio Dra Vanesa Gutiérrez usa ete" (ver `VERIFICACION.md`, nota 1).
3. **Direcciones:** mostrar las dos placas del Edificio Alto Prado.
4. **WhatsApp:** el 324 492 5383 recibe WhatsApp.
5. **Tonos femeninos** en todas las propuestas.
6. **Imágenes:** usar fotos de internet para simular cómo se verá con fotos, porque "las imágenes son las que más van a ayudar a generar confianza", y siempre **acompañadas de su descripción**.
7. **Ver los movimientos:** quería probar las páginas en vivo (aparición suave al bajar, encabezado fijo, botón flotante de WhatsApp en celular).
8. **Versiones fuera de lo común y más profesionales**, que no se vean genéricas, **manteniendo todos los detalles**. De ahí salieron D (editorial) y E (mosaico). Respuesta del cliente a las primeras: "se ve súper bien".

## Estructura de la página de inicio (todas las propuestas)

1. Primera pantalla: nombre, especialización, botones de WhatsApp y llamada, calificación de Google, foto.
2. Datos a la vista: dirección, teléfono y WhatsApp, horario.
3. Tratamientos (8), cada uno con foto, qué es y enlace al detalle.
4. Conoce a la doctora: formación y enfoque.
5. Así es tu primera cita: 3 pasos.
6. Opiniones en Google: 5,0 con 61 opiniones y enlace.
7. Dónde atendemos y horario completo, con botones a Google Maps y Waze.
8. Pie: datos, horario, páginas, aviso de que no se recogen datos.
9. En celular: botón flotante de WhatsApp.

## Las 5 propuestas ya hechas (no repetirlas)

| | Estilo | Colores | Letras | Rasgo principal |
|---|---|---|---|---|
| A | Cálido y elegante | Rosa empolvado `#FDF7F7`, frambuesa `#A23E5E`, vino rosado `#5E1F35` | Fraunces + Figtree | Arco con foto, tarjetas de tratamientos con una destacada |
| B | Clínico y luminoso | Lila `#FAF7FC`, ciruela `#6B3F86`, orquídea `#C2649A` | Outfit + Nunito Sans | Barra superior con teléfono y horario, tarjetas de datos sobre la primera pantalla |
| C | Editorial oscuro | Ciruela profundo `#2A1C24`, marfil `#FBF4F2`, oro rosa `#E0AE9D` | Bodoni Moda + Jost | Primera pantalla centrada y oscura, banda panorámica, botones rectos |
| D | Revista | Papel `#F6EFEA`, berenjena `#2B1E2A`, rosa `#A8455F` | Instrument Serif + Inter Tight | Portada dividida con ficha de datos, índice de tratamientos, perfil tipo hoja de vida, línea de tiempo |
| E | Mosaico moderno | Nude `#F4EEEC`, baya `#8E2F55`, rubor `#F6DCE5` | Young Serif + Hanken Grotesk | Encabezado flotante, inicio en bloques, mosaico de tratamientos, "abierto ahora" en vivo |

Capturas en `capturas/`. Enlaces en `LEEME.md`.

## Detalles que funcionaron y conviene mantener

- Cada botón de WhatsApp lleva un **mensaje ya escrito** según el tratamiento.
- **"Abierto ahora / cerrado · abre a las…"** calculado con la hora de Bogotá (propuestas D y E).
- Los nombres de los tratamientos están en las palabras del paciente, con una línea "También lo buscas como…" que recoge los términos de Google (lentes cerámicos, veneers, autoligado, zafiro, detartraje…).
- Preguntas frecuentes **visibles**, sin desplegables.
- Contraste AA comprobado en todos los colores; `prefers-reduced-motion` respetado; objetivos táctiles de 44 px o más.
- Sin formularios (no se recogen datos), así que no hace falta casilla de autorización todavía.
