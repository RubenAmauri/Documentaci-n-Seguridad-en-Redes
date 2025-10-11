## Descripción
We found this [packet capture](https://jupiter.challenges.picoctf.org/static/b506393b6f9d53b94011df000c534759/capture.pcap). Recover the flag that was pilfered from the network.
## Solución
- Descargar el archivo .pcap.
- Usaremos wireshark para abrir el archivo.
- Notaremos que hay muchos que usan el protocolo UDP, así que tomaremos el primer paquete que use ese protocolo y seguiremos su stream, esperando encontrar la bandera.
- En el paquete 32 encontraremos la marca start, la que tiene como puerto origen el 5000 y de destino el 22, también una longitud de 5.
- En el paquete 60 está la marca end, con origen 5000 y destino 22, con longitud 3.
- Con esta información, vamos a filtrar los paquetes udp cuyo puerto destino sea 22.
- Observaremos un patrón extraño: todos los paquetes tienen de destino 22 pero los origenes varían de puerto, pero todos estando en el rango de los 5000.
- Si buscamos a qué caracter corresponde cada número después del 5 en los puertos, vemos como se va formando la bandera.
- Para no decodificar paquete por paquete, lo automatizaremos con python.
- Instalaremos la herramienta *scapy*.
- Haremos un script que use esta herramienta para que lea los paquetes del archivo.
- Después de leerlos, lo que hará será filtrar los paquetes UDP que terminen en el puerto 22.
- Después hará una operación para encontrar todos los que empiecen en el puerto 5000 o mayor, luego les restará 5000 para "extraer" el número que será convertido a caracter.
- Ahora convertirá el número a código ascii. 
- Así obtendremos la bandera.
## Notas adicionales
## Referencias