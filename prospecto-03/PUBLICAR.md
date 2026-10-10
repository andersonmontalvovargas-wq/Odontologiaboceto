# Publicación en GitHub Pages

GitHub Pages publica la carpeta `docs/` de la rama por defecto. Las tres propuestas se copian a `docs/prospecto-03/`:

| Propuesta | Fuente | Publicada en |
|---|---|---|
| A | `prospecto-03/sitio-a/` | `docs/prospecto-03/a/` |
| B | `prospecto-03/sitio-b/` | `docs/prospecto-03/b/` |
| C | `prospecto-03/sitio-c/` | `docs/prospecto-03/c/` |

Las tres comparten textos y estructura (`generar.py`); cambian `css/estilos.css`, fuentes, ilustración y favicon.
Si se cambia algo, primero se regenera y luego se copia:

```sh
for v in a b c; do python3 prospecto-03/generar.py prospecto-03/sitio-$v $v; done
for v in a b c; do d=docs/prospecto-03/$v; s=prospecto-03/sitio-$v; rm -rf $d && mkdir -p $d && cp -r $s/*.html $s/css $s/js $s/assets $d/; done
```
