## Descripción
I found a web app that can help process images: PNG images only!

Additional details will be available after launching your challenge instance.
## Solución
- Abrir la página web.
- La página acepta que se suban archivos, pero valida que estos archivos sean de extensión PNG.
- Esto abre puertas a vulnerabilidades.
- En este caso, vamos a crear un archivo que cree una webshell con PHP, lo que nos permitirá usar comandos de linux en la página web.
- Desde el url/robots.txt encontramos una pista, que está no permitido entrar a instructions.txt.
- Entramos a url/intructions.txt y ahí encontramos un punto cable: los primeros bytes de un  archivo PNG son "50 4E 47" en hexadecimal; la página comprueba esos datos para saber si el archivo es subible.
- Crearemos un archivo simple con un webshell php.
- Haremos que ese archivo de texto se reconozca como un PNG para que pueda ser subido a la página.
- Subo ese archivo, el cual por cierto tiene extensión .png.php.
- Ahora para acceder a ese archivo desde la página usaremos url/uploads/nombre_del_archivo.
- Gracias a nuestro pequeño webshell, ahora podemos ejecutar comandos en la página.
- Utilizamos comando ls para descubrir el contenido de la carpeta padre, donde descubrimos un archivo "extraño".
- Usamos comando cat para leer el contenido de ese archivo y encontramos la bandera.
## Notas adicionales
## Referencias
