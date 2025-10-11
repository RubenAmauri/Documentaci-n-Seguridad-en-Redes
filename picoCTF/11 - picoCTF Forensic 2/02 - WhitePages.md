## Descripción
I stopped using YellowPages and moved onto WhitePages... but [the page they gave me](https://jupiter.challenges.picoctf.org/static/fa4a277cfa846e07a5981d8a19288a2e/whitepages.txt) is all blank!
## Solución
- Abrir la página y darse cuenta que está completamente en blanco.
- Descargamos el archivo.
- Usamos *xxd -l* para leer su contenido hexadecimal.
- Usamos comando *sed 's/\xe2\x80\x83/0/g' [nombre_del_archivo]* para convertir ciertos caracteres a puros 0.
- usamos *sed 's/\xe2\x80\x83/0/g' [nombre_del_archivo] | sed 's/\x20/1/g'*  para convertir ese contenido a binario.
- Usamos cyberchef para "traducir" de binario a unicode.
- Ahí estaba la bandera.
## Notas adicionales
- Unicode
## Referencias