## Descripción
Download this disk image and find the flag.Note: if you are using the webshell, download and extract the disk image into `/tmp` not your home directory.

- [Download compressed disk image](https://artifacts.picoctf.net/c/212/disk.flag.img.gz)
## Solución
- Descargar y descomprimir el archivo.
- Usamos mmls para ver la tabla de particiones.
- Elegimos la última partición como posible portadora de la bandera.
- Hacemos un fls para explorar la partición.
- Con grep buscamos flag.
- Encontramos dos archivos, uno parece tener coordenadas y el otro parece estar encriptado
	- Esto lo sabemos gracias a icat -o.
- Con el comandok fls -o que busca en el offset que le indicamos y también con -r para indicar recursividad en los directorios, pasamos esa información a un archivo llamado files.
- Con la información del árbol de directorios en el archivo files, usamos el editor de texto *vi* para explorar el archivo.
- Volvemos a buscar la bandera, en este caso, el directorio en el que se encontraba también se encontraba el archivo .ash_history, el cual nos ayudará a saber cuáles comandos se ejecutaron para encriptar la bandera.
- Al hacer icat en la dirección del historial, vemos que sí se usó un comando para encriptar la bandera, para el cual se usó openssl en formato aes256.
- Usaremos los parametros man y -help con el comando openssl para buscar una forma de desencriptar con ese comando.
- Para poder trabajar con el archivo encriptado, con ayuda de icat lo leeremos y con ayuda del operador > lo pasaremos a un archivo nuevo dentro de nuestra carpeta del reto.
- Usando el mismo comando que se usó para encriptar el archivo, haremos unas pequeñas modificaciones para cambiar el archivo de salida y el de entrada, así como agregar parámetro -d para desencriptar el archivo.
- Ahora habrá un archivo nuevo llamado flag.txt, el cual tiene nuestra bandera.
## Notas adicionales
- .ash_history: es un archivo que guarda la terminal con el historial de comandos que fueron previamente ejecutados.
## Referencias