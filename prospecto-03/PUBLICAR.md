# Publicación en GitHub Pages

GitHub Pages publica la carpeta `docs/` de la rama por defecto. Las tres propuestas se copian a `docs/prospecto-03/`:

| Propuesta | Fuente | Publicada en |
|---|---|---|
| A | `prospecto-03/sitio-a/` | `docs/prospecto-03/a/` |
| B | `prospecto-03/sitio-b/` | `docs/prospecto-03/b/` |
| C | `prospecto-03/sitio-c/` | `docs/prospecto-03/c/` |
| D | `prospecto-03/sitio-d/` | `docs/prospecto-03/d/` |
| E | `prospecto-03/sitio-e/` | `docs/prospecto-03/e/` |

A, B y C comparten textos y estructura (`generar.py`); cambian `css/estilos.css`, fuentes, ilustración y favicon.
D y E usan los mismos textos y datos de `generar.py`, pero su propia estructura (`generar_de.py`).
Si se cambia algo, primero se regenera y luego se copia:

```sh
for v in a b c; do python3 prospecto-03/generar.py prospecto-03/sitio-$v $v; done
for v in d e; do python3 prospecto-03/generar_de.py prospecto-03/sitio-$v $v; done
for v in a b c d e; do d=docs/prospecto-03/$v; s=prospecto-03/sitio-$v; rm -rf $d && mkdir -p $d && cp -r $s/*.html $s/css $s/js $s/assets $d/; done
```
