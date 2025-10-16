## Descripción
Matryoshka dolls are a set of wooden dolls of decreasing size placed one inside another. What's the final one? Image: [this](https://mercury.picoctf.net/static/205adad23bf9d8303081a0e71c9beab8/dolls.jpg)
## Solución 
- Usamos binwalk para descomprimir el archivo .jpg.
- Repetimos el proceso hasta que ya no se pueda descomprimir más.
- En la última carpeta hay un flag.txt.
- Con un cat sacamos la bandera del archivo.
## Notas adicionales
## Referencias