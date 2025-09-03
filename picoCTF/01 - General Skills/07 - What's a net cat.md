## Descripción
Using netcat (nc) is going to be pretty important. Can you connect to `jupiter.challenges.picoctf.org` at port `41120` to get the flag?

## Solución
- Utilizar el comando nc para conectar a cierta dirección web a través del puerto 41120, así:
``` shell
nc jupiter.challenges.picoctf.org 41120

```
## Notas adicionales
- nc - comando que sirve para abrir conexiones TCP o UDP a un host y un puerto, o incluso escuchar conexiones.
## Referencias
- [nc(1): arbitrary TCP/UDP connections/listens - Linux man page](https://linux.die.net/man/1/nc)