# Tarjetas PSAC / PSACP unificadas

Se usó la última exportación adjunta como base. Los comentarios antiguos que pedían cambiar únicamente selectores se interpretaron junto con el pedido más reciente: corregir estilos, interactividad y FontAwesome, y excluir la disposición Flex de prueba del carrusel.

## Archivos

- `owl-cards.css`: personalización compartida para WordPress. Conserva los tokens de proporción de la última versión, el alto de 350 px, categorías, título sobre fondo por línea, metadatos, CTA y desplazamiento del contenido al interactuar.
- `assets/fa-solid-900.woff2` y `assets/fa-regular-400.woff2`: FontAwesome 6.7.2 local. El CSS usa una familia propia para evitar conflictos con versiones cargadas por plugins.
- `owl-test-corregido.html`: exportación corregida, con las URLs originales de imágenes y estilos del sitio. Se añadieron 23 botones ausentes y se corrigió el destino del botón existente usando el enlace del título. Se añadieron etiquetas accesibles a los enlaces de cobertura e iconos decorativos.
- `preview.html`: comparación controlada y autónoma con dos estructuras y el mismo contenido. Usa una ilustración de prueba, colores aproximados y fuentes locales. NO constituye una reproducción certificada de los recursos gráficos del sitio.
- `comparacion.png` / `hover.png`: capturas de la comparación controlada.
- `snapshot-preview.js`: inicialización exclusiva de la exportación estática; elimina los wrappers y clones exportados y permite a Owl reconstruirlos. No instalar en WordPress.

## Aplicación en WordPress

1. Reemplazar el bloque de personalización anterior por `owl-cards.css`, cargándolo después de los estilos de Enfold y del plugin. No apilarlo sobre el bloque viejo: ese bloque contiene overrides de sandbox que rompen Owl.
2. Copiar `assets/fa-solid-900.woff2` y `assets/fa-regular-400.woff2` junto al CSS, conservando la carpeta relativa `assets/`. Si se pega el CSS en el personalizador, convertir esas dos URLs en URLs absolutas del sitio.
3. Mantener los CSS y JS oficiales del plugin y su inicialización. No cargar de nuevo jQuery ni Owl en WordPress. Los archivos locales de estas librerías incluidos aquí son exclusivamente para las vistas de prueba.
4. Mantener habilitada la opción «Leer más» en el shortcode para todas las entradas. El CSS no puede crear enlaces ausentes. El HTML entregado los completa para la exportación; el plugin debe generarlos en el sitio real.
5. No copiar `preview.css`, `snapshot-preview.js` ni los estilos de Flex/grid del sandbox a la personalización de WordPress.

El CSS hereda del tema `--maincolor`, `--darkbg`, `--lightbg`, `--lightbg-transp`, `--darkblue`, `--darkblue2`, `--border-color`, `--border-radius` y `--mainfont`. Los valores de prueba viven únicamente en `preview.css`.

## Cambios concretos

- Una misma regla por función para PSAC y PSACP. El equivalente visual del contenido antiguo es `.psacp-post-overlay`; `.psacp-post-carousel-content` es un wrapper distinto.
- Fondo centrado con `background-size: cover` y altura común; se corrige la altura inline de 400 px del export antiguo. `background-attachment` permanece en `scroll`.
- Capas de imagen, filtro, enlace general, contenido y CTA ordenadas para que los enlaces sean clicables sin que los contenedores transparentes los bloqueen.
- La transición y el desplazamiento del título y del CTA son iguales en ambas estructuras. El foco del teclado reproduce el estado de interacción; se respeta la preferencia de movimiento reducido.
- Icono de usuario sólido, reloj regular y flecha sólida de FontAwesome. La versión antigua recibe los mismos iconos mediante pseudoelementos para igualar ambas estructuras.
- Se conservan los tamaños tipográficos de la referencia, incluido `.5rem` en metadatos. Se permite que los metadatos pasen a otra fila en anchos pequeños para evitar recortes.
- Se corrigen las expresiones de color de borde no válidas y se eliminan duplicados y reglas provisionales.
- No hay overrides de `display`, `flex`, `grid`, `transform` ni ancho en `.owl-stage`, `.owl-stage-outer` o en el contenedor del carrusel. El Flex interno de las tarjetas y de los puntos de navegación solo distribuye su contenido.

## Verificación realizada

Chromium con Owl Carousel 2.3.4 real:

- Geometría y estilos medidos de imagen, contenido, título, categorías, metadatos, CTA y botón: sin diferencias entre las dos estructuras a 239, 360 y 460 px de ancho, con igual contenido.
- Mismo desplazamiento y geometría en hover.
- Categorías, título, CTA y enlace de fondo alcanzables.
- Foco de teclado y movimiento reducido comprobados.
- Fuentes FontAwesome sólida y regular cargadas.
- Avance por flechas y arrastre comprobados; stage en `display: block`, gestionado por Owl.
- Exportación completa inicializada: todos los botones nuevos presentes y con el mismo destino que el título de su tarjeta.

Limitación: el entorno respondió con bloqueo de conexión al dominio `agustinaodonnell.com`. Por eso no se certifica igualdad píxel a píxel con el tema y las imágenes reales ni se ha publicado nada en WordPress. La comprobación definitiva de la cascada del sitio debe hacerse con esos recursos disponibles. Las capturas incluidas identifican explícitamente los recursos de prueba.

## Uso local

Descomprimir y abrir `preview.html`. Para servir el paquete localmente también se puede ejecutar `python -m http.server 8000` en su carpeta y visitar `http://localhost:8000/preview.html`.

`owl-test-corregido.html` usa las imágenes y el tema reales, por lo que requiere acceso al sitio. La inicialización de esa exportación está pensada para inspección, no para insertarla en una página que ya inicializa el plugin.

Las licencias de FontAwesome, las fuentes de la comparación, jQuery y Owl se incluyen en `assets/`.
