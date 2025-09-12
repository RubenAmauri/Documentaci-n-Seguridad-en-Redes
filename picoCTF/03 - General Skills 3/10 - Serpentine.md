## Descripción
Find the flag in the Python script![Download Python script](https://artifacts.picoctf.net/c/36/serpentine.py)
## Solución
- Descargar el archivo.
- Correr el archivo con "*python3"
- El archivo imprimía una serpiente, te daba 3 opciones, la primera imprimía un mensaje aleatorio, la segunda supuestamente escribía la bandera y la tercera  cerraba el programa.
- Al usar la segunda opción, el programa imprimía un mensaje que mencionaba que seguramente olvidó llamar a la función que desencripta la bandera.
- Abrir el archivo con "*nano*"
- Examinando el archivo ví que sí existía una función que desencriptaba la bandera, pero no se estaba utilizando, así que modifiqué el programa para que en lugar de escribir la línea que decía que olvidó llamar a la función, llame a la función.
- Al correr de nuevo el programa y elegir la opción de imprimir bandera, ahora sí la imprimió correctamente.
## Notas adicionales

## Referencias
