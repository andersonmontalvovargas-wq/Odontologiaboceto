# Publicación en GitHub Pages

GitHub Pages publica la carpeta `docs/` de la rama por defecto. Las tres propuestas se copian a `docs/prospecto-03/`:

| Propuesta | Fuente | Publicada en |
|---|---|---|
| A | `prospecto-03/sitio-a/` | `docs/prospecto-03/a/` |
| B | `prospecto-03/sitio-b/` | `docs/prospecto-03/b/` |
| C | `prospecto-03/sitio-c/` | `docs/prospecto-03/c/` |
| D | `prospecto-03/sitio-d/` | `docs/prospecto-03/d/` |
| E | `prospecto-03/sitio-e/` | `docs/prospecto-03/e/` |
| F | `prospecto-03/sitio-f/` | `docs/prospecto-03/f/` |
| G | `prospecto-03/sitio-g/` | `docs/prospecto-03/g/` |
| H | `prospecto-03/sitio-h/` | `docs/prospecto-03/h/` |

A, B y C comparten textos y estructura (`generar.py`); cambian `css/estilos.css`, fuentes, ilustración y favicon.
D y E usan los mismos textos y datos de `generar.py`, pero su propia estructura (`generar_de.py`). F, G y H hacen lo mismo con `generar_f.py`, `generar_g.py` y `generar_h.py`.
Si se cambia algo, primero se regenera y luego se copia:

```sh
for v in a b c; do python3 prospecto-03/generar.py prospecto-03/sitio-$v $v; done
for v in d e; do python3 prospecto-03/generar_de.py prospecto-03/sitio-$v $v; done
for v in f g h; do python3 prospecto-03/generar_$v.py prospecto-03/sitio-$v; done
for v in a b c d e f g h; do d=docs/prospecto-03/$v; s=prospecto-03/sitio-$v; rm -rf $d && mkdir -p $d && cp -r $s/*.html $s/css $s/js $s/assets $d/; done
```
