# Publicación en GitHub Pages

GitHub Pages publica la carpeta `docs/` de la rama por defecto. Este boceto se copia a `docs/prospecto-03/`.
Solo se copian `*.html`, `css/`, `js/` y `assets/`. Si se cambia algo, primero se regenera y luego se copia:

```sh
python3 prospecto-03/generar.py prospecto-03/sitio
d=docs/prospecto-03; s=prospecto-03/sitio; rm -rf $d && mkdir -p $d && cp -r $s/*.html $s/css $s/js $s/assets $d/
```
