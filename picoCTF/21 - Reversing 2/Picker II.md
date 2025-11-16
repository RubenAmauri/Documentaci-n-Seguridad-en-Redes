## Descripción
Can you figure out how this program works to get the flag?Connect to the program with netcat:`$ nc saturn.picoctf.net 64564`The program's source code can be downloaded [here](https://artifacts.picoctf.net/c/523/picker-II.py).
## Solución
- Analizamos el código.
- El código es parecido al del reto anterior, podemos llamar una función si la escribimos en la entrada del programa.
- Ahora hay un obstáculo, una función llamada "filter". Lo que hace esta función es detectar si se escribió la palabra "win" en la entrad del programa, y si lo hizo, se marca automáticamente como inválida.
- Usaremos una función de python que devuelve un diccionario de variables locales, la cual es "globals()".
- Y para poder lograr que ejecute win, le pasamos la palabra como una sumatoria de cadenas, de esta forma:
  ``` python
  globals()['w'+'i'+'n']
  ```
- Así conseguimos hacer que el programa nos imprima la bandera sin tener que escribir "win" directamente.
- Ya solo queda usar cyberchef para convertirla de hexadecimal a ascii y así obtener la bandera.
## Notas adicionales
## Referencias