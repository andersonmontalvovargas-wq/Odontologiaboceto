# Reglas del repositorio

## Bocetos: siempre noindex

Todo lo que hay aquí son bocetos para clientes, no sitios reales. Ninguna página debe aparecer en buscadores.

- Toda página HTML (nueva o existente) lleva en el `<head>`, justo después del `viewport`:
  `<meta name="robots" content="noindex, nofollow">`
- Aplica a todas las copias de cada boceto: la carpeta fuente, la vista previa y lo publicado en GitHub Pages. Al copiar o regenerar páginas, verificar que la etiqueta siga ahí.
- No usar `robots.txt` con `Disallow` en su lugar: en GitHub Pages de proyecto no está en la raíz del dominio, y bloquear el rastreo impide que Google vea el `noindex`.
- Solo se quita cuando el cliente apruebe y el sitio pase a su dominio definitivo, y solo si el usuario lo pide.
