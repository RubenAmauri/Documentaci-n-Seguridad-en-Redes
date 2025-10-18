## Descripción
Download this disk image, find the key and log into the remote machine.Note: if you are using the webshell, download and extract the disk image into `/tmp` not your home directory.

- [Download disk image](https://artifacts.picoctf.net/c/70/disk.img.gz)
- Remote machine: `ssh -i key_file -p 64531 ctf-player@saturn.picoctf.net`
## Solución
- Descargar y descomprimir el archivo.
- Hacemos mmls para ver la tabla de particiones de la imagen de disco.
- Vamos a empezar a buscar en la última partición de linux, ya que tenemos 2.
- Usamos fls -o para buscar en la última partición del índice.
- con fls usamos -r para indicar que vamos a buscar recursivamente en el offset indicado, y con un pipe haremos un grep ssh.
- Encontramos un folder llamado .ssh, donde probablemente esté la llave que estamos buscando, seguimos con ayuda de fls -o para buscar en el offset que indica tal folder.
- Encontramos dos archivos, uno con una key pública y uno con una privada.
- Usamos icat para leer el archivo con la llave privada y con ayuda del operador *">"* pasamos su contenido a un archivo llamado "key_file".
- Usamos chmod para cambiar los permisos del archivo por seguridad.
	- Esto lo hacemos porque al usar ssh con un archivo llave con permisos "regulares", podría ser que no nos permita iniciar sesión.
- Nos conectamos con ssh al servidor que nos indica el reto, copiando y pegando el comando que el reto indica, ya que le pusimos el mismo nombre a la llave que el comando del reto está llamando.
- Al querer conectarme me falló la llave, ya que contenía "demasiados permisos", por lo que tuve que modificarlos de nuevo, con un chmod 600.
- Ahora al conectarme al ssh pude entrar sin problemas, usé ls para ver los archivos.
- Había un archivo flag.txt, usé cat para ver el contenido y era la bandera.
## Notas adicionales
- /.ssh es un folder donde comunmente se guardan las llaves ssh.
- *chmod og-r*: con este comando lo que estamos haciendo es cambiando los permisos del lectura para varios usuarios de un archivo específico:
	- con chmod estamos cambiando los permisos del archivo.
	- con og-r estamos indicando 3 cosas
		- o = others: Cualquier usuario en el sistema que no sea el dueño ni pertenezca al grupo del arhcivo.
		- g = group: Todos los usuarios que pertenecen al mismo grupo que el archivo.
		- -r = usamos "-" como un operador, en este caso, remueve permisos. r = al permiso de lectura (read).
- chmod 600: 
	- Este comando establece los permisos de la siguiente manera:
	- **`6`** (Dueño): `4` (lectura) + `2` (escritura) = **Leer y Escribir**.    
	- **`0`** (Grupo): **Sin permisos**.    
	- **`0`** (Otros): **Sin permisos**.
## Referencias