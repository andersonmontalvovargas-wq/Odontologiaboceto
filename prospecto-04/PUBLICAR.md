# Publicación en GitHub Pages

GitHub Pages publica la carpeta `docs/` de la rama por defecto. Las tres propuestas se copian a `docs/prospecto-04/`:

| Propuesta | Fuente | Publicada en |
|---|---|---|
| A | `prospecto-04/sitio-a/` | `docs/prospecto-04/a/` |
| B | `prospecto-04/sitio-b/` | `docs/prospecto-04/b/` |
| C | `prospecto-04/sitio-c/` | `docs/prospecto-04/c/` |

Si se cambia algo, primero se regenera y luego se copia:

```sh
for v in a b c; do python3 prospecto-04/generar.py prospecto-04/sitio-$v $v; done
for v in a b c; do d=docs/prospecto-04/$v; s=prospecto-04/sitio-$v; rm -rf $d && mkdir -p $d && cp -r $s/*.html $s/css $s/js $s/assets $d/; done
```
