## Descripción
Unzip this archive and find the flag.

- [Download zip file](https://artifacts.picoctf.net/c/505/big-zip-files.zip)
## Solución
- Descargué el archivo con wget.
- Descomprimí usando unzip.
- Se descomprimieron muchísimas carpetas con subcarpetas.
- Usé grep -r para buscar "picoCTF" en la carpeta padre, ahí encontré la bandera.
## Notas adicionales
- grep -r: -r indica recursivo, lo que hace que grep busqué en todas las subdirecciones de esa dirección.
## Referencias
