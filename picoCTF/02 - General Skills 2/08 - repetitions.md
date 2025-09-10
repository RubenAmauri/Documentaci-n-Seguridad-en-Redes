## Descripción
Can you make sense of this file?Download the file [here](https://artifacts.picoctf.net/c/473/enc_flag).
## Solución
- El archivo era un archivo de texto plano, el cual contenía un texto codificado.
- Comencé a investigar y en linux es posible decodificar base64 usando comando "*base64 -d *"
- Al decodificar parecía que me daba el mismo resultado, pero resulta que se decodificaba igual en base64
- Usé varias pipes para llegar al resultado, decodificando al menos 5 veces el texto desde base64, hasta que conseguí la bandera.
## Notas adicionales
- pipe (|) es fácilmente escrita con alt + 124
## Referencias
