## Descripción
[🥛](http://mercury.picoctf.net:48319/)
## Solución
 - Para este reto, tendríamos que descargar la imagen que se encuentra en la página, pero no hay manera de descargarla por el método habitual.
 - En firefox, presionamos alt y nos aparece una nueva barra de herramientas.
 - Damos en la pestaña "tools" y procedemos  ir a "page info".
 - Se abre una nueva ventana, en la cual encontraremos una pestaña llamada "media".
 - En esta pestaña encontraremos el archivo que necesitamos descargar.
 - El archivo parece simplemente ser una secuencia de imágenes, pero algo nos sugiere que tiene un mensaje oculto con esteganografía.
 - Usamos comando zsteg y encontramos la bandera.
## Notas adicionales
## Referencias