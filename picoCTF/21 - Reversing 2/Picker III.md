## Descripción
Can you figure out how this program works to get the flag?Connect to the program with netcat:`$ nc saturn.picoctf.net 54149`The program's source code can be downloaded [here](https://artifacts.picoctf.net/c/524/picker-III.py).
## Solución
- En este nos pusieron obstáculos más ingeniosos, ahora se limitó con una variable numérica las funciones a las que podemos llamar.
- Ahora analizamos el código, y nos damos cuenta de que al ejecutar el programa no solo podemos leer, sino también escribir, para poder ejecutar win, tenemos que usar las funciones de escritura del programa y cumplir con ciertas condiciones:
	- Hay una variable tipo string que guarda la tabla, llamada func_table, esta tiene que cumplir una condición, ser exactamente 128 bytes.
	- Aquí la idea es "burlar" la seguridad el programa haciendo que se reemplace la primera función de la tabla por la función win, y luego mandar a llamar la primera función, de esta manera:
		- Primero, llamaremos a la tercer función de la tabla, la cual puede editar una variable dentro del código.
		- Luego, le diremos que queremos escribir la variable "func_table".
		- A esta variable le daremos este nuevo valor: ``'win' + ' ' * 29 + 'read_variable' + ' ' * 19 + 'write_variable' + ' ' * 18 + 'getRandomNumber' + ' ' * 17`` 
		  - Este valor esta escrito de esta manera con el propósito de completar exactamente los 128 bytes, multiplicando los espacios en blanco para lograrlo.
- Ahora la tabla está modificada, y la primera función llama a win en lugar de la función predeterminada.
- Ahora por último sería mandar llamar la primera función, y luego pasar ese contenido por cyberchef para convertirlo de hexadecimal a ascii.
## Notas adicionales
## Referencias