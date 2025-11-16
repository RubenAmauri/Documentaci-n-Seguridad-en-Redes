## Descripción
This service can provide you with a random number, but can it do anything else?Connect to the program with netcat:`$ nc saturn.picoctf.net 60134`The program's source code can be downloaded [here](https://artifacts.picoctf.net/c/515/picker-I.py).
## Solución
- Analizamos el código.
- Parece ser muy extenso, pero hay dos funciones clave:
	- tryRandomNumber:
		- El programa te sugiere que escribas esa función, es "todo" lo que hace si simplemente lo ejecutas, pero ahí está la primera pista, si escribes el nombre de una función, la ejecuta.
	- win()
		- Esta función imprime la bandera en formato hexadecimal, si al ejecutar el programa, escribimos el nombre de esta función en lugar de la que recomienda, la ejecuta y nos da una cadena hexadecimal.
- Después de llamar a la función win(), pasamos la cadena que nos dió a cyberchef y usamos "From hex" para obtener la bandera.
## Notas adicionales
## Referencias