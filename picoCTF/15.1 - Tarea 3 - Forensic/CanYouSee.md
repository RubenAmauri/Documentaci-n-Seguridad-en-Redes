## Descripción
How about some hide and seek?Download this file [here](https://artifacts.picoctf.net/c_titan/6/unknown.zip).
## Solución
- Descargar y descomprimir el archivo.
- Usar exiftools para ver la información del archivo jpg que estaba dentro del zip.
- Entre toda la información, había un valor muy raro que destacaba entre los demás, asignado a Attribution URL, parece ser base64.
- Al decodificarlo usando comando *base64 -d*, conseguimos la bandera.
## Notas adicionales
## Referencias