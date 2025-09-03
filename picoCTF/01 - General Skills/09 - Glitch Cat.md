## Descripción
Our flag printing service has started glitching!

Additional details will be available after launching your challenge instance.
## Solución
- Me conecté a la dirección obtenida de picoCTF, usé un pipe para concatenar un grep y buscar la bandera:
``` shell
nc saturn.picoctf.net 12345 | grep picoCTF

```
- La salida salió encriptada, debía descubrir el mensaje conviertiendo esa salida a código ASCII:
``` Terminal
'picoCTF{gl17ch_m3_n07_' + chr(0x61) + chr(0x34) + chr(0x33) + chr(0x39) + chr(0x32) + chr(0x64) + chr(0x32) + chr(0x65) + '}'
```
- Bandera desencriptada con cyberchef: picoCTF{gl17ch_m3_n07_a4392d2e}

## Notas adicionales
## Referencias