# Propuesta D: muestra con la skill `adrian-saenz-hostinger-premium-website`

Página única para JO SMILE, hecha siguiendo la skill y respetando `CLAUDE.md` del proyecto.

## Arquetipo elegido
**04 · Glassmorphism Modern.** Es el que la skill recomienda para bienestar y servicios con tono sereno, y es distinto de las propuestas A, B y C. La paleta del arquetipo (pasteles cálidos) se cambió por la que pidió el cliente: azul medio, grises y blanco.

## Efectos (los 5 del arquetipo)
1. Degradado de fondo en movimiento, de 3 colores, en ciclos de 30 a 38 s.
2. Tarjetas de vidrio translúcido (`backdrop-filter`), con fondo sólido de respaldo.
3. Foto principal flotando en un marco de vidrio.
4. Botones magnéticos que siguen el mouse (solo con mouse).
5. Subrayado que se desliza entre los enlaces del menú y marca la sección visible.

## Reglas de la skill aplicadas
Patrón IIFE sin módulos, `defer` en los scripts, `?v=20261011` en CSS y JS, `.htaccess` para Hostinger, scroll nativo, contenido escrito en el HTML, cada función protegida con `safe()`, apariciones con umbral bajo y red de seguridad a los 6 s. Verificador de la skill: 0 errores.

## Donde se siguió `CLAUDE.md` en vez de la skill
| Tema | Skill | Decisión |
|---|---|---|
| Preguntas frecuentes | Acordeón | Respuestas a la vista (CLAUDE.md §3) |
| Contacto | Formulario de correo | WhatsApp, sin formulario ni datos personales (CLAUDE.md §8) |
| Movimiento reducido | No apagar efectos | Se detienen el degradado, la flotación y el botón magnético; siguen los cambios al pasar el mouse y las apariciones (criterio de ambos) |
| Fotos | Openverse, descargadas en WebP | Openverse está bloqueado desde el entorno: fotos de Pexels enlazadas, marcadas como "Foto de referencia", con ilustración de respaldo |
| GSAP y Lenis | GSAP siempre | No se usan: ningún efecto los necesita y la página pesa menos en celular (CLAUDE.md §4). El verificador lo marca como advertencia |
| Boceto | — | `noindex` y aviso "Propuesta de diseño D… No es el sitio oficial" (CLAUDE.md §2) |

## Tipografía
Plus Jakarta Sans (sans geométrica, como pide el arquetipo) y una sola expresión por titular en Instrument Serif cursiva como acento.

## Contraste
Texto principal 14,6:1 y secundario 8,3:1 sobre vidrio; blanco sobre azul 8,1:1.
