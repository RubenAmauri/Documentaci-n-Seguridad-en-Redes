## Descripción
Class, take your seats! It's PRIME-time for a quiz... `nc jupiter.challenges.picoctf.org 1981`
## Solución
 - Lo primero fue informarse sobre rsa y aprender las fórmulas (las cuales están en la sección de notas adicionales).
 - Ya teniendo las fórmulas y el nombre de las variables que usaremos para resolver los problemas, procedemos a conectarnos al netcat que nos proporciona el reto.
 - El netcat nos dirige a una especie de "examen", en el que tenemos que resolver matemáticamente los problemas de cifrado.
 - Con la información que nos otorga cada índice del examen, primero determinamos si es posible calcular la respuesta que pide con los valores que nos da.
 - Algunas respuestas no son posibles de calcular con los valores que se proporcionan.
 - Cuando logramos contestar la última (que ya es como tal un descifrado de rsa), el mismo examen nos indica que esa respuesta es la bandera, pero debe ser convertido a hexadecimal y luego a ASCII.
 - Usando python (que fue el que usamos para calcular todas las respuestas), convertimos el mensaje descifrado en hexadecimal y de hexadecimal a ASCII.
 - Así obtuvimos la bandera.
## Notas adicionales
- RSA - llave pública - asimétrico; Variables
	- m - mensaje original o mensaje en texto plano
	- c - mensaje cifrado (ciphertext)
	- p, q - son dos números primos distintos y muy grandes
	- n - es el módulo (Lo compartes con las llaves públicas como privada)
	- tn - totient n (función de euler)
	- e - llave public - 65537 (exponente) 2 ^ 16 +1 
	- d - llave privada
- cálculos:
	- n = p\*q
	- tn = (p-q) \* (q-1)
	- d = e ^ -1(mod tn)                   - pow(e, -1, tn)
- Cifrar:
	- c = m ^ e (mod n)                    - pow(m, e, n)
- Decifrar:
	- m = c ^ d (mod n)                    - pow(c, d, n)

- Para convertir un número decimal a hexadecimal y de hexadecimal a código ASCII con python: 
	- bytes.fromhex( hex(m)[2:] ).decode()
		- Donde "m", es el valor decimal que queremos convertir
## Referencias
[RSA info](https://simple.wikipedia.org/wiki/RSA_algorithm)