## Descripción
Files can always be changed in a secret way. Can you find the flag? [cat.jpg](https://mercury.picoctf.net/static/c28a959c5605d5f67480d5dd3a77f302/cat.jpg)
## Solución
- Descargar el archivo.
- Usar exiftool para ver su información.
- Hay un valor asignado a License que destaca por su sintaxis, suponemos que es base64.
- Usar *base64 -d* para decodificar ese mensaje y revela la bandera.
## Notas adicionales
## Referencias