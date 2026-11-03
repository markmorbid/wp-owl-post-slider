# Trabajo entre browser y desktop

GitHub guarda los archivos, backups y contexto. El chat sirve para pedir cambios; no debe ser el único lugar de entrega.

1. Clonar el repositorio o descargar su ZIP desde GitHub.
2. Abrir esa carpeta como proyecto en Codex desktop.
3. Iniciar un hilo nuevo: «Lee AGENTS.md y README.md. Los cinco archivos finales están aprobados. Mi tarea es: …».
4. Pedir un cambio concreto, revisar el diff y las comprobaciones pertinentes.
5. Subir el commit y comprobar que aparece en GitHub antes de cambiar de entorno.
6. En la otra copia, ejecutar git pull --ff-only sobre un árbol limpio.

## Si desktop se queda pensando

La causa no ha sido diagnosticada: este entorno no tiene acceso a los logs ni a la aplicación de tu equipo. Un hilo nuevo en la carpeta clonada evita depender de este hilo largo; no garantiza resolver un fallo de la aplicación.

Si falla también una petición mínima de lectura en un hilo nuevo, registrar versión, sistema operativo, hora y mensaje visible y reportarlo desde la aplicación o help.openai.com. No compartir credenciales. No borrar el proyecto ni reinstalar como primer paso.

## Entrega verificable

Pedir el enlace al commit o PR y la prueba realizada. Descargar mediante Code → Download ZIP. Una ruta /workspace no es una descarga ni una ruta de tu equipo.
