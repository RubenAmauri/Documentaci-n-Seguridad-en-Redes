## Descripción
## Solución
- Descargar el archivo.
- Resulta que la bandera está escondida con una técnica de esteganografía.
- Usamos una página que decodifica el texto escondido detrás de ese archivo de imagen.
- También se puede hacer usando un comando *gema en ruby*
- El comando es *zsteg*.
- Lo instalamos con ````
  ``` zsh
  gem install zsteg
  ```
  - usamos comando 
  - ```
    zsteg -a building.jpg | grep pico
    ```
- así nos da la bandera.
## Notas adicionales
- Esteganografía: Técnica de ocultar información 
## Referencias
https://stylesuxx.github.io/steganography/