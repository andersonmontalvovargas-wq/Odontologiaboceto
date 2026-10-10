# Contenido para el boceto — prospecto-04

> Para quien construya el sitio: este archivo es la única fuente. Etiquetas:
> `[EXTRAÍDO]` = dato real verificado · `[SUGERIDO]` = texto genérico, verdadero para cualquier consultorio, se puede usar en el boceto ·
> `[PENDIENTE]` = dato real que falta. En el boceto, muéstralo como marcador visible y **nunca lo rellenes con datos inventados**.
> No prometas resultados clínicos (nada de "sin dolor", "garantizado", "sonrisa perfecta").

Estado: datos básicos extraídos de la ficha de Google (octubre de 2026). Faltan WhatsApp, equipo, redes y reseñas para citar.

## 1. Contexto (CLAUDE.md, sección 1)

| Variable | Valor | Origen |
|---|---|---|
| Tipo de entrega | Boceto | — |
| Sector | Salud (odontología): sensibilidad alta | [EXTRAÍDO] categoría de Google "clínica dental" |
| Acción principal | Agendar valoración | [SUGERIDO] |
| Canal | Llamada o WhatsApp al 314 394 3828 (celular). Falta confirmar que recibe WhatsApp | [PENDIENTE] confirmar |
| Presencia física | Consultorio con local; la búsqueda filtraba por "entrada accesible para silla de ruedas", así que la ficha probablemente lo tiene marcado | [PENDIENTE] confirmar |
| Tipo de marca | Marca de negocio (nombre comercial "Vía Oral"); el equipo acompaña como respaldo | [EXTRAÍDO] nombre · enfoque [SUGERIDO] |

## 2. Datos de contacto

| Dato | Valor | Origen |
|---|---|---|
| Nombre en Google | Clínica Odontológica Vía Oral | [EXTRAÍDO] |
| Dirección | Cl. 43 # 34-31, Cabecera del Llano, Bucaramanga, Santander | [EXTRAÍDO] (coincide con su listado en Doctoralia) |
| Google Maps (enlace corto, derivado del ID de la ficha) | `https://maps.google.com/?cid=8339109239465121267` | [EXTRAÍDO] |
| ID de Google (Knowledge Graph) | `/g/11bbrs0dzb` | [EXTRAÍDO] |
| Teléfono | 314 394 3828 · para enlaces: `tel:+573143943828` | [EXTRAÍDO] |
| WhatsApp | Su Instagram usa el enlace `https://wa.link/rriglm` para agendar. No se pudo abrir para ver el número; si es el 314 394 3828, en la página usar `https://wa.me/573143943828` | [EXTRAÍDO] enlace · número [PENDIENTE] |
| Calificación en Google | 5,0 con 322 opiniones | [EXTRAÍDO] |
| Coordenadas (para `geo`) | — | [PENDIENTE] |
| Instagram | Tiene cuenta (biografía abajo); falta el usuario exacto para el enlace y `sameAs` | [PENDIENTE] usuario |
| Correo, sitio web | No encontrados | [PENDIENTE] |
| Otros perfiles | Doctoralia: "Clinica odontológica Via Oral", misma dirección | [EXTRAÍDO] |

Frase de reseñas para la página (CLAUDE.md, sección 3): "Mira nuestras más de 300 reseñas en Google", con enlace a la ficha. No marcar las reseñas con datos estructurados.

### Biografía de Instagram [EXTRAÍDO]

> CLÍNICA VÍA ORAL · Todas las especialidades · Líderes en ortodoncia invisible · Salvamos tus dientes · Diseños de sonrisa estéticos · Bucaramanga · ¡Agenda tu cita!

Cómo usarla en la página (CLAUDE.md, secciones 3 y 8):
- **Nombre que se muestra:** "Clínica Vía Oral" (así se presenta ella misma).
- **Acción principal confirmada:** agendar cita por WhatsApp.
- **"Todas las especialidades":** se puede decir como "Especialidades odontológicas en un solo lugar", respaldado por la lista de servicios.
- **"Líderes en ortodoncia invisible":** no usarlo en el boceto. Es una afirmación de liderazgo sin respaldo (Ley 1480, arts. 29 y 30). Sí se puede destacar la ortodoncia con alineadores como servicio principal.
- **"Salvamos tus dientes":** no usarlo como promesa. Se puede decir: "Tratamos de conservar tu diente natural siempre que sea posible (endodoncia, periodoncia)" `[SUGERIDO]`.
- **Servicios destacados para la portada:** ortodoncia con alineadores, endodoncia y diseño de sonrisa (los que ella resalta).

## 3. Horario

| Día | Horario | Origen |
|---|---|---|
| Lunes a viernes | 7:00 a. m. – 12:00 m. y 2:00 – 7:00 p. m. | [EXTRAÍDO] |
| Sábado | 8:00 a. m. – 12:00 m. | [EXTRAÍDO] |
| Domingo | Cerrado | [EXTRAÍDO] |

Notas:
- Cierra al mediodía (12:00 m. – 2:00 p. m.) de lunes a viernes.
- Google marca el lunes festivo (Día de la Raza) con el horario normal y el aviso "El horario puede variar". Hay que preguntar cómo atiende en festivos antes de publicarlo. En la página se puede poner: "Festivos: confirma por WhatsApp" `[SUGERIDO]`.

Texto listo para la página:

> **Horario de atención**
> Lunes a viernes: 7:00 a. m. – 12:00 m. y 2:00 – 7:00 p. m.
> Sábados: 8:00 a. m. – 12:00 m.
> Domingos: cerrado.

Para el JSON-LD (`openingHoursSpecification`):

```json
[
  { "@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday","Tuesday","Wednesday","Thursday","Friday"], "opens": "07:00", "closes": "12:00" },
  { "@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday","Tuesday","Wednesday","Thursday","Friday"], "opens": "14:00", "closes": "19:00" },
  { "@type": "OpeningHoursSpecification", "dayOfWeek": "Saturday", "opens": "08:00", "closes": "12:00" }
]
```

## 4. Servicios (lista de la ficha de Google)

Nombres tal como los busca un paciente; úsalos así en la navegación.

| Servicio | Origen |
|---|---|
| Blanqueamiento dental | [EXTRAÍDO] |
| Carillas y coronas | [EXTRAÍDO] |
| Cirugía oral | [EXTRAÍDO] |
| Implantes dentales | [EXTRAÍDO] |
| Ortodoncia con alineadores | [EXTRAÍDO] |
| Rehabilitación oral | [EXTRAÍDO] |
| Periodoncia (encías) | [EXTRAÍDO] |
| Endodoncia (tratamiento de conductos) | [EXTRAÍDO] |
| Diseño de sonrisa | [EXTRAÍDO] |

Descripciones de cada servicio: `[PENDIENTE]`. Como es tema de salud, las debe revisar y firmar un odontólogo de la clínica. En el boceto se pueden usar textos generales que expliquen qué es cada tratamiento, sin prometer resultados `[SUGERIDO]`.

No se publican precios: el único dato visto (cirugía preprotésica en Doctoralia) no está confirmado por la clínica.

## 5. Lo que falta pedir o extraer

Número detrás de `wa.link/rriglm` y usuario de Instagram; odontólogos y especialistas con nombre y formación; sitio web; coordenadas; atributos (accesibilidad, parqueadero, formas de pago), fotos del lugar (solo para referencia, no se usan en el boceto) y 3 reseñas representativas con autor y enlace.
