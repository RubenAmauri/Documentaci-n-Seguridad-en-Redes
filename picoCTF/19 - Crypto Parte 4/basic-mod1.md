## Descripción
We found this weird message being passed around on the servers, we think we have a working decryption scheme. Download the message [here](https://artifacts.picoctf.net/c/128/message.txt). Take each number mod 37 and map it to the following character set: 0-25 is the alphabet (uppercase), 26-35 are the decimal digits, and 36 is an underscore. Wrap your decrypted message in the picoCTF flag format (i.e. `picoCTF{decrypted_message}`)
## Solución
- Descargué el archivo.
- El archivo solo era un .txt con números al azar.
- Según las pistas del reto, debíamos hacer unos cálculos con esos números, usando el operador mod y luego convertirlos a ascii.
- Para automatizar eso, hicimos un script en python:
``` python
numeros = open('message.txt').read().split()
flag = ' '

for numero in numeros:
        mod = int(numero) % 37
        if mod>=0 and mod <=25:
                c = chr(mod+65)
        elif mod >= 26 and mod <= 35:
                c = chr(mod+22)
        elif mod == 36:
                c = '_'

        flag += c
print (flag)
```
- Al ejecutarlo, nos revela la bandera.
## Notas adicionales
## Referencias