## Descripción
Find the flag in this [picture](https://jupiter.challenges.picoctf.org/static/916b07b4c87062c165ace1d3d31ef655/pico_img.png).
## Solución
- Descargar el archivo en su carpeta.
- Investigamos sobre una herramienta que se incluye en kali linux "exiftools"
- Utilizamos esa herramienta para saber quién fue el autor de la imagen que descargamos
- Como autor estaba la bandera.
## Notas adicionales
- exiftools: Programa que se usa desde la terminal para leer metadatos de archivos:
  ``` zsh
  exiftools -Artist ...
  ```
  Este comando puede ayudarnos a leer el metadato del autor del archivo.
## Referencias