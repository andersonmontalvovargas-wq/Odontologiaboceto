# Lo que hay que pedirle o confirmarle a la doctora

En el código, cada hueco está marcado con `<!-- PENDIENTE: ... -->`. Los textos se cambian en `generar.py` y luego se vuelven a generar las páginas.

## Imprescindible
1. **Confirmar que el 324 492 5383 recibe WhatsApp.** Hoy todos los botones escriben a ese número.
2. **Fotos reales**: retrato de la doctora (para la primera pantalla y "La doctora"), la doctora atendiendo, la fachada o entrada y el consultorio. Los espacios están marcados en la página.
3. **Formación comprobable**: título exacto de la especialización en la UNICID (Brasil), universidad del pregrado y año. Registro profesional (ReTHUS) si quiere mostrarlo.
4. **Dirección exacta**: en Google aparecen "Cra 34 # 36-31 local 2" y "Cra 34 # 36-33". Confirmar cuál se usa.
5. **Revisión de los textos de salud** (tratamientos y preguntas) por la doctora, y que los firme.

## Muy recomendable
6. Qué tratamientos hace ella y cuáles un especialista aliado (la lista de Google menciona periodoncista, ortodoncia, implantes y conductos).
7. 3 opiniones reales de Google para copiar con autor y enlace a la reseña original.
8. Precio de la valoración, si incluye radiografías, formas de pago y financiación.
9. Un texto corto de la doctora en primera persona sobre cómo trabaja.
10. Si atiende en inglés (su biografía dice "Smile Design / Porcelain Veneers"). Si sí, se puede agregar una página en inglés.

## Para completar
11. Logo, si tiene. Hoy hay un monograma provisional "VG".
12. Instagram u otras redes, enlace directo a su perfil de Google, parqueadero y acceso para silla de ruedas.
13. Política de tratamiento de datos (Ley 1581 de 2012) para enlazar en el pie de página.

## De boceto a sitio final (CLAUDE.md)
- Quitar `noindex` y la franja "Propuesta de diseño".
- Completar el JSON-LD `Dentist` con `url`, `geo` (5 decimales) e `image`; agregar `Organization` con `logo`, `sameAs` y `contactPoint`.
- Search Console, Google Analytics 4 con eventos de clic en WhatsApp y en llamar, y `robots.txt` que no bloquee a Googlebot ni a OAI-SearchBot.
- Fotos en WebP con `width` y `height`; la del inicio con `fetchpriority="high"`.
- PageSpeed Insights en móvil y prueba en un celular real.
