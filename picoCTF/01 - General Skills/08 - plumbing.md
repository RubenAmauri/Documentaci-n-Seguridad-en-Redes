## Descripción
Sometimes you need to handle process data outside of a file. Can you find a way to keep the output from this program and search for the flag? Connect to `jupiter.challenges.picoctf.org 4427`.
## Solución
- Aplicar los conocimientos del reto anterior para resolverlo; Usé comando nc para abrir la conexión, después usé un pipe para pasarle esa salida como entrada al siguiente comando, el cual fue un grep para encontrar la bandera.
``` shell
nc jupiter.challenges.picoctf.org 4427 | grep picoCTF

```

## Notas adicionales
- | - Pasa la salida del comando anterior como entrada del siguiente comando
## Referencias
- [All about pipes, by The Linux Information Project (LINFO)](https://www.linfo.org/pipes.html)