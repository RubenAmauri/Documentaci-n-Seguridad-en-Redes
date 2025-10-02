## Descripción
This [garden](https://jupiter.challenges.picoctf.org/static/43c4743b3946f427e883f6b286f47467/garden.jpg) contains more than it seems.
## Solución
- Descargar el archivo.
- El archivo es un .jpg, el cual no es legible en ese estado.
- Es un archivo binario, el cual podría tener alguna cadena en su código.
- También podemos ver su contenido de manera hexadecimal, si lo editamos podemos cambiar bytes específicos del archivo.
- Usamos comando xxd para ver el contenido hexadecimal del archivo.
- Al final de ese contenido estaba escondida la bandera.
## Notas adicionales
- hexeditor: Editor hexadecimal de linux
- xxd: Comando para ver el contenido hexadecimal de un archivo.
## Referencias