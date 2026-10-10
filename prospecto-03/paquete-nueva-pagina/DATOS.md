# Datos del consultorio

**Fuentes:** perfil público del consultorio en Google Maps y biografía pública de la doctora, consultados el 9 y 10 de octubre de 2026. El horario lo copió el usuario desde Google. Lo marcado como "confirmado" lo confirmó el usuario.

## Identidad

| Dato | Valor | Estado |
|---|---|---|
| Nombre que se muestra | **Consultorio Dra. Vanesa Gutiérrez** | Confirmado por el usuario |
| Profesional | Dra. Vanesa Gutiérrez | Público |
| Nombre completo en Google | Consultorio Dra Vanesa Gutiérrez/odontologia/Estetica dental/clínica dental/implantes/diseño de sonrisa/Lentes cerámicos/ | Público (es el nombre de la ficha; en la página se usa el corto) |
| Categoría en Google | Clínica dental | Público |
| Tipo de marca | Marca personal: la doctora es la marca, con nombre de consultorio | Decisión de diseño |
| Profesión | Odontóloga | Público |
| Especialización | Estética, UNICID (Universidade Cidade de São Paulo, Brasil) | Público; **título exacto pendiente** |
| Logo | No se tiene. Se usa un monograma provisional "VG" | Pendiente |

**Biografía pública de la doctora** (tal cual, en dos idiomas):
- Diseño de sonrisa / Smile Design
- Lentes cerámicos / Porcelain Veneers
- ESP. ESTÉTICA 🇧🇷 UNICID
- 🇨🇴 📍 Bucaramanga, Cra 34 # 36-31, Edificio Alto Prado

Que la biografía esté en inglés y español sugiere que puede atender pacientes extranjeros; **no está confirmado** (ver `PENDIENTES.md`).

## Contacto

| Dato | Valor |
|---|---|
| Teléfono | 324 492 5383 · formato internacional +57 324 492 5383 (`tel:+573244925383`) |
| WhatsApp | El mismo número, **confirmado** por el usuario · `https://wa.me/573244925383` |
| Mensaje base de WhatsApp | "Hola, Dra. Vanesa. Quiero agendar una valoración." |
| Dirección | **Edificio Alto Prado, Cra. 34 # 36-31, local 2 y Cra. 34 # 36-33**, Bucaramanga, Santander, Colombia |
| Nota de dirección | En Google aparecen las dos placas. El usuario pidió **mostrar ambas** |
| Google Maps | https://www.google.com/maps/search/?api=1&query=Consultorio%20Dra%20Vanesa%20Guti%C3%A9rrez%20Edificio%20Alto%20Prado%20Bucaramanga |
| Waze | https://waze.com/ul?q=Carrera%2034%20%2336-31%20Bucaramanga&navigate=yes |
| Correo, Instagram, otras redes | No se tienen |
| Coordenadas (geo) | No se tienen |

## Horario (de Google)

| Día | Horario |
|---|---|
| Lunes | 8:00 a. m. – 8:00 p. m. |
| Martes | 8:00 a. m. – 8:00 p. m. |
| Miércoles | 8:00 a. m. – 8:00 p. m. |
| Jueves | 8:00 a. m. – 8:00 p. m. |
| Viernes | 8:00 a. m. – 8:00 p. m. |
| Sábado | 8:00 a. m. – 8:00 p. m. |
| Domingo | 9:00 a. m. – 8:00 p. m. |

En festivos puede variar (Google dice "El horario puede variar"; el lunes festivo del Día de la Raza figuraba de 8 a. m. a 8 p. m.).

## Reputación en Google

- **Calificación 5,0 con 61 opiniones** (octubre de 2026).
- Frase permitida por las reglas: "Mira sus 61 opiniones en Google" (o "más de 60").
- No se copió ninguna opinión textual. Si se usan, deben ir con autor, enlace a la reseña original y la marca Google, y **sin** datos estructurados de estrellas.

## Servicios (tal cual aparecen en Google)

Blanqueamiento dental, Carillas y coronas, Cirugía oral, Implantes dentales, Ortodoncia, Brackets, Aclaramiento, Diseño de sonrisa, Lentes ceramicos, Cerámica, Calzas, Resinas, Rehabilitación, Implantes, Implante, Limpieza, Limpieza profunda, Perfeccionamiento de sonrisa, Conductos, Retratamientos, Periodoncista, Porcelana, Veneer, Smile, Dentis, Odontólogo, Odontóloga, Odontología general, Bordes en resina, Autoligado, Zafiro, Coronas y Detartraje.

**Agrupados en 8 tratamientos** con el nombre que usa el paciente (textos completos en `TEXTOS.md`):

1. Diseño de sonrisa (smile design, perfeccionamiento de sonrisa, estética dental)
2. Carillas y lentes cerámicos (porcelana, porcelain veneers, carillas en resina, bordes en resina)
3. Blanqueamiento dental (aclaramiento)
4. Implantes dentales y coronas (implante, rehabilitación oral, coronas en cerámica)
5. Ortodoncia y brackets (autoligado, brackets de zafiro)
6. Tratamiento de conductos (endodoncia, retratamientos)
7. Limpieza dental y encías (limpieza profunda, detartraje, periodoncia, periodoncista)
8. Odontología general y cirugía oral (calzas, resinas)

**No confirmado:** qué tratamientos hace ella y cuáles un especialista aliado (la ficha menciona "periodoncista").

## Datos estructurados (JSON-LD) ya usados

```json
{
  "@context": "https://schema.org",
  "@type": "Dentist",
  "name": "Consultorio Dra. Vanesa Gutiérrez",
  "telephone": "+573244925383",
  "address": {"@type": "PostalAddress", "streetAddress": "Edificio Alto Prado, Carrera 34 # 36-31, local 2 y Carrera 34 # 36-33", "addressLocality": "Bucaramanga", "addressRegion": "Santander", "addressCountry": "CO"},
  "openingHoursSpecification": [
    {"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"], "opens": "08:00", "closes": "20:00"},
    {"@type": "OpeningHoursSpecification", "dayOfWeek": "Sunday", "opens": "09:00", "closes": "20:00"}
  ],
  "employee": {"@type": "Person", "name": "Vanesa Gutiérrez", "jobTitle": "Odontóloga"}
}
```

Faltan `url`, `geo` (5 decimales) e `image` para el sitio final. Sin `aggregateRating`.

## Contexto del proyecto (CLAUDE.md, sección 1)

| Variable | Valor |
|---|---|
| Acción principal | Agendar una valoración |
| Canal | WhatsApp (principal) y llamada |
| Sensibilidad del sector | Alta: salud. Más exigencia de confianza; textos de salud firmados por la doctora; nada de promesas ni cifras sin respaldo |
| Presencia física | Consultorio visible en el Edificio Alto Prado |
| Tipo de marca | Marca personal, con nombre de consultorio |
| Etapa | **Boceto** (propuesta para un prospecto): `noindex` y aviso "Propuesta de diseño… No es el sitio oficial" |
