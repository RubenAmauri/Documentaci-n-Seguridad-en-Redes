## Descripción
To get truly 1337, you must understand different data encodings, such as hexadecimal or binary. Can you get the flag from this program to prove you are on the way to becoming 1337? Connect with `nc jupiter.challenges.picoctf.org 15130`.
## Solución
- Busqué cómo hacer conversiones de bases en python, encontré una misma solución para base 2 y base 8:
``` python
# base 2
py -c "print(''.join(chr(int(c, 2)) for c in 'Binario'.split()))" # el split es para separar espacios
#base 8
py -c "print(''.join(chr(int(c, 8)) for c in '01100011 01101000 01100001 01101001 01110010'.split()))" # Sólo se cambia una parte del código, donde el 2 se cambia por el 8 para indicar que es otra base.
```
- Para convertir desde hexadecimal la historia fue diferente, ya que python tiene otra función más directa para la conversión de hexadecimales:
``` python
py -c "print(bytes.fromhex('hexadecimal').decode())"
```
## Notas adicionales
- lambda - Función anónima (Que no tiene nombre) útil para tareas sencillas que se ejecutan en una sola línea de código, sin necesidad de un return explícito. 
## Referencias