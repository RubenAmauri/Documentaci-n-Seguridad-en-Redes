## Descripción
We found this [file](https://mercury.picoctf.net/static/21c07c9dd20cd9f2459a0ae75d99af6e/tunn3l_v1s10n). Recover the flag.
## Solución
- Descargamos el archivo.
- Nos damos cuenta de que es un archivo corrupto, así que revisamos los bytes.
- En el header hay bits malos, también el mismo header nos indica que es un archivo .bmp.
- Buscamos cómo deben ir los bytes de un archivo .bmp para corregirlos en hexeditor.
- La imagen ya sirve, pero nos topamos con un mensaje que dice *notaflag{sorry}*.
- Intentamos aumentando el heigh de nuestro bitmap, editando algunos bytes en hexeditor.
- Lo que logramos es que el mensaje de *notaflag*, se moviera por la imagen.
- Intentamos aumentar un poco más el heigh de nuestro archivo y al abrirlo notamos que se puede ver una pequeña porción de la bandera.
- Ahora intentaremos aumentar el width, al hacer esto y abrir el bitmap, se nos revela la bandera.
## Notas adicionales
## Referencias