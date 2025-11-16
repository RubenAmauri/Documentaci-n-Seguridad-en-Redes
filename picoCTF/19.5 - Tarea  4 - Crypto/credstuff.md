## Descripción
We found a leak of a blackmarket website's login credentials. Can you find the password of the user `cultiris` and successfully decrypt it?Download the leak [here](https://artifacts.picoctf.net/c/151/leak.tar).The first user in `usernames.txt` corresponds to the first password in `passwords.txt`. The second user corresponds to the second password, and so on.
## Solución
 - Descargué el archivo y lo descomprimí.
 - Para encontrar una contraseña convincente, usé un "grep {" en el archivo de contraseñas.
 - Así encontré uno que coincide con el formato de la bandera.
 - Usé cyberchef para desencriptar la bandera. Probé varios métodos hasta que funcionó con ROT13.
 - Así obtuve la bandera.
## Notas adicionales
## Referencias
