# Lo que hay que pedirle o confirmarle a la clínica

En el código, cada hueco está marcado con `<!-- PENDIENTE: ... -->`. Los textos se cambian en `generar.py` y luego se vuelven a generar las páginas.

## Ya confirmado
- Teléfono y WhatsApp: 314 394 3828 (enlace directo `wa.me`, sin el `wa.link` de Instagram).
- Dirección: Calle 43 # 34-31, Cabecera del Llano, Bucaramanga.
- Horario: lunes a viernes 7–12 y 2–7; sábado 8–12; domingo cerrado.
- Instagram: @clinicaviaoralbga.

## Imprescindible
1. **Equipo:** nombre, especialidad, universidad y foto de cada odontólogo. Hoy hay tarjetas marcadas como pendientes.
2. **Fotos reales:** fachada o entrada, recepción, consultorios y equipo.
3. **Revisión de los textos de salud** (especialidades, alineadores y preguntas) por un odontólogo de la clínica, que los firme.

## Muy recomendable
4. Qué especialista hace cada tratamiento.
5. 3 opiniones reales de Google para copiar, con autor y enlace a la reseña original.
6. Precio de la valoración, si incluye radiografías, formas de pago y financiación.
7. Marca de alineadores que usan, si la quieren mostrar.
8. Cómo atienden en festivos.
9. Un texto corto de la dirección de la clínica: desde cuándo atienden y cómo trabajan.

## Para completar
10. Logo y colores de la marca. Hoy hay un monograma provisional "VO".
11. Piso o local, referencias para llegar, parqueadero y si la entrada es accesible en silla de ruedas.
12. Coordenadas del lugar (para `geo` en el JSON-LD).
13. Política de tratamiento de datos (Ley 1581 de 2012) para enlazar en el pie de página.

## De boceto a sitio final (CLAUDE.md)
- Quitar `noindex` y la franja "Propuesta de diseño".
- Completar el JSON-LD `Dentist` con `url`, `geo` (5 decimales) e `image`; agregar `Organization` con `logo`, `sameAs` y `contactPoint`.
- Search Console, Google Analytics 4 con eventos de clic en WhatsApp y en llamar, y `robots.txt` que no bloquee a Googlebot ni a OAI-SearchBot.
- Fotos en WebP con `width` y `height`; la del inicio con `fetchpriority="high"`.
- PageSpeed Insights en móvil y prueba en un celular real.
