## Descripción
Do you know how to move between directories and read files in the shell? Start the container, `ssh` to it, and then `ls` once connected to begin. Login via `ssh` as `ctf-player` with the password, `481e7b14`

Additional details will be available after launching your challenge instance.

After:
Do you know how to move between directories and read files in the shell? Start the container, `ssh` to it, and then `ls` once connected to begin. Login via `ssh` as `ctf-player` with the password, `481e7b14`
## Solución
- Acceder a la dirección con ssh, con el usuario y contraseña proporcionados
- Usé ls para ver los archivos en la carpeta actual.
- Había dos archivos de texto, uno tenía una parte de la llave (1of3) y el otro tenía instrucciones para la siguiente parte de la llave (instructions_to_2of3).
- Las instrucciones me indicaron que fuera al root, o sea "*cd /*".
- Ahí había otros dos archivos relevantes, la segunda parte de la bandera y las instrucciones para llegar a la tercera parte.
- Las instrucciones me mandaron a la ruta home: "*cd  ~*" 
- Ahí estaba la última parte de la bandera, al combinarlas pude resolver el reto.
## Notas adicionales
- Usé comando cat para leer los archivos de texto (El cual encontré en el cheatsheet de github que está en la sección de referencias)
## Referencias
- [Bash scripting cheatsheet](https://devhints.io/bash)
- [RehanSaeed/Bash-Cheat-Sheet: A cheat sheet for bash commands.](https://github.com/RehanSaeed/Bash-Cheat-Sheet)