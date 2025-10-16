## Descripción
I've hidden a flag in this file. Can you find it? [Forensics is fun.pptm](https://mercury.picoctf.net/static/c00c449c3b08daaccacca6f9d5c55d49/Forensics%20is%20fun.pptm)
## Solución
- Descargamos el archivo.
- Si intentamos hacerle strings al archivo, nos damos cuenta de que nos da unos directorios.
- Hacemos unzip al archivo pptm.
- Se descomprime en varios directorios, si analizamos, el último directorio tiene un archivo "hidden".
- Si hacemos strings a ese archivo, nos encontramos con un mensaje codificado en base64.
- Al decodificar el mensaje obtenemos la bandera.
## Notas adicionales
## Referencias