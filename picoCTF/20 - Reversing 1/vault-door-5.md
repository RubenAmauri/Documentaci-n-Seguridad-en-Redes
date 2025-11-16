## Descripción
In the last challenge, you mastered octal (base 8), decimal (base 10), and hexadecimal (base 16) numbers, but this vault door uses a different change of base as well as URL encoding!The source code for this vault is here: [VaultDoor5.java](https://challenge-files.picoctf.net/c_fickle_tempest/bd4f8f70a70dacc0e57dfc24ff34f5297a3db3c9c4366fd8df02f6bf47c794c8/VaultDoor5.java)
## Solución
- En el código notamos algo importante, ahora la cadena la codifica primero a url y luego a base64.
- Para deshacer esos procesos, haremos un script en python:
  ``` python
  from base64 import b64decode
  from urllib.parse import unquote
  
  cadena = 'JTYzJTMwJTZlJTc2JTMzJTcyJTc0JTMxJTZlJTY3JTVmJTY2JTcyJTMwJTZkJTVmJTYyJTYxJTM1JTY1JTVmJTM2JTM0JTVmJTYyJTY1JTM5JTY2JTMxJTMwJTYxJTM0'
  cad = b64decode(cadena)
  cadurl = unquote(cad)
  print(cadurl)
  ```
- Ese código aplica la ingeniería inversa al código java anterior, y nos revela la bandera, solo hay que darle formato.
## Notas adicionales
## Referencias
