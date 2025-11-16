## Descripción
This vault uses some complicated arrays! I hope you can make sense of it, special agent. The source code for this vault is here: [VaultDoor1.java](https://jupiter.challenges.picoctf.org/static/87e103a8db01087de9ccf5a7a022ddf8/VaultDoor1.java)
## Solución
- La bandera de nuevo estaba en el archivo, pero desordenada.
- Para poder automatizar su ordenamiento, usamos una serie de comandos, que completos quedaron así:
  ``` zsh
  cat flag.java | sort | awk '{print($3)}' | tr -d "'" | tr -d "\n"
  ```
  - Eso nos dió la bandera, solo había que darle el formato de picoCTF{}.
## Notas adicionales
- El comando:
  ``` zsh
  cat flag.java | sort | awk '{print($3)}' | tr -d "'" | tr -d "\n"
  ```
  Lo que hace es:
  Sort: ordena en orden ascendente los caracteres que están en el archivo.
  awk: Eso es para mandarle la orden de que solo imprima el contenido de la tercer columna.
  tr: Este "recorta" caracteres de la cadena que se está imprimiendo, en este caso la comilla sencilla (') y el salto de línea, que se indica con un "\n".
## Referencias1
