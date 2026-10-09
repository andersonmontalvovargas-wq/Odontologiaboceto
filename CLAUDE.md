# Reglas para construir páginas web de negocios de servicios

Estas reglas se aplican a toda página que se construya en este proyecto. Son las bases; lo que cambia es la adaptación a cada negocio. Si una regla no aplica, se dice por qué. Nada se inventa: cifras, credenciales, reseñas y promesas deben ser reales y comprobables.

## 1. Antes de construir: definir el contexto

Pregunta o deduce estas cuatro variables antes de escribir código:

| Variable | Pregunta |
| --- | --- |
| Acción principal | ¿Agendar cita, pedir cotización, comprar o llamar? |
| Canal | ¿WhatsApp, llamada, formulario o reserva en línea? |
| Sensibilidad del sector | ¿Afecta salud, dinero o seguridad? Si sí, más exigencia de confianza y revisar reglas de publicidad del sector. |
| Presencia física | ¿Local visible o va donde el cliente? |
| Tipo de marca | ¿Marca personal (el nombre del profesional es la marca) o marca de negocio (un nombre comercial)? |

Define también si es **boceto** (propuesta para un prospecto) o **sitio final**.

**Según el tipo de marca:**
- **Marca personal:** la página gira en torno al profesional: su nombre, formación y foto en primer plano. En Google puede tener su propio perfil de profesional.
- **Marca de negocio:** la página gira en torno al nombre comercial; el equipo aparece como respaldo. En Google, el perfil es del negocio.
- Si conviven las dos (un negocio con profesionales visibles), se decide cuál lidera y la otra acompaña.

## Nombres y datos en ejemplos y documentación

- En reglas, plantillas, ejemplos y documentación general se usan **nombres inventados**, con el tipo de marca entre paréntesis. Por ejemplo: "Dra. Ana Ruiz (marca personal, profesional)" o "Centro Vital Norte (marca de negocio, consultorio)".
- Nunca se escriben en estos archivos nombres, teléfonos, direcciones ni datos de prospectos o clientes reales.
- Los datos de un prospecto real solo viven en la carpeta de su boceto, y esa carpeta lleva un nombre neutro (por ejemplo, `prospecto-01/`), no el nombre de la persona o del negocio.

## 2. Boceto o sitio final

**Boceto:**
- `<meta name="robots" content="noindex">` en todas las páginas.
- Aviso visible arriba: "Propuesta de diseño para [negocio]. No es el sitio oficial."
- Solo información pública del negocio. No usar su logo o fotos de forma que parezca aprobado.
- El repositorio y la carpeta del boceto llevan nombres neutros, no el nombre del prospecto.
- Diseño propio para cada prospecto: no repetir la misma plantilla con otro logo, ni textos o fotos entre clientes.

**Sitio final:**
- Quitar el `noindex` (si queda, Google no muestra el sitio ni lee sus datos estructurados).
- Etiqueta `google-site-verification` de Search Console en el `<head>` de la página de inicio.
- Etiqueta de Google Analytics 4 justo después de `<head>` en cada página.
- `robots.txt` que no bloquee a Googlebot ni a OAI-SearchBot.

## 3. Contenido y confianza

- Teléfono o WhatsApp, dirección y horarios visibles sin buscar; el llamado a la acción principal en la primera pantalla.
- Navegación con las palabras del cliente (el nombre común del servicio, no uno ingenioso).
- Mostrar personas y lugares reales: equipo con nombre y formación, fotos propias, cómo es el primer paso con el cliente.
- Nunca simular un equipo con imágenes de relleno ni poner credenciales que no se puedan comprobar.
- Textos de temas sensibles firmados por el profesional real.
- Toda la información clave en texto HTML, no solo en imágenes, PDF o video. Si hay video, acompañarlo de un resumen escrito.
- Preguntas reales con respuestas cortas que se entiendan solas. No esconder respuestas clave en pestañas o desplegables.
- Encabezados que nombren cada idea; nada de "Más información" genérico.
- Sin frases vagas ("de última generación") ni cifras sin respaldo.

**Reseñas en la página:**
- La frase se adapta a la cantidad real: con un número que respalde, "Mira nuestras más de X reseñas en Google"; con pocas, "Revisa algunas de nuestras reseñas en Google"; si casi no hay, solo reseñas internas reales.
- Si se traen de Google, mostrar autor, enlace a la reseña original y la marca Google.
- No marcar reseñas propias con datos estructurados para buscar estrellas.

## 4. Velocidad (medir en móvil)

Metas de Core Web Vitals: LCP ≤ 2,5 s, INP ≤ 200 ms, CLS ≤ 0,1.

- Imagen principal en el HTML, sin `loading="lazy"` y con `fetchpriority="high"`.
- Imágenes fuera de la primera pantalla y diapositivas de carrusel con `loading="lazy"` o `fetchpriority="low"`.
- Formatos WebP o AVIF, tamaño adecuado y comprimidas; `width` y `height` declarados.
- Pocas fuentes web, con `font-display: swap`.
- Scripts con `defer` o `async`; nada síncrono que bloquee en el `<head>`.
- Video con imagen de portada y sin carga automática pesada.
- Lo crítico alojado en el mismo dominio cuando sea posible.

## 5. Accesibilidad (WCAG 2.2, nivel AA)

- Contraste mínimo 4,5:1 en texto normal y 3:1 en texto grande.
- `alt` descriptivo en imágenes con contenido; `alt=""` en las decorativas.
- Cada campo de formulario con su etiqueta visible.
- Todo enlace y botón con nombre accesible, incluidos los de solo ícono (WhatsApp, redes): `aria-label`.
- `<html lang="es">`.
- Objetivos táctiles de al menos 24 × 24 píxeles CSS.
- Todo contenido que se mueva solo más de 5 segundos (carruseles) debe poder pausarse.
- Respetar `prefers-reduced-motion` y mantener visible el foco del teclado (buena práctica; pendiente de verificar con fuente oficial).

## 6. SEO y datos estructurados

- Un `<title>` y una meta descripción propios por página; un solo `<h1>` que refleje el título.
- JSON-LD con `LocalBusiness` (subtipo más específico) si hay local: `name` y `address` obligatorios; `telephone` con código de país, `url`, `geo` con 5 decimales, `openingHoursSpecification`.
- `Organization` en inicio o "Sobre nosotros": `logo` de al menos 112 × 112 px, `sameAs` con redes y perfiles de reseñas, `contactPoint`.
- El marcado describe solo lo visible y coincide con la página y con el perfil de Google.
- No usar marcado de preguntas frecuentes buscando resultados enriquecidos (Google dejó de mostrarlos el 7 de mayo de 2026).
- Nada de archivos especiales "para IA": no son necesarios para Google.

## 7. Medición

- Eventos clave en GA4: clic a WhatsApp, clic en llamar, envío de formulario (`generate_lead`).
- Las cuentas de Search Console, Analytics y el perfil de Google van a nombre del negocio, con el proveedor como administrador invitado.

## 8. Legal (Colombia; no es asesoría legal)

- Política de tratamiento de datos (Ley 1581 de 2012) enlazada en el pie de página.
- En cada formulario: casilla de autorización sin marcar, enlace a la política y aviso breve de quién recibe los datos y para qué.
- Pedir solo los datos necesarios; nada sensible sin razón y autorización expresa.
- Promesas, cifras y garantías comprobables (Ley 1480 de 2011, arts. 29 y 30).
- Si vende en línea: nombre o razón social, NIT, dirección, teléfono, correo, precio total, derecho de retracto, canal de quejas y enlace a la autoridad del consumidor (Ley 1480, art. 50).

## 9. Propiedad y licencias

- Registrar en un archivo `CREDITOS.md` cada recurso de terceros (fuentes, fotos, íconos, librerías) con su licencia.
- Google Fonts: licencias abiertas (sobre todo SIL OFL); se pueden alojar en el sitio.
- Fotos solo propias del negocio o de bancos con licencia comercial.
- Marca, logo, fotos y textos del cliente son del cliente.

## 10. Seguridad y mantenimiento

- Preferir sitio estático cuando alcanza: menos software que mantener.
- Si es WordPress: pocos plugins y actualizaciones al día.
- HTTPS con renovación automática del certificado.
- Sin claves, tokens ni datos privados en el código.

## 11. Verificación antes de entregar

- [ ] PageSpeed Insights en móvil: rendimiento y accesibilidad, con LCP, INP y CLS dentro de las metas.
- [ ] Prueba de resultados enriquecidos de Google sin errores.
- [ ] Prueba en un celular real: WhatsApp abre con número real, botones fáciles de tocar, texto legible.
- [ ] Ningún texto de relleno ni sección vacía.
- [ ] Boceto con `noindex` y aviso; sitio final sin `noindex` y con medición instalada.
- [ ] Política de datos y autorización en formularios.
- [ ] `CREDITOS.md` completo.

## Honestidad

Nunca prometer posiciones en Google ni que una IA recomiende al negocio. Lo que se ofrece: una página clara, rápida, accesible y medible, con la información lista para que buscadores e IA la entiendan.
