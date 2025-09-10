## Descripción
Unzip this archive and find the file named 'uber-secret.txt'

- [Download zip file](https://artifacts.picoctf.net/c/502/files.zip)
## Solución
- Descargué el archivo con wget.
- Descomprimí el archivo con unzip.
- Se utilizó comando find para buscar la ruta del archivo.
- Leí el archivo con cat y ahí estaba la bandera.
``` bash
find files -type f -name "uber-secret.txt"
cat files/adequate_books/more_books/.secret/deeper_secrets/deepest_secrets/uber-secret.txt
```
## Notas adicionales
- find: comando para buscar archivos y directorios.
- files era el nombre de la carpeta en la que se iba a buscar.
- -type es para indicar qué se está buscando; usar f después del -type le indicó al bash que estaba buscando un "archivo"(file).
- -name es para indicar el nombre del archivo que se está buscando, pero aún así se puede buscar sin el nombre

## Referencias
