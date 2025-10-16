## Descripción
We found this [packet capture](https://jupiter.challenges.picoctf.org/static/0c84d3636dd088d9fe4efd5d0d869a06/capture.pcap) and [key](https://jupiter.challenges.picoctf.org/static/0c84d3636dd088d9fe4efd5d0d869a06/picopico.key). Recover the flag.
## Solución
- Descargamos los archivos.
- En la misma carpeta, ejecutamos el comando: *ssldump -r capture.pcap -k picopico.key -d > output*.
- Este comando lo que hará es leer el archivo .pcap y gracias a la llave .key, lo decodificará, luego eso lo escribirá en un nuevo archivo llamado output.
- Teniendo el archivo decodificado, procedemos a analizarlo con nano.
- Analizando usamos la opción de buscar y buscamos "picoCTF".
- Nos manda directo a la ubicación de la bandera.
## Notas adicionales
- ssldump: es una herramienta diseñada especificamente para analizar, decodificar y mostrar contenido de trafico de red.
- ssldump -r: para decirle al comando que lea el archivo.
- ssldump -k: le indica al comando que el archivo es una llave.
- ssldump -d: está opción sirve para indicarle al programa que no solo muestre los detalles del tráfico, sino también, decodifique y muestre los datos que se transmitieron.
## Referencias