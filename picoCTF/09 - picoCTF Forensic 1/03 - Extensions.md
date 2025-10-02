## Descripción
This is a really weird text file [TXT](https://jupiter.challenges.picoctf.org/static/e7e5d188621ee705ceeb0452525412ef/flag.txt)? Can you find the flag?
## Solución
- Descargamos el archivo.
- Comprobamos qué tipo de archivo es con el comando *file*
- El archivo tiene extensión .txt pero según el comando file, en realidad es un archivo png
- Usamos comando mv para cambiar el nombre del archivo, junto con su extensión:
	``` zsh
	  mv flag.txt flag.png
	  ```
- Este archivo lo abrimos con comando open y resulta que es una imagen que tiene la bandera.
## Notas adicionales
- Magicbytes
- mv: Mueve archivos de carpeta o les cambia el nombre dentro del mismo directorio.
## Referencias