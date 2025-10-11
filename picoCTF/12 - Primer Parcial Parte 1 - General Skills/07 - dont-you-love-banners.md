Can you abuse the banner? The server has been leaking some crucial information on `tethys.picoctf.net 57855`. Use the leaked information to get to the server. To connect to the running application use `nc tethys.picoctf.net 53631`. From the above information abuse the machine and find the flag in the /root directory.
## Solucion
- Conectarse al primer puerto, el cual da una contraseña.
- Conectarse al segundo con la contraseña.
- Crear un link de flag.txt a banner.
- Desconectarse y al volverse a conectar aparecerá la bandera.