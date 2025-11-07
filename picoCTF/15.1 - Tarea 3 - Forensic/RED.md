## Descripción
RED, RED, RED, REDDownload the image: [red.png](https://challenge-files.picoctf.net/c_verbal_sleep/831307718b34193b288dde31e557484876fb84978b5818e2627e453a54aa9ba6/red.png)
## Solución
- Descargar la imagen.
- Usar exiftool para ver los metadatos.
- Hay un poema, el cual con las letras mayúsculas nos da una pista "Check LSB"
- En cyberchef subir la imagen y usamos "extract  lsb".
- En las pistas del reto, uno indicaba el patron de colores que usaría el LSB, el cual sería RGBA.
- Usando ese patrón, encontramos un mensaje que parecía estar en base 64.
- Decodificarlo con la terminal para conseguir la bandera.
## Notas adicionales
## Referencias