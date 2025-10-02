## Descripción
We found this [packet capture](https://jupiter.challenges.picoctf.org/static/483e50268fe7e015c49caf51a69063d0/capture.pcap). Recover the flag.
## Solución
- Descargamos el archivo.
- Abrimos el archivo con el programa wireshark, para ver los paquetes que contiene.
- En wireshark usamos la opción open y seleccionamos el archivo pcap.
- Buscamos algún paquete haya usado protocolo UDP.
- Damos click derecho en el paquete y seleccionamos follow.
- Después nos aparecerá otra ventana que tiene el contenido de la cadena de paquetes, vamos a ir hacía atrás para buscar el contenido de ellos.
- La bandera estaba oculta entre un paso de la cadena.
## Notas adicionales
- Archivos pcap.
- Programa wireshark
## Referencias