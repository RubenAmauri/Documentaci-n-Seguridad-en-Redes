## Descripción
Decrypt this [message](https://jupiter.challenges.picoctf.org/static/49f31c8f17817dc2d367428c9e5ab0bc/ciphertext).
## Solución
- Descargar el archivo.
- Al leerlo, nos damos cuenta que está encriptado con CAESAR.
- Usamos cyberchef con ROT13 para desencriptar.
- Con la rotación en 13 caracteres no daba la bandera, así que experimentamos con los valores de rotación hasta que forme una palabra con coherencia.
- Llegamos hasta el valor 4 y encontramos la bandera.
## Notas adicionales
## Referencias