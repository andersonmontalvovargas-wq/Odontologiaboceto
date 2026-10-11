# Publicación en GitHub Pages

GitHub Pages publica la carpeta `docs/` de la rama por defecto del repositorio.
Las tres propuestas de este prospecto se copian a `docs/prospecto-02/`:

| Propuesta | Fuente | Publicada en |
|---|---|---|
| A | `prospecto-02/sitio/` | `docs/prospecto-02/a/` |
| B | `prospecto-02/sitio-b/` | `docs/prospecto-02/b/` |
| C | `prospecto-02/sitio-c/` | `docs/prospecto-02/c/` |
| D (muestra con la skill de sitios premium) | `prospecto-02/sitio-d/` | `docs/prospecto-02/d/` |

Solo se copian `*.html`, `css/`, `js/` y `assets/` (en D: `index.html`, `styles.css`, `main.js`, `lib/` y `assets/`); las notas (`PENDIENTES.md`, `CREDITOS.md`, `NOTAS-DE-DISEÑO.md`) se quedan en la fuente.
Si se cambia una fuente, hay que volver a copiarla:

```sh
for v in a:sitio b:sitio-b c:sitio-c; do d=docs/prospecto-02/${v%%:*}; s=prospecto-02/${v##*:}; rm -rf $d && mkdir -p $d && cp -r $s/*.html $s/css $s/js $s/assets $d/; done
```

Para D:

```sh
d=docs/prospecto-02/d; rm -rf $d && mkdir -p $d && cp -r prospecto-02/sitio-d/{index.html,styles.css,main.js,lib,assets} $d/
```
