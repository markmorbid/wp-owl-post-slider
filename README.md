# WP Owl Post Slider

Personalización CSS de tarjetas PSAC/PSACP para Owl Carousel y WordPress, implementada en https://agustinaodonnell.com/#blog.

Este repositorio contiene CSS y exportaciones HTML; todavía no es un plugin WordPress instalable con PHP y shortcodes propios.

## Archivos definitivos

Los cinco archivos del autor se conservan byte por byte:

| Archivo | Uso |
| --- | --- |
| `owl-cards-final.css` | Referencia final de la personalización implementada |
| `owl-cards.css` | Variante conservada y utilizada por las vistas HTML |
| `owl-test.html` | Sandbox aportado por el autor |
| `owl-test-corregido.html` | Exportación corregida |
| `preview.html` | Comparación de estructuras PSAC y PSACP |

No cargar ambas variantes CSS simultáneamente. La comparación usa `owl-cards.css`; no certifica por sí sola la versión `owl-cards-final.css` en WordPress.

`assets/`, `preview.css` y `snapshot-preview.js` restauran dependencias locales recuperadas de la entrega anterior. Las vistas también usan recursos externos del sitio y CDN: requieren conexión. Los colores y la imagen de prueba de preview.css/assets no son la referencia de producción.

## Descarga y uso local

[Descargar ZIP de main](https://github.com/markmorbid/wp-owl-post-slider/archive/refs/heads/main.zip), también disponible en **Code → Download ZIP**.

```sh
git clone https://github.com/markmorbid/wp-owl-post-slider.git
cd wp-owl-post-slider
python -m http.server 8000
```

Abrir http://localhost:8000/preview.html o http://localhost:8000/owl-test-corregido.html. En Windows se puede usar `py -m http.server 8000`.

En Codex desktop, abrir la carpeta clonada como proyecto y comenzar un hilo nuevo. Leer `AGENTS.md` y `docs/WORKFLOW.md`; no hace falta importar este chat.

Antes de trabajar: `git status` y `git pull --ff-only`, resolviendo primero cualquier cambio local pendiente. Después de revisar: `git add`, `git commit`, `git push`. Clonar o descargar incluye backup/ en tu computadora.

## Conservación y validación

`backup/2026-11-03/` conserva versiones anteriores y el README previo. No son archivos de producción. `scripts/check_repository.py` comprueba los hashes de los cinco finales y sus dependencias locales:

```sh
python scripts/check_repository.py
```

GitHub Actions ejecuta la comprobación en push y pull request. No despliega WordPress. Integridad de archivos no equivale a validación visual del sitio.

Se conserva LICENSE y las licencias de terceros en assets/.
