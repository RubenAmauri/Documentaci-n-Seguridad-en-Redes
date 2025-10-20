## Descripción
Can you get the real meaning from this file. Download the file [here](https://artifacts.picoctf.net/c_titan/3/enc_flag).
## Solución
- Descargamos el archivo.
- Usamos cat para leerlo.
- Parece estar en base64.
- Podemos decodificarlo una vez con base64, pero después ya no funciona.
- Al decodificarlo la primera vez, debemos tomar lo que está entre comillas para volver a decodificarlo en base64.
- Nos da un nuevo mensaje encriptado, parece ya ser la bandera, ya que hay un mensaje ilegible entre llaves.
- Usamos cyberchef con rot13 para desencriptar el mensaje, jugando con los valores de rotación.
- Así obtuvimos la bandera
## Notas adicionales
## Referencias