## Descripción
Can you figure out how this program works to get the flag?Connect to the program with netcat:`$ nc saturn.picoctf.net 50349`The program's source code can be downloaded [here](https://artifacts.picoctf.net/c/527/picker-IV.c). The binary can be downloaded [here](https://artifacts.picoctf.net/c/527/picker-IV).
## Solución
- Ahora tenemos dos archivos, el código fuente en c y un archivo binario.
- Al ejecutar el archivo en c, lo que hace es preguntarnos una dirección de memoria en hexadecimal, así que tenemos que buscar la manera de saber la dirección de la función "win" para mandar llamar esa dirección.
- Para conocer la dirección en memoria de dicha función, utilizaremos un depurador, con este comando:
  ``` zsh
  gdb ./nombre_del_binario
  ```
  - Así analizaremos el binario con el depurador, y ahora simplemente le pediremos que imprima el símbolo "win".
  - Así obtuvimos la dirección de memoria de win, la copiamos exceptuando el 0x (Porque el programa lo indica).
  - Ahora le pasamos esa dirección al programa y nos entrega la bandera.
## Notas adicionales
## Referencias