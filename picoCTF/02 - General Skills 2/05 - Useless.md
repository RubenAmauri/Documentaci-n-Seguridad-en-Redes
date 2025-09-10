## Descripción
There's an interesting script in the user's home directory

Additional details will be available after launching your challenge instance.

There's an interesting script in the user's home directory. The work computer is running SSH. We've been given a script which performs some basic calculations, explore the script and find a flag.
## Solución
- Conectarse a la dirección remota que te otorga picoCTF con el comando ssh.
- La página te da un puerto el cual debes usar para conectarte a esa dirección; también te da un usuario y una contraseña.
- Al acceder a la dirección usé comando ls para ver los archivos que hubiera, había un solo archivo llamado "useless".
- Use comando "*file useless*" para saber qué tipo de archivo era y qué hacer con él, descubrí que era un archivo ejecutable.
- Al tratar de ejecutarlo me suelta un mensaje que decía "read the code first", por lo que decidí usar man para leer el manual de usuario y me tomó por sorpresa que ahí estaba la bandera.
## Notas adicionales
- Para conectarme con el comando ssh usando un puerto específico usé el comando -p "*ssh -p  #puerto*"
- Para conectarme con mi usuario, la sintaxis es "*ssh  nombredeusuario@direcciondedominio*"
- Como nota, la contraseña parece que no está siendo escrita, pero sí está siendo registrada
## Referencias
