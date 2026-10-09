# Lo que hay que pedirle a JO SMILE

Ordenado por importancia. En el código, cada hueco está marcado con `<!-- PENDIENTE: ... -->`.

## Imprescindible (sin esto el sitio no puede publicarse)
1. **Número de WhatsApp.** Se pone en una sola línea: `js/main.js` → `WHATSAPP_NUMERO = "57XXXXXXXXXX"`. Desde ese momento, todos los botones del sitio escriben directo a la clínica.
2. **Qué especialidades ofrecen de verdad.** Hoy aparecen 6 provisionales (valoración general, ortodoncia, endodoncia, encías, rehabilitación e implantes, estética). Hay que confirmar cuáles quedan, cuáles salen y si falta alguna (niños, cordales, urgencias).
3. **Dirección exacta** (calle, número, edificio, consultorio, barrio y municipio). Con ella se pone el mapa en Contacto y se completa el pie de página. La ficha de Google parece ubicarla en la zona de Cañaveral, Floridablanca: hay que confirmarlo.
4. **Logo.** Hoy se usa un símbolo provisional (un diente dentro de un cuadro verde). Con el logo real también se ajustan los colores si hace falta.

## Muy recomendable (es lo que más genera confianza)
5. **Los especialistas.** Por cada uno: foto, nombre completo, especialidad, universidad y, si quieren, registro profesional.
6. **3 a 5 opiniones reales de Google**, copiadas tal cual con nombre o inicial, y la calificación promedio.
7. **Fotos reales**: fachada o entrada, recepción, sala de atención y equipo de trabajo. Hoy el sitio usa ilustraciones propias (una escena de consultorio y una por servicio), que se pueden reemplazar o combinar con las fotos.
8. **Horario de atención.**
9. **Precio de la valoración** y si incluye radiografías.
10. **Formas de pago y financiación.**

## Para completar
11. Si atienden **urgencias** (y en qué horario) y si tienen **convenios** con EPS o prepagadas.
12. **Historia de la clínica**: desde cuándo existe y qué significa "JO".
13. Teléfono fijo, correo y redes sociales (Instagram o Facebook), si los tienen.
14. **Política de tratamiento de datos personales (Ley 1581 de 2012).** El sitio no tiene formularios ni recoge datos, pero se recomienda publicar la política de la clínica si ya existe. También el código de habilitación (REPS), si quieren mostrarlo.
15. **Imagen para compartir el link** (logo o foto, 1200×630) y el dominio final del sitio.

## Notas técnicas
- **Transiciones entre páginas:** funcionan en Chrome y Edge cuando el sitio se ve desde una dirección web (por ejemplo, GitHub Pages). Al abrir los archivos con doble clic, el navegador no las aplica; el resto del sitio funciona igual.
- **Encabezado y pie:** el HTML está repetido en las 5 páginas. Si se cambia algo ahí, hay que cambiarlo en todas.

## De boceto a sitio final (según CLAUDE.md)
Cuando la clínica apruebe la propuesta:
- Quitar `<meta name="robots" content="noindex">` de todas las páginas y la franja "Propuesta de diseño".
- Agregar el JSON-LD tipo `Dentist` con `name`, `address`, `telephone` (+57), `url`, `geo` con 5 decimales (7.06777, -73.10755) y `openingHoursSpecification`. Hoy no está porque falta la dirección, que es obligatoria.
- Agregar `Organization` (logo de al menos 112 × 112 px, `sameAs` con redes y perfil de Google, `contactPoint`).
- Etiqueta de verificación de Search Console en el inicio y Google Analytics 4 en cada página, con evento al hacer clic en WhatsApp.
- `robots.txt` que no bloquee a Googlebot ni a OAI-SearchBot.
- Política de tratamiento de datos (Ley 1581 de 2012) enlazada en el pie de página.
- Revisar con PageSpeed Insights en móvil (LCP ≤ 2,5 s, INP ≤ 200 ms, CLS ≤ 0,1) y probar en un celular real con el número de WhatsApp real.
- Las cuentas de Search Console, Analytics y el perfil de Google van a nombre de la clínica.
