## Descripción
Can you find the flag in [file](https://jupiter.challenges.picoctf.org/static/94d00153b0057d37da225ee79a846c62/strings) without running it?
## Solución
- Usé el comando strings para mostrar las líneas imprimibles del archivo .ELF;  concatené grep con una pipe para encotrar la bandera.
## Notas adicionales
- wget - para descargar archivos desde la terminal a la dirección marcada en el prompt
- rm - para borrar archivos
- rm -rf - para borrar carpetas con archivos
- .ELF - Archivo ejecutable de linux
- strings - Despliega las cadenas imprimibles en [archivo]
## Referencias
- [strings(1) - Linux man page](https://linux.die.net/man/1/strings)