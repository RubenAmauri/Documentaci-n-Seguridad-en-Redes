## Descripción
We found this [file](https://jupiter.challenges.picoctf.org/static/ab30fcb7d47364b4190a7d3d40edb551/mystery). Recover the flag.
## Solución
- Descargamos el archivo.
- Buscamos qué tipo de archivo es, pero al parecer es un archivo corrupto.
- utilizamos *xxd mystery | head* para ver los primeros bytes que tiene y determinar qué tipo de archivo debería ser
- Sus primeros bytes no corresponden a algún tipo de archivo conocido.
- Usaremos hexeditor para corregirlos.
- Cambiamos los primeros bytes del encabezado para tratar de convertirlo en un archivo, pero no funcionó.
- Después del encabezado siguen los chunks.
- Los corregimos también.
- Al corregir, el archivo ya se reconoce como un archivo .png, pero no tiene ningún contenido.
- Descargaremos una herramienta llamada *pngcheck* que nos ayuda a comprobar los errores que puede tener nuestro archivo.
- Gracias a la herramienta, vemos que tiene un error de redundancia cíclica.
- El archivo tenía problemas en varios de sus chunks, los corregimos con hexeditor.
- La imagen ya puede abrirse y podemos ver la bandera.
## Notas adicionales
## Referencias