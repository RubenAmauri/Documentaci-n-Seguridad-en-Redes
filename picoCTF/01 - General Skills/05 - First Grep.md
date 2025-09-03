## Descripción
Can you find the flag in [file](https://jupiter.challenges.picoctf.org/static/515f19f3612bfd97cd3f0c0ba32bd864/file)? This would be really tedious to look through manually, something tells me there is a better way.
## Solución
- Descargar el archivo en la webshell de picoCTF usando wget
- Usar ls para ver los archivos en esa dirección
- Contar las líneas y caracteres del archivo
- Aplicar el comando grep 'picoCTF' file
## Notas adicionales
- **wc** - cuenta las líneas, bytes y caracteres de un archivo de texto.
- **ls** - es para ver los archivos en la dirección actual
- **file** - Determina el tipo de archivo
## Referencias
grep [tutorial](https://ryanstutorials.net/linuxtutorial/grep.php)
