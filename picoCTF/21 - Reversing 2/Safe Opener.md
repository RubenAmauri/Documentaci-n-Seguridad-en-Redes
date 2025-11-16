## Descripción
Can you open this safe?I forgot the key to my safe but this [program](https://artifacts.picoctf.net/c/83/SafeOpener.java) is supposed to help me with retrieving the lost key. Can you help me unlock my safe?Put the password you recover into the picoCTF flag format like:`picoCTF{password}`
## Solución
- Analizar el código.
- En el código nos dimos cuenta de dos cosas importantes, la primera, es que la contraseña se decodifica de base64, la segunda, es que la contraseña estaba en el mismo código.
- Copié la contraseña del código para pegarla en la terminal, para decodificarla de esta manera:
  ``` zsh
  echo "contraseña_en_base64" | base64 -d
  ```
  - Así obtuve la bandera, solo había que darle el formato.
## Notas adicionales
## Referencias
