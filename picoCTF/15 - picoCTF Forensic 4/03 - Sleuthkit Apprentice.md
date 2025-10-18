## Descripción
Download this disk image and find the flag.Note: if you are using the webshell, download and extract the disk image into `/tmp` not your home directory.

- [Download compressed disk image](https://artifacts.picoctf.net/c/138/disk.flag.img.gz)
## Solución
- Descargar y descomprimir el archivo.
- con el comando mmls pudimos ver las particiones del archivo de imagen.
- Nos interesó la partición principal de linux, así que usaremos su Start como offset para los siguientes comandos.
- Usé fls con el offset del sector de la partición linux para enlistar los directorios que había en esa partición.
- Con el mismo comando usé -r para que buscara de manera recursiva en todos los directorios, y luego usé un grep para encontrar algún archivo que tuviera que ver con "flag".
- Encontré dos archivos que tenían ese nombre, los cuales tenían un identificador, el cual usaré para leerlos con un icat.
- Usando el  comando icat -o, le indiqué el offset con el identificador de los archivos que quería leer y en uno de ellos se encontraba la bandera.
  
## Notas adicionales
- mmls: muestra el índice o la tabla de particiones de un archivo de imagen de disco.
- fls: enlista los archivos que hay en el archivo de imagen, usé -o para indicarle un sector de partida y no tuviera que buscar en todo.
- icat: inode cat
## Referencias