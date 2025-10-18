## Descripción
Download the disk image and use `mmls` on it to find the size of the Linux partition. Connect to the remote checker service to check your answer and get the flag.Note: if you are using the webshell, download and extract the disk image into `/tmp` not your home directory.[Download disk image](https://artifacts.picoctf.net/c/164/disk.img.gz)Access checker program: `nc saturn.picoctf.net 59960`
## Solución
- Descargar y descomprimir el archivo de imagen.
- Usar mmls para ver el índice de particiones.
- Conectarse al nc que indica el reto, al conectarse nos pregunta el tamaño de la partición de linux.
- Respondemos con ayuda de la información que mostró mmls y nos da la bandera.
## Notas adicionales
## Referencias