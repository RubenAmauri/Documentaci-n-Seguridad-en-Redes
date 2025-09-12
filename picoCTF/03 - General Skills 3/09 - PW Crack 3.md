## Descripción
Can you crack the password to get the flag?Download the password checker [here](https://artifacts.picoctf.net/c/16/level3.py) and you'll need the encrypted [flag](https://artifacts.picoctf.net/c/16/level3.flag.txt.enc) and the [hash](https://artifacts.picoctf.net/c/16/level3.hash.bin) in the same directory too.There are 7 potential passwords with 1 being correct. You can find these by examining the password checker script.
## Solución
- Descargar los archivos.
- Leer cuidadosamente el script de python; Al ejecutar el archivo se pediría una contraseña, la cual al ser correcta, usaría los otros dos archivos para desencriptar la bandera.
- En el mismo archivo había un arreglo con la lista de las posibles contraseñas.
- Para evitar ingresar todas de una por una, implementé un ciclo que recorriera todas las contraseñas hasta ingresar la correcta.
- Funcionó el ciclo y se encontró la bandera.
## Notas adicionales
Este fue el código que estaba en el reto:
``` python
import hashlib

### THIS FUNCTION WILL NOT HELP YOU FIND THE FLAG --LT ########################
def str_xor(secret, key):
    #extend key to secret length
    new_key = key
    i = 0
    while len(new_key) < len(secret):
        new_key = new_key + key[i]
        i = (i + 1) % len(key)        
    return "".join([chr(ord(secret_c) ^ ord(new_key_c)) for (secret_c,new_key_c) in zip(secret,new_key)])
###############################################################################

flag_enc = open('level3.flag.txt.enc', 'rb').read()
correct_pw_hash = open('level3.hash.bin', 'rb').read()


def hash_pw(pw_str):
    pw_bytes = bytearray()
    pw_bytes.extend(pw_str.encode())
    m = hashlib.md5()
    m.update(pw_bytes)
    return m.digest()


def level_3_pw_check():
    user_pw = input("Please enter correct password for flag: ")
    user_pw_hash = hash_pw(user_pw)
    
    if( user_pw_hash == correct_pw_hash ):
        print("Welcome back... your flag, user:")
        decryption = str_xor(flag_enc.decode(), user_pw)
        print(decryption)
        return
    print("That password is incorrect")



level_3_pw_check()


# The strings below are 7 possibilities for the correct password. 
#   (Only 1 is correct)
pos_pw_list = ["6997", "3ac8", "f0ac", "4b17", "ec27", "4e66", "865e"]
# Aqui terminaba el código original
# Aquí comienza el ciclo implementado por mí para llegar a la contraeña correcta, recorriendo el arreglo que se proporcionaba en el código original
for pw in pos_pw_list:
    if hash_pw(pw) == correct_pw_hash:
        print(f"Found password: {pw}")
        decryption = str_xor(flag_enc.decode(), pw)
        print("Flag / contenido decodificado:")
        print(decryption)
        break
else:
    print("Ninguna contraseña de la lista fue correcta.")

```
## Referencias
