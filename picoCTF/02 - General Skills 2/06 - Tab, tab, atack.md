## Descripción
Using tabcomplete in the Terminal will add years to your life, esp. when dealing with long rambling directory structures and filenames: [Addadshashanammu.zip](https://mercury.picoctf.net/static/9689f2b453ad5daeb73ca7534e4d1521/Addadshashanammu.zip)
## Solución
- Usar wget para descargar el archivo .zip que te proporcionaba el reto.
- Sabía que existía el comando zip, así que ingresé a su manual para ver cómo usarlo para descomprimir archivos; En el manual encontré que hay otro comando que cumple esa función: unzip.
- Usé unzip para descomprimir el archivo zip. Importante mencionar que usé tab para no escribir el nombre del archivo letra por letra
- De ahí me puse a navegar por la familia de carpetas que fue creada, siempre usando cd *tab* para escribir inmediatamente el nombre, hasta que dejó de autorellenarse
- Cuando dejó de autorellenarse, vi que en la carpeta había ahora un archivo ejecutable, el cual ejecuté con ./*tab*, ahí estaba la bandera.
## Notas adicionales
- Usé rm -r para eliminar los archivos de esta práctica.
## Referencias