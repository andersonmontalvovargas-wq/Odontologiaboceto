# Notas de diseño: sitio JO SMILE (boceto para aprobación)

## Páginas
- `index.html`: inicio. Propuesta, señales de confianza reales, resumen de servicios, cómo es la primera cita, testimonios, preguntas clave y cierre.
- `servicios.html`: las 6 especialidades provisionales de `CONTENIDO.md`, cada una con su ancla y su botón de WhatsApp, más el selector "¿Qué te gustaría resolver?".
- `nosotros.html`: la clínica, cómo trabaja, el espacio para el equipo y los testimonios.
- `preguntas.html`: las 8 preguntas frecuentes (son más de 4, así que van en página propia).
- `contacto.html`: WhatsApp, ubicación, horario y cómo llegar.

## Paleta (sin logo conocido: paleta propia, sin el clásico azul clínico)
| Token | Color | Uso |
|---|---|---|
| `--pino` | `#1E4D48` | Principal: verde pino profundo, sereno, distinto al azul de clínica genérica |
| `--pino-900` | `#163A36` | Fondos oscuros, hover |
| `--terracota` | `#B35A34` | Acento cálido (botón secundario, detalles); con texto, `#A24F2C` |
| `--hueso` | `#FAF7F2` | Fondo general (blanco hueso, no blanco puro) |
| `--arena` | `#F2EBE0` | Secciones alternas |
| `--tinta` | `#1D2B2A` | Texto |

Contraste verificado: texto sobre hueso 6.8:1, blanco sobre pino 9.5:1, terracota de texto sobre hueso 5.3:1 (todos AA).

## Tipografía
- **Fraunces** para titulares: serif con calidez y carácter que se siente humana y cuidada, no corporativa.
- **Figtree** para el texto: sans geométrica muy legible en celular, amable sin ser infantil.

## Canal de contacto
WhatsApp en todos los botones, con mensaje precargado según el contexto. El número está pendiente: se configura en **una sola línea** (`js/main.js`, `WHATSAPP_NUMERO`). Mientras tanto, los enlaces abren WhatsApp con el mensaje escrito para que la persona elija el contacto.

## Decisiones
- Sin fotos reales, todo lo visual es ilustración SVG abstracta (arcos, curvas, trazo de diente). No hay stock ni nada que finja ser el equipo o el consultorio.
- No se usó la franja "Boceto de propuesta" del boceto anterior: este debe verse terminado. Los huecos se resuelven con texto neutro y comentarios `<!-- PENDIENTE -->`.
- Dirección escrita pendiente: según la especificación, no se pone el mapa incrustado. En su lugar va un marco ilustrado con el botón "Ver ubicación en Google Maps", que usa el enlace real de la ficha (dato extraído).
- Preguntas cuyo dato es pendiente (precio de la valoración, pagos, urgencias, EPS): se responden de forma neutra invitando a preguntar por WhatsApp, sin inventar cifras.
- Equipo: sin nombres, va un bloque intencional ("Aquí presentaremos a cada especialista…"). No se ponen tarjetas vacías porque sugerirían un número de especialistas.
- "Por qué confiar" solo usa hechos reales: es una clínica de especialidades (nombre), está en el área metropolitana de Bucaramanga (ubicación de la ficha) y tiene opiniones públicas en Google (ficha).
- Ciudad en los textos: "Bucaramanga y su área metropolitana". La ficha parece estar en Floridablanca; se ajusta cuando se confirme.
- Servicios: se usan los 6 `[SUGERIDO]` de `CONTENIDO.md` (permitidos para el boceto). Quedan marcados como pendientes de confirmación.
- Botones: el principal es verde pino con el ícono de WhatsApp, para que combine con la marca. El botón flotante sí lleva el verde de WhatsApp, para que se reconozca al instante.
- En celular, en lugar del botón flotante hay una barra fija abajo (WhatsApp + Ubicación), para no duplicar botones.
- Sin imagen para compartir (og:image): no hay foto ni logo real. Queda en pendientes.
- Git: la carpeta ya está dentro de un repositorio, así que se hace el commit ahí en vez de crear un repositorio anidado.
- El HTML repetido (encabezado y pie) se generó con un script local para que sea idéntico en todas las páginas. El resultado es HTML estático puro.
